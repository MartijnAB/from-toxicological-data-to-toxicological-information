"""
TODO: add standart docsrin
test bestand in plaats van de jupier noot boeks
"""
# from main.model.WikiPathways import WikiPathways
# import model.WikiPathways.WikiPathways
# from main.model import WikiPathways
import main.model.WikiPathways
def main():
    """
    TODO: add Docstring
    :return: None
    """

    run = WikiPathways()
    run.get_wikipathway_id("WP1604")


if __name__ == '__main__':
    main()