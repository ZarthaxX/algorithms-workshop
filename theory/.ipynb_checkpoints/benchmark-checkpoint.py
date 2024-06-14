import time
import statistics
import copy

def measureTime(func):
    start = time.process_time_ns()
    func()
    end = time.process_time_ns()
    return (end - start) / 10**6

def benchmarkFunc(times,f, args, copyCase = False):
    def runner():
        argsCopy = args
        if copyCase:
            argsCopy = copy.deepcopy(args)
        return measureTime(lambda: f(*argsCopy))

    times = [runner() for _ in range(times)]

    return statistics.fmean(times)

def benchmarkFuncForCases(times, f, cases, copyCase = False):
    results = []
    for case in cases:
        results.append(benchmarkFunc(times, f, case, copyCase))

    return results