from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._idMapSighting = {}
        for s in DAO.get_all_sightings():
            self._idMapSighting[s.id] = s

    def getYears(self):
        return DAO.getYears()

    def getShape(self):
        return DAO.getShape()

    def buildGraph(self, year, shape):
        self._graph.clear()
        nodes = DAO.getNodes(year, shape)
        self._graph.add_nodes_from(nodes)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)
