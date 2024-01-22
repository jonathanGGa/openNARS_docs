## _class ValueReporter
**ValueReporter**: The ValueReporter class is responsible for reporting values and calculating the frequency and confidence of sensed values based on a given input.

**Attributes**:
- `values`: A list that stores the values reported by the ValueReporter.
- `AIKR_Limit`: An optional parameter that sets the limit for the number of values to be stored in the `values` list.

**Code Description**:
The `ValueReporter` class has an `__init__` method that initializes the `values` list and sets the `AIKR_Limit` attribute. The `reportValue` method takes an input value `x` and calculates the frequency and confidence of the sensed value based on the values stored in the `values` list.

The `reportValue` method first checks if `RangeUpdate` is set to True. If it is, the input value `x` is appended to the `values` list. If the `AIKR_Limit` attribute is not None, the `values` list is truncated to the last `AIKR_Limit` values.

Next, the method calculates the weights `wplus` and `wminus` based on the values in the `values` list. The weight is determined by the absolute difference between the input value `x` and each value in the `values` list. If a value in the `values` list is less than `x`, the weight is added to `wplus`. If a value in the `values` list is greater than `x`, the weight is added to `wminus`.

The total weight `w` is calculated as the sum of `wplus` and `wminus`. The frequency is calculated as the ratio of `wplus` to the total weight `w`, and the confidence is calculated as the ratio of `w` to `w+1.0`. The sensed value truth is represented as a tuple `(frequency, confidence * Sensation_Reliance)`.

If the `Print` parameter is set to True, the sensed value truth is printed to the console. Finally, the sensed value truth is returned.

**Note**: 
- The `ValueReporter` class can be used to track and analyze the frequency and confidence of sensed values over time.
- The `AIKR_Limit` attribute can be used to limit the number of values stored in the `values` list.
- The `reportValue` method calculates the frequency and confidence of the sensed value based on the values stored in the `values` list.
- The `RangeUpdate` parameter determines whether the `values` list should be updated with the new input value.
- The `Uniform_Weight` parameter determines whether the weights should be calculated uniformly or based on the absolute difference between the input value and each value in the `values` list.
- The `Print` parameter determines whether the sensed value truth should be printed to the console.

**Output Example**:
If the `Print` parameter is set to True, the following output may be printed to the console:
```
<{S} --> [P]>. :|: {frequency, confidence * Sensation_Reliance} from value x
```
The sensed value truth is returned as a tuple `(frequency, confidence * Sensation_Reliance)`.
### _class_function reportValue(self, x, Sensation_Reliance, RangeUpdate, Uniform_Weight, Print)
**reportValue**: The function of reportValue is to calculate the frequency and confidence of a given value based on a list of previously reported values.

**parameters**:
- x: The value for which the frequency and confidence need to be calculated.
- Sensation_Reliance (optional): The reliance factor for the confidence calculation. Default value is 0.9.
- RangeUpdate (optional): A boolean flag indicating whether to update the list of values. Default value is True.
- Uniform_Weight (optional): A boolean flag indicating whether to use uniform weight for the calculation. Default value is False.
- Print (optional): A boolean flag indicating whether to print the calculated values. Default value is False.

**Code Description**:
The function first checks if the RangeUpdate flag is set to True. If it is, the given value is appended to the list of values. If the AIKR_Limit (an attribute of the object) is not None, the list of values is trimmed to the last AIKR_Limit elements.

Next, the function initializes two variables, wplus and wminus, to keep track of the weights for values greater than and less than the given value, respectively.

Then, a loop iterates over each value in the list of values. For each value, the weight is calculated as either 1.0 (if Uniform_Weight is True) or the absolute difference between the given value and the current value. If the current value is less than the given value, the weight is added to wplus. If the current value is greater than the given value, the weight is added to wminus.

After the loop, the total weight, w, is calculated as the sum of wplus and wminus. The frequency is calculated as the ratio of wplus to the total weight (wplus + wminus), unless the total weight is 0, in which case the frequency is set to 0.5. The confidence is calculated as the ratio of w to (w + 1.0), unless the total weight is 0, in which case the confidence is set to 0.0.

The Sensed_Value_Truth is then calculated as a tuple containing the frequency and the confidence multiplied by the Sensation_Reliance.

If the Print flag is set to True, the calculated values are printed.

Finally, the Sensed_Value_Truth is returned as the output of the function.

**Note**:
- The RangeUpdate flag determines whether the list of values should be updated with the given value. If set to False, the list remains unchanged.
- The Uniform_Weight flag determines whether all values have equal weight in the calculation. If set to True, the weight is always 1.0.
- The Print flag can be used to display the calculated values for debugging or monitoring purposes.

**Output Example**:
If the function is called with x=5, Sensation_Reliance=0.9, RangeUpdate=True, Uniform_Weight=False, and Print=False, the output could be:
(0.75, 0.6923076923076923)
## _function Truth_c2w(c)
**Truth_c2w**: The function of Truth_c2w is to calculate the complementary value of a given confidence value.

**parameters**:
- c: A float value representing the confidence value.

**Code Description**:
The Truth_c2w function takes a confidence value as input and calculates its complementary value using the formula c / (1 - c). This formula is derived from the definition of confidence in the context of the NARS (Non-Axiomatic Reasoning System) framework.

In the NARS framework, confidence represents the degree of belief in a statement or proposition. It ranges from 0 to 1, where 0 indicates complete disbelief and 1 indicates absolute certainty. The complementary value of confidence is used to represent the degree of disbelief.

The function first calculates the complementary value by dividing the confidence value by the difference between 1 and the confidence value. This ensures that the result is within the range of 0 to 1.

**Note**:
- The input confidence value should be a float between 0 and 1, inclusive.
- The function does not handle division by zero. If the input confidence value is 1, the function will raise a ZeroDivisionError.

**Output Example**:
- Example 1:
  - Input: c = 0.7
  - Output: 2.3333333333333335
