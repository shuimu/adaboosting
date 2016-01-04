
class sample(object):
    def __init__(self, feature, label, weight):
        self.feature = feature
        self.label = label
        self.weight = weight

class stump(object):
    def __init__(self, dimension, sample_L):
        self.dimension = 0
        self.threshold = 0
        self.leftLable = 0
        self.rightLable = 0
        self.error = 0
        self.weigth = 0

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



