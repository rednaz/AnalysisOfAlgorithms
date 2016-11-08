#James Musselman, Mason Urnen, Zander Nelson
#Comp 569
#Assignment 4, Problem 3.8

from pip._vendor.distlib.compat import raw_input
import math

class Node:
    def __init__(self, value):
        self.Value = value
        self.Edges = list()

    def __eq__(self, other):
        return self.Value == other.Value

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

    for i in range(2**n): #n^2 nodes in the graph
        newNode = Node(i + 1)
        nodes.append(newNode)
        graph.AddNode(newNode)
        print("Created node: " + str(i))
    print()

    for x in range(2**n):
        for y in range(2**n):
            if ((y == (x+1)) or (y == (x-1)) or (y == (x+n)) or (y == (x-n))): #If y is adjacent to x...
                graph.AddDirectedEdge(nodes[x], nodes[y]) #connect the two nodes.
                #print(str(x) + " -> " + str(y)) #Uncomment this to check for correct edges

    #Print graph
    print("nxn graph with " + str(2**n) + " nodes:")
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

def printStack(stack):
    for line in reversed(stack):
        print (line)
    print ("----------------")

class Bucket():
    def __init__(self, stack):
        self.Stack = stack

    def pop(self):
        self.Stack.pop()

#Savitch's Algorithm
def k_edge_path(s, t, k, bucket):
    if k == 0:
        bucket.pop()
        if (s == t):
            print ("T")
            printStack(bucket.Stack)
            return True
        else:
            return False
    if k == 1:
        bucket.pop()
        if (s == t):
            print ("T")
            printStack(bucket.Stack)
            return True

        for edge in s.Edges:
            if (edge.Node == t):
                print ("T")
                printStack(bucket.Stack)
                return True
        for edge in t.Edges:
            if (edge.Node == s):
                print ("T")
                printStack(bucket.Stack)
                return True
        return False
    for u in s.Edges + t.Edges:
        bucket.Stack.append("R(%s,%s,%s)" % (u.Node.Value, t.Value, math.ceil(k / 2)))
        bucket.Stack.append("R(%s,%s,%s)" % (s.Value, u.Node.Value, math.floor(k / 2)))
        printStack(bucket.Stack)
        if k_edge_path(s, u.Node, math.floor(k / 2), bucket):
            if k_edge_path(u.Node, t, math.ceil(k / 2), bucket):
                bucket.pop()
                print ("T")
                printStack(bucket.Stack)
                return True
        else:
            bucket.pop()

    bucket.pop()
    return False

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

k = 2**int(n)

stack = list()

stack.append("R(%s,%s,%s)" % (graph.Nodes[0].Value, graph.Nodes[(k)-1].Value, k))

bucket = Bucket(stack)
printStack(bucket.Stack)

print (str(k_edge_path(graph.Nodes[0], graph.Nodes[(k)-1], k, bucket)))