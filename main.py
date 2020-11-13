from src.CosineMeasure import CosineMeasure
#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Muhammad Ghazi Muharam"
__version__ = "0.1.0"
__license__ = "MIT"

DOCUMENTS_DIR = './Documents'
QUERY = 'do big dogs run on the carpet with cat'


def main():
    measure = CosineMeasure(query=QUERY, dir_path=DOCUMENTS_DIR)
    measure.document_ranking()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
