from src.CosineMeasure import CosineMeasure
#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Muhammad Ghazi Muharam"
__version__ = "0.1.0"
__license__ = "MIT"

DOCUMENTS_DIR = './Documents'
QUERY = 'home sales'


def main():
    measure = CosineMeasure(query=QUERY, dir_path=DOCUMENTS_DIR)
    measure.word2documents()
    print(measure.get_word())
    print(measure.calculate_idf())
    print(measure.count_tf())
    measure.document_vector()
    measure.query_vector()
    measure.cosine_measure()


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
