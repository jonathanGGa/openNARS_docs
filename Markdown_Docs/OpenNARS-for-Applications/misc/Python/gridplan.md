## _function state(XY)
**state**: The function of state is to convert a given XY coordinate into a string representation.

**parameters**:
- XY: A tuple representing the XY coordinate.

**Code Description**:
The `state` function takes a tuple `XY` as input, which represents the XY coordinate. It then converts the XY coordinate into a string representation by concatenating the string representations of the X and Y values with an underscore in between. The resulting string is returned as the output.

The code first converts the X value of the XY coordinate to a string using the `str` function. It then concatenates the string representation of the X value with an underscore character using the `+` operator. Next, it converts the Y value of the XY coordinate to a string using the `str` function. Finally, it concatenates the string representation of the Y value with the previously created string using the `+` operator. The resulting string is returned as the output of the function.

This function is called by the `contingency` function in the `gridplan.py` file. The `contingency` function uses the `state` function to convert the pre and cons coordinates into string representations, which are then used to construct a contingency statement.

**Note**:
- The input `XY` should be a tuple containing two values representing the X and Y coordinates.
- The function assumes that the input `XY` will always be a valid tuple.

**Output Example**:
If the input `XY` is `(3, 5)`, the function will return the string `"3_5"`.
## _function contingency(pre, op, cons)
**contingency**: The function of contingency is to construct a contingency statement by combining the string representations of the pre and cons coordinates with the given operation.

**parameters**:
- pre: A tuple representing the pre coordinate.
- op: A string representing the operation.
- cons: A tuple representing the cons coordinate.

**Code Description**:
The `contingency` function takes three parameters: `pre`, `op`, and `cons`. It constructs a contingency statement by combining the string representations of the `pre` and `cons` coordinates with the given operation `op`. The resulting contingency statement is returned as the output.

The code first calls the `state` function to convert the `pre` coordinate into a string representation. It passes the `pre` coordinate as an argument to the `state` function, which returns the string representation of the `pre` coordinate. The string representation is then concatenated with the `op` string using the `+` operator.

Next, the code concatenates the resulting string with the string representation of the `cons` coordinate. It calls the `state` function again, passing the `cons` coordinate as an argument, and receives the string representation of the `cons` coordinate. Finally, the code concatenates the string representation of the `cons` coordinate with the previously created string using the `+` operator.

The resulting string represents a contingency statement in the form "<(pre &/ op) =/> cons>.". The function returns this contingency statement as the output.

This function is called within the `gridplan.py` file and is used to construct contingency statements based on the pre and cons coordinates and the specified operation.

**Note**:
- The `pre` and `cons` coordinates should be tuples containing two values representing the X and Y coordinates.
- The `op` parameter should be a string representing the operation to be performed in the contingency statement.
- The function assumes that the input coordinates and operation are valid.

**Output Example**:
If the `pre` coordinate is `(3, 5)`, the `op` is `"move"`, and the `cons` coordinate is `(4, 6)`, the function will return the string "<(3_5 &/ move) =/> 4_6>.".
## _function execute(executions)
**execute**: The function of execute is to perform a series of executions based on the given list of executions.

**parameters**:
- executions: A list of executions to be performed.

**Code Description**:
The `execute` function is responsible for executing a series of actions based on the given list of executions. It starts by initializing a variable `lastposition` with the current value of the global variable `position`. This `lastposition` variable is used to store the previous position in case the current position becomes unreachable.

The function then checks if the `executions` list is not empty. If it is not empty, it retrieves the first execution from the list and assigns it to the variable `execution`. 

Next, the function checks the value of the `"operator"` key in the `execution` dictionary. If the value is `"^left"`, the function updates the `position` variable by subtracting 1 from the x-coordinate of the current position. The `max` function is used to ensure that the x-coordinate does not go below 0. After updating the `position` variable, the function prints the string `^left`.

Similarly, if the value of the `"operator"` key is `"^right"`, the function updates the `position` variable by adding 1 to the x-coordinate of the current position. The `min` function is used to ensure that the x-coordinate does not exceed the maximum x-coordinate value `SX-1`. After updating the `position` variable, the function prints the string `^right`.

If the value of the `"operator"` key is `"^up"`, the function updates the `position` variable by adding 1 to the y-coordinate of the current position. The `min` function is used to ensure that the y-coordinate does not exceed the maximum y-coordinate value `SY-1`. After updating the `position` variable, the function prints the string `^up`.

Similarly, if the value of the `"operator"` key is `"^down"`, the function updates the `position` variable by subtracting 1 from the y-coordinate of the current position. The `max` function is used to ensure that the y-coordinate does not go below 0. After updating the `position` variable, the function prints the string `^down`.

After executing the action based on the first execution, the function checks if the current position is in the `unreachables` list. If the current position is in the `unreachables` list, the function reverts the `position` variable back to the previous position stored in the `lastposition` variable.

**Note**: It is important to provide a valid list of executions as the parameter to ensure the correct execution of actions. The `position` variable is a global variable that is modified within the function. The `unreachables` list is used to determine if a position is unreachable.