- Example 2:
  - Input: c = 0.2
  - Output: 0.25
## _function Truth_w2c(w)
**Truth_w2c**: The function of Truth_w2c is to calculate the truth value confidence based on the given weight.

**parameters**:
- w: A numeric value representing the weight.

**Code Description**:
The Truth_w2c function takes a weight value as input and calculates the truth value confidence based on the weight. It uses a conditional statement to check if the weight is greater than 0. If it is, the function calculates the truth value confidence by dividing the weight by the sum of the weight and 1. If the weight is not greater than 0, the function returns 0.

This function is used in several other functions within the project. It is called by the following objects:

1. OpenNARS-for-Applications\misc\Python\Nalifier.py/TruthValue:
   - The TruthValue function calls the Truth_w2c function as part of its return statement. It passes the sum of two weight values (w_plus and w_minus) as the input to the Truth_w2c function. The return value of the Truth_w2c function is used to calculate the second element of the return value of the TruthValue function.

2. OpenNARS-for-Applications\misc\Python\Nalifier.py/Truth_Abduction:
   - The Truth_Abduction function calls the Truth_w2c function as part of its return statement. It passes the product of three values (f1, c1, and c2) as the input to the Truth_w2c function. The return value of the Truth_w2c function is used to calculate the second element of the return value of the Truth_Abduction function.

3. OpenNARS-for-Applications\misc\Python\Nalifier.py/Truth_Comparison:
   - The Truth_Comparison function calls the Truth_w2c function as part of its return statement. It passes the product of three values (f0, c1, and c2) as the input to the Truth_w2c function. The return value of the Truth_w2c function is used to calculate the second element of the return value of the Truth_Comparison function.

4. OpenNARS-for-Applications\misc\Python\Nalifier.py/Truth_Revision:
   - The Truth_Revision function calls the Truth_w2c function as part of its return statement. It passes the product of three values (f0, c1, and c2) as the input to the Truth_w2c function. The return value of the Truth_w2c function is used to calculate the second element of the return value of the Truth_Revision function.

**Note**: 
- The Truth_w2c function expects a numeric value as input for the weight parameter.
- The function returns a numeric value representing the truth value confidence.
- The function uses a conditional statement to handle the case when the weight is not greater than 0.

**Output Example**:
If the weight value is 2, the function will return 0.6666666666666666.
## _function Truth_w2f(w_plus, w_minus)
**Truth_w2f**: The function of Truth_w2f is to calculate the truth value of a given proposition based on the positive and negative weights assigned to it.

**parameters**:
- w_plus: A numeric value representing the positive weight of the proposition.
- w_minus: A numeric value representing the negative weight of the proposition.

**Code Description**:
The Truth_w2f function takes two parameters, w_plus and w_minus, which represent the positive and negative weights of a proposition, respectively. It calculates the truth value of the proposition using the following formula:

```
w_plus / (w_plus + w_minus) if w_plus + w_minus > 0 else 0.5
```

If the sum of w_plus and w_minus is greater than 0, the function divides w_plus by the sum of w_plus and w_minus to calculate the truth value. Otherwise, it returns a default truth value of 0.5.

This function is called by the TruthValue function in the Nalifier.py module. The TruthValue function uses the Truth_w2f function to calculate the truth value of a proposition and combines it with the truth value calculated by the Truth_w2c function to return a tuple of truth values.

**Note**:
- The Truth_w2f function assumes that the positive and negative weights provided are numeric values.
- If the sum of w_plus and w_minus is 0 or less, the function returns a default truth value of 0.5.

**Output Example**:
If w_plus is 3 and w_minus is 1, the function will return 0.75.
## _function TruthValue(w_plus, w_minus)
**TruthValue**: The function of TruthValue is to calculate the truth value of a proposition based on the positive and negative weights assigned to it.

**parameters**:
- w_plus: A numeric value representing the positive weight of the proposition.
- w_minus: A numeric value representing the negative weight of the proposition.

**Code Description**:
The TruthValue function takes two parameters, w_plus and w_minus, which represent the positive and negative weights of a proposition, respectively. It calculates the truth value of the proposition by calling two other functions: Truth_w2f and Truth_w2c. 

The Truth_w2f function is responsible for calculating the truth value based on the positive and negative weights. It divides the positive weight (w_plus) by the sum of the positive and negative weights (w_plus + w_minus) to calculate the truth value. If the sum of the weights is 0 or less, the function returns a default truth value of 0.5.

The Truth_w2c function is responsible for calculating the truth value confidence based on the given weight. It takes a weight value as input and calculates the truth value confidence by dividing the weight by the sum of the weight and 1. If the weight is not greater than 0, the function returns 0.

The TruthValue function calls both the Truth_w2f and Truth_w2c functions as part of its return statement. It passes the positive and negative weights (w_plus and w_minus) to the Truth_w2f function and the sum of the weights to the Truth_w2c function. The return values of both functions are combined into a tuple and returned as the result of the TruthValue function.

This function is used in several other functions within the project. It is called by the following objects:

1. Truth_Abduction: The Truth_Abduction function calls the TruthValue function as part of its return statement. It passes the product of three values (f1, c1, and c2) as the input to the TruthValue function. The return value of the TruthValue function is used to calculate the second element of the return value of the Truth_Abduction function.

2. Truth_Comparison: The Truth_Comparison function calls the TruthValue function as part of its return statement. It passes the product of three values (f0, c1, and c2) as the input to the TruthValue function. The return value of the TruthValue function is used to calculate the second element of the return value of the Truth_Comparison function.

3. Truth_Revision: The Truth_Revision function calls the TruthValue function as part of its return statement. It passes the product of three values (f0, c1, and c2) as the input to the TruthValue function. The return value of the TruthValue function is used to calculate the second element of the return value of the Truth_Revision function.

