## _function op_left
**op_left**: The function of op_left is to perform a specific operation called "op_left" in the NAR (Non-Axiomatic Reasoning) system.

**parameters**:
- None

**Code Description**:
The op_left function is a simple function that performs the "op_left" operation in the NAR system. It starts by declaring a global variable called "fovea". 

Next, it calls the AddInput function from the NAR module to add a Narsese input to the NAR system. The Narsese input is "G. :|: {0.0 0.05}". The AddInput function sends the input to the NAR system for processing and returns the parsed output.

After adding the input, the function assigns the value "L" to the "fovea" variable.

**Note**:
- The op_left function assumes that the NAR system is already running and the AddInput function is accessible.
- The function does not take any parameters.
- The function modifies the global variable "fovea" and calls the AddInput function to interact with the NAR system.

**Relationship with other objects**:
- The op_left function calls the AddInput function from the NAR module to add a Narsese input to the NAR system.

Raw code:
```python
def op_left():
    global fovea
    NAR.AddInput("G. :|: {0.0 0.05}")
    fovea = "L"
```
## _function op_right
**op_right**: The function of op_right is to perform a specific operation in the context of the NAR (Non-Axiomatic Reasoning) system. 

**parameters**:
- None

**Code Description**:
The op_right function is a part of the OpenNARS-for-Applications project and is located in the matchtosample_handeye.py file. This function is responsible for executing a specific operation within the NAR system. 

The function starts by declaring the variable "fovea" as a global variable. This allows the function to access and modify the value of "fovea" outside of its scope. 

Next, the function calls the AddInput function from the NAR.py module. The AddInput function is responsible for sending a Narsese input to the NAR system for processing. In this case, the Narsese input is "G. :|: {0.0 0.05}". The AddInput function communicates with the NAR system through its standard input and output streams. 

After calling the AddInput function, the function assigns the value "R" to the "fovea" variable. This indicates that the operation performed by the op_right function is related to the right side of the fovea. 

**Note**:
- The op_right function assumes that the NAR system is already running and its standard input and output streams are accessible.
- The function relies on the AddInput function from the NAR.py module to send the Narsese input to the NAR system.
- The function modifies the global variable "fovea" to indicate the operation performed by the op_right function.
- The specific details of the operation performed by the op_right function are not provided in the code snippet.
## _function op_up
**op_up**: The function of op_up is to update the value of the global variable "fovea" and add a Narsese input to the NAR (Non-Axiomatic Reasoning) system.

**parameters**:
- None

**Code Description**:
The op_up function begins by declaring the "fovea" variable as a global variable. This allows the function to modify the value of "fovea" outside of its local scope.

Next, the function calls the AddInput function from the NAR module. The AddInput function is responsible for sending a Narsese input to the NAR system for processing. In this case, the Narsese input is "G. :|: {0.0 0.05}". The function passes this input as a parameter to the AddInput function.

After calling the AddInput function, the op_up function assigns the value "U" to the "fovea" variable. This updates the value of the global variable "fovea" to "U".

**Note**:
- The op_up function assumes that the NAR system is already running and accessible.
- The function relies on the AddInput function from the NAR module to send the Narsese input to the NAR system.
- The function updates the value of the global variable "fovea" to "U" after adding the Narsese input to the NAR system.

The op_up function is called within the project hierarchy from the matchtosample_handeye.py file. It is part of the Python module within the misc directory. The op_up function interacts with the NAR system by using the AddInput function from the NAR module. The AddInput function is responsible for sending Narsese inputs to the NAR system and processing the output. By calling the AddInput function, the op_up function adds the Narsese input "G. :|: {0.0 0.05}" to the NAR system. After adding the input, the op_up function updates the value of the global variable "fovea" to "U".

Please refer to the documentation of the AddInput function in the NAR module for more information on how the Narsese input is processed and the output is handled.

**Note**:
- The op_up function assumes that the NAR system is already running and accessible.
- The function relies on the AddInput function from the NAR module to send the Narsese input to the NAR system.
- The function updates the value of the global variable "fovea" to "U" after adding the Narsese input to the NAR system.
## _function create_new_match_to_sample_scenario
**create_new_match_to_sample_scenario**: The function of create_new_match_to_sample_scenario is to generate a new scenario for the match-to-sample task in the NAR (Non-Axiomatic Reasoning) system.

**parameters**:
- None

**Code Description**:
The create_new_match_to_sample_scenario function starts by printing "//NEW SCENARIO!!!!" to indicate the start of a new scenario. 

Next, the function randomly selects one of the four predefined items, which are represented as dictionaries with keys "U", "L", and "R". Each key represents a different stimulus location. The selected item is assigned to the global variable "items".

