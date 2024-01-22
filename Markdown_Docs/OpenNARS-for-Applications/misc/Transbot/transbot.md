## _function pick_failed
**pick_failed**: The function of pick_failed is to perform a sequence of actions when a pick operation fails.

**parameters**:
- None

**Code Description**:
The `pick_failed` function is called in the `pick_with_feedback` function of the `transbot.py` file when a pick operation fails. It is responsible for executing a series of actions to handle the failure and reposition the Transbot for another attempt.

First, the function calls the `arm_up` function to move the Transbot's gripper arm to an upward position. This ensures that the arm is clear of any obstacles before repositioning the Transbot.

Next, the function calls the `backward` function twice to move the Transbot backward. This helps to create distance between the Transbot and the object that failed to be picked.

After moving backward, the function calls the `right` function three times to make the Transbot move to the right. This allows the Transbot to reposition itself and potentially find a better angle for picking the object.

Finally, the function calls the `open_gripper` function to open the gripper of the Transbot's arm. This prepares the gripper for another pick attempt.

Overall, the `pick_failed` function performs a sequence of actions to handle a failed pick operation. It ensures that the Transbot is repositioned and ready for another attempt to pick the object.

**Note**: It is important to note that the `pick_failed` function relies on the `arm_up`, `backward`, `right`, and `open_gripper` functions to perform the necessary actions. Therefore, these functions should be properly implemented and available before calling `pick_failed`. Additionally, the `pick_failed` function is called within the context of the `pick_with_feedback` function, which provides additional functionality and control over the pick operation.
## _function pick_with_feedback(pickobj, location, ForwardSleep)
**pick_with_feedback**: The function of pick_with_feedback is to perform a pick operation with visual feedback using the Transbot's gripper arm.

**parameters**:
- pickobj (optional): The object to be picked. If not specified, the function will attempt to pick any object within its visual range.
- location (optional): The desired location of the object relative to the gripper. Valid values are "left", "right", or None. If not specified, the function will attempt to pick the object in the center.
- ForwardSleep (optional): The duration in seconds to sleep between forward movements. The default value is 0.5 seconds.

**Code Description**:
The `pick_with_feedback` function is responsible for performing a pick operation with visual feedback using the Transbot's gripper arm. It starts by checking if the `pickobj` parameter contains the special character " * ". If it does, the function extracts the `location` and `pickobj` values from the parameter. Otherwise, it uses the default values of `None` for `pickobj` and `location`.

Next, the function checks if an object has already been picked by calling the `getPicked` function. If an object has been picked, the function returns without performing any further actions.

The function then calls the `arm_down` function to move the Transbot's gripper arm to a downward position. This ensures that the arm is clear of any obstacles before attempting to pick the object.

After a brief pause of 1 second, the function initializes variables for the maximum number of operations (`max_ops`), the number of move steps (`move_steps`), the maximum number of swaps (`max_swaps`), and the number of swaps performed (`swaps`). It also sets the `swap_Left` and `swap_Right` variables to `False`.

The function then enters a while loop that continues indefinitely until a break statement is encountered. Within the loop, the function flushes the standard output and increments the `move_steps` variable.

If the `move_steps` variable exceeds the `max_ops` value, the function prints a feedback message indicating that the pick has failed due to the object being too far away. It then calls the `pick_failed` function and breaks out of the loop.

If the `move_steps` variable is within the `max_ops` limit, the function waits for a key press event using the `cv.waitKey` function. It also calls the `detect_objects` function to detect objects in the current frame.

The function then initializes temporary variables for the real coordinates of the object (`x_real_temp` and `y_real_temp`). If the `location` parameter is `None`, the function compares the `y_real` value of each detected object and updates the temporary variables if a higher value is found. If the `location` parameter is "left", the function compares the `x_real` value of each detected object and updates the temporary variables if a lower value is found. If the `location` parameter is "right", the function compares the `x_real` value of each detected object and updates the temporary variables if a higher value is found.

If the temporary variables have been updated, the function checks if the `y_real_temp` value is less than a predefined threshold (`y_too_far_to_grab`). If it is, the function prints a feedback message indicating that the pick has failed due to the object being too far away. It then calls the `pick_failed` function and breaks out of the loop.

