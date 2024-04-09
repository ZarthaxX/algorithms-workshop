EPSILON = 0.0000000001

def getCoeff(realTimes, theoricalTimes, n_0, op):
    coeff = op([realTimes[i] / theoricalTimes[i] for i in range(n_0, len(realTimes))])
    
    return list(map(lambda e: e * coeff, theoricalTimes))

def adjustUpper(realTimes, theoricalTimes, n_0):
    return getCoeff(realTimes, theoricalTimes, n_0, max)

def fitWorstCaseCurve(cases, realTimes, worstCaseFunc, n_0 = 0):
    theoricalTimes = [worstCaseFunc(*c) for c in cases]
    
    return adjustUpper(realTimes, theoricalTimes, n_0)

def adjustBottom(realTimes, theoricalTimes, n_0):
    return getCoeff(realTimes, theoricalTimes, n_0, min)

def fitBestCaseCurve(cases, realTimes, bestCaseFunc, n_0 = 0):
    theoricalTimes = [bestCaseFunc(*c) for c in cases]

    return adjustBottom(realTimes, theoricalTimes, n_0)

def fitAverageCaseCurves(cases, realTimes, averageCaseFunc, n_0 = 0):
    theoricalTimes = [averageCaseFunc(*c) for c in cases]

    return adjustUpper(realTimes, theoricalTimes, n_0), \
           adjustBottom(realTimes, theoricalTimes, n_0)

def fitRealCurve(cases, realTimes, fittingCurve, errorEpsilon = 0.00000001):
    theoricalTimes = [fittingCurve(*c) for c in cases]
    
    realSum = sum(realTimes)
    theoricalSum = sum(theoricalTimes)

    l = 0
    r = 1000000000
    while r - l > errorEpsilon:
        m = (r+l)/2

        error = m * theoricalSum - realSum

        if error > 0:
            r = m
        else:
            l = m
        
    coeff = (r+l)/2
    return list(map(lambda e: e * coeff, theoricalTimes))
