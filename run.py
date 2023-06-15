#!/bin/python

from dharma.main import DharmaApplication
import sys

def main(version):
    """The application's entry point."""
    app = DharmaApplication()
    return app.run(sys.argv)


if __name__ == "__main__":
    sys.exit(main('0.0.2'))