# SOLVER CLASSES WHERE AGENT CODES GO
from helper import *
import random
import math


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
    def getSolution(self, state, maxIterations=-1):
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None
        
        # YOUR CODE HERE




        return []                       #remove me
        #return bestNode.getActions()   #uncomment me



# DFS Agent Code
class DFSAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None

        # YOUR CODE HERE




        return []                       #remove me
        #return bestNode.getActions()   #uncomment me



#####    ASSIGNMENT 2 AGENTS    #####



# AStar Agent Code
class AStarAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        #setup
        balance = 1
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None
        Node.balance = balance

        #initialize priority queue
        queue = PriorityQueue()
        queue.put(Node(state.clone(), None, None))
        visited = set()

        while (iterations < maxIterations or maxIterations <= 0) and queue.qsize > 0:
            iterations += 1

            ## YOUR CODE HERE ##




        return bestNode.getActions()


# Hill Climber Agent code
class HillClimberAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        #setup
        intializeDeadlocks(state)
        iterations = 0
        
        seqLen = 50            # maximum length of the sequences generated
        coinFlip = 0.5          # chance to mutate

        #initialize the first sequence (random movements)
        bestSeq = []
        for i in range(seqLen):
            bestSeq.append(random.choice(directions))

        #mutate the best sequence until the iterations runs out or a solution sequence is found
        while (iterations < maxIterations):
            iterations += 1
            
            ## YOUR CODE HERE ##




        #return the best sequence found
        return bestSeq  



#####    ASSIGNMENT 3 AGENTS    #####


# Genetic Algorithm code
class GeneticAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        #setup
        intializeDeadlocks(state)

        iterations = 0
        seqLen = 50             # maximum length of the sequences generated
        popSize = 10            # size of the population to sample from
        parentRand = 0.5        # chance to select action from parent 1 (50/50)
        mutRand = 0.3           # chance to mutate offspring action

        bestSeq = []            #best sequence to use in case iterations max out

        bestEval = float('inf')
        #initialize the population with sequences of 50 actions (random movements)
        population = []
        for p in range(popSize):
            bestSeq = []
            for i in range(seqLen):
                bestSeq.append(random.choice(directions))
            population.append(bestSeq)

        #mutate until the iterations runs out or a solution sequence is found
        while (iterations < maxIterations):
            iterations += 1

            #1. evaluate the population
            eval = []
            for seq in population:
                newState = state.clone()
                v = -1
                for i in range(seqLen):
                    newState.update(seq[i]["x"], seq[i]["y"])
                    if newState.checkWin():
                        v = 0
                        break
                if v == -1:
                    eval.append(getHeuristic(newState))
                else:
                    eval.append(0)

            #2. sort the population by fitness (low to high)
            eval = list(enumerate(eval))
            eval.sort(key=lambda x:x[1])
            population = [population[i] for i, _ in eval]

            #2.1 save bestSeq from best evaluated sequence
            if bestEval > eval[0][1]:
                bestEval = eval[0][1]
                bestSeq = population[0]
                if bestEval == 0:
                    newState = state.clone()
                    for i in range(seqLen):
                        newState.update(bestSeq[i]["x"], bestSeq[i]["y"])
                        if newState.checkWin():
                            bestSeq = bestSeq[:i+1]
                            break
                    

            #3. generate probabilities for parent selection based on fitness
            denom = (1+popSize) * popSize // 2
            probs = [(popSize-i)/denom for i in range(popSize)]


            #4. populate by crossover and mutation
            new_pop = []
            for i in range(int(popSize/2)):
                #4.1 select 2 parents sequences based on probabilities generated
                par1 = []
                par2 = []
                rand1, rand2 = random.random(), random.random()
                summ = 0
                for i in range(popSize):
                    summ += probs[i]
                    if not par1 and summ >= rand1:
                        par1 = population[i]
                    if not par2 and summ >= rand2:
                        par2 = population[i]
                    if par1 and par2:
                        break

                #4.2 make a child from the crossover of the two parent sequences
                offspring = []
                for i in range(seqLen):
                    if random.random() < parentRand:
                        offspring.append(par1[i])
                    else:
                        offspring.append(par2[i])


                #4.3 mutate the child's actions
                for i in range(seqLen):
                    if random.random() < mutRand:
                        offspring[i] = random.choice(directions)

                #4.4 add the child to the new population
                new_pop.append(list(offspring))


            #5. add top half from last population (mu + lambda)
            new_pop += population[:popSize-int(popSize/2)]


            #6. replace the old population with the new one
            population = list(new_pop)

        #return the best found sequence 
        return bestSeq

