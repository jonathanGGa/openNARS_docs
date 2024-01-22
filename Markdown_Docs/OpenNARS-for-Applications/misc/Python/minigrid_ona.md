## _function ASCIIpaint(COLOR, objectchar)
**ASCIIpaint**: The function of ASCIIpaint is to generate ASCII art representations of objects with different colors.

**parameters**:
- COLOR: A string representing the color of the object.
- objectchar: A string representing the character to be used for the object.

**Code Description**:
The ASCIIpaint function takes in two parameters: COLOR and objectchar. It first checks the value of objectchar and based on its value, it returns a specific ASCII art representation of the object with the specified color.

If objectchar is equal to "W", the function returns a white background with a space character.
If objectchar is equal to "L", the function returns the specified color with the character "L".
If objectchar is equal to "V", the function returns the color red with the character "v".
If objectchar is equal to "^", the function returns the color red with the character "^".
If objectchar is equal to "<", the function returns the color red with the character "<".
If objectchar is equal to ">", the function returns the color red with the character ">".
If objectchar is none of the above, the function returns the specified color with the character objectchar.

This function is used to generate ASCII art representations of objects with different colors. It is called by the colorify function in the minigrid_ona.py file. The colorify function takes in a string and iterates over each character. For every even-indexed character, it stores the character in the variable lasts. For every odd-indexed character, it determines the color based on the value of the character (G for green, B for blue, R for red, Y for yellow, and default to white). It then calls the ASCIIpaint function with the stored lasts character and the determined color, and appends the result to the string S. If the character is a newline character, it resets the even flag to True and appends a newline character to the string S. Finally, it returns the generated string S.

**Note**: The ASCIIpaint function is dependent on the colorify function in the minigrid_ona.py file for its usage. It is important to ensure that the colorify function is called before using the ASCIIpaint function to generate the desired ASCII art representation.

**Output Example**:
If the COLOR parameter is set to RED and the objectchar parameter is set to "L", the function will return the following ASCII art representation:
```
L
```
This represents an object with the color red and the character "L".
## _function colorify(x)
**colorify**: The function of colorify is to generate a colored ASCII art representation of a given string.

**parameters**:
- x: A string representing the input text.

**Code Description**:
The colorify function takes in a string as input and iterates over each character in the string. For every even-indexed character, it stores the character in the variable "lasts". For every odd-indexed character, it determines the color based on the value of the character. If the character is "G", the color is set to green. If the character is "B", the color is set to blue. If the character is "R", the color is set to red. If the character is "Y", the color is set to yellow. If the character is none of the above, the color is set to white.

The function then calls the ASCIIpaint function with the stored "lasts" character and the determined color. It appends the result of the ASCIIpaint function to the string "S". If the character is a newline character ("\n"), it resets the even flag to True and appends a newline character to the string "S". Finally, the function returns the generated string "S".

**Note**: The colorify function relies on the ASCIIpaint function to generate the colored ASCII art representation. It is important to ensure that the ASCIIpaint function is defined and called before using the colorify function.

**Output Example**:
If the input string is "GBRY", the colorify function will return the following colored ASCII art representation:
```
L
```
This represents an object with the colors green, blue, red, and yellow, respectively, and the characters "L".
## _function renderANSI(env)
**renderANSI**: The function of renderANSI is to render an ASCII art representation of the environment in the ANSI terminal.

**parameters**:
- env: An environment object representing the state of the environment.

**Code Description**:
The renderANSI function takes in an environment object as input and performs the following steps:

1. It uses the escape sequence "\033[1;1H\033[2J" to clear the terminal screen and move the cursor to the top-left corner.
2. It extracts the ASCII representation of the environment by splitting the string representation of the environment object at the "<PassiveEnvChecker" substring and taking the second part.
3. It calls the colorify function with the extracted ASCII representation as input to generate a colored ASCII art representation of the environment.
4. It prints the colored ASCII art representation of the environment.
5. It prints the RESET escape sequence to reset the terminal colors.