**Note**: 
- The TruthValue function expects two numeric values as input for the positive and negative weights.
- The function returns a tuple of two numeric values representing the truth value and truth value confidence.
- The Truth_w2f function assumes that the positive and negative weights provided are numeric values.
- The Truth_w2c function expects a numeric value as input for the weight parameter.
- The Truth_w2c function returns a numeric value representing the truth value confidence.
- The Truth_w2c function uses a conditional statement to handle the case when the weight is not greater than 0.

**Output Example**:
If w_plus is 3 and w_minus is 1, the function will return (0.75, 0.75).
## _function Truth_Abduction(v1, v2)
**Truth_Abduction**: The function of Truth_Abduction is to perform truth abduction based on two input values.

**parameters**:
- v1: The first input value, represented as a tuple (f1, c1).
- v2: The second input value, represented as a tuple (f2, c2).

**Code Description**:
The Truth_Abduction function takes two input values, v1 and v2, and performs truth abduction based on these values. It first unpacks the tuples to extract the factors and confidences, assigning them to variables f1, c1, f2, and c2. It then calls the Truth_w2c function with the product of f1, c1, and c2 as the input. The return value of the Truth_w2c function is combined with f2 to form a new tuple, which is returned as the result of the Truth_Abduction function.

**Note**:
- The Truth_w2c function is called within the Truth_Abduction function to calculate the truth value confidence.
- The input values v1 and v2 are expected to be tuples containing factors and confidences.
- The function assumes that the Truth_w2c function is defined and accessible.

**Output Example**:
If v1 is (0.8, 0.6) and v2 is (0.5, 0.7), the function will return (0.5, 0.4666666666666667).
## _function Truth_Induction(v1, v2)
**Truth_Induction**: The function of Truth_Induction is to perform truth induction based on two input values.

**parameters**:
- v1: The first input value, represented as a tuple (f1, c1).
- v2: The second input value, represented as a tuple (f2, c2).

**Code Description**:
The Truth_Induction function takes two input values, v1 and v2, and performs truth induction based on these values. It calls the Truth_Abduction function with v2 as the first argument and v1 as the second argument. The return value of the Truth_Abduction function is then returned as the result of the Truth_Induction function.

**Note**:
- The Truth_Abduction function is called within the Truth_Induction function to perform truth abduction.
- The input values v1 and v2 are expected to be tuples containing factors and confidences.
- The function assumes that the Truth_Abduction function is defined and accessible.

**Output Example**:
If v1 is (0.8, 0.6) and v2 is (0.5, 0.7), the function will return (0.5, 0.4666666666666667).
## _function Truth_Comparison(v1, v2)
**Truth_Comparison**: The function of Truth_Comparison is to compare the truth values of two given inputs and calculate a new truth value based on the comparison.

**parameters**:
- v1: The first input value, which is a tuple containing two elements: (f1, c1). f1 represents the belief in the truth value, and c1 represents the confidence in the truth value.
- v2: The second input value, which is also a tuple containing two elements: (f2, c2). f2 represents the belief in the truth value, and c2 represents the confidence in the truth value.

**Code Description**:
The Truth_Comparison function takes two input values, v1 and v2, and extracts the belief and confidence values from each input. It then calculates a new belief value, f0, using the formula: f0 = 1.0 - (1.0 - f1) * (1.0 - f2). This formula combines the belief values of the two inputs to calculate a new belief value.

Next, the function checks if the calculated belief value, f0, is equal to 0.0. If it is, the function returns 0.0. Otherwise, it calculates a new confidence value using the Truth_w2c function, passing the product of f0, c1, and c2 as the weight parameter. The Truth_w2c function calculates the truth value confidence based on the given weight.

Finally, the function returns a tuple containing two elements: the calculated belief value (0.0 if f0 is 0.0) and the calculated confidence value using the Truth_w2c function.

**Note**:
- The Truth_Comparison function expects two input values, v1 and v2, in the form of tuples.
- The function uses the Truth_w2c function to calculate the truth value confidence.
- The function handles the case when the calculated belief value, f0, is equal to 0.0 by returning 0.0.
- The function returns a tuple containing the calculated belief value and confidence value.

**Output Example**:
If v1 = (0.8, 0.9) and v2 = (0.6, 0.7), the function will return (0.6666666666666666, 0.8571428571428571).
## _function Truth_FrequencyComparison(v1, v2)
**Truth_FrequencyComparison**: The function of Truth_FrequencyComparison is to compare the truth values of two input values and calculate a new truth value based on their frequency difference.

**parameters**:
- v1: The first input value, which is a tuple containing a frequency value (f1) and a confidence value (c1).
- v2: The second input value, which is also a tuple containing a frequency value (f2) and a confidence value (c2).

**Code Description**:
The Truth_FrequencyComparison function takes two input values, v1 and v2, and extracts the frequency values (f1 and f2) and confidence values (c1 and c2) from them using tuple unpacking. It then calculates the absolute difference between the frequency values (abs(f1 - f2)) and subtracts it from 1.0 to obtain a new frequency value. The confidence values (c1 and c2) are multiplied together to obtain the new confidence value. Finally, the function returns a tuple containing the new frequency value and the new confidence value.

This function is called by two objects in the project: "differenceEvaluate" and "inheritances". In the "differenceEvaluate" function, the Truth_FrequencyComparison function is used to calculate the truth difference between two input values (T1 and T2). The result is then used to update the biggest difference property, truth, relation, and arguments based on certain conditions. In the "inheritances" function, the Truth_FrequencyComparison function is used to compare the truth values of two input values (T1 and T2) for different properties. The result is used to calculate the truth values for inheritance relationships and update the biggest difference property, truth, relation, and arguments.

**Note**:
- The input values (v1 and v2) should be tuples containing frequency and confidence values.
- The function assumes that the input values have the correct format and structure.
- The function does not handle any exceptions or errors that may occur during the calculation.

**Output Example**:
If v1 = (0.8, 0.9) and v2 = (0.6, 0.7), the function will return (0.4, 0.63).
## _function Truth_Negation(v1)
**Truth_Negation**: The function of Truth_Negation is to negate the truth value of a given proposition.

