import util.states.graph

from pyvis.network import Network
import colorsys

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
        # proportion = (res._visits - minVisits)/ res._visitsstategraphstategraph
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
    
    inEdges = dict()
    for (f,t) in statesGraph.getStateTransitions():
        if t not in inEdges:
            inEdges[t] = 0
        inEdges[t]+=1

    rootState = None
    for (state, edgeCnt) in inEdges:
        if edgeCnt == 0:
            rootState = state

    addNodes(statesGraph, rootState, 0)

    for (f,t) in statesGraph.getStateTransitions():
        net.add_edge(f,t,physics=True, color='black')

    net.show(f"{name}.html")