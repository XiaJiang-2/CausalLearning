import pandas as pd
import PC
import GES
import FCI
import rFCI
import FGES

# Load in the file location of dataset
fileLocation = "C:/Users/17172/Desktop/CausalLearning/sample_data/COVID3_4Nodes3.txt"
# Type in delimiter used in english i.e colon, comma, pipe, semicolon, space, tab, whitespace
fileDelimiter = "comma"

# Read dataset into dataframe
df = pd.read_csv(fileLocation)

# Adjust all categorical values to numerical
df = df.replace(to_replace='No', value=0)
df = df.replace(to_replace='Yes', value=1)
df = df.replace(to_replace='Negtive', value=0)
df = df.replace(to_replace='Positive', value=1)

# Create a PC object using the file location, it's output will be printed to the console
pcObject = PC.PC(fileLocation)
print(pcObject.output)

# # Set the output location for the png of the GES output
# GES_Output_location = 'C:/Users/17172/Desktop/CausalLearning/Outputs/GES_Output_Test.png'

# # Create the GES object, it's output will be saved as a png to the output location specified above
# gesObject = GES.GES(df, GES_Output_location)

# # Set the output location for the png of the FCI output
# FCI_Output_location = 'C:/Users/17172/Desktop/CausalLearning/Outputs/FCI_Output_Test.png'

# # Create the FCI object, it's output will be saved as a png to the output location specified above
# fciObject = FCI.FCI(df, FCI_Output_location)

# Set the output location of the output file of the rFCI output
# rFCI_Output_location = 'templates/rFCI_Outputs'
# rFCI_Output_name = "rFCI_Output"

# # Create the rFCI object, it's output will be saved as a txt file to the output location specified above
# rfciObject = rFCI.rFCI(fileLocation, fileDelimiter, rFCI_Output_location, rFCI_Output_name)

# # Set the output location of the output file of the FGES output
# FGES_Output_location = 'C:/Users/17172/Desktop/CausalLearning/Outputs'
# FGES_Output_name = "FGES_Output"

# # Create the FGES object, it's output will be saved as a txt file to the output location specified above
# fgesObject = FGES.FGES(fileLocation, fileDelimiter, FGES_Output_location, FGES_Output_name)