# MCTS Specific node to keep track of rollout and score
class MCTSNode(Node):
    def __init__(self, state, parent, action, maxDist):
        super().__init__(state,parent,action)
        self.children = []  #keep track of child nodes
        self.n = 0          #visits
        self.q = 0          #score
        self.maxDist = maxDist      #starting distance from the goal (heurstic score of initNode)

    #update get children for the MCTS
    def getChildren(self,visited):
        #if the children have already been made use them
        if(len(self.children) > 0):
            return self.children

        children = []
        for d in directions:
            childState = self.state.clone()
            crateMove = childState.update(d["x"], d["y"])
            if childState.player["x"] == self.state.player["x"] and childState.player["y"] == self.state.player["y"]:
                continue
            if crateMove and checkDeadlock(childState):
                continue
            if getHash(childState) in visited:
                print('seen')
                continue
            children.append(MCTSNode(childState, self, d, self.maxDist))

        self.children = list(children)    #save node children to generated child

        return children

    #calculates the score the distance from the starting point to the ending point (closer = better = larger number)
    def calcEvalScore(self,state):
        return self.maxDist - getHeuristic(state)

    #compares the score of 2 mcts nodes
    def __lt__(self, other):
        return self.q < other.q

    def __str__(self):
        return str(self.q) + ", " + str(self.n) + ' - ' + str(self.getActions())


# Monte Carlo Tree Search Algorithm code
class MCTSAgent(Agent):
    def getSolution(self, state, maxIterations=-1):
        #setup
        intializeDeadlocks(state)
        iterations = 0
        bestNode = None
        initNode = MCTSNode(state.clone(), None, None, getHeuristic(state))

        while(iterations < maxIterations):
            #print("\n\n---------------- ITERATION " + str(iterations+1) + " ----------------------\n\n")
            iterations += 1

            #mcts algorithm
            rollNode = self.treePolicy(initNode)
            score = self.rollout(rollNode)
            self.backpropogation(rollNode, score)

            #if in a win state, return the sequence
            if(rollNode.checkWin()):
                return rollNode.getActions()

            #set current best node
            bestNode = self.bestChildUCT(initNode)

            #if in a win state, return the sequence
            if(bestNode.checkWin()):
                return bestNode.getActions()


        #return solution of highest scoring descendent for best node
        print("timeout")
        return self.bestActions(bestNode)
        

    #returns the descendent with the best action sequence based
    def bestActions(self, node):
        bestActionSeq = []
        while(len(node.children) > 0):
            node = self.bestChildUCT(node)

        return node.getActions()


    ####  MCTS SPECIFIC FUNCTIONS BELOW  ####

    #determines which node to expand next
    def treePolicy(self, rootNode):
        curNode = rootNode
        visited = []

        ## YOUR CODE HERE ##

        while not checkDeadlock(curNode.state) and not curNode.checkWin():
            if not curNode.children:
                visited.extend(curNode.getChildren(visited))
                return random.choice(curNode.children)
            else:
                curNode = self.bestChildUCT(curNode)

        return curNode



    # uses the exploitation/exploration algorithm
    def bestChildUCT(self, node):
        c = 1               #c value in the exploration/exploitation equation
        bestChild = None

        ## YOUR CODE HERE ##
        epsilon = 0.000001
        bestVal = -float('inf')
        for child in node.children:
            childVal = child.q / (child.n+epsilon) + c*math.sqrt(2*math.log(node.n+1)/(child.n+epsilon))
            if child.checkWin():
                return child
            if childVal > bestVal:
                bestChild = child
                bestVal = childVal

        return bestChild



     #simulates a score based on random actions taken
    def rollout(self,node):
        numRolls = 7        #number of times to rollout to

        ## YOUR CODE HERE ##
        state = node.state.clone()
        for _ in range(numRolls):
            d = random.choice(directions)
            state.update(d["x"], d["y"])
            if (state.checkWin()):
                return float('inf')

        return node.calcEvalScore(state)



     #updates the score all the way up to the root node
    def backpropogation(self, node, score):
        ## YOUR CODE HERE ##
        while node:
            node.n += 1
            node.q += score
            node = node.parent
        return
        

