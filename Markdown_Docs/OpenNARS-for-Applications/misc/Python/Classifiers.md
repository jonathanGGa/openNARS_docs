## _class AdaptiveHypersphereClassifier
**AdaptiveHypersphereClassifier**: The function of AdaptiveHypersphereClassifier is to classify input data points into different categories based on a set of prototypes.

**attributes**:
- spheresize: The radius of the hypersphere used to determine the proximity of a data point to a prototype. Default value is 0.1.
- adaptation: The rate at which the prototypes adapt to new data points. Default value is 0.01.
- maxPrototypes: The maximum number of prototypes to be maintained. Default value is 10.

**Code Description**:
The AdaptiveHypersphereClassifier class implements a classifier that uses adaptive hyperspheres to classify input data points. The classifier maintains a set of prototypes, which are data points that represent different categories. The class provides methods to calculate the category of a given data point, observe new data points, and return the classification result in a Narsese format.

The `__init__` method initializes the classifier with the specified spheresize, adaptation, and maxPrototypes values. It also initializes an empty list to store the prototypes.

The `returnedPrototype` method is a helper method that returns the index of the prototype if there is more than one prototype, otherwise it returns -1 indicating that there is no way to make a distinction with just one prototype.

The `calc` method takes a data point as input and calculates its category based on the proximity to the prototypes. It iterates over the prototypes and calculates the Euclidean distance between each prototype and the input data point. If the distance is less than the spheresize and smaller than the closest distance found so far, the index of the closest prototype is updated. If a closest prototype is found, its position is updated using the adaptation rate. If no closest prototype is found, the input data point is added as a new prototype. If the number of prototypes exceeds the maximum allowed, the oldest prototype is removed. Finally, the method returns the index of the prototype or -1 if no prototype is found.

The `observe` method takes a data point and an optional name as input and returns the classification result in a Narsese format. The method calls the `calc` method to determine the category of the data point and formats the result using the provided name.

**Note**: 
- The classifier uses Euclidean distance to measure the proximity between data points and prototypes.
- The adaptation rate determines how quickly the prototypes adapt to new data points.
- The maximum number of prototypes limits the memory usage of the classifier.

**Output Example**:
If the `calc` method returns 2 and the provided name is "apple", the `observe` method will return the following Narsese format: "<2 --> [apple]>. :|:"
### _class_function __init__(self, spheresize, adaptation, maxPrototypes)
**__init__**: The function of __init__ is to initialize the AdaptiveHypersphereClassifier object with the given parameters.

**parameters**:
- spheresize: A float value representing the size of the hypersphere.
- adaptation: A float value representing the adaptation rate.
- maxPrototypes: An integer value representing the maximum number of prototypes.

**Code Description**:
The __init__ function initializes the AdaptiveHypersphereClassifier object by setting the initial values for the spheresize, adaptation, and maxPrototypes attributes. It also initializes an empty list called prototypes.

The spheresize parameter determines the size of the hypersphere used for classification. A smaller spheresize value will result in a more precise classification, while a larger value will result in a more general classification.

The adaptation parameter determines the rate at which the classifier adapts to new data. A higher adaptation value will result in faster adaptation, while a lower value will result in slower adaptation.

The maxPrototypes parameter determines the maximum number of prototypes that can be stored by the classifier. When the number of prototypes exceeds this limit, the oldest prototypes will be removed to make space for new ones.

**Note**:
- It is recommended to choose appropriate values for the spheresize, adaptation, and maxPrototypes parameters based on the specific requirements of the classification task.
- The spheresize and adaptation values can be adjusted during the classification process to fine-tune the classifier's performance.
- The prototypes attribute can be accessed and modified directly if needed.
### _class_function returnedPrototype(self, prototype)
**returnedPrototype**: The function of returnedPrototype is to return the index of the prototype that is closest to the input data point.

**parameters**:
- prototype: The input data point for which the closest prototype needs to be determined.

**Code Description**:
The returnedPrototype function is a method of the AdaptiveHypersphereClassifier class in the Classifiers.py file. This function takes an input data point called "prototype" and returns the index of the closest prototype from the list of prototypes stored in the class.