The function calculates the number of turn steps required to align the object with the Transbot's visual middle using the `robotVisualMiddle` and `center_offset` variables. If the `x_real_temp` value is within the range defined by `robotVisualMiddle-center_offset` and `robotVisualMiddle+center_offset`, the function prints a feedback message indicating that the object is in the center. It then performs a series of forward movements to approach the object, with a sleep duration between each movement specified by the `ForwardSleep` parameter. After the forward movements, the function calls the `close_gripper` function to attempt to grab the object. If the grab is successful, the function calls the `arm_up` function to lift the object and checks if the gripper is still holding the object. If the gripper is still holding the object, the function sets the `picked` global variable to `True` using the `setPicked` function. It then prints a success message and checks if the Transbot has a trailer attached. If it does, the function calls the `drop_trailer` function to detach the trailer.

If the `x_real_temp` value is greater than `robotVisualMiddle+center_offset`, the function prints a feedback message indicating that the object is on the right side. It then performs a series of right rotations to align the Transbot with the object.

If the `x_real_temp` value is less than `robotVisualMiddle-center_offset`, the function prints a feedback message indicating that
## _function TransbotExecute(executions)
**TransbotExecute**: The TransbotExecute function is responsible for executing a series of actions based on a list of executions. It iterates through each execution in the list and performs the corresponding action based on the operator specified in the execution. The function also handles special cases such as querying the location, saying a message, and activating or deactivating a feature.

**parameters**:
- executions: A list of dictionaries representing the actions to be executed. Each dictionary contains two keys: "operator" and "arguments". The "operator" key specifies the action to be performed, and the "arguments" key contains any additional arguments required for the action.

**Code Description**:
The TransbotExecute function begins by initializing a boolean variable called ActionInvoked to False. This variable keeps track of whether any action has been invoked during the execution of the function.

The function then iterates through each execution in the executions list using a for loop. For each execution, it retrieves the operator and arguments from the dictionary.

If the operator is "^forward", the function calls the OpStop function to stop the Transbot's current movement, and then calls the forward function five times to move the Transbot forward. Afterward, it calls the OpStop function again to stop the Transbot's movement.

If the operator is "^left", the function calls the OpStop function to stop the Transbot's current movement, and then calls the left function four times to make the Transbot turn left. Afterward, it calls the OpStop function again to stop the Transbot's movement.

If the operator is "^right", the function calls the OpStop function to stop the Transbot's current movement, and then calls the right function four times to make the Transbot turn right. Afterward, it calls the OpStop function again to stop the Transbot's movement.

If the operator is "^pick", the function calls the OpStop function to stop the Transbot's current movement, and then calls the pick_with_feedback function with the arguments passed to the TransbotExecute function. The pick_with_feedback function is responsible for performing a pick operation with visual feedback using the Transbot's gripper arm.

If the operator is "^drop", the function calls the OpStop function to stop the Transbot's current movement, and then calls the drop function to release the object held by the Transbot's gripper arm.

If the operator is "^activate" or "^deactivate", the function does nothing as these actions are reserved for future use.

If the operator is "^goto", the function retrieves the location query answer by calling the AddInput function from the NAR.py module with a Narsese input string. It then extracts the x, y, z, and w coordinates from the location query answer and converts them to float values. Finally, it calls the OpGo function with the extracted coordinates to navigate the Transbot to the specified location.

If the operator is "^say", the function prints the message specified in the arguments.

After iterating through all the executions, the function returns the ActionInvoked variable, which indicates whether any action has been invoked during the execution of the function.

**Note**:
- The TransbotExecute function assumes that the OpStop, forward, left, right, pick_with_feedback, drop, OpGo, and say functions are defined and accessible within the same module.
- The function relies on the AddInput function from the NAR.py module to query the location and retrieve the location query answer.
- The function assumes that the NAR.py module is imported and accessible within the same module.
- The function assumes that the OpStop, forward, left, right, pick_with_feedback, drop, OpGo, and say functions are properly implemented and perform the desired actions.
- The function assumes that the pick_with_feedback function handles the picking operation with visual feedback using the Transbot's gripper arm.
- The function assumes that the OpGo function sends a goal to the action server for the Transbot to navigate to a specified location.
- The function assumes that the say function prints a message to the console.

**Output Example**:
If any action is invoked during the execution of the TransbotExecute function, the function will return True. Otherwise, it will return False.
## _function valueToTerm(x)
**valueToTerm**: The function of valueToTerm is to convert a numerical value into a string representation.

**parameters**:
- x: A numerical value that needs to be converted into a string.

**Code Description**:
The valueToTerm function takes a numerical value as input and converts it into a string representation. It adds the value of the variable "valueToTermOffset" to the input value and then converts the result into a string. The resulting string is then truncated to the first five characters using the slice operator [:5]. The function returns the truncated string representation of the input value.

