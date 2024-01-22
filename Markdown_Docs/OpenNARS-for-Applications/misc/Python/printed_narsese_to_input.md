## _function floatPart(s)
**floatPart**: The function of floatPart is to extract the floating-point number from a given string.

**parameters**:
- s: A string from which the floating-point number needs to be extracted.

**Code Description**:
The floatPart function takes a string as input and iterates through each character in the string. It checks if the character is a digit (0-9) or a period (.) using a conditional statement. If the character is a digit or a period, it is appended to the "number" string. If the character is neither a digit nor a period, the loop is terminated using the "break" statement. Finally, the "number" string, which contains the extracted floating-point number, is returned.

**Note**:
- The function assumes that the floating-point number in the string is a valid representation and does not perform any additional validation.
- The function only extracts the floating-point number from the beginning of the string. Any characters after the first non-digit/non-period character are ignored.

**Output Example**:
- Input: "3.14 is pi"
- Output: "3.14"
