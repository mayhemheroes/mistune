#! /usr/bin/python3

import atheris
import sys
import io
import tempfile

with atheris.instrument_imports():
    import mistune


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    file_data = fdp.ConsumeBytes(atheris.ALL_REMAINING)
    temp_file = tempfile.NamedTemporaryFile()
    temp_file.write(file_data)
    temp_file.flush()
    temp_file.name = "test" + ".md"


    try:
        mistune.html(temp_file)

    except (NotImplementedError, AttributeError, DeprecationWarning):
        pass

    temp_file.close()


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
