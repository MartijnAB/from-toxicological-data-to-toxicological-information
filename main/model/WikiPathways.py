"""
TODO: add Docstring for fill
test doc
"""

from SPARQLWrapper import SPARQLWrapper, JSON #  TODO: add comment
import sys

from main.model.Pathway import Pathway





class WikiPathways:
    """
        TODO: add Docstring WikiPathways
    """

    def __init__(self):
        """
        TODO: add Docstring init
        """

        self._sparql_endpoint_ = SPARQLWrapper("http://sparql.wikipathways.org")
        self._prefixes_ = """
        PREFIX gpml:    <http://vocabularies.wikipathways.org/gpml#>
        PREFIX wp:      <http://vocabularies.wikipathways.org/wp#>
        PREFIX cur:     <http://vocabularies.wikipathways.org/wp#Curation:>
        PREFIX wprdf:   <http://rdf.wikipathways.org/>
        PREFIX biopax:  <http://www.biopax.org/release/biopax-level3.owl#> 
        PREFIX cas:     <http://identifiers.org/cas/>
        PREFIX dc:      <http://purl.org/dc/elements/1.1/> 
        PREFIX dcterms: <http://purl.org/dc/terms/>
        PREFIX foaf:    <http://xmlns.com/foaf/0.1/> 
        PREFIX ncbigene:<http://identifiers.org/ncbigene/>
        PREFIX pubmed:  <http://www.ncbi.nlm.nih.gov/pubmed/> 
        PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
        PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX skos:    <http://www.w3.org/2004/02/skos/core#>
        PREFIX xsd:     <http://www.w3.org/2001/XMLSchema#>
        """

    def get_wikipathway_id(self, wikipathway_id) -> Pathway:
        """

        :type wikipathway_id: str
        :param wikipathway_id: 
        """
        query = """
        SELECT DISTINCT ?label ?wikidata WHERE {
          ?metabolite a wp:Metabolite .
          ?metabolite rdfs:label ?label .
          ?metabolite dcterms:isPartOf ?pathway .
          ?pathway a wp:Pathway .
          ?pathway dcterms:identifier """ + '"' + wikipathway_id + '"' + """^^xsd:string .
          ?metabolite wp:bdbWikidata ?wikidata .
        }"""

        return _execute_sparql_query_(query)

    def _execute_sparql_query_(self, query):
        """

        :type query: object
        """

        self._sparql_endpoint_.setQuery(query)
        self._sparql_endpoint_.setReturnFormat(JSON)
        results = self._sparql_endpoint_.query().convert()
        print(results)

def main():
    """
    TODO:
    :return: none
    """
    print(__doc__)
    print("dit bestant was niet bedoelt om als enekl bestant uit gevoert te worden\n het zal dan ook nu stoppen ") # TODO: make enilis


if __name__ == '__main__':
    sys.exit(main())