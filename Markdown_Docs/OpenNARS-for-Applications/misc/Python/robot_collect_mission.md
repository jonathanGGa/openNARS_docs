## _function close
**close**: The function of close is to close the gripper of the robot.

**parameters**:
- This function does not take any parameters.

**Code Description**:
The `close` function is responsible for closing the gripper of the robot. It achieves this by running the `m_gripper.run` method with a power value of -70, which indicates the direction and intensity of the gripper movement. After that, the function pauses for 4 seconds using the `sleep` function.

This function is called by the `gripper_pick` function in the `robot_collect_mission.py` file. The `gripper_pick` function is responsible for picking up objects using the robot's gripper. Before closing the gripper, the `gripper_pick` function checks if the gripper is already closed. If it is closed, the function returns without performing any action. Otherwise, it moves the robot forward twice, then calls the `close` function to close the gripper. Finally, it sets the `closed_gripper` variable to `True` to indicate that the gripper is now closed.

**Note**:
- The `power` parameter of the `m_gripper.run` method determines the strength of the gripper movement. A negative value indicates closing the gripper, while a positive value indicates opening it.
- The `sleep` function is used to introduce a delay of 4 seconds before further actions are taken. This delay allows the gripper to close properly before proceeding with other tasks.
- The `closed_gripper` variable is a global variable that keeps track of the gripper's state. It is set to `True` after the gripper is closed to prevent unnecessary closing operations.
## _function open
**open**: The function of open is to control the gripper of the robot to open.

**parameters**:
- No parameters are required for this function.

**Code Description**:
The `open` function is responsible for opening the gripper of the robot. It performs the following steps:

1. The `m_gripper.run(power=70)` command is used to activate the gripper and set the power to 70. This command starts the motor of the gripper and applies a certain amount of force to open it.
2. The `sleep(2.0)` command is used to pause the execution of the program for 2 seconds. This allows the gripper to fully open and stabilize before proceeding to the next step.
3. The `m_gripper.idle()` command is used to stop the motor of the gripper. This command deactivates the gripper and stops applying force, keeping it in an open position.

The `open` function is typically called in situations where the gripper needs to be opened, such as when the robot needs to release an object it is holding. 

In the project, the `open` function is called by two other functions: `interrupt` and `gripper_drop`.

In the `interrupt` function, the `open` function is called if the gripper is currently closed. This is done to ensure that the gripper is opened before the program exits. The `interrupt` function is responsible for handling interruptions and stopping the robot's movement.

In the `gripper_drop` function, the `open` function is called after the robot moves forward three times. This is done to release the object held by the gripper. The `gripper_drop` function is responsible for dropping the object held by the gripper.

**Note**:
- The `open` function does not require any parameters.
- It is important to ensure that the gripper is closed before calling the `open` function, as calling it when the gripper is already open may result in unexpected behavior.
- The duration of the pause in the `sleep` command can be adjusted as needed, depending on the specific requirements of the gripper and the object being held.
## _function interrupt
**interrupt**: The function of interrupt is to handle interruptions and stop the robot's movement.

**parameters**:
- No parameters are required for this function.

**Code Description**:
The `interrupt` function is responsible for handling interruptions and stopping the robot's movement. It performs the following steps:

1. It checks if the touch sensor connected to port 2 (`Touch(b, PORT_2)`) is being pressed by calling the `get_sample()` method. If the touch sensor is pressed, indicating an interruption, the function proceeds to the next step. Otherwise, it does nothing.
2. The `m_left.idle()` and `m_right.idle()` commands are used to stop the left and right motors of the robot, respectively. These commands deactivate the motors and stop the robot's movement.
3. If the gripper is currently closed (`closed_gripper` is True), the `open()` function is called to open the gripper. This is done to ensure that the gripper is opened before the program exits.
4. The `exit(0)` command is used to exit the program with a status code of 0. This terminates the program execution.

The `interrupt` function is typically called in situations where the robot needs to handle interruptions and stop its movement. It is commonly used in scenarios where the robot needs to respond to external events or user input.

In the project, the `interrupt` function is called in several other functions, such as `forward`, `left`, `right`, and `gripper_pick`. These functions call the `interrupt` function to handle interruptions and stop the robot's movement before performing their respective actions.

