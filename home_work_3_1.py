import argparse
from pathlib import Path
import shutil

def display_tree(path: Path, destination: Path, indent: str = "") -> None:
    if path.is_dir():
        for child in path.iterdir():
            display_tree(child, destination, indent + "    ")
    else:
        extension = path.suffix.lower()
        dest_dir = destination / extension[1:] 
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_dir / path.name
        try:
            shutil.copy2(path, dest_file)
            print(f"Copied: {path} to {dest_file}")
        except Exception as e:
            print(f"Error copying {path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Recursively copy files and sort them into directories based on their extensions.")
    parser.add_argument("source", type=str, help="Source directory path")
    parser.add_argument("destination", type=str, nargs="?", default="dist", help="Destination directory path (default: dist)")
    args = parser.parse_args()

    source_dir = Path(args.source)
    destination_dir = Path(args.destination)

    display_tree(source_dir, destination_dir)