# HEIC to JPEG

Converts Apple HEIC photos in the current folder to JPEG.

The script looks for `.heic` files next to itself, writes a `.jpg` with the same name, and leaves the originals in place.

## Requirements

- Python 3.10 or newer
- [Pillow](https://pypi.org/project/pillow/) and [pillow-heif](https://pypi.org/project/pillow-heif/), listed in `requirements.txt`

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the virtual environment with `venv\Scripts\activate`.

## Usage

Put the `.heic` files in this folder, then run:

```bash
python heic_to_jpg.py
```

Each file is converted in place as a sibling JPEG. A photo named `IMG_0001.HEIC` becomes `IMG_0001.jpg`. Files that fail to open are reported and skipped.

The script only checks the current directory. It does not walk subfolders, and it does not delete the HEIC files after a successful conversion.
