import pandas as pd
import PC
import GES
import FCI

# Load in the dataframe
df = pd.read_csv("C:/Users/17172/Desktop/CausalLearning/sample_data/COVID3_4Nodes3.dat")

# Adjust all categorical values to numerical
df = df.replace(to_replace='No', value=0)
df = df.replace(to_replace='Yes', value=1)
df = df.replace(to_replace='Negtive', value=0)
df = df.replace(to_replace='Positive', value=1)

# Create a PC object, it's output will be printed to the console
pcObject = PC.PC(df)

# Set the output location for the png of the GES output
GES_Output_location = 'C:/Users/17172/Desktop/CausalLearning/Outputs/GES_Output_Test.png'

# Create the GES object, it's output will be saved as a png to the output location specified above
gesObject = GES.GES(df, GES_Output_location)

# Set the output location for the png of the FCI output
FCI_Output_location = 'C:/Users/17172/Desktop/CausalLearning/Outputs/FCI_Output_Test.png'

# Create the FCI object, it's output will be save as a png to the output location specified above
fciObject = FCI.FCI(df, FCI_Output_location)
