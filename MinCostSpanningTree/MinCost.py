# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 16:00:20 2016

@author: Zander
"""

class Node:
    def __init__(self, value):
        self.Value = value
        self.Edges = list()

class Edge:
    def __init__(self, fromNode, toNode, weight=1):
        self.FromNode = fromNode
        self.ToNode = toNode
        self.Weight = weight

class Graph:
    def __init__(self):
        self.Nodes = list()

    def AddNode(self, node):
        self.Nodes.append(node)

    def AddDirectedEdge(self, startNode, endNode, weight = 1):
        startNode.Edges.append(Edge(startNode, endNode, weight))

    def AddBiDirectedEdge(self, startNode, endNode, weight = 1):
        self.AddDirectedEdge(startNode, endNode, weight)
        self.AddDirectedEdge(endNode, startNode, weight)
        
    def Print(self):
        for node in self.Nodes:
            for edge in node.Edges:
                nodeValue = node.Value
                edgeNodeValue = edge.ToNode.Value
                print(str(nodeValue) + '->' + str(edgeNodeValue))

def GraphBuilder(adjacencyMatrix):
    size = len(adjacencyMatrix)
    nodes = list()
    graph = Graph()
    count = 1    
    
    for x in range(size):
        newNode = Node(count)
        nodes.append(newNode)
        graph.AddNode(newNode)
        count = count + 1
    
    for x in range(size):
        for y in range(size):
            if adjacencyMatrix[x][y] == 1:
                graph.AddDirectedEdge(nodes[x], nodes[y])
                
    graph.Print()
    
    return graph
    
class Bucket():
    def __init__(self):
        self.BucketList = list()
        
    def AddItem(self, item):
        self.BucketList.append(item)
        
    def GetAndRemoveItems(self):
        items = list()
        
        for item in self.BucketList:
            items.append(item)
        
        self.BucketList.clear()
        
        return items
    
class GraphBuckets():
    def __init__(self, nodes):
        self.Buckets = list()
        
        for node in nodes:
            bucket = Bucket()
            bucket.AddItem(node)
            self.Buckets.append(bucket)
    
    def ChangeBuckets(self, item1, item2):
        for bucket in self.Buckets:
            if (item1 in bucket.BucketList and item2 in bucket.BucketList):
                return False
            if (item1 in bucket.BucketList):
                bucket1 = bucket
                continue
            if (item2 in bucket.BucketList):
                bucket2 = bucket
                
        items = bucket2.GetAndRemoveItems()
        
        for item in items:
            bucket1.AddItem(item)
        
        return True

def MinCostSpanningTree(graph):
    mst = Graph()
    setBuckets = GraphBuckets(graph.Nodes)
    edges = set()
    
    for node in graph.Nodes:
        for edge in node.Edges:
            edges.add(edge)
        newNode = Node(node.Value)
        mst.AddNode(newNode)
    
    for edge in sorted(edges, key=lambda edge: edge.Weight):
        uIndex = graph.Nodes.index(edge.FromNode)
        vIndex = graph.Nodes.index(edge.ToNode)
        
        if (setBuckets.ChangeBuckets(edge.FromNode, edge.ToNode)):
            print("CREATING EDGE")
            mst.AddDirectedEdge(mst.Nodes[uIndex], mst.Nodes[vIndex])
    
    return mst;
    

with open('data.txt') as file:
    graphData = [[int(digit) for digit in line.strip()] for line in file]

inputGraph = GraphBuilder(graphData)

print()

MinCostSpanningTree(inputGraph).Print()