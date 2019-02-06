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

    def get_wiki_pathway_id(self, wiki_pathway_id) -> Pathway:
        """

        :type wiki_pathway_id: str
        :param wiki_pathway_id:
        """
        query = """
        SELECT DISTINCT ?label ?wikidata WHERE {
          ?metabolite a wp:Metabolite .
          ?metabolite rdfs:label ?label .
          ?metabolite dcterms:isPartOf ?pathway .
          ?pathway a wp:Pathway .
          ?pathway dcterms:identifier """ + '"' + wiki_pathway_id + '"' + """^^xsd:string .
          ?metabolite wp:bdbWikidata ?wikidata .
        }"""

        result = self._execute_sparql_query_(query)



        # TODO: add error handling
        # print(result)
        if not result["results"]["bindings"]:
            print("geen gegevans ontvagen van wiki pathw") #  TODO: maak er beter foutmelding van en in het engels mischin zelfs een error.
            exit()
        # for iet in result:
        #     print(iet)
        # # exit()
        # print(result["results"])
        # # print(result["head"])
        # for iets in result["results"]:
        #     print(iets)
        # for iets in result["results"]["bindings"]:
        #     print(iets)
        #     print(iets["wikidata"]["value"])
        #     print(iets["wikidata"]["value"][31:])
        # for iets in result["results"]["bindings"]:
        #     print(iets)
        #     print(iets["label"]["value"])
        # exit()
        tmp_wiki_data_ids = [iter_result["wikidata"]["value"][31:] for iter_result in result["results"]["bindings"]]
        # print(tmp_wiki_data_ids)

        # print(tmp_wiki_data_ids)
        # print(result["results"]["bindings"])
        # print(result["results"]["bindings"]["wikidata"])
        # for iets in result["results"]["bindings"]["wikidata"]:
        #     print(iets)
        return Pathway(wiki_pathway_id, [[iter_result["wikidata"]["value"][31:], iter_result["label"]["value"]] for iter_result in result["results"]["bindings"]])

    def _execute_sparql_query_(self, query):
        """

        :type query: object
        """

        self._sparql_endpoint_.setQuery(query)
        # TODO: add error handling and 200 stater chek
        self._sparql_endpoint_.setReturnFormat(JSON)
        return self._sparql_endpoint_.query().convert()

def main():
    """
    TODO:
    :return: none
    """
    print(__doc__)
    print("dit bestant was niet bedoelt om als enekl bestant uit gevoert te worden\n het zal dan ook nu stoppen ") # TODO: make enilis
    run = WikiPathways()
    print(run.get_wiki_pathway_id("WP1604"))

    print("\ntestonzin\n")
    run.get_wiki_pathway_id("onzin")

if __name__ == '__main__':
    sys.exit(main())