**parameters**:
- v1: A tuple representing a proposition, where the first element is the truth value (f) and the second element is the confidence value (c).

**Code Description**:
The `Truth_Negation` function takes a proposition as input and returns a new proposition with the negated truth value. The input proposition is expected to be in the form of a tuple, where the first element represents the truth value and the second element represents the confidence value.

The function first unpacks the input tuple into two variables, `f` and `c`. It then calculates the negated truth value by subtracting the original truth value from 1.0. The confidence value remains unchanged.

Finally, the function returns a new tuple with the negated truth value and the same confidence value.

This function is used in the `differenceEvaluate` method of the `Nalifier` class in the `Nalifier.py` file. In the `differenceEvaluate` method, the `Truth_Negation` function is called to negate the truth value of a comparison between two truth values. The result of this negation is used in further calculations to determine the biggest difference between two terms.

**Note**:
- The input proposition is expected to be a tuple with two elements.
- The truth value of the input proposition should be a floating-point number between 0.0 and 1.0.
- The confidence value of the input proposition can be any floating-point number.

**Output Example**:
If the input proposition is `(0.8, 0.9)`, the function will return `(0.2, 0.9)`.
## _function Truth_Revision(v1, v2)
**Truth_Revision**: The function of Truth_Revision is to perform truth revision based on the given input values.

**parameters**:
- v1: A tuple representing the first input value, consisting of a float value (f1) and a confidence value (c1).
- v2: A tuple representing the second input value, consisting of a float value (f2) and a confidence value (c2).

**Code Description**:
The Truth_Revision function takes two input values and performs truth revision based on these values. It first extracts the float values (f1 and f2) and confidence values (c1 and c2) from the input tuples (v1 and v2). Then, it calculates the weight values (w1 and w2) by calling the Truth_c2w function for each confidence value. The weight values are obtained by calculating the complementary values of the confidence values using the formula c / (1 - c).

Next, the function calculates the total weight (w) by summing up the individual weight values (w1 and w2). If the total weight is equal to 0.0, indicating that both input values have a confidence value of 0, the function returns a tuple (0.5, 0.0) representing a neutral truth value.

If the total weight is not 0.0, the function proceeds to calculate the revised truth value. It uses the formula (w1 * f1 + w2 * f2) / w to calculate the revised float value. This formula calculates the weighted average of the input float values based on their respective weights. The result is then divided by the total weight to ensure that the revised float value is within the range of 0 to 1.

The function also calculates the revised confidence value using the Truth_w2c function. It passes the total weight (w) as the input to the Truth_w2c function. The Truth_w2c function calculates the truth value confidence based on the weight. If the weight is greater than 0, the function divides the weight by the sum of the weight and 1. If the weight is not greater than 0, the function returns 0.

Finally, the function returns a tuple representing the revised truth value. The first element of the tuple is the revised float value, which is the result of the weighted average calculation. The second element of the tuple is the revised confidence value, which is the result of the Truth_w2c calculation. The function ensures that the revised confidence value is not greater than a maximum confidence value (MAX_CONFIDENCE), which is set to 0.99.

**Note**:
- The input values should be provided as tuples in the format ((float_value, confidence_value), (float_value, confidence_value)).
- The confidence values should be floats between 0 and 1, inclusive.
- The function uses the Truth_c2w and Truth_w2c functions to calculate the weight and confidence values, respectively.
- The function handles the case when both input values have a confidence value of 0, returning a neutral truth value.
- The function ensures that the revised confidence value is not greater than the maximum confidence value (MAX_CONFIDENCE).

**Output Example**:
- Example 1:
  - Input: v1 = ((0.6, 0.8), (0.7, 0.9))
  - Output: (0.65, 0.8888888888888888)
- Example 2:
  - Input: v1 = ((0.2, 0.5), (0.3, 0.6))
  - Output: (0.25, 0.6666666666666666)
## _function Truth_Difference(v1, v2)
**Truth_Difference**: The function of Truth_Difference is to calculate the difference between two truth values.

**parameters**:
- v1: The first truth value, represented as a tuple (f1, c1), where f1 is the frequency and c1 is the confidence.
- v2: The second truth value, represented as a tuple (f2, c2), where f2 is the frequency and c2 is the confidence.

**Code Description**:
The Truth_Difference function takes two truth values as input and calculates the difference between them. The truth values are represented as tuples, where the first element represents the frequency and the second element represents the confidence.

The function first unpacks the input tuples into separate variables, f1, c1, f2, and c2. It then calculates the difference between the frequencies and the product of the confidences. The difference between the frequencies is calculated by subtracting the second frequency (f2) from the first frequency (f1) and multiplying it by the first frequency (f1 * (1.0 - f2)). The product of the confidences is calculated by multiplying the first confidence (c1) with the second confidence (c2) (c1 * c2).

The function returns the calculated difference as a tuple (f1 * (1.0 - f2), c1 * c2).

This function is used in the Nalifier.py module in the differenceEvaluate method of the Nalifier class. The differenceEvaluate method calculates the difference between two truth values and updates the biggestDifferenceProp, biggestDifferenceTruth, relation, biggestDifferenceArg1, and biggestDifferenceArg2 variables based on the calculated difference and other conditions. The Truth_Difference function is called within the differenceEvaluate method to calculate the truth difference.

**Note**:
- The input truth values should be represented as tuples with two elements: the frequency and the confidence.
- The calculated difference is returned as a tuple with two elements: the difference between the frequencies and the product of the confidences.

**Output Example**:
If the input truth values are v1 = (0.8, 0.9) and v2 = (0.6, 0.7), the function will return the difference as (0.16, 0.63).
## _function Truth_Expectation(T)
**Truth_Expectation**: The function of Truth_Expectation is to calculate the expectation value of a given truth value.

**parameters**:
- T: A tuple representing a truth value, where the first element is the frequency and the second element is the confidence.

