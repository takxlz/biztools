import tarfile
import os
import sys
from pathlib import Path

def extract_targz(input_dir: Path):
    # Make output directory
    output_dir = input_dir / "_extracted"
    os.makedirs(output_dir, exist_ok=True)

    # Make subdirectories for each tar.gz file
    for targz_file in input_dir.glob("*.tar.gz"):
        each_dir = output_dir / targz_file.stem.replace(".tar", "")
        os.makedirs(each_dir, exist_ok=True)

    # Extract the tar.gz file
    with tarfile.open(targz_file, "r:gz") as tar:
        tar.extractall(path=each_dir)
        print(f"Extracted {targz_file} to {each_dir}")

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python extract_targz.py <path_to_targz_dir>")
        sys.exit(1)
    # Get the input directory from command line arguments
    # Check if the input directory exists and is a directory
    input_dir = Path(sys.argv[1])
    if not input_dir.is_dir():
        print(f"Error: {input_dir} is not a valid directory.")
        sys.exit(1)
    extract_targz(input_dir)