This function is called by the TransbotPerceiveAt object in the Transbot module. In the TransbotPerceiveAt function, the valueToTerm function is used to convert the elements of the "trans" and "rot" lists into string representations. These string representations are then concatenated using underscores to form the "transXYrotZW" string. This string is used as an input to the NAR.AddInput function.

**Note**:
- The valueToTermOffset variable is assumed to be defined and accessible within the scope of the valueToTerm function.
- The returned string representation of the input value is truncated to the first five characters using the slice operator [:5]. If the input value is shorter than five characters, the entire string representation will be returned.

**Output Example**:
If the input value is 10 and the valueToTermOffset is 5, the function will return the string "15".
## _function TransbotPerceiveAt(obj, trans, rot)
**TransbotPerceiveAt**: The function of TransbotPerceiveAt is to perceive the location of an object in the environment and send the perception information to the NAR (Non-Axiomatic Reasoning) system for further processing.

**parameters**:
- obj: A string representing the object to be perceived.
- trans: A list of three numerical values representing the translation coordinates of the object.
- rot: A list of four numerical values representing the rotation coordinates of the object.

**Code Description**:
The TransbotPerceiveAt function takes an object, its translation coordinates, and rotation coordinates as input. It converts the translation and rotation values into string representations using the valueToTerm function. The string representations are then concatenated using underscores to form the "transXYrotZW" string.

The function calls the NAR.AddInput function to send a Narsese input to the NAR system. The Narsese input is in the form "<(obj * transXYrotZW) --> at>. :|:". The "<" and ">" symbols indicate the start and end of a statement, "(obj * transXYrotZW)" represents the object and its location, "-->" indicates a relation, and "at" represents the relation type. The ". :|:" at the end of the statement is the punctuation used in Narsese.

**Note**:
- The TransbotPerceiveAt function assumes that the NAR system is already running and its standard input and output streams are accessible.
- The function relies on the valueToTerm function to convert the translation and rotation values into string representations.
- The function uses the NAR.AddInput function to send the perception information to the NAR system for processing.

Now, let's analyze the calling situation of the TransbotPerceiveAt function in the project:

The TransbotPerceiveAt function is called by the TransbotPerceiveVisual function in the Transbot module. In the TransbotPerceiveVisual function, the TransbotPerceiveAt function is used to perceive the location of an object based on its screen coordinates and send the perception information to the NAR system. The screen coordinates are converted into translation and rotation values, which are then passed as arguments to the TransbotPerceiveAt function.

The TransbotPerceiveAt function is also called by the process function in the Transbot module. In the process function, the TransbotPerceiveAt function is called when the input line ends with "? :|:" and contains "{SELF}". The process function retrieves the translation and rotation values using the getLocation function and passes them along with the "{SELF}" object to the TransbotPerceiveAt function.

The TransbotPerceiveAt function is an essential part of the Transbot module as it enables the robot to perceive the location of objects in its environment and communicate this information to the NAR system for reasoning and decision-making.

Please note that the provided documentation is based on the analysis of the code and existing documentation. It is important to review and validate the documentation for accuracy and completeness before using it in a production environment.
## _function TransbotPerceiveVisual(obj, screenX, screenY, trans, rot)
**TransbotPerceiveVisual**: The function of TransbotPerceiveVisual is to perceive the visual information of an object in the environment and send the perception information to the NAR (Non-Axiomatic Reasoning) system for further processing.

**parameters**:
- obj: A string representing the object to be perceived.
- screenX: An integer representing the X-coordinate of the object on the screen.
- screenY: An integer representing the Y-coordinate of the object on the screen.
- trans: A list of three numerical values representing the translation coordinates of the object.
- rot: A list of four numerical values representing the rotation coordinates of the object.

**Code Description**:
The TransbotPerceiveVisual function takes an object, its screen coordinates, translation coordinates, and rotation coordinates as input. It first initializes the "direction" variable with the value "front".

The function then calls the TransbotPerceiveAt function to perceive the location of the object based on its translation and rotation coordinates. This function is responsible for sending the perception information to the NAR system.

Next, the function checks the screenX value against a predefined threshold, robotVisualMiddle-center_offset, to determine the direction of the object. If the screenX value is less than the threshold, the direction is set to "left". If the screenX value is greater than the threshold, the direction is set to "right".

Finally, the function calls the NAR.AddInput function to send a Narsese input to the NAR system. The Narsese input is in the form "<(obj * direction) --> at>. :|:". The "<" and ">" symbols indicate the start and end of a statement, "(obj * direction)" represents the object and its direction, "-->" indicates a relation, and "at" represents the relation type. The ". :|:" at the end of the statement is the punctuation used in Narsese.