**Code Description**:
The `Truth_Expectation` function takes a truth value `T` as input and calculates the expectation value using the formula `(c * (f - 0.5) + 0.5)`, where `f` is the frequency and `c` is the confidence of the truth value. The function first unpacks the frequency and confidence from the input tuple `T`. It then applies the formula to calculate the expectation value. The calculated expectation value is returned as the output of the function.

This function is called by the `differenceEvaluate` and `inheritances` methods in the `Nalifier` class of the `Nalifier.py` file. In the `differenceEvaluate` method, the `Truth_Expectation` function is used to calculate the expectation value of the truth difference between two truth values. The calculated expectation value is compared with the current biggest difference truth value, and if it is greater, the biggest difference truth value is updated. In the `inheritances` method, the `Truth_Expectation` function is used to calculate the expectation value of the truth intermediate between two truth values. The calculated expectation value is used to determine the common properties between the two terms.

**Note**: 
- The input truth value `T` should be a tuple with two elements representing the frequency and confidence.
- The calculated expectation value is a float value between 0 and 1.
- The `Truth_Expectation` function assumes that the input truth value is valid and follows the expected format.

**Output Example**: 
If the input truth value `T` is `(0.7, 0.9)`, the `Truth_Expectation` function will return `0.725`.
## _class Nalifier
**Nalifier**: The Nalifier class is responsible for creating and managing instances and concepts in the NARS (Non-Axiomatic Reasoning System) framework. It implements the NAL (Non-Axiomatic Logic) inference rules for matching and inheritance between instances and concepts.

**Attributes**:
- SUFFICIENT_MATCH_EXP: A threshold value that determines when an instance is considered a match to an existing instance. Default value is 0.8.
- SUFFICIENT_DIFFERENCE_EXP: A threshold value that determines how much difference is required to consider an instance as different from the best matched one. Default value is 0.0.
- COMMON_PROPERTY_EXP: A threshold value that determines how similar properties need to be in order to be used for building new concepts. Default value is 0.5.
- InstanceCreation: A boolean flag that indicates whether new instances should be created. Default value is True.
- ConceptCreation: A boolean flag that indicates whether new concepts should be created. Default value is False.
- RelativeComparison: A boolean flag that indicates whether relative comparison should be used for property values. Default value is False.
- ClosedWorldAssumption: A boolean flag that indicates whether the closed world assumption should be used. Default value is False.
- UseIntensionalDifference: A boolean flag that indicates whether intensional difference should be used for non-continuous properties. Default value is True.
- usecounts: A dictionary that keeps track of the usage count of each prototype.
- prototypes: A dictionary that stores the prototypes (concepts) and their associated properties.
- position0: A dictionary that stores the position0 property values for instances.
- position1: A dictionary that stores the position1 property values for instances.
- conceptnames: A set that stores the names of concepts.
- current_prototypes: A dictionary that stores the current prototypes (instances) and their associated properties.
- last_instance: A variable that stores the last instance processed.
- last_winner: A dictionary that stores the best matching prototype and its associated properties.
- last_winner_truth_exp: A variable that stores the truth expectation of the best matching prototype.
- last_winner_reldata: A tuple that stores the information about the biggest difference between the last instance and the best matching prototype.
- last_winner_common_properties: A set that stores the common properties between the last instance and the best matching prototype.
- last_label: A variable that stores the last label property encountered.
- last_label_frequency: A variable that stores the frequency of the last label property.
- winner_match_asymmetric: A boolean flag that indicates whether the best match was based on asymmetric comparison.
- binary_extreme_comparison_properties: A set that stores the binary extreme comparison properties.
- continuous_comparison_properties: A set that stores the continuous comparison properties.
- label_properties: A set that stores the label properties.
- Events: A list that stores the generated events.
- concept_id: A variable that stores the concept ID.
- sensorValueReporters: A dictionary that stores the value reporters for sensor properties.
- conceptValueReporters: A dictionary that stores the value reporters for concept properties.
- BestMatch: A variable that stores the best match relationship.
- BiggestDifference: A variable that stores the biggest difference relationship.
- propertyOfInterest: A variable that stores the property of interest.

**Code Description**: The Nalifier class is initialized with an AIKR_Limit parameter, which sets the limit for the number of prototypes (concepts) that can be stored. The class provides methods for adding input, removing instance properties, evaluating differences, handling inheritances, and processing shell input.

The `removeInstanceProperties` method removes the properties associated with the worst prototype from the conceptValueReporters dictionary.

The `differenceEvaluate` method evaluates the difference between two truth values and updates the biggest difference if necessary.

The `inheritances` method calculates the inheritances between two instances and returns the inheritances, biggest difference, and common properties.

The `AddInput` method processes the input string and performs matching and inheritance operations. It updates the prototypes, usecounts, and other variables accordingly. It also generates events based on the input.

The `AddInputVector` method processes input vectors and adds them to the prototypes.

The `ShellInput` method processes shell input commands and updates the class attributes accordingly.

The `process` function is not a part of the Nalifier class, but it uses the Nalifier class to process input and perform actions based on the input.

**Note**: The Nalifier class is a key component in the NARS framework for managing instances and concepts. It provides functionality for matching, inheritance, and concept creation. The class attributes and methods should be used carefully and in accordance with the requirements of the application.

**Output Example**: None
### _class_function __init__(self, AIKR_Limit)
**__init__**: The function of __init__ is to initialize the object of the Nalifier class.

**parameters**:
- AIKR_Limit: An optional parameter that specifies the limit for the AIKR (Artificial Intelligence Knowledge Representation) system. The default value is 10.

**Code Description**:
The __init__ function is a special method in Python classes that is automatically called when a new object of the class is created. It is used to initialize the attributes of the object.

In this specific code, the __init__ function takes one parameter, AIKR_Limit, which represents the limit for the AIKR system. The AIKR system is responsible for representing and processing knowledge in the artificial intelligence system.

