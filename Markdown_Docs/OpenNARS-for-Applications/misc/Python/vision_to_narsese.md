## _function BoundingBoxFromBBStr(BBStr)
**BoundingBoxFromBBStr**: The function of BoundingBoxFromBBStr is to convert a string representation of bounding box coordinates into a dictionary format.

**parameters**:
- BBStr: A string representing the bounding box coordinates in the format "label1:value1 label2:value2 ...".

**Code Description**:
The BoundingBoxFromBBStr function takes a string representation of bounding box coordinates as input. It first initializes an empty dictionary called M. Then, it processes the input string by removing unnecessary characters such as parentheses, colons, and spaces. The processed string is split into a list of label-value pairs.

Next, the function iterates over the list of label-value pairs using a for loop. For each pair, it extracts the label and converts the corresponding value to a float. The label and value are then added to the dictionary M, with the label as the key and the value as the corresponding value.

Finally, the function returns the resulting dictionary M, which represents the bounding box coordinates in a more structured format.

This function is called by the LineToNarsese function in the vision_to_narsese.py file. In the LineToNarsese function, the BoundingBoxFromBBStr function is used to convert a string representation of a bounding box into a dictionary format. The resulting dictionary is then further processed to obtain the discretized location, which is used to generate a Narsese statement.

**Note**: 
- The input string should be in the format "label1:value1 label2:value2 ...".
- The labels should not contain any special characters or spaces.
- The values should be numeric.

**Output Example**:
If the input BBStr is "label1:0.5 label2:0.8", the function will return the following dictionary:
{
  "label1": 0.5,
  "label2": 0.8
}
## _function LocationFromDetection(BB)
**LocationFromDetection**: The function of LocationFromDetection is to calculate the location coordinates (x, y) based on the given bounding box.

**Parameters**:
- BB: A dictionary representing the bounding box, containing the following keys:
  - "left_x": The x-coordinate of the left side of the bounding box.
  - "top_y": The y-coordinate of the top side of the bounding box.
  - "width": The width of the bounding box.
  - "height": The height of the bounding box.

**Code Description**:
The LocationFromDetection function takes a bounding box as input and calculates the location coordinates (x, y) based on the given bounding box. It creates an empty dictionary called "Location" to store the calculated coordinates. 

The x-coordinate is calculated by adding the left_x coordinate of the bounding box to half of its width. Similarly, the y-coordinate is calculated by adding the top_y coordinate of the bounding box to half of its height. The calculated coordinates are then stored in the "Location" dictionary.

Finally, the function returns the "Location" dictionary containing the calculated coordinates.

This function is called by the LineToNarsese function in the vision_to_narsese.py file. The LineToNarsese function splits a line into label, percent, and bounding box string. It then calls the LocationFromDetection function to calculate the location coordinates from the bounding box string. The calculated location is further processed and printed using other functions.

**Note**: 
- The input bounding box dictionary should contain the keys "left_x", "top_y", "width", and "height".
- The function assumes that the bounding box coordinates are in a valid format.
- The function does not perform any error handling for invalid inputs.

**Output Example**:
If the input bounding box is:
BB = {"left_x": 10, "top_y": 20, "width": 30, "height": 40}

The function will return the following dictionary:
Location = {"x": 25, "y": 40}
## _function DiscretizeValue(Value, MaxValue)
**DiscretizeValue**: The function of DiscretizeValue is to discretize a given value based on a maximum value.

**Parameters**:
- Value: The value to be discretized.
- MaxValue: The maximum value used for discretization.

**Code Description**:
The DiscretizeValue function takes in a value and a maximum value as parameters. It then compares the value with one-third of the maximum value and two-thirds of the maximum value to determine the discretized value. If the value is smaller than one-third of the maximum value, the function returns "smaller". If the value is smaller than two-thirds of the maximum value, the function returns "equal". Otherwise, it returns "larger".

This function is used to categorize a value into one of three categories: "smaller", "equal", or "larger" based on the given maximum value. It is commonly used in scenarios where a continuous value needs to be represented in a discrete manner.

In the project, this function is called by the `DiscretizedLocationFromLocation` function in the `vision_to_narsese.py` file. The `DiscretizedLocationFromLocation` function takes a location as input and discretizes its x and y coordinates using the `DiscretizeValue` function. The discretized coordinates are then stored in a dictionary and returned as the output.

**Note**:
- The `DiscretizeValue` function assumes that the maximum value is a positive number.
- The function does not handle cases where the value is equal to the maximum value.
## _function DiscretizedLocationFromLocation(Location)
**DiscretizedLocationFromLocation**: The function of DiscretizedLocationFromLocation is to discretize the x and y coordinates of a given location based on the maximum values of ImgSizeX and ImgSizeY.

**Parameters**:
- Location: A dictionary representing the location with 'x' and 'y' coordinates.

