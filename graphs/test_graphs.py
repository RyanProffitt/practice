# Ryan Proffitt
# 18 May 2021
# Tests for the graphs folder code. Testing using pytest

from tools import SimpleGraph

def test_SimpleGraph():
    graph = SimpleGraph()
    assert len(graph.vertices.keys()) == 100
    all([len(graph.vertices[k])==1 for k in graph.vertices.keys()])

if __name__ == "__main__":
    test_GetSimpleGraph()