**Note**:
- The TransbotPerceiveVisual function assumes that the NAR system is already running and its standard input and output streams are accessible.
- The function relies on the TransbotPerceiveAt function to perceive the location of the object and send the perception information to the NAR system.
- The function determines the direction of the object based on its screenX value and a predefined threshold.
- The function uses the NAR.AddInput function to send the perception information to the NAR system for further processing.

The TransbotPerceiveVisual function is an important part of the Transbot module as it enables the robot to perceive the visual information of objects in its environment and communicate this information to the NAR system for reasoning and decision-making.

Please note that the provided documentation is based on the analysis of the code and existing documentation. It is important to review and validate the documentation for accuracy and completeness before using it in a production environment.
## _function reset_ona
**reset_ona**: The function of reset_ona is to reset the OpenNARS system by adding background knowledge from a file and printing a message indicating that the system has been reset.

**parameters**:
- None

**Code Description**:
The reset_ona function begins by opening the "knowledge.nal" file in read mode using the open() function and assigning the contents of the file to the BackgroundKnowledge variable.

Next, the function iterates over each line of the concatenated string of Configuration and BackgroundKnowledge, split by the newline character. Each line is stripped of leading and trailing whitespace and assigned to the bgstr variable.

If the length of bgstr is greater than 0, indicating that the line is not empty, the function calls the AddInput function from the NAR module to add the Narsese input represented by bgstr to the NAR system.

After adding all the background knowledge, the function prints the message "//transbot.py (ONA) go!" using the print() function.

**Note**:
- The reset_ona function assumes that the "knowledge.nal" file exists in the same directory as the transbot.py file.
- The function relies on the AddInput function from the NAR module to add Narsese inputs to the NAR system.
- The Configuration variable is assumed to be defined and accessible within the same module as the reset_ona function.
- The function does not return any value.

**Calling Situation**:
The reset_ona function is called in the process function from the transbot.py file. The process function is responsible for processing user input and performing corresponding actions in the OpenNARS system.

In the process function, if the user input is "*reset", the reset_ona function is called to reset the OpenNARS system. This is done by adding background knowledge from the "knowledge.nal" file and printing a message indicating that the system has been reset.

**Note**:
- The process function assumes that the reset_ona function is defined and accessible within the same module as the process function.
- The process function is assumed to be called in the context of the Transbot application, where the OpenNARS system is used for reasoning and decision-making.
## _function process(line)
**process**: The function of process is to handle different types of input lines and perform corresponding actions based on the content of the input.

**parameters**:
- line: A string representing the input line to be processed.

**Code Description**:
The `process` function takes an input line and performs different actions based on the content of the line. It first checks if the line is not empty. If it is not empty and ends with "? :|:" and contains "{SELF}", it calls the `getLocation` function to get the current location and then invokes the `TransbotPerceiveAt` function to perceive the location of the transbot at "{SELF}".

Next, it checks if the line ends with "! :|:" or is equal to "*internal". If the `getPicked` function returns True, it adds the input "<gripper --> [hold]>. :|:" to the NAR (Non-Axiomatic Reasoning) system. Otherwise, it adds the input "<gripper --> [open]>. :|:".

Then, it checks if the line ends with "! :|:" or is equal to "*see". It calls the `getCollision` function to get the collision status and the `getLocation` function to get the current location. It also waits for a key event using the `cv.waitKey` function and detects objects using the `detect_objects` function. It then sorts the detections based on their size and selects the nearest object. If there is a valid object, it calculates the real-world coordinates of the object and calls the `TransbotPerceiveVisual` function to perceive the visual information of the object.

If the object is too far to grab, it checks if there are at least two detections and if the first two detections have the same object. If they do, it extracts color and size vectors from the detections and uses the `Nalifier` class to compare the color and size vectors. Based on the comparison result, it adds corresponding statements to the NAR system. If the first two detections have different objects, it iterates over the first two detections, calculates the real-world coordinates, and calls the `TransbotPerceiveVisual` function to perceive the visual information of the objects.

Next, it checks if the object is too far to grab or if there is an obstacle on the right side. If either condition is true, it adds the corresponding obstacle input to the NAR system.

After that, it displays the frame using the `cv.imshow` function.