The renderANSI function relies on the colorify function to generate the colored ASCII art representation of the environment. It is important to ensure that the colorify function is defined and called before using the renderANSI function.

**Note**: The renderANSI function assumes that the terminal supports ANSI escape sequences for color and cursor control. The function may not work correctly if the terminal does not support these features.

The renderANSI function is part of the minigrid_ona.py module in the OpenNARS-for-Applications project. It is called to render the environment state in the terminal for visualization purposes.

**Note**: The renderANSI function is typically called in a loop to continuously update and display the environment state in real-time.

Please refer to the documentation of the colorify function for more information on how the colored ASCII art representation is generated.
## _function coneForward(viewDistance)
**coneForward**: The function of coneForward is to generate a list of coordinates representing a cone-shaped view in front of an agent in a grid environment.

**Parameters**:
- viewDistance: An optional parameter that specifies the distance of the cone-shaped view. The default value is 6.

**Code Description**:
The function starts by initializing an empty list `L` to store the coordinates of the cone-shaped view. It also initializes an index variable to keep track of the number of cells added to the list. The starting position of the cone is set to (2, 5) using the variables `StartIndexX` and `StartIndexY`. Two more variables, `indexX` and `indexY`, are used to keep track of the current position while iterating through the cone.

The width of the cone is initially set to 3, representing the three cells right in front of the agent. The function then enters a nested loop, where the outer loop iterates `viewDistance` times and the inner loop iterates `width` times. In each iteration, the function checks if the current index is not 0 or 2 (representing the corner cells of the cone). If it is not a corner cell, the current coordinates `(indexX, indexY, k)` are appended to the list `L`. The `indexX` is incremented by 1 in each iteration, and the `index` is incremented as well.

After each inner loop iteration, the `StartIndexX` is updated by subtracting 1, ensuring that the cone moves one cell to the left in the next iteration. The `indexX` is reset to the updated `StartIndexX`, and the `indexY` is decremented by 1 to move the cone one cell up. The width of the cone is increased by 2, but limited to a maximum of 7 cells.

Once all iterations are completed, the function returns the list `L` containing the coordinates of the cone-shaped view.

**Note**: 
- The cone-shaped view is represented by a list of tuples, where each tuple contains the x-coordinate, y-coordinate, and the distance from the agent.
- The cone starts with the three cells right in front of the agent and expands wider as it moves forward.
- The corner cells of the cone are excluded from the view as the system cannot toggle switches diagonally.

**Output Example**:
If `viewDistance` is set to 6, the function may return the following list of coordinates:
[(2, 5, 0), (3, 5, 0), (4, 5, 0), (3, 4, 1), (4, 4, 1), (5, 4, 1), (2, 3, 2), (3, 3, 2), (4, 3, 2), (5, 3, 2), (6, 3, 2), (1, 2, 3), (2, 2, 3), (3, 2, 3), (4, 2, 3), (5, 2, 3), (6, 2, 3), (7, 2, 3), (0, 1, 4), (1, 1, 4), (2, 1, 4), (3, 1, 4), (4, 1, 4), (5, 1, 4), (6, 1, 4), (7, 1, 4), (8, 1, 4), (0, 0, 5), (1, 0, 5), (2, 0, 5), (3, 0, 5), (4, 0, 5), (5, 0, 5), (6, 0, 5), (7, 0, 5), (8, 0, 5), (9, 0, 5)]
## _function coneRight(viewDistance)
**coneRight**: The function of coneRight is to generate a list of coordinates representing a cone shape to the right of a given starting point. The cone shape is determined by the view distance parameter.

**parameters**:
- viewDistance: An optional parameter that specifies the distance of the cone shape. The default value is 3.

**Code Description**:
The function starts by initializing an empty list L to store the coordinates of the cone shape. It then sets the starting index coordinates (StartIndexX, StartIndexY) to (3, 6). Two additional variables (indexX, indexY) are initialized with the starting index values.

