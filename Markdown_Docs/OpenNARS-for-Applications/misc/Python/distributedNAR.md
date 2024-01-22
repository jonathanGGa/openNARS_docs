## _function selectOfPunctuation(selections, punctuation)
**selectOfPunctuation**: The function of selectOfPunctuation is to filter a list of selections based on a specified punctuation value.

**parameters**:
- selections: A list of selections, where each selection is a dictionary.
- punctuation: The punctuation value to filter the selections.

**Code Description**:
The `selectOfPunctuation` function takes in a list of selections and a punctuation value as parameters. It then filters the selections based on the specified punctuation value and returns a new list containing only the selections that have the same punctuation value.

The function uses a list comprehension to iterate over each selection in the `selections` list. For each selection, it checks if the value of the "punctuation" key in the selection dictionary is equal to the specified punctuation value. If it is, the selection is included in the new list. If not, it is skipped.

This function is useful when you have a list of selections and you want to extract only the selections that have a specific punctuation value. It provides a convenient way to filter the selections based on a specific criterion.

**Note**:
- The `selections` parameter should be a list of dictionaries, where each dictionary represents a selection.
- The `punctuation` parameter should be a value that can be compared to the "punctuation" key in the selection dictionaries.

**Output Example**:
If we have the following list of selections:
```
selections = [
    {"punctuation": "!"},
    {"punctuation": "."},
    {"punctuation": "?"},
    {"punctuation": "."}
]
```
And we call the `selectOfPunctuation` function with `selections` and the punctuation value ".":
```
result = selectOfPunctuation(selections, ".")
print(result)
```
The output will be:
```
[
    {"punctuation": "."},
    {"punctuation": "."}
]
```

In the project, the `selectOfPunctuation` function is called by two other functions: `Trickle` and `AddInput`. 

In the `Trickle` function, the `selectOfPunctuation` function is used to filter the selections returned by the `NAR.AddInput` function based on the punctuation value "!". The filtered selections are then passed as an argument to the recursive call of the `Trickle` function.

In the `AddInput` function, the `selectOfPunctuation` function is used twice. First, it is used to filter the selections returned by the `NAR.AddInput` function based on the punctuation value "!". The filtered selections are then passed as an argument to the recursive call of the `Trickle` function. Second, it is used to filter the selections returned by the `NAR.AddInput` function based on the punctuation value ".". The filtered selections are then passed as an argument to the recursive call of the `Trickle` function.

These usages demonstrate how the `selectOfPunctuation` function can be used in the context of the project to filter selections based on different punctuation values before further processing.
## _function selectionToNarsese(selection)
**selectionToNarsese**: The function of selectionToNarsese is to convert a selection object into a Narsese string representation.

**parameters**:
- selection: A dictionary object representing a selection, which contains the following keys:
  - "term": A string representing the term of the selection.
  - "punctuation": A string representing the punctuation of the selection.
  - "truth": A dictionary representing the truth value of the selection, which contains the following keys:
    - "frequency": A float representing the frequency of the selection.
    - "confidence": A float representing the confidence of the selection.

**Code Description**:
The `selectionToNarsese` function takes a selection object as input and returns a Narsese string representation of the selection. The Narsese string is constructed by concatenating the term, punctuation, and truth values of the selection.

The function first accesses the "term" key of the selection dictionary and concatenates it with the "punctuation" key. Then, it appends the Narsese truth value representation by converting the "frequency" and "confidence" values from the "truth" dictionary to strings and concatenating them with the Narsese truth value syntax.

The function then returns the constructed Narsese string representation of the selection.

This function is called within the `Trickle` function in the `distributedNAR.py` file. In the `Trickle` function, the `selectionToNarsese` function is used to convert a selection object into a Narsese string representation. The resulting Narsese string is then used as input for further processing within the `Trickle` function.

**Note**:
- The input selection object must be a dictionary with the required keys ("term", "punctuation", "truth") and their corresponding values.
- The "term" and "punctuation" values should be strings.
- The "frequency" and "confidence" values in the "truth" dictionary should be floats.

**Output Example**:
If the input selection object is:
```
{
  "term": "apple",
  "punctuation": "!",
  "truth": {
    "frequency": 0.8,
    "confidence": 0.9
  }
}
```
The function will return the following Narsese string:
```
"apple! :|: {0.8 0.9}"
```
## _function Trickle(node, selections, Down)
**Trickle**: The function of Trickle is to perform a recursive traversal of a given node and its selections, filtering them based on priority thresholds and punctuation values.

**parameters**:
- node: The node to start the traversal from.
- selections: A list of selections, where each selection is a dictionary.
- Down (optional): A boolean value indicating the direction of the traversal. Default is True.

**Code Description**:
The `Trickle` function takes in a node, a list of selections, and an optional parameter indicating the direction of the traversal. It then performs a recursive traversal of the node and its selections, filtering them based on priority thresholds and punctuation values.

The function starts by printing the current node using the `print` function. This provides a visual indication of the traversal progress.

Next, the function iterates over each selection in the `selections` list. For each selection, it checks if the `Down` parameter is True and the priority of the selection is less than the `priorityThresholdGoals`. If both conditions are met, the selection is skipped and the loop moves on to the next selection. Similarly, if the `Down` parameter is False and the priority of the selection is less than the `priorityThresholdBeliefs`, the selection is skipped.

If the selection passes the priority threshold checks, the function converts the selection to a Narsese string representation using the `selectionToNarsese` function. The resulting Narsese string is then used as input for further processing.

If the `Down` parameter is True, the function recursively calls itself for each incoming node of the current node. It passes the incoming node, the filtered selections with a punctuation value of "!", and sets the `Down` parameter to True.

