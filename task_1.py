import argparse
import os
from pathlib import Path
import shutil


def read_dir(src: Path, dst: Path):
    try:
        if src.is_dir():
            for child in src.iterdir():
                read_dir(child, dst)
        else:
            file_extension = os.path.splitext(src)[1].split(".")[1]
            file_path = Path(f"{dst}/{file_extension}")
            try:
                file_path.mkdir(exist_ok=True, parents=True)
                shutil.copy2(src, file_path)
            except Exception as error:
                print(error)
    except Exception as error:
        print(error)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-S", "--source", type=Path, required=True,
                        help="Папка з якої має відбутись копіювання")
    parser.add_argument("-O", "--output", type=Path, default=Path("dist"),
                        help="Папка в якому має відбутись копіювання")
    return parser.parse_args()


def main():
    args = parse_args()
    if os.path.exists(args.source):
        read_dir(args.source, args.output)
    else:
        print(f"За цим шляхом '{args.source}' нічого не знайдено.")


if __name__ == "__main__":
    main()