The function uses nested for loops to iterate over the range of viewDistance. The outer loop controls the height of the cone, while the inner loop controls the width of each row. Within the inner loop, the x-coordinate of the left side of the cone (xLeft) is calculated by incrementing the indexX value by 1. The coordinates (xLeft, indexY, h) are then appended to the list L. After each iteration of the inner loop, the indexX value is incremented by 1.

Once the inner loop completes, the StartIndexX value is incremented by 1, and the indexX value is reset to the updated StartIndexX value. The indexY value is decremented by 1 to move to the next row of the cone.

After the completion of the outer loop, the function inserts an additional coordinate (4, 5, 1) at index 1 of the list L.

Finally, the function returns the list L, which contains the coordinates representing the cone shape to the right of the starting point.

The function is called by two other objects in the project: nearestObject and observationToEvent. In the nearestObject function, the coneRight function is used along with coneForward and coneLeft to scan the cells and determine the nearest object. The result of the coneRight function is used in the comparison to decide the direction of the nearest object. In the observationToEvent function, the coneRight function is again used to scan the cells and encode the state of the cone shape to the right.

**Note**: 
- The viewDistance parameter determines the size of the cone shape. Increasing the value will result in a larger cone.
- The starting index coordinates (StartIndexX, StartIndexY) can be modified to change the starting point of the cone shape.
- The function assumes that the cells variable is defined and accessible within the scope of the function.

**Output Example**:
[(4, 6, 0), (5, 6, 0), (6, 6, 0), (5, 5, 1), (6, 5, 1), (6, 4, 1)]
## _function coneLeft(viewDistance)
**coneLeft**: The function of coneLeft is to generate a list of coordinates representing a cone-shaped view to the left of a given starting position.

**parameters**:
- viewDistance (optional): An integer representing the distance of the cone-shaped view. The default value is 3.

**Code Description**:
The coneLeft function takes an optional parameter, viewDistance, which determines the distance of the cone-shaped view. The function initializes an empty list, L, to store the coordinates of the cone-shaped view. It also initializes the starting position coordinates, StartIndexX and StartIndexY, to (3, 6). Two additional variables, indexX and indexY, are set to the starting position coordinates.

The function then enters a nested loop, where the outer loop iterates over the range of viewDistance, and the inner loop iterates over the range of viewDistance minus the current outer loop index. Within the inner loop, the variable xLeft is calculated by subtracting 1 from indexX. The coordinates (xLeft, indexY, h) are appended to the list L. The indexX is decremented by 1 in each iteration of the inner loop.

After the inner loop completes, the starting position coordinates, StartIndexX and StartIndexY, are decremented by 1. The indexX is reset to the updated StartIndexX, and the indexY is decremented by 1. This process is repeated for the remaining iterations of the outer loop.

Finally, the coordinates (2, 5, 1) are inserted at index 1 in the list L. The function then returns the list L.

**Note**: 
- The coneLeft function generates a cone-shaped view to the left of the starting position.
- The viewDistance parameter determines the distance of the cone-shaped view. The default value is 3.
- The coordinates in the returned list represent the x and y positions, as well as the height (h) of each point in the cone-shaped view.

**Output Example**:
[(2, 5, 1), (2, 6, 0), (1, 6, 0), (1, 7, 0), (0, 7, 0), (0, 8, 0)]
## _function scan(cone, cells, colorBlind, wall)
**scan**: The function of scan is to perform a scan of the environment using a cone-shaped sensor and return information about the nearest object or wall.

**parameters**:
- cone: A function that represents the cone-shaped sensor used for scanning the environment.
- cells: A 3-dimensional array representing the grid cells of the environment.
- colorBlind: A boolean parameter indicating whether the scanning should be color-blind or not. It is set to True by default.
- wall: A boolean parameter indicating whether the scanning should consider walls or not. It is set to False by default.

**Code Description**:
The scan function starts by checking if the scanning should be color-blind. If colorBlind is True, it sets the value of the cell at position (3, 6, 1) in the cells array to 0.

Next, it calls the cone function and assigns the returned value to the variable L.