Inside the __init__ function, the AIKR_Limit parameter is assigned to the self.AIKR_Limit attribute of the object. The self keyword refers to the current instance of the class, and by assigning the AIKR_Limit parameter to self.AIKR_Limit, we are initializing the attribute with the provided value.

**Note**:
- The __init__ function is called automatically when creating a new object of the Nalifier class.
- The AIKR_Limit parameter is optional and has a default value of 10. If no value is provided, the AIKR_Limit attribute will be initialized with the default value.
### _class_function removeInstanceProperties(self, worstproto)
**removeInstanceProperties**: The function of removeInstanceProperties is to remove instance properties from the conceptValueReporters dictionary.

**parameters**:
- self: The current object.
- worstproto: The worst prototype to remove instance properties for.

**Code Description**:
The removeInstanceProperties function takes in the worstproto parameter and removes all instance properties that start with the worstproto value followed by an underscore from the conceptValueReporters dictionary. It does this by iterating over the keys of the conceptValueReporters dictionary and checking if each key starts with the worstproto value followed by an underscore. If a key matches this condition, it is added to the removals list. Finally, the function iterates over the removals list and deletes each key from the conceptValueReporters dictionary.

This function is called within the AddInput function of the Nalifier class in the Nalifier.py file. In the AddInput function, if the inp parameter is equal to "1", the removeInstanceProperties function is called with the last_instance as the worstproto value. This ensures that instance properties are removed for the last_instance when a new input is received.

**Note**:
- It is important to note that this function only removes instance properties from the conceptValueReporters dictionary and does not remove the entire concept node or prototype associated with the instance.
### _class_function differenceEvaluate(self, T1, T2, property, biggestDifferenceProp, biggestDifferenceTruth, term1, term2, relation, biggestDifferenceArg1, biggestDifferenceArg2, relativeDifference)
**differenceEvaluate**: The function of differenceEvaluate is to calculate the difference between two truth values and update the biggest difference property, truth, relation, and arguments based on certain conditions.

**parameters**:
- T1: The first truth value, represented as a tuple (f1, c1), where f1 is the frequency and c1 is the confidence.
- T2: The second truth value, represented as a tuple (f2, c2), where f2 is the frequency and c2 is the confidence.
- property: The property associated with the truth values.
- biggestDifferenceProp: The current biggest difference property.
- biggestDifferenceTruth: The current biggest difference truth value.
- term1: The first term associated with the truth values.
- term2: The second term associated with the truth values.
- relation: The relation between the terms.
- biggestDifferenceArg1: The current biggest difference argument 1.
- biggestDifferenceArg2: The current biggest difference argument 2.
- relativeDifference (optional): The relative difference between the truth values.

**Code Description**:
The differenceEvaluate function takes two truth values, T1 and T2, along with other parameters, and calculates the difference between them. It first checks if the property is in the list of continuous comparison properties. If it is, the function uses the Truth_FrequencyComparison function from the Truth_FrequencyComparison object to calculate the truth difference. Otherwise, it uses the Truth_Difference function from the Truth_Difference object.

If the relativeDifference parameter is provided, the function updates the truth difference to the relative difference. Then, it checks if the property of interest is None or if the current property is equal to the property of interest. If either condition is true and the expectation value of the truth difference is greater than the expectation value of the current biggest difference truth value, the function updates the biggest difference property, truth value, relation, and arguments.

Finally, the function returns the updated biggest difference property, truth value, relation, and arguments.

**Note**:
- The function assumes that the input truth values have the correct format and structure.
- The function relies on the Truth_FrequencyComparison and Truth_Difference functions to calculate the truth difference.
- The function updates the biggest difference property, truth value, relation, and arguments based on certain conditions.
- The relativeDifference parameter is optional and can be used to override the calculated truth difference.

**Output Example**:
If T1 = (0.8, 0.9), T2 = (0.6, 0.7), property = "example", biggestDifferenceProp = None, biggestDifferenceTruth = (0.0, 1.0), term1 = "term1", term2 = "term2", relation = "+", biggestDifferenceArg1 = None, biggestDifferenceArg2 = None, and relativeDifference = None, the function will return ("example", (0.16, 0.63), "-", "term1", "term2").
### _class_function inheritances(self, term1, terms_term1, term2, terms_term2, requireSameProperties, asymmetricComparison)
**inheritances**: The function of inheritances is to calculate the inheritance relationships between two terms based on their associated truth values and properties. It determines the common properties between the terms, calculates the truth values for inheritance relationships, and updates the biggest difference property, truth value, relation, and arguments based on certain conditions.

**parameters**:
- term1: The first term for which the inheritance relationships are calculated.
- terms_term1: The associated truth values and properties of term1, represented as a tuple of two sets: (extension1, intension1). extension1 contains the extensional properties of term1, while intension1 contains the intensional properties of term1.
- term2: The second term for which the inheritance relationships are calculated.
- terms_term2: The associated truth values and properties of term2, represented as a tuple of two sets: (extension2, intension2). extension2 contains the extensional properties of term2, while intension2 contains the intensional properties of term2.
- requireSameProperties (optional): A boolean value indicating whether the terms must have the same properties for inheritance. Default is False.
- asymmetricComparison (optional): A boolean value indicating whether the comparison between terms is asymmetric. Default is True.

**Code Description**:
The inheritances function takes two terms, term1 and term2, along with their associated truth values and properties, and calculates the inheritance relationships between them. It first initializes variables to store the biggest difference property, truth value, relation, and arguments. It also initializes other variables for further calculations.

The function then proceeds to iterate over the intensional properties of term1 and term2. For each matching property, it updates the truth values based on the type of comparison (induction or frequency comparison) and checks if the property meets the common property expectation. If it does, the property is added to the set of common properties.

Next, the function iterates over the extensional properties of term1 and term2. For each matching property, it updates the truth values based on the type of comparison (abduction or frequency comparison).

After that, the function checks for missing properties in term2 when requireSameProperties is True. If a missing property is found, the hadMissingProp variable is set to True.

