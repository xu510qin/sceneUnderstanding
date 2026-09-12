import argparse
from pathlib import Path


def require_path(label, value):
    path = Path(value)
    exists = path.exists()
    marker = "OK" if exists else "MISSING"
    print(f"{marker:7} {label}: {path}")
    return exists


def parse_scalar(value):
    value = value.strip()
    if value in {"true", "True"}:
        return True
    if value in {"false", "False"}:
        return False
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    if len(value) >= 2 and value[0] == value[-1] == "'":
        return value[1:-1]
    return value


def load_config(config_path):
    try:
        import yaml

        with config_path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    except ModuleNotFoundError:
        pass

    config = {}
    stack = [(-1, config)]
    with config_path.open("r", encoding="utf-8") as f:
        for raw_line in f:
            if not raw_line.strip() or raw_line.lstrip().startswith("#"):
                continue

            indent = len(raw_line) - len(raw_line.lstrip(" "))
            line = raw_line.strip()
            if ":" not in line:
                continue

            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            while stack and indent <= stack[-1][0]:
                stack.pop()

            parent = stack[-1][1]
            if value == "":
                child = {}
                parent[key] = child
                stack.append((indent, child))
            else:
                parent[key] = parse_scalar(value)

    return config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to paths.local.yaml")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")

    config = load_config(config_path)

    print("Global paths")
    for key in [
        "data_root",
        "raw_data_root",
        "processed_data_root",
        "output_root",
        "checkpoint_root",
        "log_root",
    ]:
        if key in config:
            require_path(key, config[key])

    print("\nDatasets")
    datasets = config.get("datasets", {})
    if not datasets:
        print("No datasets configured.")
        return

    for name, dataset in datasets.items():
        print(f"\n{name}")
        if not dataset.get("enabled", False):
            print("  disabled")
            continue
        for key in ["raw_dir", "processed_dir", "split_dir"]:
            if key in dataset:
                require_path(f"{name}.{key}", dataset[key])


if __name__ == "__main__":
    main()
