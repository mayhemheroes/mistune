#! /usr/bin/python3

import atheris
import sys
import io
import tempfile

with atheris.instrument_imports():
    import mistune


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    file_data = fdp.ConsumeString(atheris.ALL_REMAINING)
   

    try:
        mistune.html(file_data)

    except (NotImplementedError, AttributeError, DeprecationWarning):
        pass

    temp_file.close()


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