**Note**:
- The `interrupt` function does not require any parameters.
- It is important to ensure that the touch sensor is properly connected to the correct port (`PORT_2`) for the `get_sample()` method to work correctly.
- The `open()` function is called if the gripper is currently closed to ensure that the gripper is opened before the program exits.
## _function forward(mul)
**forward**: The function of forward is to move the robot forward for a specified duration.

**parameters**:
- mul (optional): A multiplier for the power of the motors. By default, it is set to 1.

**Code Description**:
The `forward` function is responsible for moving the robot forward for a specified duration. It performs the following steps:

1. It calls the `interrupt` function to handle interruptions and stop the robot's movement.
2. It calculates the power (`P`) for the motors based on the state of the gripper. If the gripper is closed (`closed_gripper` is True), the power is set to 70. Otherwise, it is set to 64.
3. It calls the `run` method of the left and right motors (`m_left.run()` and `m_right.run()`) with the calculated power multiplied by the `mul` parameter. This sets the motors to run at the specified power.
4. It pauses the execution for 1.3 seconds using the `sleep` function from the `time` module.
5. It calls the `idle` method of the left and right motors (`m_left.idle()` and `m_right.idle()`) to stop the motors and put them in an idle state.
6. It returns the string "forward" to indicate that the forward action has been completed.

The `forward` function is typically called when the robot needs to move forward for a certain duration. It is commonly used in scenarios where the robot needs to navigate a specific path or reach a particular location.

**Note**:
- The `mul` parameter can be used to adjust the power of the motors. A higher value will result in faster movement, while a lower value will result in slower movement.
- The `interrupt` function is called at the beginning of the `forward` function to handle interruptions and stop the robot's movement if necessary.
- The duration of the forward movement is fixed at 1.3 seconds in the current implementation.
- The `forward` function does not return any value other than the string "forward" to indicate completion.

**Output Example**:
"forward"
## _function left(doScan)
**left**: The function of left is to make the robot turn left by controlling the left and right motors.

**parameters**:
- doScan (optional): A boolean parameter that indicates whether the robot should perform a scan while turning left. By default, it is set to False.

**Code Description**:
The `left` function is responsible for making the robot turn left by controlling the left and right motors. It performs the following steps:

1. It calls the `interrupt` function to handle interruptions and stop the robot's movement.
2. It sets the power (`P`) of the left motor based on the state of the gripper. If the gripper is closed (`closed_gripper` is True), the power is set to 70. Otherwise, it is set to 64.
3. It calls the `run()` method of the `m_left` motor with the calculated power (`P`) to make the left motor rotate.
4. It calls the `run()` method of the `m_right` motor with the negative value of the calculated power (`-P`) to make the right motor rotate in the opposite direction.
5. It pauses the execution for a certain duration depending on the value of the `doScan` parameter. If `doScan` is True, the pause duration is set to 0.45 seconds. Otherwise, it is set to 1.0 second.
6. It calls the `idle()` method of both the `m_left` and `m_right` motors to stop their rotation and put them in an idle state.
7. Finally, it returns the string "left" to indicate that the robot has turned left.

The `left` function is typically called when the robot needs to turn left. It can be used in various scenarios, such as navigating a maze or following a specific path.

**Note**:
- The `doScan` parameter is optional and can be omitted when calling the `left` function.
- The `interrupt` function is called at the beginning of the `left` function to handle interruptions and stop the robot's movement.
- The power (`P`) of the left motor is determined based on the state of the gripper. If the gripper is closed, a higher power is used to compensate for the additional weight.
- The pause duration during execution is determined by the value of the `doScan` parameter. If `doScan` is True, a shorter pause duration is used to allow for scanning while turning left.
- The `left` function returns the string "left" to indicate that the robot has turned left.

**Output Example**: "left"
## _function right(doScan)
**right**: The function of right is to make the robot turn right.

**parameters**:
- doScan (optional): A boolean parameter indicating whether the robot should perform a scan while turning. By default, it is set to False.

**Code Description**:
The `right` function is responsible for making the robot turn right. It performs the following steps:

1. It calls the `interrupt` function to handle interruptions and stop the robot's movement.
2. It calculates the power value `P` based on the state of the gripper. If the gripper is closed (`closed_gripper` is True), the power value is set to 70. Otherwise, it is set to 64.
3. It runs the left motor (`m_left`) with a negative power value of `-P`, causing the robot to turn right.
4. It runs the right motor (`m_right`) with a power value of `P`, causing the robot to turn right.
5. It pauses the execution for a certain duration. If the `doScan` parameter is True, the pause duration is set to 0.45 seconds. Otherwise, it is set to 1.0 second.
6. It stops the left and right motors by calling the `idle()` method on both motors.
7. It returns the string "right" to indicate that the function has successfully executed.

The `right` function is typically called when the robot needs to turn right. It can be used in various scenarios, such as navigating a maze or following a specific path.

**Note**:
- The `doScan` parameter is optional and defaults to False. If set to True, the robot will perform a scan while turning.
- The power value `P` determines the speed at which the robot turns. Adjusting this value can affect the turning speed of the robot.
- The pause duration can also be adjusted based on the specific requirements of the application.

**Output Example**: "right"
## _function gripper_pick
**gripper_pick**: The function of gripper_pick is to pick up objects using the robot's gripper.

**parameters**:
- This function does not take any parameters.

**Code Description**:
The `gripper_pick` function is responsible for picking up objects using the robot's gripper. It performs the following steps:

1. It calls the `interrupt` function to handle interruptions and stop the robot's movement.
2. It checks if the gripper is already closed (`closed_gripper` is True). If it is closed, indicating that an object is already picked up, the function returns without performing any action.
3. If the gripper is not closed, the function moves the robot forward twice by calling the `forward` function.
4. It then calls the `close` function to close the gripper.
5. After closing the gripper, the `closed_gripper` variable is set to `True` to indicate that the gripper is now closed.
6. Finally, the function returns the string "gripper_pick" to indicate that the gripper pick action has been completed.

The `gripper_pick` function is typically called when the robot needs to pick up objects using its gripper. It is commonly used in scenarios where the robot needs to collect or manipulate objects.

**Note**:
- The `interrupt` function is called at the beginning of the `gripper_pick` function to handle interruptions and stop the robot's movement if necessary.
- The `closed_gripper` variable is a global variable that keeps track of the gripper's state. It is set to `True` after the gripper is closed to prevent unnecessary closing operations.
- The `forward` function is called twice before closing the gripper to position the robot correctly for the pick action.
- The `close` function is responsible for closing the gripper of the robot. It is called by the `gripper_pick` function to perform the gripper closing action.
- The `gripper_pick` function does not take any parameters.
- The return value of the `gripper_pick` function is the string "gripper_pick" to indicate completion.

**Output Example**:
"gripper_pick"
## _function gripper_drop
**gripper_drop**: The function of gripper_drop is to drop the object held by the gripper of the robot.

**parameters**:
- No parameters are required for this function.

**Code Description**:
The `gripper_drop` function is responsible for dropping the object held by the gripper of the robot. It performs the following steps:

1. It checks the state of the `closed_gripper` variable. If the gripper is not closed (i.e., `closed_gripper` is False), the function returns without performing any action.
2. It calls the `forward` function three times to move the robot forward.
3. It calls the `open` function to open the gripper and release the object.
4. It calls the `forward` function twice with a negative multiplier (`mul=-1`) to move the robot backward.
5. It updates the state of the `closed_gripper` variable to indicate that the gripper is now open.
6. It returns the string "gripper_drop" to indicate that the gripper drop action has been completed.

The `gripper_drop` function is typically called when the robot needs to release an object it is holding. It is commonly used in scenarios where the robot needs to collect and deposit objects.

**Note**:
- The `gripper_drop` function does not require any parameters.
- It is important to ensure that the gripper is closed before calling the `gripper_drop` function, as calling it when the gripper is already open may result in unexpected behavior.
- The `forward` function is called before and after the `open` function to ensure that the gripper is in the correct position for dropping the object.
- The `forward` function is called three times before the `open` function to move the robot forward and position it correctly for dropping the object.
- The `forward` function is called twice with a negative multiplier after the `open` function to move the robot backward and return it to its original position.
- The `open` function is called to open the gripper and release the object.
- The `closed_gripper` variable is updated to indicate that the gripper is now open.
- The `gripper_drop` function does not return any value other than the string "gripper_drop" to indicate completion.