The function then iterates over the intensional properties of term2. For each property, it checks if term1 has the same property. If not, it sets AHasProperty to False. If requireSameProperties is True and AHasProperty is False, hadMissingProp is set to True.

Next, the function iterates over the extensional properties of term1. For each property, it checks if term2 has the same instance. If not, it sets BHasInstance to False. If BHasInstance is False and applyCWA is True, hadMissingProp is set to True.

If hadMissingProp is False or requireSameProperties is False, the function adds the inheritance relationships to the Inheritances dictionary.

Finally, the function removes any incomparable terms from the Inheritances dictionary and returns the Inheritances dictionary, the biggest difference property, truth value, relation, and arguments, and the set of common properties.

**Note**:
- The function assumes that the input terms and their associated truth values and properties are in the correct format.
- The function uses other helper functions, such as differenceEvaluate and Truth_Expectation, to calculate the truth differences and expectations.
- The function handles different types of comparisons based on the properties and settings.
- The function updates the biggest difference property, truth value, relation, and arguments based on certain conditions.
- The relativeDifference parameter is used to override the calculated truth difference, if provided.
- The function returns the Inheritances dictionary, the biggest difference property, truth value, relation, and arguments, and the set of common properties.

**Output Example**:
If term1 is "term1", terms_term1 is (({("prop1", (0.8, 0.9))}, {("prop2", (0.6, 0.7))}), ({}, {})), term2 is "term2", terms_term2 is (({("prop1", (0.7, 0.9))}, {("prop2", (0.5, 0.7))}), ({}, {})), requireSameProperties is False, and asymmetricComparison is True, the function will return ({'term2': (0.4, 0.63)}, ('prop1', (0.16, 0.63), '-', 'term1', 'term2'), {('prop2', (0.5, 0.7))}).
### _class_function AddInput(self, inp, inverted, Print, Sensation_Reliance)
**AddInput**: The AddInput function is responsible for processing input and performing various operations based on the input received.

**parameters**:
- `self`: The current object.
- `inp`: The input string to be processed.
- `inverted` (optional): A boolean value indicating whether the input should be inverted. Default is False.
- `Print` (optional): A boolean value indicating whether the processed input should be printed. Default is False.
- `Sensation_Reliance` (optional): A float value indicating the reliance on sensation. Default is 0.9.

**Code Description**:
The AddInput function takes an input string `inp` and performs operations based on the input. It first checks if the input starts with "//". If it does, the input is printed and the function returns.

Next, the function checks if the input is equal to "1". If it is, the function performs several operations. It determines the best match in the current prototypes based on the last winner and its truth expectation. If a best match is found and its truth expectation is greater than the sufficient match expectation, the function updates the use count for the best match and determines the biggest difference property, truth, relation, and arguments based on the last winner's relation data. It also updates the last label and last label frequency if the property starts with "label_". If the input is not inverted and the property is in the binary extreme comparison properties, the function adds a new input with an anti-property to the NAL_AddInput function.

If the input is equal to "1" or the instance is different from the last instance and the last instance is not None, the function performs additional operations. It checks if the last winner is not None and its truth expectation is greater than the sufficient match expectation. If it is, the function updates the use count for the last winner and determines the biggest difference property, truth, relation, and arguments based on the last winner's relation data. It also updates the best match and biggest difference based on the relation and arguments. If the relative comparison is enabled, the function updates the concept value reporters with the frequency and sensation reliance of the instance property. It then creates an evidence statement based on the last label and last label frequency. If the position properties are present, the function creates additional evidence statements based on the position values. The evidence statements are added to the events list.

If the input is equal to "1", the function updates the property of interest and removes instance properties for the last instance if it is not present in the prototypes.

The function then updates the last instance with the current instance and prints the input if the Print parameter is True.

Finally, the function performs additional operations based on the instance and property values. It checks if the instance is not in the current prototypes and adds the instance properties to the current prototypes. It also updates the concept value reporters with the frequency and sensation reliance of the instance property. The function then calculates the truth expectation for the last winner and performs inheritance calculations between the current instance and the prototypes. The function updates the biggest difference property, truth, relation, and arguments based on the inheritance calculations. It also updates the last winner and last winner truth expectation. If the capacity limit is exceeded, the function removes the prototype with the lowest use count.

**Note**:
- The AddInput function is a key function in the Nalifier class that processes input and performs various operations based on the input received.
- The function handles different types of input, including "//" comments, "1" input, and other input strings.
- The function updates the prototypes, current prototypes, concept value reporters, position properties, and other attributes based on the input and current state.
- The function calculates truth expectations, performs inheritance calculations, and updates the biggest difference property, truth, relation, and arguments based on certain conditions.
- The function handles capacity limits and removes prototypes with the lowest use count when necessary.
- The function uses other helper functions, such as NAL_AddInput, Truth_Revision, Truth_Expectation, and removeInstanceProperties, to perform specific operations.
- The function updates the last instance, last label, last label frequency, last winner, and other attributes based on the input and current state.

**Output Example**:
If the input is "1" and the best match is found, the function may add evidence statements to the events list and print the evidence statements to the console:
```
(<{inst1} * {inst2}> --> (+ {property})). :|: %{frequency};{0.9}%
```
The evidence statements represent the best match between two instances and the associated property with the given frequency and confidence values.
### _class_function AddInputVector(self, name, values, dimname, Print, UseHistogram, Sensation_Reliance)
**AddInputVector**: The AddInputVector function is responsible for adding an input vector to the current object. It takes several parameters, including the name of the vector, the values of the vector, the dimension name (optional), a Print flag (optional), and a Sensation_Reliance value (optional).

**parameters**:
- `self`: The current object.
- `name`: The name of the input vector.
- `values`: The values of the input vector.
- `dimname` (optional): The dimension name of the input vector. If not provided, it defaults to the name of the vector.
- `Print` (optional): A boolean value indicating whether the input should be printed. Default is False.
- `UseHistogram` (optional): A boolean value indicating whether to use a histogram for comparison. Default is True.
- `Sensation_Reliance` (optional): A float value indicating the reliance on sensation. Default is 0.9.

