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
    count = 0

    for i in range(n**2): #n^2 nodes in the graph
        newNode = Node([1, n])
        nodes.append(newNode)
        graph.AddNode(newNode)
        print("Created node: " + str(i))
    print()

    for x in range(n**2):
        for y in range(n**2):
            if ((y == (x+1)) or (y == (x-1)) or (y == (x+n)) or (y == (x-n))): #If y is adjacent to x...
                graph.AddDirectedEdge(nodes[x], nodes[y]) #connect the two nodes.
                #print(str(x) + " -> " + str(y)) #Uncomment this to check for correct edges

    #Print graph
    print("nxn graph with " + str(n**2) + " nodes:")
    for x in range(n):
        for y in range(n):
            if (y == (n-1)):
                print("*", end="")
            else:
                print("*-", end="")
        print()

        if (x != (n-1)):
            for z in range(n):
                print("| ", end="")
        print()

    return graph

#Savitch's Algorithm
def k_edge_path(s, t, k):
    if k == 0:
        return s == t
    if k == 1:
        return s == t or (s, t) in edges
    for u in vertices:
        if k_edge_path(s, u, floor(k / 2)) and k_edge_path(u, t, ceil(k / 2)):
            return true
    return false

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