The function then sets the fovea variable to "U" to indicate that the fovea is focused on the upper stimulus location. This assignment is currently commented out, and the fovea is always set to "U".

The function adds four Narsese inputs to the NAR system using the AddInput function. Each input represents a pick action for one of the stimulus locations. The inputs have the form "dt=1.0 <(LB1 &/ ^pick) =/> G>. {0.0 0.99}", where "LB1" is the location of the stimulus and "G" is the goal to be achieved. The parameters "dt=1.0" and "{0.0 0.99}" specify the time and confidence values associated with the input.

**Note**:
- The create_new_match_to_sample_scenario function assumes that the NAR system is already running and the AddInput function is accessible.
- The function generates a new scenario by selecting a random item and setting the fovea variable.
- The Narsese inputs added to the NAR system represent pick actions for each stimulus location.

**Calling Situation**:
The create_new_match_to_sample_scenario function is called within the op_pick function in the matchtosample_handeye.py file. After a successful or failed pick action, the op_pick function calls create_new_match_to_sample_scenario to generate a new scenario for the match-to-sample task. The function is also called at the end of the op_pick function to continue the loop and perform the next pick action.

The op_pick function is called within the main loop of the program, which suggests that the create_new_match_to_sample_scenario function is an essential part of the overall functionality of the program.

**Note**:
- The op_pick function is responsible for handling the logic of successful and failed pick actions in the match-to-sample task.
- The create_new_match_to_sample_scenario function is called within the op_pick function to generate new scenarios for the task.
## _function rewarded_after_pick
**rewarded_after_pick**: The function of rewarded_after_pick is to determine whether a pick action is rewarded or not based on the match-to-sample cases.

**parameters**:
- No parameters are passed to this function.

**Code Description**:
The function `rewarded_after_pick` checks if a pick action is rewarded by iterating through a list of match-to-sample cases. Each match-to-sample case is a tuple containing two elements: a sample and another item. The function then checks if the fovea (a variable that is not defined in the given code snippet) is not equal to "U" and if the item at index "U" in the `items` dictionary is equal to the sample, and the item at index `fovea` in the `items` dictionary is equal to the other item. If all these conditions are met for any match-to-sample case, the function returns True, indicating that the pick action is rewarded. If none of the match-to-sample cases satisfy the conditions, the function returns False, indicating that the pick action is not rewarded.

**Note**:
- The code snippet provided does not include the definition of the `fovea` variable and the `items` dictionary. Therefore, the behavior of the function may not be accurately described without this information.

**Output Example**:
- If the match_to_sample_cases list is `[("X1", "B2"), ("A1", "B1")]`, and the `fovea` variable is not equal to "U", and the `items` dictionary has the values `{"U": "X1", "A1": "B1"}`, then the function will return True.
## _function stats
**stats**: The function of stats is to calculate and return the statistics of successes, failures, ratio, and t.

**parameters**:
- None

**Code Description**:
The `stats` function calculates the statistics of successes, failures, ratio, and t. It first calculates the ratio by dividing the number of successes by the sum of successes and failures. If the sum of successes and failures is 0, the ratio is set to 0 to avoid division by zero. The function then returns a formatted string that includes the values of failures, successes, ratio, and t.

This function is called by the following objects in the project:
- `op_pick` function in `OpenNARS-for-Applications/misc/Python/matchtosample_handeye.py/op_pick`

In the `op_pick` function, the `stats` function is called to print the statistics after each pick operation. If the pick operation is successful, the `successes` counter is incremented and the `stats` function is called with the prefix "//SUCCESS +++++++". If the pick operation fails, the `failures` counter is incremented and the `stats` function is called with the prefix "//FAILURE +++++++". The `stats` function is also called when the `op_pick` function is executed every 1000 iterations.

After the `stats` function is called, the output is flushed to the standard output using `sys.stdout.flush()`. If the sum of successes and failures reaches 1000, the program exits. Finally, a new match-to-sample scenario is created and the value "20" is added as input to the NAR system.

**Note**:
- The `successes` and `failures` variables are assumed to be defined and accessible in the scope of the `stats` function.
- The `t` variable is assumed to be defined and accessible in the scope of the `stats` function.
- The `NAR` object is assumed to be defined and accessible in the scope of the `op_pick` function.
- The `rewarded_after_pick` function is assumed to be defined and accessible in the scope of the `op_pick` function.
- The `time` module is assumed to be imported and accessible in the scope of the `op_pick` function.

**Output Example**:
"failures=10, successes=90 ratio=0.9, t=1000"
## _function op_pick(failure)
**op_pick**: The function of op_pick is to handle the logic of successful and failed pick actions in the match-to-sample task. It determines whether a pick action is rewarded or not based on the match-to-sample cases and updates the statistics accordingly.

