from SPARQLWrapper import SPARQLWrapper, JSON #  TODO: add comment
import sys


class WikiPathways:
    """
        TODO: add Docstring WikiPathways
    """

    def __init__(self):
        """
        TODO: add Docstring init
        """

        self.sparql = SPARQLWrapper("http://sparql.wikipathways.org")

def main():
    """
    TODO: 
    :return: none
    """


if __name__ == '__main__':
    sys.exit(main())