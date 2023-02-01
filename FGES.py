import time
import os

class FGES:
    def __init__(self, fileLocation, fileDelimiter, output):
        self.fl = fileLocation
        self.delim = fileDelimiter
        self.output = output
        self.timeToComplete = self.calculateFGES()

    def calculateFGES(self):
        startTime = time.time()

        os.system("java -jar causal-cmd-1.3.0-jar-with-dependencies.jar --algorithm fges --data-type continuous --dataset " + self.fl + " --delimiter " + self.delim + " --score sem-bic-score --out " + self.output)

        return startTime - time.time()