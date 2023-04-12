import zipfile
import pathlib


def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    print(dest_path)
    with zipfile.ZipFile(dest_path, "w") as archive:
        for fp in filepaths:
            fp = pathlib.Path(fp)
            archive.write(fp, arcname=fp.name)


if __name__ == "__main__":
    make_archive(["convertor.py"], dest_dir='test')
