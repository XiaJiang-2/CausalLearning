# CausalLearning
This package combines MXM, Causallearn, and Causal CMD in order to have ease of access to multiple causal learning algorithms.

Dependencies:
- Pandas
- Causallearn
- rpy2
- numpy
- matplotlib
- pydot

### Algorithm's available

Currently there are 5 working functions:
- PC (MXM)
- GES (Causallearn)
- FCI (Causallearn)
- rFCI (Causal CMD)
- FGES (Causal CMD)

These algorithms use the dataset COVID3_4Nodes3.dat in the sample_data directory for all examples.

If you have any further issues in determing how these functions operate or how their internal functions work, it is highly encouraged you check out the original packages documentation, which can be found below.

<br/>

[Causallearn] (https://github.com/cmu-phil/causal-learn)

[MXM] (https://cran.r-project.org/web/packages/MXM/index.html)

[Causal CMD] (https://bd2kccd.github.io/docs/causal-cmd/)

## How to use

This section is to give a simple explanation of how to use the causalLearn.py in order to implement any of the currently available functions for your own dataset.

1. Set the location for your dataset. Import your dataset using the file location and pandas, and ensure all values in your dataset are numeric. In the sample causalLearn.py, most of the values are "negative" or "positive", these are then adjusted to be 0 and 1, respectively, in order for the algorithms to properly work.

![Image 1 Causal Learning](https://user-images.githubusercontent.com/79263753/216166746-8aad9636-844d-4d95-ad61-09dcd3f2ee91.png)

2. Create the object of the algorithm you want to use. For PC, only the datasets location is required as the output will be in the terminal. For both GES and FCI, both the dataframe and the location of the output for the png are required, as both these functions produce pngs as their respective outputs. For both FGES and rFCI, the dataset location is required (the dataset is also required to be a txt file), the delimiter used for the file (i.e. colon, comma, pipe, semicolon, space, tab, whitespace), and the output location, as both these functions produce txt files as their respective outputs.

![Image 2 Causal learning](https://user-images.githubusercontent.com/79263753/216165765-513e1e9d-15b6-4813-8252-8123bf1b6e65.png)

3. Run the program. PC will output to the console, FCI and GES will output to the desired location as pngs, and rFCI and FGES will output to the desired location as txt files.

The current causalLearn.py has examples of all the current algorithms using the COVID3_4Nodes3.dat dataset for the examples.
