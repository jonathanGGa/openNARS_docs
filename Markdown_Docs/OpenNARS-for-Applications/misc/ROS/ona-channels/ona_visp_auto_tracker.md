## _function detectionToNarseseStatementsList(position, orientation)
**detectionToNarseseStatementsList**: The function of detectionToNarseseStatementsList is to convert the position and orientation of a detected object into a list of Narsese statements.

**parameters**:
- position: A list representing the position of the detected object, with the x, y, and z coordinates.
- orientation: A list representing the orientation of the detected object, with the x, y, z, and w components of the quaternion.

**Code Description**:
The detectionToNarseseStatementsList function takes in the position and orientation of a detected object and converts them into a list of Narsese statements. It first initializes an empty list called narseseStatementsList. Then, it extracts the x and y coordinates from the position list and assigns them to variables x and y, respectively.

Next, the function calls the foveaRelativePosition function from the ona_roslib.py module to obtain the relative position labels for the x and y coordinates. The foveaRelativePosition function discretizes the position and compares it with a midpoint to determine the relative position labels. The labels are assigned to variables xLabel and yLabel, respectively.

The function then determines the door state based on the z component of the orientation. If the z orientation is greater than 80 degrees, the doorstate variable is set to "open"; otherwise, it is set to "closed".

Finally, the function calls the object_narsese function from the ona_roslib.py module, passing the doorstate, "door" as the class, and the xLabel and yLabel as parameters. The object_narsese function generates a Narsese statement based on the given parameters. The generated Narsese statement is appended to the narseseStatementsList.

The function returns the narseseStatementsList, which contains the Narsese statements representing the detected object's properties, class, and position.

**Note**:
- The foveaRelativePosition function, which is called by detectionToNarseseStatementsList, determines the relative position of a point with respect to a midpoint in a discretized manner. It assumes that the discretization factor is non-zero to avoid division by zero errors.
- The object_narsese function, which is also called by detectionToNarseseStatementsList, generates a Narsese statement based on the given parameters. The generated Narsese statement follows a specific format and should be used accordingly in the project.

**Output Example**:
If the position is [10, 20, 30] and the orientation is [0.1, 0.2, 90, 0.5], calling the detectionToNarseseStatementsList function would return a list containing the following Narsese statement:
["<([closed] & door) --> [centeredX centeredY]>. :|: {1.0 0.9}"]
## _class TrackerUtility
**TrackerUtility**: The function of TrackerUtility is to provide utility functions for tracking objects using the visp_auto_tracker package in ROS.

**attributes**:
- `narsese_pub`: A ROS publisher object used to publish Narsese statements.
- `rate`: A ROS rate object used to control the publishing rate.

**Code Description**:
The `TrackerUtility` class is responsible for initializing the necessary ROS nodes and subscribers, as well as providing a callback function for tracking object positions. 

In the `__init__` method, the class initializes a ROS node with the name "TrackerUtility" and sets the anonymous parameter to False. It then subscribes to the "/visp_auto_tracker/object_position" topic, expecting messages of type `PoseStamped`. Additionally, it creates a ROS publisher object named `narsese_pub` that publishes messages of type `String` to the "/ona_ros/nars/narsese" topic. The queue size for the publisher is set to 1. Finally, a ROS rate object named `rate` is created with a rate of 10 Hz.

The `tracker_callback` method is the callback function for the "/visp_auto_tracker/object_position" topic. It takes in the `data` parameter, which contains the pose information of the tracked object. The pose information is extracted from the `data` object and stored in the `pose`, `position`, and `orientation` variables. 

The `position` variable is a list containing the x, y, and z coordinates of the object's position. The `orientation` variable is a list containing the x, y, z, and w components of the object's orientation quaternion.

The `detectionToNarseseStatementsList` function is called with the `position` and `orientation` variables as arguments. This function returns a list of Narsese statements based on the detected object's position and orientation.

