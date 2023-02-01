import time
import os

class rFCI:
    def __init__(self, fileLocation, fileDelimiter, output):
        self.fl = fileLocation
        self.delim = fileDelimiter
        self.output = output
        self.timeToComplete = self.calculateRFCI()

    def calculateRFCI(self):
        startTime = time.time()

        os.system("java -jar causal-cmd-1.3.0-jar-with-dependencies.jar --algorithm rfci --data-type continuous --dataset " + self.fl + " --delimiter " + self.delim + " --test fisher-z-test --out " + self.output)

        return startTime - time.time()