The function first checks if the number of prototypes is equal to 1. If it is, the function returns -1, indicating that there is no way to make a distinction with just one prototype.

If there are more than one prototype, the function returns the index of the prototype that is closest to the input data point. The index is determined based on the Euclidean distance between each prototype and the input data point. The prototype with the smallest distance is considered the closest.

**Note**: 
- The function assumes that the prototypes are stored in the "prototypes" attribute of the AdaptiveHypersphereClassifier class.
- The function assumes that the input data point and the prototypes are in the same dimensional space.

**Output Example**:
If the input data point is [1, 2, 3] and the prototypes are [[4, 5, 6], [7, 8, 9], [1, 2, 3]], the function will return 2, indicating that the prototype at index 2 ([1, 2, 3]) is the closest to the input data point.
### _class_function calc(self, x)
**calc**: The function of calc is to calculate the index of the prototype that is closest to the input data point and update the prototypes accordingly.

**parameters**:
- x: The input data point for which the closest prototype needs to be determined.

**Code Description**:
The calc function is a method of the AdaptiveHypersphereClassifier class in the Classifiers.py file. This function takes an input data point called "x" and calculates the index of the closest prototype from the list of prototypes stored in the class.

The function iterates over each prototype in the list and calculates the Euclidean distance between the prototype and the input data point using the np.linalg.norm() function. It then compares the calculated distance with the current closest distance. If the calculated distance is smaller than the spheresize and smaller than the current closest distance, the closest_i variable is updated with the index of the current prototype and the closest_dist variable is updated with the calculated distance.

After iterating through all the prototypes, the function checks if a closest prototype was found by comparing closest_i with -1. If a closest prototype was found, the function updates the closest prototype by applying the adaptation formula: self.prototypes[closest_i] = self.prototypes[closest_i] + (x - self.prototypes[closest_i]) * self.adaptation. The function then returns the index of the closest prototype by calling the returnedPrototype() function.

If no closest prototype was found, the function appends the input data point to the list of prototypes and ensures that the list does not exceed the maximum number of prototypes specified by the maxPrototypes attribute. Finally, the function returns the index of the last added prototype by calling the returnedPrototype() function.

**Note**: 
- The function assumes that the prototypes are stored in the "prototypes" attribute of the AdaptiveHypersphereClassifier class.
- The function assumes that the input data point and the prototypes are in the same dimensional space.

**Output Example**:
If the input data point is [1, 2, 3] and the prototypes are [[4, 5, 6], [7, 8, 9], [1, 2, 3]], the function will update the prototype at index 2 ([1, 2, 3]) and return 2, indicating that the updated prototype is the closest to the input data point.
### _class_function observe(self, x, name)
**observe**: The function of observe is to calculate the index of the prototype that is closest to the input data point and return it as a Narsese statement.

**parameters**:
- x: The input data point for which the closest prototype needs to be determined.
- name (optional): The name of the prototype.

**Code Description**:
The observe function is a method of the AdaptiveHypersphereClassifier class in the Classifiers.py file. This function takes an input data point called "x" and an optional name parameter. It uses the calc function to calculate the index of the closest prototype to the input data point and generates a Narsese statement based on the result.

The function first checks if the name parameter is empty. If it is, it creates a Narsese statement template using the format "%d%s. :|:". Otherwise, it creates a Narsese statement template using the format "<%d --> [%s]>. :|:". The %d and %s placeholders in the template will be replaced with the calculated index and the name parameter, respectively.

The function then calls the calc function with the input data point to get the index of the closest prototype. It uses this index and the name parameter to generate the final Narsese statement by replacing the placeholders in the template.

Finally, the function returns the generated Narsese statement as a list.

**Note**: 
- The function assumes that the calc function is defined and accessible within the same class.
- The function assumes that the calc function returns the index of the closest prototype.
- The function assumes that the Narsese statement format is compatible with the NARS (Non-Axiomatic Reasoning System) framework.

**Output Example**:
If the input data point is [1, 2, 3] and the name parameter is "example", the function will calculate the index of the closest prototype using the calc function and generate the Narsese statement "<2 --> [example]>. :|:". The function will return this statement as a list.