If the `Down` parameter is False, the function recursively calls itself for each outgoing node of the current node. It passes the outgoing node, the filtered selections with a punctuation value of ".", and sets the `Down` parameter to False.

This recursive traversal continues until all nodes and their selections have been processed.

**Note**:
- The `node` parameter should be a valid node in the traversal hierarchy.
- The `selections` parameter should be a list of dictionaries, where each dictionary represents a selection.
- The `Down` parameter determines the direction of the traversal. If set to True, the traversal goes downwards from the current node. If set to False, the traversal goes upwards from the current node.
- The `priorityThresholdGoals` and `priorityThresholdBeliefs` variables are assumed to be defined and accessible within the same module as the `Trickle` function.
- The `selectionToNarsese` function is assumed to be defined and accessible within the same module as the `Trickle` function.

This function is called within the `distributedNAR.py` file in the `OpenNARS-for-Applications` project. It is called by the `AddInput` function and is used to perform recursive traversals of nodes and their selections based on priority thresholds and punctuation values. The `selectOfPunctuation` function is also called within the `Trickle` function to filter selections based on punctuation values before further processing.

The `Trickle` function provides a way to traverse and filter selections in a hierarchical structure, allowing for more targeted and controlled processing of the data. It is a crucial component in the overall functionality of the `distributedNAR.py` module.
## _function PerformIndependentSteps(ticks)
**PerformIndependentSteps**: The function of PerformIndependentSteps is to perform a specified number of independent steps in parallel using the NAR system.

**parameters**:
- ticks (optional): An integer representing the number of steps to perform. Default is 1.

**Code Description**:
The PerformIndependentSteps function utilizes the Parallel function from the joblib library to perform a specified number of independent steps in parallel. The number of steps is determined by the "ticks" parameter, which defaults to 1 if not provided.

Within the function, the Parallel function is called with the "n_jobs" parameter set to "num_cores" and the "require" parameter set to "sharedmem". This configuration allows the steps to be executed in parallel using shared memory.

The steps are performed by calling the AddInput function from the NAR module for each process in the "processes" dictionary. The AddInput function is called with the following parameters: the string representation of the "ticks" parameter, the "Print" parameter set to True, and the "usedNAR" parameter set to the corresponding process from the "processes" dictionary.

The AddInput function sends the Narsese input to the NAR system for processing and returns the parsed output. By calling the AddInput function in parallel for each process, the steps are performed independently and concurrently.

**Note**:
- The PerformIndependentSteps function assumes that the NAR system is already running and the necessary processes are available in the "processes" dictionary.
- The function relies on the AddInput function from the NAR module to send the Narsese input to the NAR system and retrieve the parsed output.
- The function uses the Parallel function from the joblib library to execute the steps in parallel using shared memory.
- The number of steps to perform is determined by the "ticks" parameter, which defaults to 1 if not provided.

The PerformIndependentSteps function is called by the AddInput function in the distributedNAR.py module. The AddInput function checks the input string and performs different actions based on its content. If the input string consists of digits, indicating the number of steps to perform, the PerformIndependentSteps function is called with the parsed integer value of the input string.

By calling the PerformIndependentSteps function, the AddInput function performs the specified number of independent steps in parallel using the NAR system.

Additionally, the AddInput function in the distributedNAR.py module is called by other parts of the project to send Narsese inputs to the NAR system. The function handles different types of inputs, including goals and regular Narsese statements, and utilizes the PerformIndependentSteps function to perform the steps in parallel.

Overall, the PerformIndependentSteps function plays a crucial role in executing independent steps in parallel using the NAR system, providing efficient processing capabilities for the project.
## _function AddInput(narsese, node)
**AddInput**: The function of AddInput is to send a Narsese input to the NAR (Non-Axiomatic Reasoning) system and process the output.

**parameters**:
- narsese: A string representing the Narsese input to be added.
- node (optional): The node to which the input is added. Default is None.

**Code Description**:
The `AddInput` function is a key component of the distributedNAR.py module in the OpenNARS-for-Applications project. It is responsible for sending a Narsese input to the NAR system and processing the output.

The function takes two parameters: `narsese`, which is a string representing the Narsese input to be added, and `node`, which is an optional parameter representing the node to which the input is added. If the `node` parameter is not provided, it defaults to None.

The function starts by checking if the `narsese` input is a digit. If it is, it calls the `PerformIndependentSteps` function with the parsed integer value of the `narsese` input. This function performs the specified number of independent steps in parallel using the NAR system.

If the `narsese` input does not consist of digits, the function checks if it ends with "! :|:". This indicates that the input is a goal. In this case, the function calls the `Trickle` function with the `master` node, the filtered selections based on the punctuation value "!", and sets the `Down` parameter to True. The `Trickle` function performs a recursive traversal of the node and its selections, filtering them based on priority thresholds and punctuation values.

If the `narsese` input does not meet the above conditions, the function calls the `Trickle` function with the `node` parameter, the filtered selections based on the punctuation value ".", and sets the `Down` parameter to False. This performs a recursive traversal of the node and its selections in the opposite direction.

The `AddInput` function provides a way to add Narsese inputs to the NAR system and perform various operations based on the input content. It leverages other functions in the module, such as `PerformIndependentSteps` and `Trickle`, to execute the necessary steps and process the output.

**Note**:
- The `narsese` parameter should be a valid Narsese input string.
- The `node` parameter is optional and defaults to None if not provided.
- The function relies on other functions in the distributedNAR.py module, such as `PerformIndependentSteps` and `Trickle`, to perform specific operations based on the input content.
- The function assumes that the NAR system is already running and the necessary processes and nodes are available for traversal.
- The function provides flexibility in handling different types of Narsese inputs, including goals and regular statements, and performs the appropriate operations based on the input content.