**Output Example**:
"gripper_drop"
## _function scan
**scan**: The function of scan is to perform a scanning operation using an ultrasonic sensor and determine if the proximity to an object is less than 20.

**parameters**:
- None

**Code Description**:
The `scan` function is responsible for performing a scanning operation using an ultrasonic sensor to measure the proximity to an object. It follows the steps below:

1. It initializes the `Proximity` variable with a value of 1000.
2. It calls the `Ultrasonic` class with the parameters `b` and `PORT_3` to create an instance of the ultrasonic sensor.
3. It retrieves the sample value from the ultrasonic sensor using the `get_sample()` method and compares it with the current value of `Proximity`. The `min()` function is used to update `Proximity` with the minimum value between the current `Proximity` and the retrieved sample value.
4. It calls the `left` function with the parameter `doScan` set to `True` to make the robot turn left and potentially perform a scan.
5. It retrieves another sample value from the ultrasonic sensor and updates `Proximity` with the minimum value between the current `Proximity` and the retrieved sample value.
6. It calls the `right` function with the parameter `doScan` set to `True` to make the robot turn right and potentially perform a scan.
7. It retrieves another sample value from the ultrasonic sensor and updates `Proximity` with the minimum value between the current `Proximity` and the retrieved sample value.
8. It calls the `right` function with the parameter `doScan` set to `True` to make the robot turn right and potentially perform a scan.
9. It retrieves another sample value from the ultrasonic sensor and updates `Proximity` with the minimum value between the current `Proximity` and the retrieved sample value.
10. It calls the `left` function with the parameter `doScan` set to `True` to make the robot turn left and potentially perform a scan.
11. It retrieves another sample value from the ultrasonic sensor and updates `Proximity` with the minimum value between the current `Proximity` and the retrieved sample value.
12. It checks if the value of `Proximity` is less than 20 and returns `True` if it is, indicating that the proximity to an object is less than 20. Otherwise, it returns `False`.

The `scan` function is typically used when the robot needs to perform a scanning operation to detect nearby objects. It can be used in various scenarios, such as obstacle avoidance or object detection.

**Note**:
- The `Proximity` variable is used to store the minimum proximity value detected during the scanning operation.
- The `Ultrasonic` class is used to interface with the ultrasonic sensor and retrieve sample values.
- The `left` and `right` functions are called to make the robot turn left and right, respectively, potentially allowing for scanning during the turning operation.
- The `doScan` parameter of the `left` and `right` functions determines whether a scan should be performed while turning.
- The `scan` function returns `True` if the proximity to an object is less than 20, and `False` otherwise.

**Output Example**: True
## _function ExecMotorCommands(executions, DisableForward)
**ExecMotorCommands**: The function of ExecMotorCommands is to execute a series of motor commands based on the given list of executions. It determines the appropriate action for each execution based on the "operator" value and calls the corresponding functions to perform the desired motor action. The function also has an optional parameter, DisableForward, which can be used to disable the forward action if necessary.

**parameters**:
- executions: A list of dictionaries representing the motor commands to be executed. Each dictionary should have an "operator" key indicating the desired action.
- DisableForward (optional): A boolean parameter that, when set to True, disables the forward action. By default, it is set to False.

**Code Description**:
The `ExecMotorCommands` function iterates over the list of executions and performs the following steps for each execution:

1. It prints the execution for debugging purposes.
2. It checks the value of the "operator" key in the execution dictionary to determine the desired action.
3. If the "operator" value is "^left", it calls the `left` function to make the robot turn left.
4. If the "operator" value is "^right", it calls the `right` function to make the robot turn right.
5. If the "operator" value is "^forward" and the DisableForward parameter is False, it calls the `forward` function to move the robot forward.
6. If the "operator" value is "^pick" and the DisableForward parameter is False, it calls the `gripper_pick` function to pick up an object using the gripper.
7. If the "operator" value is "^drop" and the DisableForward parameter is False, it calls the `gripper_drop` function to drop the object held by the gripper.
8. After executing the appropriate action for each execution, it returns the value of the `action` variable.

