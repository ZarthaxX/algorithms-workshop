import util.complexity
import pandas as pd
import matplotlib.pyplot as plt

def setAsymptoticTable(axe, 
                       y_axis_label, 
                       x_axis_label, 
                       funcSymbol,
                       asymptoticSymbol,
                       n_0):
    axe.title.set_text(f"Algoritmo f({x_axis_label}) ∈ {asymptoticSymbol}({funcSymbol})")
    axe.set_xlabel(x_axis_label)
    axe.set_ylabel(y_axis_label)
    axe.axvline(n_0, color='r', linestyle='--', linewidth=1)

def setBigOTable(axes, y_axis_label, x_axis_label, funcSymbol, n_0):
    setAsymptoticTable(axes[0], y_axis_label, x_axis_label, funcSymbol, "O", n_0)

def setBigOmegaTable(axes, y_axis_label, x_axis_label, funcSymbol, n_0):
    setAsymptoticTable(axes[1], y_axis_label, x_axis_label, funcSymbol, "Ω", n_0)

def setBigThetaTable(axes, y_axis_label, x_axis_label, funcSymbol, n_0):
    setAsymptoticTable(axes[2], y_axis_label, x_axis_label, funcSymbol, "Θ", n_0)

def plotFuncComplexityAnalysis(Ns, cases, realTimes, 
                              bigOFuncSymbol,bigOFunc, 
                              bigOmegaFuncSymbol, bigOmegaFunc, 
                              bigThetaFuncSymbol,bigThetaFunc, 
                              n_0 = 0,
                              y_axis_label = "tiempo (ms)",
                              x_axis_label = "n"
                             ):
    bigOCurve = util.complexity.fitWorstCaseCurve(cases, realTimes, bigOFunc, n_0)
    bigOCurveDf = pd.DataFrame({
        f"f({x_axis_label})": realTimes,
        f"C g({x_axis_label})": bigOCurve,
    }, index = Ns)
        
    bigOmegaCurve = util.complexity.fitBestCaseCurve(cases, realTimes, bigOmegaFunc, n_0)
    bigOmegaCurveDf = pd.DataFrame({
        f"f({x_axis_label})": realTimes,
        f"C g({x_axis_label})": bigOmegaCurve,
    }, index = Ns)

    bigThetaCurves = util.complexity.fitAverageCaseCurves(cases, realTimes,bigThetaFunc, n_0)
    bigThetaCurveDf = pd.DataFrame({
         f"f({x_axis_label})": realTimes,
        f"C₁ g({x_axis_label})": bigThetaCurves[0],
        f"C₂ g({x_axis_label})": bigThetaCurves[1],
    }, index = Ns)

    _, axes = plt.subplots(3, 1, figsize=(8, 15))

    setBigOTable(axes, y_axis_label, x_axis_label, bigOFuncSymbol, Ns[n_0])
    bigOCurveDf.plot(ax=axes[0])
    setBigOmegaTable(axes, y_axis_label, x_axis_label, bigOmegaFuncSymbol, Ns[n_0])
    bigOmegaCurveDf.plot(ax=axes[1])
    setBigThetaTable(axes, y_axis_label, x_axis_label, bigThetaFuncSymbol, Ns[n_0])
    bigThetaCurveDf.plot(ax=axes[2])

    plt.show()

def plotFuncBigOAnalysis(Ns, cases, realTimes, 
                              bigOFuncSymbol,bigOFunc, 
                              n_0 = 0,
                              y_axis_label = "tiempo (ms)",
                              x_axis_label = "n"
                             ):
    bigOCurve = util.complexity.fitWorstCaseCurve(cases, realTimes, bigOFunc, n_0)
    bigOCurveDf = pd.DataFrame({
        f"f({x_axis_label})": realTimes,
        f"C g({x_axis_label})": bigOCurve,
    }, index = Ns)
        
    _, ax = plt.subplots(1, 1, figsize=(8, 8))

    ax.title.set_text(f"Algoritmo f({x_axis_label}) ∈ O({bigOFuncSymbol})")
    ax.set_xlabel(x_axis_label)
    ax.set_ylabel(y_axis_label)
    ax.axvline(Ns[n_0], color='r', linestyle='--', linewidth=1)
    bigOCurveDf.plot(ax=ax)

    plt.show()