Then, it iterates over each tuple (x, y, distance) in L. For each tuple, it checks if the scanning should be color-blind. If colorBlind is True, it sets the value of the cell at position (x, y, 1) in the cells array to 0.

It then checks if the value of the cell at position (x, y, 0) in the cells array is not equal to 0, 1, and if the distance is 0 or wall is True or the value of the cell at position (x, y, 0) is not equal to 2. If this condition is true, it returns the distance and the cell at position (x, y) in the cells array.

If no non-empty cell is found, it checks if wall is False. If wall is False, it recursively calls the scan function with the same parameters but with wall set to True. This is done to find the nearest wall.

If no non-empty cell or wall is found, it returns a distance of 9999 and a numpy array representing an empty cell.

**Note**: 
- The scan function assumes that the cells array is properly initialized and has the correct dimensions.
- The cone function is expected to return a list of tuples representing the objects detected by the sensor. Each tuple contains the x and y coordinates of the object and the distance from the sensor.

**Output Example**:
- If a non-empty cell is found, the function may return a tuple like (3, [1, 0, 0]) representing the distance and the cell's state.
- If no non-empty cell or wall is found, the function may return (9999, [1, 0, 0]) representing a distance of 9999 and an empty cell.
## _function stateconcat(state)
**stateconcat**: The function of stateconcat is to concatenate the elements of a given state into a single string, removing any newline characters and spaces.

**parameters**:
- state: A state object containing multiple elements.

**Code Description**:
The stateconcat function takes a state object as input and converts it into a string representation. It achieves this by first converting the state object to a string using the str() function. Then, it uses the replace() method to remove any newline characters ("\n") and spaces (" ") from the string representation of the state. The resulting string is then returned as the output of the function.

This function is used to convert the state objects into a format that can be easily processed or compared with other strings. By removing newline characters and spaces, the resulting string can be used as a compact representation of the state.

In the context of the project, the stateconcat function is called by two other functions: nearestObject and observationToEvent. Both of these functions use the stateconcat function to convert the state objects into strings before further processing or encoding them.

The nearestObject function uses the stateconcat function to convert the "forward", "left", and "right" states into strings before encoding them using the encode() function. The resulting encoded strings are then returned as the output of the nearestObject function.

The observationToEvent function also uses the stateconcat function to convert the "forward", "left", and "right" states into strings before encoding them using the encode() function. Additionally, it uses the stateconcat function to convert the "holding" state into a string representation. These encoded strings are then combined with the logical operators " &/ " and " :|: " to form a Narsese statement, which is returned as the output of the observationToEvent function.

**Note**: 
- The stateconcat function assumes that the input state object has a valid string representation.
- The resulting string from the stateconcat function may not preserve the original formatting of the state object.
- The stateconcat function only removes newline characters and spaces from the string representation of the state. Other characters or formatting may still be present in the resulting string.

