## _function Allow_requery_if_not_in_ONA(term)
**Allow_requery_if_not_in_ONA**: The function of Allow_requery_if_not_in_ONA is to check if a previously queried item is still present in the ONA (OpenNARS-for-Applications) memory. If the item is no longer in memory, it sets it up for re-query by removing it from the retrieved set.

**parameters**:
- term: A string representing the item to be checked for re-query.

**Code Description**:
The Allow_requery_if_not_in_ONA function first checks if the given term is present in the retrieved set. If it is, it calls the AddInput function from the NAR (Non-Axiomatic Reasoning) system to send a Narsese input for processing. The Narsese input is constructed by appending a question mark to the term. The Print parameter is set to False to prevent printing the raw output.

The function then checks if the returned output contains answers and if the first answer has a "truth" key and a value of "None". If both conditions are met, it means that the item is no longer in the ONA memory. In this case, the function removes the term from the retrieved set.

**Note**:
- The AddInput function is called from the NAR system to send a Narsese input for processing.
- The retrieved set is used to keep track of previously queried items.
- The function assumes that the retrieved set, NAR system, and the AddInput function are defined and accessible within the same module.

The Allow_requery_if_not_in_ONA function is called by the query function in the persistentNAR.py file. The query function first calls the Allow_requery_if_not_in_ONA function to check if the given term is still in the ONA memory. If the term is not in the retrieved set but is present in the memory, it adds the term to the retrieved set and performs additional processing.

If the term contains "?1", the query function performs a simple query matching by splitting the term into two parts. It then iterates over the memory to find the best matching term based on a truth expectation function. If a matching term is found, the Allow_requery_if_not_in_ONA function is called to check if the term is still in the ONA memory. If the term is not in the retrieved set, it adds the term to the retrieved set and performs additional processing.

Finally, the query function adds the term to the retrieved set.

**Note**:
- The query function relies on the Allow_requery_if_not_in_ONA function to check if a term needs to be re-queried.
- The function performs additional processing for terms that are not in the retrieved set but are present in the memory.
- The function assumes that the retrieved set, memory, and the Allow_requery_if_not_in_ONA function are defined and accessible within the same module.
## _function query(term)
**query**: The function of query is to perform a query in the OpenNARS-for-Applications (ONA) system based on the given term.

**parameters**:
- term: A string representing the term to be queried.

**Code Description**:
The query function is responsible for executing a query in the ONA system. It first calls the Allow_requery_if_not_in_ONA function to check if the given term needs to be re-queried. If the term is not in the retrieved set but is present in the memory, it adds the term to the retrieved set and performs additional processing.

If the term contains "?1", the function performs a simple query matching by splitting the term into two parts. It then iterates over the memory to find the best matching term based on a truth expectation function. The truth expectation function calculates the truth value of a term based on its frequency and confidence values. If a matching term is found, the Allow_requery_if_not_in_ONA function is called to check if the term is still in the ONA memory. If the term is not in the retrieved set, it adds the term to the retrieved set and performs additional processing.

Finally, the function adds the term to the retrieved set.

**Note**:
- The Allow_requery_if_not_in_ONA function is called to check if a term needs to be re-queried.
- The function performs additional processing for terms that are not in the retrieved set but are present in the memory.
- The function assumes that the retrieved set, memory, and the Allow_requery_if_not_in_ONA function are defined and accessible within the same module.

The query function is called in the ProcessNAROutput function in the persistentNAR.py file. The ProcessNAROutput function processes the output received from the ONA system and performs further actions based on the derived terms. If a valid derivation is found, the query function is called to execute a query based on the derived term. The frequency and confidence values of the derived term are used to update the memory.

**Note**:
- The ProcessNAROutput function relies on the query function to execute queries based on derived terms.
- The function assumes that the memory and query function are defined and accessible within the same module.
## _function ProcessNAROutput(ret, backups)
**ProcessNAROutput**: The function of ProcessNAROutput is to process the output received from the OpenNARS-for-Applications (ONA) system and update the memory based on the derived terms.

**parameters**:
- ret: A dictionary representing the output received from the ONA system.
- backups (optional): A list of strings representing the backup types to be processed. The default value is ["input", "answers", "derivations"].

**Code Description**:
The ProcessNAROutput function iterates over the specified backup types in the ret dictionary. For each backup, it further iterates over the derivations in that backup. It checks if a derivation meets certain conditions, including having a punctuation value of ".", an occurrenceTime value of "eternal", and a non-empty term. If a valid derivation is found, the function performs the following steps:

1. Extracts the term from the derivation.
2. Removes the time delta prefix ("dt=") from the term if present.
3. Calls the query function with the extracted term.
4. Retrieves the frequency and confidence values from the derivation's truth dictionary.
5. Retrieves the stamp value from the derivation.
6. Determines the usefulness addition based on the presence of the "Priority" key in the derivation and its value.
7. Checks if the term is already present in the memory. If so, retrieves the existing frequency, confidence, usefulness, and stamp values.
8. Compares the confidence value of the current derivation with the existing confidence value in the memory. If the current derivation has a higher confidence value, updates the memory with the new frequency, confidence, usefulness, and stamp values.
9. If the term is not already present in the memory, adds it to the memory with the new frequency, confidence, usefulness, and stamp values.

**Note**:
- The query function is called to execute queries based on the derived terms.
- The memory is assumed to be defined and accessible within the same module.

The ProcessNAROutput function is called in the OpenNARS-for-Applications\misc\Python\persistentNAR.py file. It is used to process the output received from the ONA system and update the memory based on the derived terms. The function assumes that the query function and memory are defined and accessible within the same module.

**Note**:
- The ProcessNAROutput function relies on the query function to execute queries based on derived terms.
- The function assumes that the memory and query function are defined and accessible within the same module.
## _function SimplisticTermNormalizer(inp)
**SimplisticTermNormalizer**: The function of SimplisticTermNormalizer is to normalize the input string by handling space variations in involved parentheses.

**parameters**:
- inp: A string representing the input to be normalized.

**Code Description**:
The SimplisticTermNormalizer function takes an input string and performs a series of string replacements to normalize the input. It replaces occurrences of "-->", "<->", "==>", "<=>", and "=/>" with their corresponding variations followed by a space. It then replaces any consecutive spaces with a single space. Additionally, it removes any leading or trailing spaces. Finally, it replaces occurrences of "[ ", " ]", "{ ", " }", "< ", " >", " )", and "( " with their corresponding variations without the space. Again, it replaces any consecutive spaces with a single space and removes any leading or trailing spaces.

**Note**:
- The SimplisticTermNormalizer function only handles space variations in involved parentheses and does not perform any other form of normalization.
- The function assumes that the input string is well-formed and does not perform any validation or error handling.

**Output Example**:
If the input string is "A-->B<->C==>D<=>E=/>F", the SimplisticTermNormalizer function will return "A --> B <-> C ==> D <=> E =/> F".
