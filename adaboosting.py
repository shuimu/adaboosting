
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
        self.error = None
        self.weigth = None
        
        ## get the best threshold ##
        for sample_x in sample_L:
            threshold_x = sample_x.feature[self.dimension]
            leftLabel_x = None
            rightLabel_x = None
            error_x = self.getError(leftLabel_x, rightLabel_x)
            if self.error is None or self.error > error_x:
                self.threshold = threshold_x
                self.leftLabel = leftLabel_x
                self.rightLabel = rightLabel_x
                self.error = error_x 
        self.weigth = self.getWeight() 

    def getWeight():
        pass

    def getError(self, leftLabel_x, rightLabel_x):
        pass

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

        
if __name__ == "__main__": run() 

