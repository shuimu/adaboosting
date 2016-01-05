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
        self.leftLabel_x = None
        self.rightLabel_x = None
        self.sample_L = sample_L
        self.total_error = sum([sample_x.weight for sample_x in sample_L])
        
        ## get the best threshold ##
        for sample_x in sample_L:
            threshold_x = sample_x.feature[self.dimension]
            error_rate_x = self.getErrorRate(threshold_x)
            if self.error_rate is None or self.error_rate > error_rate_x:
                self.threshold = threshold_x
                self.leftLabel = self.leftLabel_x
                self.rightLabel = self.rightLabel_x
                self.error_rate = error_rate_x 
        self.weight = self.getWeight() 

    def getWeight(self): 
        return 0.5*math.log((1-self.error_rate)/max(self.error_rate, 0.0001))

    def getErrorRate(self, threshold_x):
        left_1_error = 0.0
        left_0_error = 0.0
        right_1_error = 0.0
        right_0_error = 0.0
        ## get left errors ##
        for sample_y in self.sample_L:
            if sample_y.feature[self.dimension] <= threshold_x:
                if sample_y.label == -1:
                    left_1_error += sample_y.weight
                else:
                    left_0_error += sample_y.weight
            else:
                if sample_y.label == -1:
                    right_1_error += sample_y.weight
                else:
                    right_0_error += sample_y.weight
        ## get error and labels ##
        if left_1_error < left_0_error:
            self.leftLabel_x = 1
        else:
            self.leftLabel_x = -1
        if right_1_error < right_0_error:
            self.rightLabel_x = 1
        else:
            self.rightLabel_x = -1
        return (min(left_1_error, left_0_error) + min(right_1_error, right_0_error))/self.total_error

    def reWeightSample(self):
        for i in range(len(self.sample_L)):
            if (self.sample_L[i].feature[self.dimension] <= self.threshold and self.leftLabel == self.sample_L[i].label) \
                or (self.sample_L[i].feature[self.dimension] > self.threshold and self.rightLabel == self.sample_L[i].label): 
                self.sample_L[i].weight *= math.sqrt(self.error_rate/max(1-self.error_rate, 0.0001))
            else:
                self.sample_L[i].weight *= math.sqrt((1-self.error_rate)/max(self.error_rate, 0.0001))

    def predict(self, sample_x):
        if sample_x.feature[self.dimension] <= self.threshold:
            return self.leftLabel
        else: return self.rightLabel

nWeak = 40
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
    inFp.close()

    ## train weak classfier ##
    for t in range(nWeak):
        dimension = t % 2
        stump_x = stump(dimension, sample_L)
        stump_x.reWeightSample()                
        print "...."
        print "the dimension is %d"%stump_x.dimension
        print "the threshold is %.9f"%stump_x.threshold
        print "the leftLabel is %d"%stump_x.leftLabel
        print "the rightLabel is %d"%stump_x.rightLabel
        print "the error_rate is %.9f"%stump_x.error_rate 
        print "the weight is %.9f"%stump_x.weight
        print [sample_x.weight for sample_x in sample_L]
        stump_L.append(stump_x)

    ## predict ##
    for sample_x in sample_L:
        predict_one = 0
        for stump_x in stump_L:
            predict_one += stump_x.weight*stump_x.predict(sample_x)
        if predict_one > 0:
            print "predict is 1"
        else:
            print "predict is -1"

if __name__ == "__main__": 
    run() 