**Code Description**:
The AddInputVector function first checks if the dimension name is None. If it is, the dimension name is set to the name of the vector.

Next, the function iterates over the values in the input vector. For each value, it creates a property name based on the dimension name and the index of the value. If UseHistogram is True and the property name is not in the sensorValueReporters dictionary, a new ValueReporter object is created and added to the dictionary. The continuous_comparison_properties set is also updated with the property name.

The function then calls the reportValue method of the ValueReporter object to calculate the frequency and confidence of the sensed value. The method returns a tuple (f, c) representing the frequency and confidence.

If UseHistogram is False, the frequency and confidence are set to the value and Sensation_Reliance, respectively.

Finally, the function calls the AddInput method of the current object to add the input with the appropriate format, including the name, property name, frequency, and Sensation_Reliance.

**Note**:
- The AddInputVector function is used to add an input vector to the current object.
- The function calculates the frequency and confidence of the sensed value based on the values in the input vector.
- The UseHistogram parameter determines whether to use a histogram for comparison.
- The Sensation_Reliance parameter determines the reliance on sensation.
- The function uses the ValueReporter class to track and analyze the frequency and confidence of sensed values.
- The AddInput method is called to add the input with the appropriate format.
- The Print parameter determines whether the input should be printed.
- The continuous_comparison_properties set is updated with the property names.
- The AddInputVector function is called within the Nalifier.py/Nalifier/AddInput method.

**Output Example**:
If the Print parameter is set to True, the following output may be printed to the console:
```
<{name} |-> [propertyName]>. :|: %{frequency}%
```
The sensed value truth is returned as a tuple `(frequency, confidence * Sensation_Reliance)`.
### _class_function ShellInput(self, inp)
**ShellInput**: The ShellInput function is responsible for processing input and performing various operations based on the input received.

**Parameters**:
- `self`: The current object.
- `inp`: The input string to be processed.

**Code Description**:
The ShellInput function takes an input string `inp` and performs operations based on the input. It first checks if the input starts with "*SET_CONTINUOUS=". If it does, the function extracts the property name from the input and adds it to the `sensorValueReporters` dictionary if it is not already present. It also adds the property name to the `continuous_comparison_properties` set. The function returns None.

If the input starts with "*PROTOTYPES", the function prints the current prototypes to the console and returns None.

If the input starts with "*PROPERTY_OF_INTEREST=", the function extracts the property name from the input and assigns it to the `propertyOfInterest` attribute. If the property name is an empty string, the `propertyOfInterest` attribute is set to None. The function returns None.

If the input starts with "*RESET_PROTOTYPES=", the function creates a new instance of the Nalifier class with the specified capacity limit and assigns it to the `self` object. The function returns None.

If the input starts with "*SUFFICIENT_MATCH_EXP=", the function extracts the float value for the sufficient match expectation from the input and assigns it to the `SUFFICIENT_MATCH_EXP` attribute. The function returns None.

If the input starts with "*SUFFICIENT_DIFFERENCE_EXP=", the function extracts the float value for the sufficient difference expectation from the input and assigns it to the `SUFFICIENT_DIFFERENCE_EXP` attribute. The function returns None.

If the input starts with "*COMMON_PROPERTY_EXP=", the function extracts the float value for the common property expectation from the input and assigns it to the `COMMON_PROPERTY_EXP` attribute. The function returns None.

If the input starts with "*CONCEPT_CREATION=", the function extracts the boolean value for the concept creation from the input and assigns it to the `ConceptCreation` attribute. The function returns None.

If the input starts with "*INSTANCE_CREATION=", the function extracts the boolean value for the instance creation from the input and assigns it to the `InstanceCreation` attribute. The function returns None.

If the input starts with "*RELATIVE_COMPARISON=", the function extracts the boolean value for the relative comparison from the input and assigns it to the `RelativeComparison` attribute. The function returns None.

If the input starts with "*CLOSED_WORLD_ASSUMPTION=", the function extracts the boolean value for the closed world assumption from the input and assigns it to the `ClosedWorldAssumption` attribute. The function returns None.

If the input starts with "*USE_INTENSIONAL_DIFFERENCE=", the function extracts the boolean value for the use intensional difference from the input and assigns it to the `UseIntensionalDifference` attribute. The function returns None.

If none of the above conditions are met, the function performs additional operations based on the input. It splits the input string into two parts: `lhs` and `rhs` using the ". :|:" separator. If the input is equal to "1", the function calls the AddInput function with the input and the Print parameter set to True. If the input contains "{" and "}" and "[" and "]" and does not contain " * ", the function calls the AddInput function with the input and the Print parameter set to True. Otherwise, the function returns the input string.

**Note**:
- The ShellInput function is a key function in the Nalifier class that processes input and performs various operations based on the input received.
- The function handles different types of input, including setting continuous properties, printing prototypes, setting the property of interest, resetting prototypes, and setting various attributes.
- The function calls the AddInput function to process input strings that meet certain conditions.
- The function updates various attributes of the Nalifier object based on the input and current state.
- The function returns None for most input strings, except for specific conditions where the AddInput function is called or the input string is returned.

**Output Example**:
If the input is "*SET_CONTINUOUS=temperature", the function returns None.
If the input is "*PROTOTYPES", the function prints the current prototypes to the console and returns None.
If the input is "*PROPERTY_OF_INTEREST=humidity", the function returns None.
If the input is "*RESET_PROTOTYPES=1000", the function creates a new instance of the Nalifier class with a capacity limit of 1000 and returns None.
If the input is "*SUFFICIENT_MATCH_EXP=0.8", the function returns None.
If the input is "*SUFFICIENT_DIFFERENCE_EXP=0.5", the function returns None.
If the input is "*COMMON_PROPERTY_EXP=0.7", the function returns None.
If the input is "*CONCEPT_CREATION=true", the function returns None.
If
