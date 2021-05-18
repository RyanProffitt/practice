# Ryan Proffitt
# 17 May 2021
# A set of tools to help me practice working with graphs.

from random import randint

# A simple 10x10 graph where each vertex has just one connection
class SimpleGraph():
    def __init__(self, num_vertices=100, max_edges_per_vertex=1):
        assert not num_vertices < 1
        assert not max_edges_per_vertex < 1

        self.vertices = {}
        self.num_vertices = num_vertices

        # Randomly assign connections
        for i in range(num_vertices):
            edges = [randint(0, num_vertices - 1) for j in range(max_edges_per_vertex)]

            self.vertices[i] = edges
