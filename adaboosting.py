import math

class sample(object):
    def __init__(self, feature, label, weight):
        self.feature = feature
        self.label = label
        self.weight = weight

class stump(object):
    def __init__(self, dimension, sample_L):
        self.dimension = dimension
        self.threshold = None
        self.leftLabel = None
        self.rightLabel = None
        self.error_rate = None
        self.weight = None
        self.total_error = sum([sample_x.weight for sample_x in sample_L])

        ## get the best threshold ##
        for sample_x in sample_L:
            threshold_x = sample_x.feature[self.dimension]
            leftLabel_x = None
            rightLabel_x = None
            error_rate_x = self.getErrorRate(threshold_x, leftLabel_x, rightLabel_x)
            if self.error_rate is None or self.error_rate > error_rate_x:
                self.threshold = threshold_x
                self.leftLabel = leftLabel_x
                self.rightLabel = rightLabel_x
                self.error_rate = error_rate_x 
        self.weight = self.getWeight() 

    def getWeight(): 
        return 0.5*math.log((1-self.error_rate)/max(self.error_rate, 0.0001))

    def getError(self, threshold_x, leftLabel_x, rightLabel_x):
        left_1_error = 0.0
        left_0_error = 0.0
        right_1_error = 0.0
        right_0_error = 0.0
        ## get left errors ##
        for sample_y in sample_L:
            if sample_y.feature[self.dimension] <= threshold_x:
                if sample_y.label == 0:
                    left_1_error += sample_y.weight
                else:
                    left_0_error += sample_y.weight
            else:
                if sample_y.label == 0:
                    right_1_error += sample_y.weight
                else:
                    right_0_error += sample_y.weight
        ## get error and labels ##
        if left_1_error < left_0_error:
            leftLabel_x = 1
        else:
            leftLabel_x = 0
        if right_1_error < right_0_error:
            rightLabel_x = 1
        else:
            rightLabel_x = 0
        return (min(left_1_error, left_0_error) + min(right_1_error, right_0_error))/self.total_error

    def reWeightSample():
        pass 

nWeak = 4
nSample = -1
sample_L = []
stump_L = []

def run():
    ## input data ##
    inFp = open("sample", 'r')
    nSample = int(inFp.readline().strip())
    while True:
        line = inFp.readline()
        if not line:
            break
        item = map(int, line.strip().split("\t"))
        sample_x = sample(item[1:], item[0], 1.0/nSample)
        sample_L.append(sample_x)
        print sample_x.feature
    inFp.close()

    ## train weak classfier ##
    for t in range(nWeak):
        dimension = t % 2
        stump_x = stump(dimension, sample_L)
        stump_x.reWeightSample()                

        
if __name__ == "__main__": 
    run() 
