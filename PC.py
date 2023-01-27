import numpy as np
import pandas as pd
import time

import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr, data

class PC:
    def __init__(self, dataframe):
        self.df = dataframe
        self.timeToComplete = self.calculatePC()

    def calculatePC(self): 

        # Import the basics for the MXM r package
        utils = importr('utils')
        base = importr('base')
        utils.install_packages('MXM')
        MXM = importr('MXM')

        # Start the timer for how long the algorithm takes to run
        start = time.time()

        # Run the r package MXM in order to produce the adjacency matrix using the PC algorithm
        x = robjects.r('''
            x <- read.table("C:/Users/17172/Desktop/CausalLearning/sample_data/COVID3_4Nodes3.dat", sep=",", header=TRUE)
            df <- as.data.frame.matrix(x)
            mat <- data.matrix(df)
            skeleton <- pc.skel(mat)
            DAG <- pc.or(skeleton)
            print(DAG$G)
        ''')

        # Return the length of time the algorithm took to run
        return time.time()-start