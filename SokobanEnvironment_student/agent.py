# SOLVER CLASSES WHERE AGENT CODES GO
from helper import *
import random

# Base class of agent (DO NOT TOUCH!)
class Agent:
    def getSolution(self, state, maxIterations):
        return []       # set of actions


#####       EXAMPLE AGENTS      #####

# Do Nothing Agent code - the laziest of the agents
class DoNothingAgent(Agent):
    def getSolution(self, state, maxIterations):
        if maxIterations == -1:     # RIP your machine if you remove this block
            return []

        #make idle action set
        nothActionSet = []
        for i in range(20):
            nothActionSet.append({"x":0,"y":0})

        return nothActionSet

# Random Agent code - completes random actions
class RandomAgent(Agent):
    def getSolution(self, state, maxIterations):

        #make random action set
        randActionSet = []
        for i in range(20):
            randActionSet.append(random.choice(directions))

        return randActionSet


#####    ASSIGNMENT 1 AGENTS    #####


# BFS Agent code
class BFSAgent(Agent):        
    def BFS(self, node, visited, maxIterations):
        restIterations = maxIterations if maxIterations >= 0 else float("inf")

        if node.checkWin():
            return node
            
        bestNode = None
        visited.add(node.getHash())
        queue = [node]

        while restIterations > 0 and queue:
            restIterations -= 1
            node = queue.pop()
            for childNode in node.getChildren():
                childHash = childNode.getHash()
                if childHash not in visited:
                    visited.add(childHash)
                    if childNode.checkWin():
                        return childNode
                    if not bestNode:
                        bestNode = childNode
                    else:
                        child_heu, best_heu = childNode.getHeuristic(), bestNode.getHeuristic()
                        if child_heu < best_heu or (child_heu == best_heu and childNode.getCost() < node.getCost()):
                            bestNode = childNode
                    queue.insert(0, childNode)
        return bestNode

    def getSolution(self, state, maxIterations=-1):
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None
        
        # YOUR CODE HERE
        initialNode = Node(state=state, parent=None, action=None)
        bestNode = self.BFS(node=initialNode, visited=set(), maxIterations=maxIterations)

        if bestNode:
            return bestNode.getActions()   #uncomment me
        return []



# DFS Agent Code
class DFSAgent(Agent):

    def DFS(self, node, visited, maxIterations):
        restIterations = maxIterations if maxIterations >= 0 else float("inf")

        if node.checkWin():
            return node

        bestNode = None
        visited.add(node.getHash())
        stack = [node]

        while restIterations > 0 and stack:
            restIterations -= 1
            node = stack.pop()
            for childNode in node.getChildren():
                childHash = childNode.getHash()
                if childHash not in visited:
                    visited.add(childHash)
                    if childNode.checkWin():
                        return childNode
                    if not bestNode:
                        bestNode = childNode
                    else:
                        child_heu, best_heu = childNode.getHeuristic(), bestNode.getHeuristic()
                        if child_heu < best_heu or (child_heu == best_heu and childNode.getCost() < node.getCost()):
                            bestNode = childNode
                    stack += childNode,
        return bestNode

    def getSolution(self, state, maxIterations=-1):
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE

        initialNode = Node(state=state, parent=None, action=None)
        bestNode = self.DFS(node=initialNode, visited=set(), maxIterations=maxIterations)

        if bestNode:
            return bestNode.getActions()   #uncomment me
        return []



# AStar Agent Code
class AStarAgent(Agent):
    def insert(self, arr, target):
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r) // 2
            if arr[mid] > target:
                l = mid+1
            else:
                r = mid
        arr.insert(l, target)

    def Astar(self, node, visited, maxIterations):
        restIterations = maxIterations if maxIterations >= 0 else float("inf")

        bestNode = None
        hq = [(node.getCost()+node.getHeuristic(), node)]
        while hq and restIterations > 0:
            restIterations -= 1
            value, topNode = hq.pop()
            if topNode.checkWin():
                return topNode
            if not bestNode or value < bestNode.getCost()+bestNode.getHeuristic():
                bestNode = topNode
            for childNode in topNode.getChildren():
                if childNode.getHash() not in visited:
                    visited.add(childNode.getHash())
                    self.insert(hq, (childNode.getCost()+childNode.getHeuristic(), childNode))
        return bestNode



    def getSolution(self, state, maxIterations=-1):
        balance=1

        intializeDeadlocks(state)
        iterations = 0
        bestNode = None
        Node.balance = balance
        
        # YOUR CODE HERE
        initialNode = Node(state=state, parent=None, action=None)
        bestNode = self.Astar(node=initialNode, visited=set(), maxIterations=maxIterations)

        if bestNode:
            return bestNode.getActions()   #uncomment me
        return []                       #remove me


#####    ASSIGNMENT 2 AGENTS    #####


# Hill Climber Agent code
class HillClimberAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        #setup
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE




        return []                       #remove me
        #return bestNode.getActions()   #uncomment me


# Genetic Algorithm code
class GeneticAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        #setup
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE




        return []                       #remove me
        #return bestNode.getActions()   #uncomment me


# Monte Carlo Tree Search Algorithm code
class MCTSAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        #setup
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE


        

        return []                       #remove me
        #return bestNode.getActions()   #uncomment me
