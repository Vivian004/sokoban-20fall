# SOLVER CLASSES WHERE AGENT CODES GO
from helper import *
import random


# Base class of agent (DO NOT TOUCH!)
class Agent:
    def getSolution(self, state, maxIterations):
        return []  # set of actions


#####       EXAMPLE AGENTS      #####

# Do Nothing Agent code - the laziest of the agents
class DoNothingAgent(Agent):
    def getSolution(self, state, maxIterations):
        if maxIterations == -1:  # RIP your machine if you remove this block
            return []

        # make idle action set
        nothActionSet = []
        for i in range(20):
            nothActionSet.append({"x": 0, "y": 0})

        return nothActionSet


# Random Agent code - completes random actions
class RandomAgent(Agent):
    def getSolution(self, state, maxIterations):

        # make random action set
        randActionSet = []
        for i in range(20):
            randActionSet.append(random.choice(directions))

        return randActionSet


#####    ASSIGNMENT 1 AGENTS    #####


# BFS Agent code
class BFSAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE

        return []  # remove me
        # return bestNode.getActions()   #uncomment me


# DFS Agent Code
class DFSAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE

        return []  # remove me
        # return bestNode.getActions()   #uncomment me


#####    ASSIGNMENT 2 AGENTS    #####


# AStar Agent Code
class AStarAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        # setup
        balance = 1
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None
        Node.balance = balance

        # initialize priority queue
        queue = PriorityQueue()
        queue.put(Node(state.clone(), None, None))
        visited = set()

        while (iterations < maxIterations or maxIterations <= 0) and queue.qsize() > 0:
            iterations += 1

            ## YOUR CODE HERE ##
            topNode = queue.get()
            visited.add(topNode)
            if topNode.checkWin():
                bestNode = topNode
                break
            if (
                not bestNode
                or topNode.getCost() + topNode.getHeuristic()
                < bestNode.getCost() + bestNode.getHeuristic()
            ):
                bestNode = topNode
            for childNode in topNode.getChildren():
                if childNode.getHash() not in visited:
                    visited.add(childNode.getHash())
                    queue.put(childNode)

        return bestNode.getActions()


# Hill Climber Agent code
class HillClimberAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        # setup
        intializeDeadlocks(state)
        iterations = 0

        seqLen = 50  # maximum length of the sequences generated
        coinFlip = 0.5  # chance to mutate

        # initialize the first sequence (random movements)
        bestSeq = []
        for i in range(seqLen):
            bestSeq.append(random.choice(directions))

        # mutate the best sequence until the iterations runs out or a solution sequence is found
        while iterations < maxIterations:
            iterations += 1

            ## YOUR CODE HERE ##
            mutates = bestSeq
            oldState = state.clone()
            newState = state.clone()
            for i in range(seqLen):
                if random.random() < coinFlip:
                    mutates[i] = random.choice(directions)
                else:
                    mutates[i] = bestSeq[i]
                oldState.update(bestSeq[i]["x"], bestSeq[i]["y"])
                newState.update(mutates[i]["x"], mutates[i]["y"])
                if oldState.checkWin():
                    return bestSeq[: i + 1]
            if getHeuristic(newState) < getHeuristic(oldState):
                bestSeq = newState

        # return the best sequence found
        return bestSeq


#####    ASSIGNMENT 3 AGENTS    #####


# Genetic Algorithm code
class GeneticAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        # setup
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE

        return []  # remove me
        # return bestNode.getActions()   #uncomment me


# Monte Carlo Tree Search Algorithm code
class MCTSAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        # setup
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE

        return []  # remove me
        # return bestNode.getActions()   #uncomment me
