#!/usr/bin/env python3
"""news-image-20261120 entry: write the front-page image to the output
directory. The image itself (entry.png, 1024x1024) is drawn by draw.py
and committed beside this file; this program only copies it, so it runs
with the standard library alone, no network, and writes identical bytes
every run. Output goes to $MAKEFUN_OUTPUT_DIR, or /output by default.
Run:  MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png missing next to main.py")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Sanity check the copy: the gate reads exactly these bytes, so the
    # copy must be byte-identical to the committed image.
    assert os.path.getsize(dst) == os.path.getsize(src), "copy size mismatch"
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
