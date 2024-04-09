import util.complexity
import pandas as pd
import matplotlib.pyplot as plt

def getFuncComplexityAnalysis(Ns, cases, realTimes, 
                              worstFuncSymbol,worstFunc, 
                              bestFuncSymbol, bestFunc, 
                              avgFuncSymbol,avgFunc, 
                              n_0 = 0):
    worstCurve = util.complexity.fitWorstCaseCurve(cases, realTimes, worstFunc, n_0)
    worstCurveDf = pd.DataFrame({
        "Real time": realTimes,
        f"c {worstFuncSymbol}": worstCurve,
    }, index = Ns)
        
    bestCurve = util.complexity.fitBestCaseCurve(cases, realTimes, bestFunc, n_0)
    bestCurveDf = pd.DataFrame({
        "Real time": realTimes,
        f"c {bestFuncSymbol}": bestCurve,
    }, index = Ns)

    avgCurves = util.complexity.fitAverageCaseCurves(cases, realTimes,avgFunc, n_0)
    avgCurveDf = pd.DataFrame({
        "Real time": realTimes,
        f"c₁ {avgFuncSymbol}": avgCurves[0],
        f"c₂ {avgFuncSymbol}": avgCurves[1],
    }, index = Ns)


    _, axes = plt.subplots(3, 1, figsize=(8, 15))

    axes[0].title.set_text(f"Algorithm O({worstFuncSymbol})")
    axes[0].set_xlabel("N")
    axes[0].set_ylabel("time (ms)")
    worstCurveDf.plot(ax=axes[0])
    axes[1].title.set_text(f"Algorithm Ω({bestFuncSymbol})")
    axes[1].set_xlabel("N")
    axes[2].set_ylabel("time (ms)")
    bestCurveDf.plot(ax=axes[1])
    axes[2].title.set_text(f"Algorithm Θ({avgFuncSymbol})")
    axes[2].set_xlabel("N")
    axes[2].set_ylabel("time (ms)")
    avgCurveDf.plot(ax=axes[2])

    plt.show()