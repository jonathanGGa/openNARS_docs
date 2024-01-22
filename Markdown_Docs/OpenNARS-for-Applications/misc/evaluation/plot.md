## _function Plot(example, successCriteria)
**Plot**: The function of Plot is to generate a plot showing the success ratio over time for different branches of a given example.

**parameters**:
- example: A string representing the name of the example.
- successCriteria: A string representing the success criteria to be plotted.

**Code Description**:
The Plot function begins by creating a new figure using the `plt.figure()` function. It then sets the title of the plot to the value of the `example` parameter using `plt.title()`. The y-axis label is set to "Success ratio" using `plt.ylabel()`, and the x-axis label is set to "Time" using `plt.xlabel()`.

Next, a list of colors is defined as `['g', 'y', 'r', 'b']`. Four patches are created using the `mpatches.Patch()` function, each representing a different branch. The color and label of each patch is set based on the branches list. These patches are then added to the plot legend using `plt.legend()`.

A dictionary `BranchRatios` is initialized to store the success ratios for each branch at different time steps. A variable `k` is set to -1 to keep track of the current branch index.

The function then iterates over each branch in the branches list. For each branch, it iterates over each seed in the seeds list. It constructs a filename based on the example, branch, and seed. It opens the corresponding file in read mode and reads its lines. The lines are reversed using `reversed()` to process them in reverse order.

For each line, if it is empty, it is skipped. Otherwise, it extracts the success ratio value based on the `successCriteria` parameter. The ratio is converted to a float and added to the ratios list. The ratio is also added to the `BranchRatios` dictionary, grouped by branch and time step.

The success ratios for each branch are then plotted using `plt.plot()`, with the corresponding color from the colors list.

Next, the function iterates over each branch again. It increments `k` to get the next color from the colors list. For each time step, it calculates the average success ratio for the branch and adds it to the `BranchRatioAvgs` list. The average success ratios for each branch are then plotted using `plt.plot()`.

Finally, the plot is saved as a PNG file with the name based on the example using `plt.savefig()`.

**Note**: This function assumes that the `branches` and `seeds` lists are defined and contain the necessary values. It also assumes that there are text files with the naming convention "example_branch_seed.txt" containing the success ratio values for each branch and seed.
