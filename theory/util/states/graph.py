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