**Code Description**:
The DiscretizedLocationFromLocation function takes in a location as a parameter and discretizes its x and y coordinates using the DiscretizeValue function. It creates an empty dictionary called DiscretizedLocation. The x coordinate of the location is discretized by calling the DiscretizeValue function with the 'x' coordinate of the location and the maximum value ImgSizeX. The result is stored in the DiscretizedLocation dictionary with the key 'x'. Similarly, the y coordinate of the location is discretized by calling the DiscretizeValue function with the 'y' coordinate of the location and the maximum value ImgSizeY. The result is stored in the DiscretizedLocation dictionary with the key 'y'. Finally, the DiscretizedLocation dictionary is returned as the output of the function.

The DiscretizedLocationFromLocation function is used in the project to convert a continuous location into a discrete representation. This can be useful in various applications where discrete values are required, such as image processing or computer vision tasks. By discretizing the location coordinates, it becomes easier to perform further analysis or processing on the data.

**Note**:
- The DiscretizedLocationFromLocation function assumes that the maximum values ImgSizeX and ImgSizeY are positive numbers.
- The function relies on the DiscretizeValue function to perform the actual discretization of the coordinates.

**Output Example**:
If the input location is {'x': 0.5, 'y': 0.8}, and the maximum values ImgSizeX and ImgSizeY are 1.0, the function will return the following dictionary:
{'x': 'equal', 'y': 'larger'}
## _function Narsesefy(label, percent, DiscretizedLocation)
**Narsesefy**: The function of Narsesefy is to convert a given label, percentage, and discretized location into a Narsese statement.

**Parameters**:
- `label`: A string representing the label of the object.
- `percent`: A float representing the percentage confidence of the object detection.
- `DiscretizedLocation`: A dictionary containing the discretized location of the object along different axes.

**Code Description**:
The `Narsesefy` function takes in a label, percentage, and discretized location as input parameters. It then iterates over the `EncodeAxes` list and constructs a string representation of the location by concatenating the discretized location values with their corresponding axis labels. The constructed location string is stored in the `Loc` variable.

Finally, the function returns a Narsese statement by combining the label, location, and percentage information. The label is enclosed in angle brackets, the location is enclosed in square brackets, and the percentage is included in the Narsese statement as a confidence value. The Narsese statement is formatted as "<label --> [location]>. :|: {1.0 confidence}".

**Note**: 
- The `EncodeAxes` list is not defined within the `Narsesefy` function. It should be defined before calling the function to ensure proper execution.
- The `DiscretizedLocation` parameter is expected to be a dictionary with keys corresponding to the axes defined in the `EncodeAxes` list.

**Output Example**:
If we call the `Narsesefy` function with the following parameters:
- `label`: "cat"
- `percent`: 85.0
- `DiscretizedLocation`: {"x": 2, "y": 3, "z": 1}

The function will return the following Narsese statement:
"<cat --> [2X 3Y 1Z]>. :|: {1.0 0.85}"
## _function LineToNarsese(line)
**LineToNarsese**: The function of LineToNarsese is to convert a given line into a Narsese statement by extracting the label, percentage, and discretized location from the line and passing them to the Narsesefy function.

**parameters**:
- `line`: A string representing a line of input containing the label, percentage, and bounding box information.

**Code Description**:
The LineToNarsese function takes a line of input as a parameter. It first splits the line based on the "%" character to separate the label and bounding box information. The label and percentage are extracted from the first part of the split line by splitting it based on the ":" character. The label is obtained by taking the first element of the resulting split, and the percentage is obtained by converting the second element to a float after removing any leading or trailing whitespace.

The BoundingBoxFromBBStr function is then called with the second part of the split line (representing the bounding box information) as an argument. This function converts the bounding box string into a dictionary format.

The LocationFromDetection function is called with the resulting dictionary from BoundingBoxFromBBStr as an argument. This function calculates the location coordinates (x, y) based on the given bounding box.

The DiscretizedLocationFromLocation function is called with the resulting location dictionary as an argument. This function discretizes the x and y coordinates of the location based on the maximum values of ImgSizeX and ImgSizeY.

Finally, the Narsesefy function is called with the label, percentage, and discretized location as arguments. This function converts the label, percentage, and discretized location into a Narsese statement.

The resulting Narsese statement is printed as the output of the LineToNarsese function.

**Note**: 
- The input line should be in the format "label:percent%bounding_box".
- The label should not contain any special characters or spaces.
- The percentage should be a numeric value.
- The bounding box string should be in a valid format.
- The maximum values ImgSizeX and ImgSizeY should be defined before calling the LineToNarsese function.

**Example**:
If we call the LineToNarsese function with the following line:
```
"cat:85.0%label1:0.5 label2:0.8"
```
The function will convert the line into a Narsese statement and print it as follows:
```
"<cat --> [equalX largerY]>. :|: {1.0 0.85}"
```