**parameters**:
- failure (optional): A boolean value indicating whether the pick action is a failure. Default is False.

**Code Description**:
The `op_pick` function starts by checking if the `failure` parameter is False and if the pick action is rewarded by calling the `rewarded_after_pick` function. If the pick action is rewarded, the function adds a Narsese input "G. :|:" to the NAR system using the `AddInput` function. The `successes` counter is incremented, and the statistics are printed using the `stats` function with the prefix "//SUCCESS +++++++". The output is flushed to the standard output using `sys.stdout.flush()`. If the current iteration `t` is a multiple of 1000, the function sleeps for 1 second.

If the pick action is not rewarded or the `failure` parameter is True, the function adds a Narsese input "G. :|: {0.0 0.999}" to the NAR system using the `AddInput` function. The `failures` counter is incremented, and the statistics are printed using the `stats` function with the prefix "//FAILURE +++++++". The output is flushed to the standard output using `sys.stdout.flush()`. If the current iteration `t` is a multiple of 1000, the function sleeps for 1 second.

After each pick action, the function checks if the total number of successes and failures is equal to 1000. If this condition is true, the program exits.

Finally, the function calls the `create_new_match_to_sample_scenario` function to generate a new scenario for the match-to-sample task by creating new Narsese inputs and setting the fovea variable. The function also adds the Narsese input "20" to the NAR system.

**Note**:
- The `failures` and `successes` variables are assumed to be defined and accessible in the scope of the `op_pick` function.
- The `t` variable is assumed to be defined and accessible in the scope of the `op_pick` function.
- The `NAR` object is assumed to be defined and accessible in the scope of the `op_pick` function.
- The `rewarded_after_pick` function is assumed to be defined and accessible in the scope of the `op_pick` function.
- The `time` module is assumed to be imported and accessible in the scope of the `op_pick` function.

**Calling Situation**:
The `op_pick` function is called within the main loop of the program. It is responsible for handling the logic of successful and failed pick actions in the match-to-sample task. After a successful or failed pick action, the function calls the `create_new_match_to_sample_scenario` function to generate a new scenario for the task. The function is also called at the end of the `op_pick` function to continue the loop and perform the next pick action.

The `op_pick` function is an essential part of the overall functionality of the program, as it determines the success or failure of pick actions and updates the statistics accordingly.

**Note**:
- The `create_new_match_to_sample_scenario` function is called within the `op_pick` function to generate new scenarios for the match-to-sample task.
- The `rewarded_after_pick` function is called within the `op_pick` function to determine whether a pick action is rewarded or not based on the match-to-sample cases.
- The `stats` function is called within the `op_pick` function to calculate and print the statistics of successes, failures, ratio, and `t`.
- The `AddInput` function is called within the `op_pick` function to add Narsese inputs to the NAR system.
## _function step
**step**: The function of step is to perform a single step of the match-to-sample hand-eye coordination task.

**parameters**:
- None

**Code Description**:
The step function is responsible for executing a single step of the match-to-sample hand-eye coordination task. It performs the following steps:

1. Retrieve the value of the item at the fovea position: The variable "val" is assigned the value of the item at the fovea position in the "items" list.

2. Add input to the NAR system: The AddInput function is called to send a Narsese input to the NAR system. The Narsese input is constructed by concatenating the fovea position, the value at the fovea position, and ". :|:". This input represents a statement that asserts the value at the fovea position. The AddInput function processes the input and returns the output.

3. Retrieve the executions from the NAR system: The executions variable is assigned the value of the "executions" key in the output returned by the AddInput function. This represents the executions generated by the NAR system in response to the input.

4. Execute the first execution: If there are any executions, the function enters a loop and iterates over each execution. The "i" variable represents the index of the current execution, and the "execution" variable represents the current execution itself.

5. Retrieve the operator name: The opname variable is assigned the value of the "operator" key in the current execution. This represents the name of the operator associated with the execution.

6. Execute the operator: The ops dictionary is accessed using the opname as the key, and the corresponding value (a function) is called. This executes the operator associated with the current execution.

7. Break the loop: After executing the operator, the loop is broken using the "break" statement. This ensures that only the first execution is processed.

**Note**:
- The step function assumes that the "items" list, the "fovea" variable, the "NAR" object, and the "ops" dictionary are defined and accessible within the same module as the step function.
- The function relies on the AddInput function to send input to the NAR system and retrieve the executions.
- The function assumes that the AddInput function is defined and accessible within the same module as the step function.
- The function assumes that the NAR system is already running and its standard input and output streams are accessible.
- The function assumes that the ops dictionary contains the necessary operator functions to be executed based on the operator names retrieved from the NAR system.
- The function only executes the first execution and breaks the loop. If there are multiple executions, the remaining executions will not be processed.
