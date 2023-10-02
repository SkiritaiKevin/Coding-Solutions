#dictionary, statistics

import statistics

goals = [20, 37, 8, 17, 55, 82]

def goalStats(*values):
    stats = {}

    average = statistics.mean(values)
    stats["mean"] = average

    stdDev = statistics.stdev(values)
    stats["standard deviation"] = stdDev

    minimum = min(values)
    stats["minimum"] = minimum

    return stats

goalInfo = goalStats(*goals)
print(goalInfo)
print("The average is {:.3f}".format(goalInfo["mean"]))

