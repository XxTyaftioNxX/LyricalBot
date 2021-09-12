#Markov Chain Representation

import random

#define the graph in terms of vertices
class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent = {}     #nodes that have edge to this vertex
        self.neighbours = []
        self.neighbour_weights = []

    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    def increment_edge(self, vetex):
        #incrementing the weight of the vertex
        self.adjacent[vetex] = self.adjacent.get(vetex, 0) + 1

    def get_probability_map(self):
        for(vertex, weight) in self.adjacent.items():
            self.neighbours.append(vertex)
            self.neighbour_weights.append(weight)

    def next_word(self):
        #select next word based on weights  as list and returns the first 
        return random.choices(self.neighbours, weights = self.neighbour_weights)[0]

#making graph out of the vertices
class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        #it returns all the posssible words (values of the all vertex)
        return set(self.vertices.keys())

    def add_vertex(self, value):
        #creating new vertex
        self.vertices[value] = Vertex(value)
    
    def get_vertex(self, value):
        if value not in  self.vertices:
            self.add_vertex(value)
        #returns the vertex object
        return self.vertices[value]   

    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()
    
    
 
