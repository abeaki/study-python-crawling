from SPARQLWrapper import SPARQLWrapper


class SPARQLClient:

    def __init__(self, endpoint): #, method='GET', request_method='urlencoded', format='json'):
        self.endpoint = endpoint
        self.sparql = SPARQLWrapper(endpoint)
        #self.sparql.setMethod(method)

    def query(self, query):
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat('json')
        results = self.sparql.query().convert()

        return results["results"]["bindings"]
