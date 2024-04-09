import time
import statistics

def measureTime(func):
    start = time.process_time()
    func()
    end = time.process_time()
    return (end - start)

def benchmarkFunc(times,f, *args):
    func = lambda: f(*args)

    times = [measureTime(func) for _ in range(times)]

    return statistics.fmean(times)

def benchmarkFuncForCases(times, f, cases):
    results = []
    for case in cases:
        results.append(benchmarkFunc(times, f, *case))

    return results