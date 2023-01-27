# CausalLearning
This package combines two other causal learning packages, pycausal and causallearn, in order to have ease of access to multiple causal learning algorithms.

Dependencies:
- Pandas
- Causallearn
- Pycausal

## DISCLAIMER:

This package is not complete and pycausal, as well as its associated causal learning methods, is still being implemented.

### Algorithm's available

Currently there are 3 working functions:
- PC (MXM)
- GES (Causallearn)
- FCI (Causallearn)

These algorithms use the dataset COVID3_4Nodes3.dat in the sample_data directory for all examples.

If you have any further issues in determing how these functions operate or how their internal functions work, it is highly encouraged you check out the original packages documentation, which can be found below.

<br/>

[Causallearn] (https://github.com/cmu-phil/causal-learn)

[MXM] (https://cran.r-project.org/web/packages/MXM/index.html)

## How to use

This section is to give a simple explanation of how to use the causalLearn.py in order to implement any of the currently available functions for your own dataset.

1. Import your dataset via pandas and ensure all values are numeric. In the sample causalLearn.py, most of the values are "negative" or "positive", these are then adjusted to be 0 and 1, respectively, in order for the algorithms to properly work.
![CausalLearn step1](https://user-images.githubusercontent.com/79263753/215180723-944e1c79-215b-4aa7-b1f6-a716816a578b.png)

2. Create the object of the algorithm you want to use. For PC, only the dataframe is required as the output will be in the terminal. For both GES and FCI, both the dataframe and the location of the output for the png are required, as both these functions produce pngs as their respective outputs.
![CausalLearn step2](https://user-images.githubusercontent.com/79263753/215180872-17d35776-2b81-4c7f-a09f-184e9979191f.png)

3. Run the program. For the PC algorithm, as it uses r as its basis, it will ask for CRAN location, it is recommended you pick the location from the list that is closest to you.
![CausalLearn step3](https://user-images.githubusercontent.com/79263753/215181260-e1547870-ae0a-44f5-b7d0-0d0ba72f9e37.png)

The current causalLearn.py has examples of all the current algorithms using the COVID3_4Nodes3.dat dataset for the examples.
