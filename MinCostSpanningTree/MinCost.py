# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 16:00:20 2016

@author: Zander
"""

import math

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
        size = int(math.sqrt(len(self.Nodes)))

        row = 0

        self.PrintNodeLine(row, size)
        
        while (row < size - 1):
            self.PrintEdgeLine(row, size)
        
            row = row + 1
            
            self.PrintNodeLine(row, size)
    
    def PrintEdgeLine(self, row, size):
            #* - * - * - *
            #|   |   |   |
        line = ""
        
        node = row * size
        
        while (int(node / size) == row):
            node  = node + 1
            
            if (self.NodeInEdges(self.Nodes[node - 1], self.Nodes[node + size - 1].Edges) or self.NodeInEdges(self.Nodes[node + size - 1], self.Nodes[node - 1].Edges)):
                line = line + "| "
            else:
                line = line + "  "  
            
            line = line + "  "
            
        print (line)
        
    def PrintNodeLine(self, row, size):        
        line = ""
        
        node = row * size
        
        line = line + "* "
        
        node = node + 1
        
        while(int(node / size) == row):  
            
            if (self.NodeInEdges(self.Nodes[node - 1], self.Nodes[node].Edges) or self.NodeInEdges(self.Nodes[node], self.Nodes[node - 1].Edges)):
                line = line + "- "
            else:
                line = line + "  "   
                          
            line = line + "* "
                
            node = node + 1            
        
        print(line)
        
    def NodeInEdges(self, node, edges):
        for edge in edges:
            if edge.ToNode == node:
                return True
        
        return False

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
            mst.AddDirectedEdge(mst.Nodes[uIndex], mst.Nodes[vIndex])
    
    return mst

file2 = (open('graph.txt', 'r')).read().split("(")
graphTreeData = list()
for numberSet in file2:
    singleEdge = list()
    temp = ""
    for digit in numberSet:
        if digit.isdigit():
            temp = temp + digit
        elif temp != "":
            singleEdge.append(temp)
            temp = ""
    graphTreeData.append(singleEdge)

#graphTreeData = [int(x) for x in graphTreeData.split() if x.isdigit()]

def buildTree(data):
    print("Tree data: " + str(data))
    nGrid = int(data[0][0]) ** 2

    tree = Graph()

    for x in range(nGrid):
        tree.AddNode(Node(x + 1))

    count = 1

    while (count < len(data)):
        startNode = list(filter(lambda node: node.Value == int(data[count][0]), tree.Nodes))
        endNode = list(filter(lambda node: node.Value == int(data[count][1]), tree.Nodes))
        tree.AddDirectedEdge(startNode[0], endNode[0], int(data[count][2]))

        count = count + 1

    return tree

t = buildTree(graphTreeData)

t.Print()

print()

MinCostSpanningTree(t).Print()