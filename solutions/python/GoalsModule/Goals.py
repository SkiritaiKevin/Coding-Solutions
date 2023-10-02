import statistics

def goalStats(*values):
    stats = {}

    average = statistics.mean(values)
    stats["mean"] = average

    stdDev = statistics.stdev(values)
    stats["standard deviation"] = stdDev

    minimum = min(values)
    stats["minimum"] = minimum

    return stats