If the line ends with "! :|:", it adds the input line to the NAR system and retrieves the number of executions from the result. It then enters a loop with a reasoning time limit and adds the input "1" to the NAR system in each iteration. It invokes the `TransbotExecute` function with the accumulated executions and checks if an action has been invoked. If an action has been invoked, it adds the remaining thinking time to the NAR system and breaks out of the loop.

If the line ends with ".", ". :|:", "?", or "? :|:", it simply adds the input line to the NAR system.

If the line is equal to "*pick_with_feedback", it calls the `pick_with_feedback` function.

If the line is equal to "*left", it calls the `left` function with an angular value of 0.6.

If the line is equal to "*right", it calls the `right` function with an angular value of 0.6.

If the line is equal to "*forward", it calls the `forward` function with a linear value of 0.6.

If the line is equal to "*backward", it calls the `backward` function with a linear value of 0.6.

If the line is equal to "*arm_down", it calls the `arm_down` function.

If the line is equal to "*arm_up", it calls the `arm_up` function.

If the line is equal to "*pick", it stops the operation using the `OpStop` function and then calls the `pick` function with the force parameter set to True.

If the line is equal to "*drop", it stops the operation using the `OpStop` function and then calls the `drop` function with the force parameter set to True.

If the line is equal to "*droptrailer", it calls the `drop_trailer` function with the force parameter set to True.

If the line is equal to "*reset", it sets the picked status to False using the `setPicked` function, stops the operation using the `OpStop` function, initializes the pose using the `init_pose` function, and resets the NAR system using the `reset_ona` function.

If the line is a digit or starts with "*volume", "*motorbabbling", or ends with "}", it adds the line to the NAR system.

Finally, the function returns the value of the `ActionInvoked` variable.

**Note**: 
- The `process` function handles different
## _function shell_step(lastLine)
**shell_step**: The function of `shell_step` is to process the input line and perform various actions based on its content. It handles different types of commands and executes corresponding operations accordingly.

**Parameters**:
- `lastLine` (optional): A string representing the previous input line (default value: "").

**Code Description**:
The `shell_step` function takes an input line as a parameter and performs different actions based on the content of the line. It first tries to read an input line from the user and removes any trailing newline characters. If an exception occurs during the input process, the function exits.

Next, it checks if the input line is empty. If it is empty, it assigns the value of the previous input line to the `line` variable. Otherwise, it assigns the current input line to the `line` variable.

The function then prints the processed line by appending "//PROCESSED LINE: " to the line.

The function further checks if the line ends with "! :|:". If it does, it assigns the line to the `lastGoal` variable.

If the line starts with "*clearpoints", the `points` list is cleared, and the line is returned.

If the line starts with "*point", it extracts the location coordinates using the `getLocation` function and appends them to the `points` list. The line is then returned.

If the line starts with "*patrol ", it extracts the number of repetitions from the line and iterates over the `points` list. For each point, it calls the `OpGo` function to navigate to the specified location, and then calls the `TransbotPerceiveAt` function to perceive the location of the transbot and the specified point. It also checks the `lastGoal` for a certain number of checkpoint decisions. If the `process` function returns True, indicating a successful decision, the loop breaks. The line is returned.

If the line starts with "*savepoints", it opens a file named "points.json" in write mode and writes the `points` list to the file in JSON format. The line is returned.

If the line starts with "*loadpoints", it opens a file named "points.json" in read mode and loads the contents of the file into the `points` list. The line is returned.

If the line starts with "*hastrailer ", it extracts the value after the prefix and sets the global variable `hastrailer` to the corresponding boolean value. The line is returned.

If the line is equal to "*loop", it enters an infinite loop and repeatedly calls the `process` function with the `lastGoal` as the input.

If the line starts with "*steps ", it extracts the number of steps from the line and iterates over the range of steps. In each iteration, it calls the `process` function with the `lastGoal` as the input. After the loop, it prints "//\*steps DONE" to indicate the completion of the steps. The line is returned.

Finally, the function calls the `process` function with the current input line and returns the line.

**Note**:
- The `shell_step` function relies on the `input` function to read user input from the console.
- The `shell_step` function uses global variables `lastGoal` and `points` to store and retrieve data.
- The `shell_step` function interacts with other functions such as `getLocation`, `OpGo`, and `TransbotPerceiveAt` to perform specific actions.
- The `shell_step` function handles various commands and their corresponding operations, providing flexibility in controlling the behavior of the transbot.

**Output Example**:
If the input line is "*patrol 2", the function will navigate to the specified points and perform the desired actions. The line "*patrol 2" will be returned.
## _function transbot_shell
Doc has not been generated...