Each statement in the list is published using the `narsese_pub` publisher object.

**Note**: 
- This class assumes that the `detectionToNarseseStatementsList` function is defined elsewhere and returns a list of Narsese statements based on the object's position and orientation.
- The `rate` object is used to control the publishing rate of the Narsese statements. Adjust the rate value as needed for the specific application requirements.
### _class_function __init__(self)
**__init__**: The function of __init__ is to initialize the TrackerUtility object. It sets up the necessary ROS nodes, subscribers, publishers, and rate for the object.

**parameters**:
- None

**Code Description**:
The __init__ function initializes the TrackerUtility object by performing the following steps:

1. It calls the rospy.init_node() function to initialize the ROS node with the name 'TrackerUtility'. The anonymous parameter is set to False, which means that the node will have a unique name and will not be anonymous.

2. It creates a rospy.Subscriber object to subscribe to the "/visp_auto_tracker/object_position" topic. The subscriber is set to listen for messages of type PoseStamped. The callback function self.tracker_callback is specified as the function to handle the received messages.

3. It creates a rospy.Publisher object named self.narsese_pub. This publisher is used to publish messages of type String to the "/ona_ros/nars/narsese" topic. The queue_size parameter is set to 1, which means that only the latest message will be kept in the queue.

4. It creates a rospy.Rate object named self.rate with a rate of 10 Hz. This rate is used to control the frequency at which the object performs its tasks.

**Note**:
- The rospy.init_node() function initializes the ROS node with the specified name. Make sure that the name is unique and does not conflict with other nodes in the ROS system.
- The rospy.Subscriber object is used to subscribe to a specific topic and receive messages of a specific type. Make sure that the topic name and message type are correct and match the publisher that is publishing messages to that topic.
- The rospy.Publisher object is used to publish messages to a specific topic. Make sure that the topic name is correct and matches the subscriber that is listening to that topic.
- The rospy.Rate object is used to control the frequency at which the object performs its tasks. Make sure that the rate is set to an appropriate value based on the requirements of the system.

Please let me know if you need any further assistance.
### _class_function tracker_callback(self, data)
**tracker_callback**: The function of tracker_callback is to handle the callback function for the "/visp_auto_tracker/object_position" topic. It receives the pose data of a detected object and converts it into a list of Narsese statements using the detectionToNarseseStatementsList function. The generated Narsese statements are then published to the "/ona_ros/nars/narsese" topic.

**parameters**:
- data: The pose data of the detected object.

**Code Description**:
The tracker_callback function takes in the pose data of a detected object and extracts the position and orientation information from it. It first assigns the pose data to the variable "pose".

Next, the function extracts the x, y, and z coordinates from the position and assigns them to the "position" variable as a list. Similarly, it extracts the x, y, z, and w components of the quaternion from the orientation and assigns them to the "orientation" variable as a list.

The function then calls the detectionToNarseseStatementsList function, passing the position and orientation as parameters. The detectionToNarseseStatementsList function converts the position and orientation into a list of Narsese statements representing the detected object's properties, class, and position.

For each Narsese statement generated by the detectionToNarseseStatementsList function, the tracker_callback function publishes it to the "/ona_ros/nars/narsese" topic using the self.narsese_pub.publish(stmt) statement.

**Note**:
- The detectionToNarseseStatementsList function is called to convert the position and orientation of the detected object into a list of Narsese statements. Refer to the documentation of the detectionToNarseseStatementsList function for more details on its functionality.
- The self.narsese_pub.publish(stmt) statement publishes the generated Narsese statements to the "/ona_ros/nars/narsese" topic. Make sure the necessary ROS setup and configuration are in place for the messages to be successfully published.
- Ensure that the "/visp_auto_tracker/object_position" topic is being published with the correct message type (PoseStamped) and that the necessary ROS setup and configuration are in place for the messages to be received by the tracker_callback function.
