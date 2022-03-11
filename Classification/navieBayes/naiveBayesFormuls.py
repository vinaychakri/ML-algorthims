import math
import statistics

# navieBayesGaussian formula


def navieBayesGaussian(xival, yval):
    square = 1/(math.sqrt(2*math.pi*statistics.variance(yval)))
    for i in xival:
        gaussian = square * \
            (math.exp(-((i-statistics.mean(yval))**2) / (2*statistics.variance(yval))))
        print(gaussian)


y = [1, 2]
x = [1, 2, 3, 4, 4, 5]
navieBayesGaussian(x, y)