**Output Example**:
If the input state is:
```
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
The output of the stateconcat function would be:
```
'[[1,2,3],[4,5,6],[7,8,9]]'
```
## _function encode(direction, state)
**encode**: The function of encode is to encode the given direction and state into a NARSese string.

**parameters**:
- direction: A string representing the direction.
- state: A string representing the state.

**Code Description**:
The encode function takes in a direction and a state as parameters. It first removes the square brackets from the state string using the replace() method. Then, it creates a NARSese string by formatting the state and direction into a specific pattern. The state is enclosed in double curly braces, while the direction is enclosed in square brackets. The resulting NARSese string is returned as the output.

This function is called by two other objects in the project: nearestObject and observationToEvent. In the nearestObject function, the encode function is used to encode the direction and the concatenated forward, left, and right states. The encoded string is then returned as the output. In the observationToEvent function, the encode function is used to encode the directions and the concatenated forward, left, and right states. The encoded strings are further used to construct a NARSese string, which is returned as the final output.

**Note**: 
- The encode function assumes that the state parameter is a string representation of a list, where the square brackets are used to enclose the elements of the list.
- The encode function uses the f-string formatting syntax to create the NARSese string.

**Output Example**:
If the direction is "forward" and the state is "[A, B, C]", the output of the encode function would be "<{A, B, C} --> [forward]>".
## _function nearestObject(cells)
**nearestObject**: The function of nearestObject is to determine the nearest object in a grid environment based on the distances obtained from scanning the cells in different directions.

**parameters**:
- cells: A 3-dimensional array representing the grid cells of the environment.

**Code Description**:
The nearestObject function takes in the cells parameter, which represents the grid cells of the environment. It performs three scans using the coneForward, coneLeft, and coneRight functions to obtain the distances and states of the objects in front, to the left, and to the right of the agent, respectively.

The function first calls the scan function with the coneForward function and the cells parameter to obtain the distance and state of the objects in front of the agent. It then calls the scan function with the coneLeft function and the cells parameter to obtain the distance and state of the objects to the left of the agent. Finally, it calls the scan function with the coneRight function and the cells parameter to obtain the distance and state of the objects to the right of the agent.

The function then compares the distances obtained from the scans. If the distance in front is less than or equal to the distances to the left and right, it encodes the direction as "forward" and concatenates the state obtained from the scan in front. If the distance to the left is less than or equal to the distances in front and to the right, it encodes the direction as "left" and concatenates the state obtained from the scan to the left. If the distance to the right is less than or equal to the distances in front and to the left, it encodes the direction as "right" and concatenates the state obtained from the scan to the right.

The function returns the encoded direction and concatenated state as the output.

**Note**: 
- The coneForward, coneLeft, and coneRight functions are used to scan the cells and obtain the distances and states of the objects in different directions.
- The scan function is used to perform the scanning using the cone-shaped sensor and return information about the nearest object or wall.
- The encode function is used to encode the direction and state into a NARSese string.
- The stateconcat function is used to concatenate the elements of a given state into a single string.
- The cells parameter represents the grid cells of the environment, where each cell contains information about the objects present.

**Output Example**:
If the distances obtained from the scans are as follows:
- Distance in front: 2
- Distance to the left: 3
- Distance to the right: 4

The function may return the following encoded string:
"<left --> [3,4,5,6]>"
## _function observationToEvent(cells)
**observationToEvent**: The function of observationToEvent is to convert the information obtained from scanning the grid environment into a NARSese statement representing the current observation.

**parameters**:
- cells: A 3-dimensional array representing the grid cells of the environment.

**Code Description**:
The observationToEvent function takes in the cells parameter, which represents the grid cells of the environment. It performs three scans using the coneForward, coneLeft, and coneRight functions to obtain the distances and states of the objects in front, to the left, and to the right of the agent, respectively.

The function first calls the scan function with the coneForward function and the cells parameter to obtain the distance and state of the objects in front of the agent. It then calls the scan function with the coneLeft function and the cells parameter to obtain the distance and state of the objects to the left of the agent. Finally, it calls the scan function with the coneRight function and the cells parameter to obtain the distance and state of the objects to the right of the agent.

The function then uses the stateconcat function to concatenate the obtained states into single strings. It further uses the encode function to encode the directions and the concatenated states into NARSese strings. The encoded strings are combined with the logical operators " &/ " and " :|: " to form a Narsese statement representing the current observation.

The Narsese statement is returned as the output of the observationToEvent function.

**Note**: 
- The coneForward, coneLeft, and coneRight functions are used to scan the cells and obtain the distances and states of the objects in different directions.
- The scan function is used to perform the scanning using the cone-shaped sensor and return information about the nearest object or wall.
- The encode function is used to encode the direction and state into a NARSese string.
- The stateconcat function is used to concatenate the elements of a given state into a single string.
- The cells parameter represents the grid cells of the environment, where each cell contains information about the objects present.

**Output Example**:
If the distances obtained from the scans are as follows:
- Distance in front: 2
- Distance to the left: 3
- Distance to the right: 4

The function may return the following Narsese statement:
"( [3,4,5,6] &/ [1,2,3] ). :|:"
