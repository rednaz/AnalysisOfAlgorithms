#James Musselman, Mason Urnen, Zander Nelson
#Comp 569
#Assignment 4, Problem 3.8

from pip._vendor.distlib.compat import raw_input

class Node:
    def __init__(self, value):
        self.Value = value
        self.Edges = list()

class Edge:
    def __init__(self, node, weight=1):
        self.Node = node
        self.Weight = weight

class Graph:
    def __init__(self):
        self.Nodes = list()

    def AddNode(self, node):
        self.Nodes.append(node)

    def AddDirectedEdge(self, startNode, endNode, weight=1):
        startNode.Edges.append(Edge(endNode, weight))

    def AddBiDirectedEdge(self, startNode, endNode, weight=1):
        self.AddDirectedEdge(startNode, endNode, weight)
        self.AddDirectedEdge(endNode, startNode, weight)

    def Print(self):
        for node in self.Nodes:
            for edge in node.Edges:
                nodeValue = node.Value
                edgeNodeValue = edge.Node.Value
                print(str(nodeValue) + '->' + str(edgeNodeValue))

def GraphBuilder(n):
    nodes = list()
    graph = Graph()

    for i in range(n):
        newNode = Node([1, n])
        nodes.append(newNode)
        graph.AddNode(newNode)
        #print "created node..."

    for x in range(n):
        for y in range(n):
            graph.AddDirectedEdge(nodes[x], nodes[y]) #directed of bidirected? Change if need be
            print(str(x) + " -> " + str(y))
    return graph

#Main
invalid = True
n = str

while invalid:
    n = raw_input("Enter an n value for graph of size 2^n: ")
    try:
        int(n)
    except ValueError:
        print("Invalid value! (Must be positive integer)")
        print()
    else:
        invalid = False
print("")

print("Building graph")
graph = GraphBuilder(int(n))

