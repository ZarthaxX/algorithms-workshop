from pyvis.network import Network
import colorsys

class StateInfo:
    def __init__(self):
        self._value = None
        self._visits = 0

    def incrementVisits(self):
        self._visits += 1

    def setValue(self, value):
        self._value = value

class StatesGraph:
    def __init__(self):
        self._states = dict()
        self._stateTransitions = dict()

    def addStateVisit(self, state):
        if state not in self._states:
            self._states[state] = StateInfo()
            self._stateTransitions[state] = set()

        self._states[state].incrementVisits()

    def setStateValue(self, state, value):
        self._states[state].setValue(value)

    def addStateTransition(self, fromState, toState):
        if fromState in self._states and toState in self._states:
            self._stateTransitions[fromState].add(toState)
            return

        raise Exception()
    
    def getStateTransitions(self):
        return [(f,t) for f, transitions in self._stateTransitions.items() for t in transitions]

    def getStates(self):
        return list(self._states.items())


def trackStatesGraph(graph):
    def wrapFunc(f):
        parentNode = None
        def wrappedFunc(*args):
            nonlocal parentNode, graph

            parentNodeCopy = parentNode
            parentNode = f'{",".join(map(str,args))}'
            graph.addStateVisit(parentNode)
            if parentNodeCopy is not None: # we have a root
                graph.addStateTransition(parentNodeCopy, parentNode)

            res = f(*args)

            graph.setStateValue(parentNode,str(res))
            parentNode = parentNodeCopy

            return res
        
        return wrappedFunc
    
    return wrapFunc

def getColor(value):
    # value from 0 to 1
    hue=(1-value) * colorsys.ONE_THIRD
    r,g,b=colorsys.hls_to_rgb(hue, 0.5, 1.0)
    v = f'#{"{:02x}".format(int(r*255))}{"{:02x}".format(int(g*255))}{"{:02x}".format(int(b*255))}'
    return v

def drawTreeGraph(statesGraph, name):
    net = Network(layout="hierarchical",directed=True, height = "1000px", width = "1000px")
    visits = ([s._visits for (_,s) in statesGraph.getStates()])
    maxVisits = max(visits)
    minVisits = min(visits)
    totalVisits = sum(visits)

    visitsByState = list(set([s._visits for (_,s) in statesGraph.getStates()]))
    visitsByState.sort()
    visitsRank = dict()
    for idx, v in enumerate(visitsByState):
        visitsRank[v] = idx
    
    def addNodes(graph, args, depth):
        childs = graph._stateTransitions[args]
        for to in childs:
            addNodes(graph,to,depth+1)
        
        res = graph._states[args]

        # proportion = (res._visits - minVisits)/(maxVisits-minVisits+1)
        # proportion = (res._visits - minVisits)/ res._visits
        # proportion = res._visits / totalVisits
        proportion = visitsRank[res._visits] / len(visitsRank)
        # e = 20
        # proportion = 1 - (2**e - 2**(e*proportion)) / 2**e

        net.add_node(args,bordercolor='black',
                     label=f'args:{args}\nres:{res._value}\nvisits:{res._visits}', 
                     shape="ellipse",
                     color=getColor(proportion), 
                     level=depth,physics=False,
                     )
        
    addNodes(statesGraph, "20", 0)

    for (f,t) in statesGraph.getStateTransitions():
        net.add_edge(f,t,physics=True, color='black')

    net.show(f"{name}.html")