The `ExecMotorCommands` function is typically used to execute a sequence of motor commands based on a predefined plan or set of instructions. It allows the robot to perform complex tasks by combining different motor actions.

**Note**:
- The `DisableForward` parameter can be used to prevent the robot from moving forward if necessary. This can be useful in situations where forward movement is not desired or may cause hardware damage.
- The function only performs one action for each execution. If multiple actions need to be performed simultaneously, they should be specified as separate executions in the list.
- The function returns the value of the `action` variable, which represents the last executed action. If no action is executed, the return value will be None.

**Output Example**: The return value of the `ExecMotorCommands` function depends on the executed action. It can be one of the following: "left", "right", "forward", "gripper_pick", "gripper_drop", or None.
## _function NAR_Invoke(Proximity, VisualEvents)
**NAR_Invoke**: The function of NAR_Invoke is to invoke the NAR (Non-Axiomatic Reasoning) system based on the given proximity and visual events. It processes the inputs and determines the appropriate actions to be taken by the robot.

**parameters**:
- Proximity: A boolean value indicating whether there is an obstacle in proximity to the robot.
- VisualEvents: A list of visual events representing the objects observed by the robot.

**Code Description**:
The `NAR_Invoke` function starts by initializing the variable `SeenSomethingMissionRelevant` as False. This variable is used to keep track of whether any mission-relevant objects have been observed.

If there is an obstacle in proximity (`Proximity` is True), the function calls the `AddInput` function from the `NAR.py` module to add a Narsese input "<obstacle --> [observed]>." to the NAR system. This input represents the observation of an obstacle. 

If there is no obstacle in proximity, the function checks the status of the gripper. If the gripper is closed, it adds the Narsese input "<gripper --> [closed]>." to the NAR system. Otherwise, it adds the input "<gripper --> [open]>." to represent the status of the gripper.

Next, the function checks if there are any visual events. If the length of the `VisualEvents` list is greater than 0, it iterates over each object in the `VisibleObjects` list and each visual event in the `VisualEvents` list. It checks if the object is present in any of the visual events. If it is, it adds the visual event as a Narsese input to the NAR system and sets `SeenSomethingMissionRelevant` to True.

If no mission-relevant objects have been observed (`SeenSomethingMissionRelevant` is still False), the function adds the Narsese input "(! <obstacle --> [observed]>)." to the NAR system. This input represents the negation of the observation of an obstacle.

The function then determines the appropriate action based on the proximity and the observation of mission-relevant objects. If there is an obstacle in proximity and no mission-relevant objects have been observed, it calls the `AddInput` function to add the Narsese input "(! <obstacle --> [observed]>)!" to the NAR system. This input represents the negation of the observation of an obstacle and is used to prevent the robot from moving forward as a reflex to avoid damaging the hardware. The function retrieves the executions from the NAR system's output and calls the `ExecMotorCommands` function to execute the motor commands, disabling the forward action.

If there is no obstacle in proximity or mission-relevant objects have been observed, the function adds the Narsese input "<mission --> [progressed]>!" or "<{SELF} --> [moved]>!" to the NAR system, depending on whether mission-relevant objects have been observed. It also adds the input "5" to represent a predefined action. The function retrieves the executions from the NAR system's output and calls the `ExecMotorCommands` function to execute the motor commands.

Finally, if the executed action is "forward", the function adds the Narsese input "<{SELF} --> [moved]>." to the NAR system.

**Note**:
- The `NAR_Invoke` function relies on the `AddInput` function from the `NAR.py` module to communicate with the NAR system and process the inputs.
- The function uses the `ExecMotorCommands` function to execute the motor commands based on the output from the NAR system.
- The function assumes that the `VisibleObjects` list is defined and contains the objects visible to the robot.
- The function assumes that the `closed_gripper` variable is defined and represents the status of the gripper.
- The function assumes that the `NAR` module is imported and accessible within the same module as the `NAR_Invoke` function.
