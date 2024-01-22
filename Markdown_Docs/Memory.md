## _function SetPrint(Flag)
**SetPrint**: The function of SetPrint is to set the value of the global variable "Print" based on the input flag.

**parameters**:
- Flag: A boolean value that determines the value of the global variable "Print". If Flag is True, the value of Print will be set to True. If Flag is False, the value of Print will be set to False.

**Code Description**:
The SetPrint function is a simple function that sets the value of the global variable "Print" based on the input flag. The global keyword is used to indicate that the variable "Print" is a global variable and can be accessed and modified from anywhere in the code.

The function takes one parameter, Flag, which is a boolean value. If Flag is True, the value of Print is set to True. If Flag is False, the value of Print is set to False.

By setting the value of Print, this function controls whether certain print statements in the code will be executed or not. If Print is True, the print statements will be executed. If Print is False, the print statements will be skipped.

This function is typically called before executing other parts of the code that contain print statements. By setting the value of Print to True or False, developers can control the verbosity of the code and choose whether to display certain output or not.

**Note**: 
- It is important to call this function before executing any code that contains print statements, as it determines whether the print statements will be executed or skipped.
- The global variable "Print" is shared across the entire codebase, so changing its value in one part of the code will affect its value in other parts of the code as well.
## _function GetPrint
**GetPrint**: The function of GetPrint is to return the Print object.

**parameters**:
- This function does not take any parameters.

**Code Description**:
The GetPrint function is a simple function that returns the Print object. It does not perform any operations or calculations, but simply returns the Print object as it is.

**Note**:
There are no specific points to note about the use of this code, as it is a straightforward function that returns an object.

**Output Example**:
The return value of the GetPrint function would be the Print object.
## _function ReplaceEncode(word)
**ReplaceEncode**: The function of ReplaceEncode is to remove the suffix "encode" from a word if it ends with "encode" and has a length greater than 6 characters.

**parameters**:
- word: A string representing the word to be processed.

**Code Description**:
The ReplaceEncode function takes a word as input and checks if it ends with the suffix "encode" and has a length greater than 6 characters. If both conditions are met, it removes the last 6 characters from the word. The modified word is then returned as the output.

This function is used in the project within the "Lemmatize" and "notIncluded" objects. In the "Lemmatize" object, the ReplaceEncode function is called to preprocess the word before performing lemmatization. The word is converted to lowercase and any spaces or hyphens are replaced with underscores. If the word contains underscores and the part of speech tag is a noun, the last part of the word is lemmatized separately and then joined with the remaining parts. If the part of speech tag is a verb, certain verb forms are checked and replaced with the standard form "isa". Finally, the resulting word is returned.

In the "notIncluded" object, the ReplaceEncode function is called to preprocess the word before checking if it is included in a given input string. The underscores in the word are replaced with spaces, and the modified word is then compared with the input string. If the modified word is not found in the input string, the function returns True, indicating that the word is not included.

**Note**: 
- The ReplaceEncode function is specifically designed to handle words that end with "encode" and have a length greater than 6 characters. It may not produce the desired result for words that do not meet these criteria.
- The ReplaceEncode function does not modify the original word if it does not meet the specified conditions.

**Output Example**:
- Input: "exampleencode"
- Output: "example"
## _function MergeInto(RET_DICT, ret)
**MergeInto**: The function of MergeInto is to merge the contents of the 'ret' dictionary into the 'RET_DICT' dictionary.

**parameters**:
- RET_DICT: A dictionary that stores the merged contents.
- ret: A dictionary containing the contents to be merged into RET_DICT.

**Code Description**:
The MergeInto function takes two dictionaries as input parameters: RET_DICT and ret. It iterates over the keys in the 'ret' dictionary and performs the following operations for each key:
- If the key is present in both RET_DICT and ret, and the key is not equal to "reason", the values corresponding to the key in both dictionaries are added together and stored in RET_DICT.
- If the key is not present in RET_DICT, the value corresponding to the key in ret is added to RET_DICT.

This function is used to merge the contents of the 'ret' dictionary into the 'RET_DICT' dictionary. It is called by two objects in the project: Memory.py/Allow_requery_if_not_in_ONA and Memory.py/ProcessInput.

In the Memory.py/Allow_requery_if_not_in_ONA object, the MergeInto function is called after checking if a previously queried item is not in ONA memory anymore. If the item is still present in memory, the NAR.AddInput function is called with a modified term. The resulting dictionary 'ret' is then merged into the 'RET_DICT' dictionary using the MergeInto function. If the 'ret' dictionary contains an "answers" key with a non-empty value, the first answer is checked for the absence of "truth" and a term value of "None". If these conditions are met, the item is removed from the 'retrieved' list.

In the Memory.py/ProcessInput object, the MergeInto function is called after adding an input to the NAR system using the NAR.AddInput function. The resulting dictionary 'ret' is then merged into the 'RET_DICT' dictionary using the MergeInto function. The function also performs additional operations on the 'ret' dictionary, such as extracting information about executed actions and tested causal hypotheses. It iterates over the 'ret' dictionary and checks for specific conditions to continue or skip certain operations. Finally, the function returns the merged dictionary 'ret' and the updated 'currentTime' value.

**Note**: 
- The MergeInto function is designed to merge the contents of one dictionary into another dictionary.
- The function assumes that the 'ret' dictionary contains keys that are compatible with the 'RET_DICT' dictionary.
- The function does not handle cases where the values of the same key in both dictionaries are of different types.
- The function does not handle cases where the values of the same key in both dictionaries are not compatible for addition.
- The function does not handle cases where the 'ret' dictionary contains keys that should not be merged into the 'RET_DICT' dictionary.

**Output Example**:
If the 'RET_DICT' dictionary initially contains {'key1': 10, 'key2': 20} and the 'ret' dictionary contains {'key2': 30, 'key3': 40}, the merged 'RET_DICT' dictionary will be {'key1': 10, 'key2': 50, 'key3': 40}.
## _function get_embedding_robust(inp)
**get_embedding_robust**: The function of get_embedding_robust is to retrieve the embedding for a given input. It handles exceptions that may occur during the retrieval process and retries the API call after a delay.

**parameters**:
- inp: The input for which the embedding needs to be retrieved.

**Code Description**:
The `get_embedding_robust` function is a robust implementation of the `get_embedding` function. It ensures that the embedding is retrieved successfully by handling any exceptions that may occur during the API call. The function uses a while loop to continuously attempt to retrieve the embedding until it succeeds.

Within the while loop, the function tries to call the `get_embedding` function with the given input. If an exception occurs, it prints a message indicating the failure and waits for 10 seconds before retrying the API call. This delay allows for potential issues with the API to be resolved before attempting the call again. Once the API call is successful, the function breaks out of the while loop and returns the retrieved embedding.

**Note**: 
- It is important to ensure that the `get_embedding` function is implemented and available for this function to work correctly.
- The function assumes that the `time` module is imported and available for use.

**Output Example**:
If the API call is successful, the function returns the retrieved embedding.
## _function ProductPrettify(term)
**ProductPrettify**: The function of ProductPrettify is to prettify a given term by modifying its format and removing unnecessary characters.

**parameters**:
- term: A string representing the term to be prettified.

**Code Description**:
The ProductPrettify function takes a term as input and prettifies it by performing the following steps:

1. It checks if the term contains the string " --> " and the string " * " in the part before " --> ". If both conditions are met, it splits the term into three parts: arg1, arg2, and relarg. The arg1 is obtained by splitting the term using " * " and taking the first part, which is then stripped of leading and trailing spaces. The arg2 is obtained by splitting the term using " * " and " --> " and taking the first part of the resulting split, which is then stripped of leading and trailing spaces. The relarg is obtained by splitting the term using " --> " and taking the second part, which is then stripped of leading and trailing spaces. Finally, the term is updated by concatenating arg1, relarg, and arg2 with spaces in between.

2. The function then replaces any occurrence of "(" and ")" in the term with an empty string.

3. The function returns the modified term.

This function is used to prettify terms in the context of the project. It is called by the Term_AsSentence function, which processes terms and converts them into sentences. The Term_AsSentence function first checks if the term does not contain the string "=/>". If this condition is true, it calls the ProductPrettify function to prettify the term. Otherwise, it performs additional operations on the term before returning the final result.

**Note**: 
- The ProductPrettify function assumes that the input term follows a specific format with " --> " and " * " as separators.
- The function removes parentheses from the term, which may affect the meaning of the term if parentheses are used for grouping.
- The function does not handle any other formatting or modification of the term.

**Output Example**:
- Input: "arg1 * arg2 --> relarg"
- Output: "arg1 relarg arg2"
## _function Term_AsSentence(T)
**Term_AsSentence**: The function of Term_AsSentence is to convert a given term into a sentence by applying specific formatting rules and transformations.

**parameters**:
- T: A string representing the term to be converted into a sentence.

**Code Description**:
The Term_AsSentence function takes a term as input and processes it to generate a sentence by following the steps outlined below:

1. The function checks if the term contains the "<" character. If it does, it extracts the substring of the term starting from the second character and ending at the second-to-last character. Otherwise, it assigns the entire term to the variable "term".

2. The function checks if the term does not contain the string "=/>". If this condition is true, it calls the ProductPrettify function to prettify the term. The ProductPrettify function modifies the format of the term by removing unnecessary characters and adjusting the order of its components.

3. If the term contains the string " =/> ", the function performs additional operations on the term. It splits the term into two parts using the " =/> " delimiter. The first part represents the preceding conditions, which are further split using the " &/ " delimiter. Each condition is then prettified using the ProductPrettify function. The resulting prettified conditions are concatenated using the " and when then " string. The second part represents the consequent, which is prettified using the ProductPrettify function. The final sentence is constructed by combining the prettified conditions, the prettified consequent, and the appropriate connecting words.

4. The function replaces specific strings in the term to adjust the sentence structure. It replaces " --> [" with " hasproperty ", "]" with an empty string, "[" with an empty string, " --> " with " isa ", " &/ " with " then ", and " =/> " with " causes ". Additionally, it replaces " + " with a space.

5. The modified term is returned as the output of the function.

This function is used in the context of the project to convert terms into sentences. It is called by other functions, such as Term_Embedded, Memory_generate_prompt, and ground, to process terms and generate meaningful representations.

**Note**: 
- The Term_AsSentence function assumes that the input term follows specific formatting rules and contains certain delimiters.
- The function relies on the ProductPrettify function to modify the format of the term.
- The function performs specific string replacements to adjust the sentence structure.
- The function does not handle any other formatting or modification of the term.

**Output Example**:
- Input: "arg1 * arg2 --> relarg"
- Output: "When 'arg1' then 'relarg' causes 'arg2'"
## _function Term_Embedded(T)
**Term_Embedded**: The function of Term_Embedded is to retrieve the embedding for a given input term by applying specific formatting rules and transformations.

**parameters**:
- T: A string representing the term for which the embedding needs to be retrieved.

**Code Description**:
The `Term_Embedded` function takes a term as input and processes it to retrieve the embedding by following the steps outlined below:

1. The function calls the `Term_AsSentence` function to convert the input term into a sentence by applying specific formatting rules and transformations.

2. The resulting sentence is then processed further to replace certain characters and adjust the sentence structure. The function replaces "-" with a space and "_" with a space in the sentence.

3. The modified sentence is passed as input to the `get_embedding_robust` function, which retrieves the embedding for the sentence. The `get_embedding_robust` function is a robust implementation of the `get_embedding` function, which ensures that the embedding is retrieved successfully by handling any exceptions that may occur during the API call.

4. The retrieved embedding is returned as the output of the `Term_Embedded` function.

This function is used in the context of the project to retrieve embeddings for terms. It is called by other functions, such as ProcessInput, to process terms and generate meaningful representations.

**Note**: 
- The `Term_Embedded` function assumes that the input term follows specific formatting rules and contains certain characters.
- The function relies on the `Term_AsSentence` function to convert the term into a sentence.
- The function uses the `get_embedding_robust` function to retrieve the embedding for the sentence.
- It is important to ensure that the `get_embedding` function is implemented and available for this function to work correctly.

**Output Example**:
- Input: "term_example"
- Output: [0.1, 0.2, 0.3, ...] (embedding vector)
## _function RetrieveQuestionRelatedBeliefs(memory, view, inp, max_LTM_retrievals)
**RetrieveQuestionRelatedBeliefs**: The function of RetrieveQuestionRelatedBeliefs is to retrieve a list of beliefs related to a given question from the memory. It uses a matching algorithm to find the beliefs that are most relevant to the question and returns them in descending order of match quality and truth expectation.

**parameters**:
- memory: A dictionary representing the memory, where each key is a belief ID and each value is a tuple containing belief information.
- view: A list of beliefs that are currently in the view.
- inp: The input question for which related beliefs need to be retrieved.
- max_LTM_retrievals (optional): An integer representing the maximum number of beliefs to retrieve from long-term memory. Default value is 30.

**Code Description**:
The `RetrieveQuestionRelatedBeliefs` function starts by initializing an empty dictionary called `primed`, which will store the beliefs related to the question. It then retrieves the embedding for the input question using the `get_embedding_robust` function. 

Next, the function iterates over each belief in the memory. If the belief is not already in the view, it calculates the match quality between the question embedding and the belief embedding using the `cosine_similarity` function. The belief and its match quality are added to the `primed` dictionary.

After iterating over all beliefs in the memory, the `primed` dictionary is converted to a list of tuples using the `items` method. The list is then sorted based on two criteria: first by match quality in descending order, and then by truth expectation value using the `Truth_Expectation` function in descending order. The `primed` list is then truncated to contain a maximum of `max_LTM_retrievals` beliefs.

Finally, the `primed` list is reversed and converted to a list of tuples containing belief IDs and belief information. This reversed list is returned as the output of the function.

**Note**: 
- The `get_embedding_robust` function is called to retrieve the embedding for the input question. It is important to ensure that the `get_embedding` function is implemented and available for this function to work correctly.
- The `Truth_Expectation` function is used to calculate the truth expectation value for each belief. It expects a tuple with two elements as input, otherwise it may result in an error.
- The `cosine_similarity` function is used to calculate the match quality between the question embedding and the belief embedding. It is important to ensure that the `cosine_similarity` function is implemented and available for this function to work correctly.

**Output Example**: 
If the input question is "What is the capital of France?", the function may return a list of beliefs related to the question, such as:
[(belief_id_1, belief_info_1), (belief_id_2, belief_info_2), ...]
## _function Memory_view(memory, relevantViewSize, recentViewSize, inpQuestion)
**Memory_view**: The function of Memory_view is to generate a view of beliefs from the memory based on the specified parameters. It retrieves beliefs from the memory and sorts them based on their relevance to a given question and their recency. The function also has an optional input question parameter that can be used to further filter the beliefs based on their relevance to the question.

**parameters**:
- memory: A dictionary representing the memory, where each key is a belief ID and each value is a tuple containing belief information.
- relevantViewSize: An integer representing the maximum number of beliefs to include in the view based on their relevance to the question.
- recentViewSize: An integer representing the maximum number of beliefs to include in the view based on their recency.
- inpQuestion (optional): A string representing the input question for which related beliefs need to be retrieved. Default value is None.

**Code Description**:
The `Memory_view` function starts by initializing an empty list called `view` to store the beliefs in the view. It then creates a list called `recent_item_list` by converting the memory dictionary into a list of key-value pairs.

Next, the function sorts the `recent_item_list` based on the first element of each value in descending order. This element represents the recency of the belief. The function then appends a slice of the sorted `recent_item_list` to the `view` list, starting from the first element and ending at the index specified by `recentViewSize`. This ensures that the most recent beliefs are included in the view.

If the `inpQuestion` parameter is not None, the function calls the `RetrieveQuestionRelatedBeliefs` function to retrieve beliefs related to the input question. The `RetrieveQuestionRelatedBeliefs` function takes the memory, the current view, the input question, and the `relevantViewSize` as parameters. The retrieved beliefs are then concatenated with the `view` list.

Finally, the function returns the `view` list, which contains the beliefs in the view.

**Note**: 
- The `RetrieveQuestionRelatedBeliefs` function is called to retrieve beliefs related to the input question. It is important to ensure that the `RetrieveQuestionRelatedBeliefs` function is implemented and available for this function to work correctly.

**Output Example**: 
If the input question is "What is the capital of France?", the function may return a list of beliefs related to the question, such as:
[(belief_id_1, belief_info_1), (belief_id_2, belief_info_2), ...]
## _function Memory_generate_prompt(currentTime, memory, prompt_start, prompt_end, relevantViewSize, recentViewSize, inpQuestion)
**Memory_generate_prompt**: The function of Memory_generate_prompt is to generate a prompt memory string based on the current time, memory, prompt start and end, relevant view size, recent view size, and an optional input question. It retrieves beliefs from the memory, processes them, and constructs a prompt memory string that includes information about each belief, such as its term, time, and confidence level.

**parameters**:
- currentTime: A float representing the current time.
- memory: A dictionary representing the memory, where each key is a belief ID and each value is a tuple containing belief information.
- prompt_start: A string representing the starting part of the prompt memory string.
- prompt_end: A string representing the ending part of the prompt memory string.
- relevantViewSize: An integer representing the maximum number of beliefs to include in the view based on their relevance to the question.
- recentViewSize: An integer representing the maximum number of beliefs to include in the view based on their recency.
- inpQuestion (optional): A string representing the input question for which related beliefs need to be retrieved. Default value is None.

**Code Description**:
The Memory_generate_prompt function starts by initializing an empty string called "prompt_memory" to store the prompt memory string. It then calls the Memory_view function to retrieve beliefs from the memory based on the specified parameters, such as relevantViewSize, recentViewSize, and inpQuestion. The retrieved beliefs are stored in the "buf" variable.

Next, the function checks if the "buf" variable is empty. If it is, the prompt_memory string is set to "EMPTY!". Otherwise, the function iterates over each belief in the "buf" variable using the enumerate() function. For each belief, it extracts the time, frequency, and confidence level from the belief tuple. It then calls the Truth_Projection function to calculate the projected truth value of the belief at the current time based on its original truth value and the time difference between the original time and the current time.

The function also calls the Term_AsSentence function to convert the belief term into a sentence by applying specific formatting rules and transformations. If the confidence level of the belief is less than 0.5, the term is modified to include the phrase "not" before the main term.

The function constructs the prompt memory string by concatenating the belief index, the converted term, the time information, and the confidence level for each belief. The prompt_memory string is updated with each iteration.

Finally, the function returns the "buf" variable, which contains the beliefs retrieved from the memory, and the constructed prompt memory string by concatenating the prompt_start, prompt_memory, and prompt_end strings.

**Note**: 
- The Memory_generate_prompt function relies on the Memory_view and Truth_Projection functions to retrieve beliefs from the memory and calculate the projected truth value of beliefs.
- The Term_AsSentence function is called to convert belief terms into sentences by applying specific formatting rules and transformations.
- The prompt memory string includes information about each belief, such as its index, term, time, and confidence level.
- If the memory is empty, the prompt memory string will be set to "EMPTY!".
- The prompt memory string is constructed by concatenating the information of each belief in the memory.
- The function provides the option to include an input question to retrieve beliefs related to the question.
- The prompt memory string can be customized by specifying the prompt start and end strings.

**Output Example**:
- Input: Memory_generate_prompt(10.0, memory, "Prompt Start:", "Prompt End.", 5, 3, "What is the capital of France?")
- Output: ([belief1, belief2, belief3], "Prompt Start:i=0: 'belief1' time=10.0 confidence=0.8\ni=1: 'belief2' time=9.5 confidence=0.6\ni=2: 'belief3' time=9.0 confidence=0.7\nPrompt End.")
## _function Lemmatize(word, tag)
**Lemmatize**: The function of Lemmatize is to perform lemmatization on a given word based on its part of speech tag.

**parameters**:
- word: A string representing the word to be lemmatized.
- tag: A part of speech tag indicating the grammatical category of the word.

**Code Description**:
The Lemmatize function takes a word and its corresponding part of speech tag as input. It first preprocesses the word by converting it to lowercase and replacing any spaces or hyphens with underscores. The ReplaceEncode function is then called to remove the suffix "encode" from the word if it ends with "encode" and has a length greater than 6 characters. 

Next, the function checks if the word contains underscores and the part of speech tag is a noun. If both conditions are met, the word is split into parts using underscores as separators. The last part of the word is lemmatized separately using the WordNetLemmatizer's lemmatize function, with the specified part of speech tag. The resulting lemmatized last part is then joined with the remaining parts using underscores. 

If the part of speech tag is a verb, the function checks if the lemmatized word matches certain predefined verb forms. If a match is found, the function returns the standard form "isa" as the output.

Finally, the function returns the lemmatized word after converting it to lowercase and replacing any spaces or hyphens with underscores.

**Note**: 
- The Lemmatize function relies on the ReplaceEncode function to preprocess the word before lemmatization. It is important to note that the ReplaceEncode function is specifically designed to handle words that end with "encode" and have a length greater than 6 characters. It may not produce the desired result for words that do not meet these criteria.
- The Lemmatize function uses the WordNetLemmatizer from the NLTK library for lemmatization. Make sure to import the necessary libraries and initialize the WordNetLemmatizer before using this function.
- The Lemmatize function assumes that the part of speech tag provided is compatible with the WordNetLemmatizer's lemmatize function.

**Output Example**:
- Input: word = "running", tag = wordnet.VERB
- Output: "run"
## _function Atomize(atom, atoms, pos, atomCreationThreshold)
**Atomize**: The function of Atomize is to retrieve or create an atom for a given input. It checks if the atom already exists in the atoms dictionary using a key generated from the input and position. If the atom exists, it retrieves the corresponding embedding from the atoms dictionary. If the atom does not exist, it calls the `get_embedding_robust` function to retrieve the embedding for the input. 

**parameters**:
- atom: The input atom to be atomized.
- atoms: A dictionary containing the existing atoms and their embeddings.
- pos: The position of the atom in the sentence (e.g., "NOUN", "VERB").
- atomCreationThreshold: The threshold value for creating a new atom.

**Code Description**:
The `Atomize` function takes an input atom, a dictionary of existing atoms, the position of the atom, and a threshold value for creating a new atom. It first generates a key for the input atom and position by concatenating them with a separator (";;"). It then checks if the key exists in the atoms dictionary. If the key exists, it retrieves the corresponding embedding from the dictionary. If the key does not exist, it calls the `get_embedding_robust` function to retrieve the embedding for the input atom.

The function then iterates over all the keys in the atoms dictionary. For each key, it splits the atom and position using the separator and checks if the position matches the given position. If the positions match, it retrieves the embedding for that key and calculates the match quality between the input atom embedding and the retrieved embedding using the cosine similarity measure. The function keeps track of the closest atom and its match quality.

After iterating through all the keys, the function checks if the closest match quality is below the atomCreationThreshold. If it is, it returns the input atom as the atomized result and adds the input atom and its embedding to the atoms dictionary using the generated key. If the closest match quality is above the threshold, it returns the closest atom as the atomized result.

**Note**: 
- The function assumes that the `get_embedding_robust` function is implemented and available for use.
- The function uses the `cosine_similarity` function to calculate the match quality between embeddings. The implementation of this function is not provided in the code snippet.

**Output Example**:
If the closest match quality is below the atomCreationThreshold, the function returns the input atom as the atomized result. If the closest match quality is above the threshold, the function returns the closest atom as the atomized result.
## _function Allow_requery_if_not_in_ONA(RET_DICT, term, time)
**Allow_requery_if_not_in_ONA**: The function of Allow_requery_if_not_in_ONA is to check if a previously queried item is still present in the ONA memory. If the item is no longer in memory, it sets it up for re-query by removing it from the 'retrieved' list.

**parameters**:
- RET_DICT: A dictionary that stores the merged contents.
- term: The term of the item to be checked.
- time: The time of the item to be checked.

**Code Description**:
The Allow_requery_if_not_in_ONA function first checks if the (term, time) tuple is present in the 'retrieved' list. If it is, it proceeds to call the NAR.AddInput function with a modified term, which appends a question mark to the original term. The resulting dictionary 'ret' is then merged into the 'RET_DICT' dictionary using the MergeInto function. 

If the 'ret' dictionary contains an "answers" key with a non-empty value, the function checks the first answer for the absence of a "truth" key and a term value of "None". If these conditions are met, it removes the (term, time) tuple from the 'retrieved' list.

**Note**: 
- The Allow_requery_if_not_in_ONA function assumes that the 'retrieved' list and the 'retrieved' list are defined and accessible within the scope of the function.
- The function does not handle cases where the 'retrieved' list is not initialized or is not of the expected type.
- The function does not handle cases where the 'retrieved' list contains tuples that are not compatible with the (term, time) format.
- The function does not handle cases where the 'retrieved' list contains tuples that should not be removed.

The Allow_requery_if_not_in_ONA function is called in the Memory.py/query object. In this object, the function is called after checking if the (term, time) tuple is not in the 'retrieved' list and is present in the 'memory' dictionary. If these conditions are met, the (term, time) tuple is added to the 'retrieved' list, and the NAR.AddInput function is called with a "*stampimport" command, passing the 'stamp' value from the 'memory' dictionary. If the 'time' value is "eternal", the ProcessInput function is called with modified parameters.

The Allow_requery_if_not_in_ONA function is also called in the Memory.py/query object when a simple query matching condition is met. In this case, the function iterates over the 'memory' dictionary and checks for terms that start with the first part of the 'term' and end with the second part of the 'term'. It selects the best matching term based on the truth expectation value and retrieves its corresponding (term, time) tuple from the 'retrieved' list. The NAR.AddInput function is then called with a "*stampimport" command, passing the 'stamp' value from the 'memory' dictionary. If the 'bestTime' value is "eternal", the ProcessInput function is called with modified parameters.

**Note**: The specific implementation and usage of the Allow_requery_if_not_in_ONA function may vary depending on the context and requirements of the project. It is important to review and understand the code and its dependencies before using it in a different project or modifying it for specific use cases.
## _function query(RET_DICT, currentTime, memory, term, time)
**query**: The function of query is to retrieve information from the memory based on a given term and time. It also handles simple query matching and updates the 'retrieved' list.

**parameters**:
- RET_DICT: A dictionary that stores the merged contents.
- currentTime: An integer representing the current time.
- memory: A dictionary that stores the memory items.
- term: A string representing the term to be queried.
- time: A string or integer representing the time of the item to be queried.

**Code Description**:
The query function starts by checking if the 'time' parameter is not equal to "eternal". If it is not, the function returns the current time. This condition is used to handle cases where the time is not "eternal" and no further processing is required.

Next, the function calls the Allow_requery_if_not_in_ONA function, passing the 'RET_DICT', 'term', and 'time' parameters. This function is responsible for checking if a previously queried item is still present in the ONA memory. If the item is no longer in memory, it sets it up for re-query by removing it from the 'retrieved' list.

After that, the function checks if the (term, time) tuple is not in the 'retrieved' list and is present in the 'memory' dictionary. If these conditions are met, the (term, time) tuple is added to the 'retrieved' list, and the NAR.AddInput function is called with a "*stampimport" command, passing the 'stamp' value from the 'memory' dictionary. This step is performed to update the NAR system with the retrieved item.

If the 'time' value is "eternal", the function proceeds to call the ProcessInput function with modified parameters. The ProcessInput function is responsible for processing the retrieved item and updating the memory and current time accordingly.

Additionally, the function handles simple query matching when the term contains "?1". It splits the term into two parts and iterates over the 'memory' dictionary to find matching terms that start with the first part and end with the second part. It selects the best matching term based on the truth expectation value and retrieves its corresponding (term, time) tuple from the 'retrieved' list. The NAR.AddInput function is then called with a "*stampimport" command, passing the 'stamp' value from the 'memory' dictionary. If the 'bestTime' value is "eternal", the ProcessInput function is called with modified parameters.

Finally, the function adds the (term, time) tuple to the 'retrieved' list and returns the current time.

**Note**: 
- The specific implementation and usage of the query function may vary depending on the context and requirements of the project. It is important to review and understand the code and its dependencies before using it in a different project or modifying it for specific use cases.
- The query function assumes that the 'retrieved' list, 'NAR' object, 'Print' variable, and other referenced functions and variables are defined and accessible within the scope of the function.
- The function does not handle cases where the 'retrieved' list is not initialized or is not of the expected type.
- The function does not handle cases where the 'memory' dictionary is not initialized or does not contain the expected keys and values.
- The function does not handle cases where the 'term' and 'time' parameters are not of the expected types or formats.
- The function does not handle cases where the 'NAR.AddInput' function does not exist or does not support the "*stampimport" command.
- The function does not handle cases where the 'ProcessInput' function does not exist or does not support the expected parameters and return values.

**Output Example**: If the 'time' parameter is not "eternal" and the conditions for re-querying are not met, the query function will return the current time.
## _function ProcessInput(RET_DICT, currentTime, memory, inputforNAR, backups)
**ProcessInput**: The function of ProcessInput is to process the input for the NAR (Non-Axiomatic Reasoning) system. It takes various parameters and performs several operations on the input data.

**parameters**:
- RET_DICT: A dictionary that stores the merged contents.
- currentTime: An integer representing the current time.
- memory: A dictionary that stores the memory items.
- inputforNAR: A string representing the input data for the NAR system.
- backups (optional): A list of strings representing the backup types to be added to memory.

**Code Description**:
The ProcessInput function starts by calling the NAR.AddInput function with the inputforNAR parameter and the Print parameter. This function adds the input to the NAR system and returns a dictionary containing the results.

The function then merges the contents of the 'ret' dictionary into the 'RET_DICT' dictionary using the MergeInto function. The MergeInto function is called with the RET_DICT and ret dictionaries as parameters. This step ensures that the contents of the 'ret' dictionary are added to the 'RET_DICT' dictionary.

Next, the function iterates over the 'ret' dictionary and performs the following operations for each execution:
- It extracts the reason and desire values from the 'ret' dictionary if they exist.
- It appends the reason hypothesis to the TestedCausalHypotheses list.
- It prints the execution, expectation, and reason values.

After that, the function iterates over the backups list and performs the following operations for each backup type:
- It retrieves the corresponding items from the 'ret' dictionary and adds them to the 'it' list.
- If the backup type is "input", it appends the TestedCausalHypotheses list to the 'it' list.
- It iterates over the 'it' list and performs the following operations for each derivation:
  - It checks if the derivation meets certain conditions to continue or skip certain operations.
  - It processes the term and extracts the time, stamp, frequency, and confidence values.
  - It checks if the (term, time) tuple is already in memory and updates the memory if necessary.
  - It creates a new entry in the memory if the (term, time) tuple is not already in memory.

The function then performs additional operations based on the inputforNAR value. If the inputforNAR contains certain characters or patterns, the currentTime value is updated accordingly.

Finally, the function returns the merged dictionary 'ret' and the updated 'currentTime' value.

**Note**:
- The ProcessInput function is designed to process the input for the NAR system and update the memory accordingly.
- The function assumes that the NAR.AddInput, MergeInto, and query functions are defined and accessible within the scope of the function.
- The function does not handle cases where the 'ret' dictionary does not contain the expected keys and values.
- The function does not handle cases where the 'backups' parameter is not of the expected type or format.
- The function does not handle cases where the 'inputforNAR' parameter is not of the expected type or format.
- The function does not handle cases where the 'Print' parameter is not of the expected type or format.

**Output Example**:
If the 'ret' dictionary initially contains {'executions': [{'execution1': 'value1'}, {'execution2': 'value2'}], 'answers': [{'answer1': 'value1'}, {'answer2': 'value2'}]}, and the 'currentTime' value is 10, the function will return the merged dictionary {'executions': [{'execution1': 'value1'}, {'execution2': 'value2'}], 'answers': [{'answer1': 'value1'}, {'answer2': 'value2'}]}, and the updated 'currentTime' value will depend on the specific operations performed in the function.
## _function notIncluded(word, inp)
**notIncluded**: The function of notIncluded is to check if a modified word is included in a given input string.

**parameters**:
- word: A string representing the word to be processed.
- inp: A string representing the input string to be checked against.

**Code Description**:
The notIncluded function takes two input parameters: "word" and "inp". The "word" parameter represents the word to be processed, while the "inp" parameter represents the input string to be checked against. 

The function first calls the ReplaceEncode function to modify the "word" parameter. The ReplaceEncode function removes the suffix "encode" from the word if it ends with "encode" and has a length greater than 6 characters. The modified word is then assigned back to the "word" parameter.

Next, the function replaces all occurrences of the underscore character "_" in the modified word with a space character " ". This is done using the replace() method of the string object. The resulting modified word is then compared with the input string "inp".

The function also performs additional replacements on the input string "inp" before the comparison. It replaces all occurrences of the substring ". " (period followed by space) with a space character " ". It also replaces all occurrences of the single quote character "'" with an empty string.

Finally, the function checks if the modified word is not found in the modified input string. If the modified word is not included in the modified input string, the function returns True, indicating that the word is not included. Otherwise, it returns False.

**Note**: 
- The ReplaceEncode function is specifically designed to handle words that end with "encode" and have a length greater than 6 characters. It may not produce the desired result for words that do not meet these criteria.
- The notIncluded function modifies the original word by calling the ReplaceEncode function. If you need to preserve the original word, make a copy before calling the notIncluded function.
- The function performs multiple replacements on the modified word and input string to ensure consistent comparison. Make sure to consider these replacements when using the function.

**Output Example**:
- Input: word = "exampleencode", inp = "This is an example."
- Output: True
## _function Relation(RET_DICT, inp, currentTime, memory, atoms, s, v, p, punctuation_tv, ImportGPTKnowledge, atomCreationThreshold)
**Relation**: The function of Relation is to process a relation between subject, verb, and predicate in a given input sentence. It performs various operations on the input data and updates the memory accordingly.

**parameters**:
- RET_DICT: A dictionary that stores the merged contents.
- inp: A string representing the input data.
- currentTime: An integer representing the current time.
- memory: A dictionary that stores the memory items.
- atoms: A dictionary containing the existing atoms and their embeddings.
- s: A string representing the subject of the relation.
- v: A string representing the verb of the relation.
- p: A string representing the predicate of the relation.
- punctuation_tv: A string representing the punctuation and truth value of the relation.
- ImportGPTKnowledge: A boolean indicating whether GPT knowledge should be imported.
- atomCreationThreshold: The threshold value for creating a new atom.

**Code Description**:
The Relation function takes various input parameters and performs several operations on the input data. It first checks if the ImportGPTKnowledge flag is False and if either the subject (s) or predicate (p) is not included in the input (inp). If these conditions are met, the function returns False, the current time, and an empty sentence.

Next, the function performs lemmatization on the subject (s), predicate (p), and verb (v) using the Lemmatize function. The Lemmatize function converts the words to lowercase, replaces spaces and hyphens with underscores, and removes the suffix "encode" if applicable. The lemmatized words are then passed to the Atomize function to retrieve or create atoms for each word. The Atomize function checks if the atoms already exist in the atoms dictionary and retrieves the corresponding embeddings. If the atoms do not exist, it calls the get_embedding_robust function to retrieve the embeddings. The function also adds the verb (v) to the set of relations.

After the lemmatization and atomization process, the function checks if any of the subject (s), verb (v), or predicate (p) is empty. If any of them is empty, the function returns False, the current time, and an empty sentence.

The function then checks if the verb (v) is "isa" or "are". If it is, the function compares the subject (s) and predicate (p). If they are the same, the function returns False, the current time, and an empty sentence. Otherwise, it constructs a sentence using angle brackets ("< >") to represent the relation and appends the punctuation_tv string. The constructed sentence is then passed to the ProcessInput function to update the memory.

If the verb (v) is not "isa" or "are", the function constructs a sentence using angle brackets ("< >") to represent the relation between the subject (s), predicate (p), and verb (v). The sentence is then passed to the ProcessInput function to update the memory.

Finally, the function returns True, the current time, and the constructed sentence.

**Note**: 
- The Relation function relies on the Lemmatize and Atomize functions to preprocess and atomize the subject, verb, and predicate before constructing the relation sentence. It is important to ensure that these functions are implemented and accessible within the scope of the Relation function.
- The Relation function assumes that the Lemmatize and Atomize functions are compatible with the specified input parameters and return the expected results.
- The Relation function uses the ProcessInput function to update the memory with the constructed relation sentence. Make sure to import the necessary libraries and initialize the required variables before using this function.
- The Relation function assumes that the ProcessInput function is implemented and accessible within the scope of the Relation function.

**Output Example**:
- Input: RET_DICT = {}, inp = "This is an example.", currentTime = 0, memory = {}, atoms = {}, s = "example", v = "is", p = "an", punctuation_tv = ".", ImportGPTKnowledge = False, atomCreationThreshold = 0.5
- Output: True, 0, "<example --> an>."
## _function Property(RET_DICT, inp, currentTime, memory, atoms, s, p, punctuation_tv, ImportGPTKnowledge, atomCreationThreshold)
**Property**: The Property function is responsible for processing a given input and determining if it satisfies certain conditions for a property relation. It checks if the input should be filtered out based on the ImportGPTKnowledge flag and if the subject or property are not included in the input. It then performs lemmatization on the subject and property using the Lemmatize function and atomizes them using the Atomize function. If the subject or property are empty or equal, the function returns False. Otherwise, it constructs a sentence string representing the property relation and passes it to the ProcessInput function for further processing. Finally, the function returns True, the current time, and the constructed sentence.

**parameters**:
- RET_DICT: A dictionary that stores the merged contents.
- inp: A string representing the input data.
- currentTime: An integer representing the current time.
- memory: A dictionary that stores the memory items.
- atoms: A dictionary containing the existing atoms and their embeddings.
- s: A string representing the subject of the property relation.
- p: A string representing the property of the property relation.
- punctuation_tv: A string representing the punctuation and truth value of the property relation.
- ImportGPTKnowledge: A boolean flag indicating whether GPT knowledge should be imported.
- atomCreationThreshold: The threshold value for creating a new atom.

**Code Description**:
The Property function takes several input parameters and performs a series of operations to determine if a given input satisfies the conditions for a property relation. 

First, the function checks if the ImportGPTKnowledge flag is False and if either the subject (s) or property (p) are not included in the input (inp). If either of these conditions is true, the function returns False, the current time (currentTime), and an empty sentence string.

Next, the function calls the Lemmatize function to perform lemmatization on the subject and property. The Lemmatize function takes a word and its corresponding part of speech tag as input and returns the lemmatized word. In this case, the Lemmatize function is called with the subject (s) and property (p) as inputs and the part of speech tags "NOUN" and "ADJ" respectively. The lemmatized subject and property are then assigned back to the s and p variables.

The function then checks if the subject (s) or property (p) are empty or if they are equal. If any of these conditions are true, the function returns False, the current time (currentTime), and an empty sentence string.

If none of the above conditions are met, the function constructs a sentence string representing the property relation using the subject (s), property (p), and punctuation_tv parameters. The sentence string is constructed by enclosing the subject in angle brackets ("< >"), followed by an arrow ("-->"), and then enclosing the property in square brackets ("[ ]"). The punctuation_tv parameter is then appended to the sentence string.

After constructing the sentence string, the function calls the ProcessInput function with the RET_DICT, currentTime, memory, and sentence parameters. The ProcessInput function processes the input for the NAR system and updates the memory accordingly. The function then returns True, the updated current time (currentTime), and the constructed sentence string.

**Note**: 
- The Property function relies on the Lemmatize and Atomize functions to process the subject and property before constructing the property relation sentence. It is important to ensure that these functions are implemented and accessible within the scope of the Property function.
- The Property function assumes that the part of speech tags provided to the Lemmatize function are compatible with the WordNetLemmatizer's lemmatize function.
- The Property function assumes that the ProcessInput function is defined and accessible within the scope of the Property function.
- The Property function assumes that the RET_DICT dictionary is initialized and accessible within the scope of the Property function.
- The Property function assumes that the memory and atoms dictionaries are initialized and accessible within the scope of the Property function.
- The Property function assumes that the punctuation_tv parameter is a string representing the punctuation and truth value of the property relation.
- The Property function assumes that the ImportGPTKnowledge flag is a boolean value indicating whether GPT knowledge should be imported.
- The Property function assumes that the atomCreationThreshold parameter is a threshold value for creating a new atom.

**Output Example**:
- Input: RET_DICT = {}, inp = "This is an example.", currentTime = 10, memory = {}, atoms = {}, s = "example", p = "property", punctuation_tv = ". :|: {0.8 0.9}", ImportGPTKnowledge = False, atomCreationThreshold = 0.5
- Output: (True, 10, "<example --> [property]> :|: {0.8 0.9}.")
## _function Memory_digest_sentence(RET_DICT, inp, currentTime, memory, atoms, sentence, truth, userGoal, PrintMemoryUpdates, TimeHandling, ImportGPTKnowledge, atomCreationThreshold)
**Memory_digest_sentence**: The function of Memory_digest_sentence is to process a given input sentence and update the memory based on the relations and properties extracted from the sentence. It performs various operations on the input data and calls other functions to handle specific cases.

**parameters**:
- RET_DICT: A dictionary that stores the merged contents.
- inp: A string representing the input data.
- currentTime: An integer representing the current time.
- memory: A dictionary that stores the memory items.
- atoms: A dictionary containing the existing atoms and their embeddings.
- sentence: A string representing the input sentence to be processed.
- truth: A tuple representing the truth value of the sentence.
- userGoal: A boolean indicating whether the sentence is a user goal.
- PrintMemoryUpdates: A boolean indicating whether to print memory updates.
- TimeHandling: A boolean indicating whether to handle time-related information.
- ImportGPTKnowledge: A boolean indicating whether GPT knowledge should be imported.
- atomCreationThreshold: The threshold value for creating a new atom.

**Code Description**:
The Memory_digest_sentence function takes various input parameters and performs several operations on the input sentence. It first checks if the current time (currentTime) is different from the last time (lastTime). If they are different, it initializes the set of hadRelation to an empty set. This set is used to keep track of the relations that have already been processed.

Next, the function checks if the input sentence is already in the set of hadRelation. If it is, the function returns False, the current time, and an empty string. This is to avoid processing duplicate sentences.

If the input sentence is not in the set of hadRelation, the function updates the lastTime to the current time. It then splits the input sentence into pieces using commas as the delimiter. Each piece is stripped of leading and trailing spaces and any spaces within are replaced with underscores. This is done to standardize the format of the pieces.

The function then determines the punctuation to be used based on whether the sentence is a user goal or not. If TimeHandling is enabled, the punctuation is formatted to include the truth value of the sentence. Otherwise, the punctuation only includes the truth value.

Next, the function checks the number of pieces in the sentence. If there are three pieces, it further checks if the second piece is "hasproperty". If it is, the function calls the Property function to process the relation. Otherwise, it calls the Relation function to process the relation. Both functions are called with the appropriate input parameters.

If the number of pieces is not three, it means that the relation cannot be formed. In this case, the function returns False, the current time, and an empty string.

**Note**: 
- The Memory_digest_sentence function relies on the Property and Relation functions to process the relations in the input sentence. It is important to ensure that these functions are implemented and accessible within the scope of the Memory_digest_sentence function.
- The Memory_digest_sentence function assumes that the lastTime and hadRelation variables are initialized and accessible within the scope of the function.
- The Memory_digest_sentence function assumes that the Property and Relation functions are compatible with the specified input parameters and return the expected results.
- The Memory_digest_sentence function assumes that the RET_DICT, memory, and atoms dictionaries are initialized and accessible within the scope of the function.
- The Memory_digest_sentence function assumes that the PrintMemoryUpdates flag is a boolean value indicating whether to print memory updates.
- The Memory_digest_sentence function assumes that the TimeHandling flag is a boolean value indicating whether to handle time-related information.
- The Memory_digest_sentence function assumes that the ImportGPTKnowledge flag is a boolean value indicating whether GPT knowledge should be imported.
- The Memory_digest_sentence function assumes that the atomCreationThreshold parameter is a threshold value for creating a new atom.

**Output Example**:
- Input: RET_DICT = {}, inp = "This is an example.", currentTime = 0, memory = {}, atoms = {}, sentence = "example hasproperty property", truth = (0.8, 0.9), userGoal = False, PrintMemoryUpdates = True, TimeHandling = True, ImportGPTKnowledge = False, atomCreationThreshold = 0.5
- Output: (True, 0, "<example --> [property]> :|: {0.8 0.9}.")
## _function Memory_load(filename)
**Memory_load**: The function of Memory_load is to load the contents of a memory file and return the loaded memory, atom embeddings, current time, and the maximum base ID.

**parameters**:
- filename: A string representing the name of the memory file to load.

**Code Description**:
The Memory_load function begins by initializing the memory variable as an empty dictionary, which will store the NARS-style long-term memory. The atoms variable is also initialized as an empty dictionary, which will map atoms to their embeddings. The currentTime variable is set to 1 initially.

The function then checks if the specified filename exists. If it does, the function proceeds to load the memory content from the file. It opens the file using the open() function and reads its contents using the json.load() function. The loaded content is stored in the variables mt and currentTime. The memory dictionary is then updated by converting the keys from strings to their corresponding Python objects using the literal_eval() function. The values are copied from mt to memory.

Next, the function constructs the atomfile name by replacing the ".json" extension of the filename with "_atoms.json". It opens the atomfile and reads its contents using the json.load() function. The loaded content is stored in the atoms dictionary.

The function then iterates over the keys in the memory dictionary and updates the maxBaseId variable by finding the maximum value among the base IDs stored in memory[key][3].

Finally, the function returns a tuple containing the memory dictionary, atoms dictionary, currentTime, and maxBaseId.

**Note**: 
- The function assumes that the filename parameter refers to a valid memory file.
- The function expects the memory file to be in JSON format.
- The function expects the atomfile to have the same name as the memory file, but with "_atoms.json" as the extension.

**Output Example**:
```python
memory = {
    'key1': [value1],
    'key2': [value2],
    ...
}
atoms = {
    'atom1': [embedding1],
    'atom2': [embedding2],
    ...
}
currentTime = 12345
maxBaseId = 100
return (memory, atoms, currentTime, maxBaseId)
```
## _function Memory_store(filename, memory, atoms, currentTime)
**Memory_store**: The function of Memory_store is to store the contents of the memory and atoms into a file in JSON format.

**parameters**:
- filename: A string representing the name of the file to store the memory.
- memory: A dictionary containing the memory data to be stored.
- atoms: A dictionary containing the atom data to be stored.
- currentTime: An integer representing the current time.

**Code Description**:
The Memory_store function first opens the specified file in write mode using the 'w' flag. It then uses the json.dump() function to write the memory and currentTime data into the file. The memory data is converted into a dictionary comprehension where the keys are converted to strings and the values are preserved. The currentTime is stored as a tuple along with the memory data.

Next, the function creates a new file name by replacing the ".json" extension of the original filename with "_atoms.json". It opens this new file in write mode and uses json.dump() to write the atoms data into the file.

**Note**:
- The Memory_store function assumes that the filename parameter is a valid file name and that the file can be opened in write mode.
- The function uses the json module to serialize the memory and atoms data into JSON format.
- It is important to ensure that the memory and atoms parameters are dictionaries before calling the Memory_store function.
## _function Memory_QuestionPriming(RET_DICT, currentTime, cmd, memory, buf)
**Memory_QuestionPriming**: The function of Memory_QuestionPriming is to process a command and prime the ONA's memory with a question. It retrieves the indices from the command, checks if they are present in the buffer, and activates the corresponding concepts in the memory by querying them.

**parameters**:
- RET_DICT: A dictionary that stores the merged contents.
- currentTime: An integer representing the current time.
- cmd: A string representing the command to be processed.
- memory: A dictionary that stores the memory items.
- buf: A list that stores the buffer items.

**Code Description**:
The Memory_QuestionPriming function starts by extracting the indices from the command using string manipulation. It replaces the "i=" substring with "item " and splits the command based on "item " to get the index references. It then iterates over the index references, extracting the digits and adding them to the indices list. This step is performed to identify the indices present in the command.

Next, the function checks if the indices are within the range of the buffer. If an index is valid, it retrieves the corresponding item from the buffer and calls the query function. The query function is responsible for retrieving information from the memory based on a given term and time. It updates the 'retrieved' list and activates the concepts in the memory.

Finally, the function adds the (term, time) tuple to the 'retrieved' list and returns the current time.

**Note**: 
- The specific implementation and usage of the Memory_QuestionPriming function may vary depending on the context and requirements of the project. It is important to review and understand the code and its dependencies before using it in a different project or modifying it for specific use cases.
- The Memory_QuestionPriming function assumes that the 'query' function, 'RET_DICT' dictionary, 'currentTime' variable, 'cmd' string, 'memory' dictionary, and 'buf' list are defined and accessible within the scope of the function.
- The function does not handle cases where the 'query' function does not exist or does not support the expected parameters and return values.
- The function does not handle cases where the 'indices' list is not initialized or does not contain valid indices.
- The function does not handle cases where the 'buf' list is not initialized or does not contain the expected items.
- The function does not handle cases where the 'memory' dictionary is not initialized or does not contain the expected keys and values.
- The function does not handle cases where the 'retrieved' list is not initialized or is not of the expected type.
- The function does not handle cases where the 'query' function does not retrieve the expected information from the memory.
- The function does not handle cases where the 'query' function does not activate the expected concepts in the memory.
- The function does not handle cases where the 'query' function does not update the 'retrieved' list.
- The function does not handle cases where the 'query' function does not return the expected current time.

**Output Example**: If the indices in the command are valid and the query function retrieves the expected information from the memory, the Memory_QuestionPriming function will update the 'retrieved' list and return the current time.
## _function Memory_Eternalize(currentTime, memory, eternalizationDistance)
**Memory_Eternalize**: The function of Memory_Eternalize is to eternalize the memory by deleting outdated beliefs and adding new beliefs based on the current time and eternalization distance.

**Parameters**:
- currentTime: The current time in the system.
- memory: The memory object containing beliefs.
- eternalizationDistance: The time duration after which beliefs are considered outdated and need to be eternalized.

**Code Description**:
The Memory_Eternalize function iterates through each belief in the memory object. If the belief is not already eternal and the time difference between the current time and the belief's timestamp is greater than the eternalization distance, the belief is considered outdated and needs to be eternalized.

For each outdated belief, the function checks if there is a corresponding belief in the memory with the "eternal" timestamp. If such a belief exists, the function retrieves the previous last used time and use count from the eternal belief. Otherwise, the previous last used time and use count are set to 0.

The outdated belief is then added to the list of beliefs to be deleted. The function also queries the ONA (Open NARS) system to get the belief truth for the outdated belief. If there are answers from the ONA system and the first answer contains the "truth" field, the function extracts the frequency and confidence values from the answer. The function also retrieves the timestamp of the answer.

Finally, the function creates a new belief with the "eternal" timestamp and updates the last used time and use count based on the previous eternal belief and the outdated belief. The frequency, confidence, and timestamp values are set to the values obtained from the ONA system. This new belief is added to the list of beliefs to be added.

After iterating through all beliefs, the function deletes the beliefs in the "deletes" list from the memory object. Then, it adds the beliefs in the "additions" list to the memory object.

**Note**: 
- This function assumes that the memory object is a dictionary where the keys are tuples representing the belief and the timestamp, and the values are the belief information.
- The function relies on the NAR.AddInput function from the NarsGPT.py module to query the ONA system and retrieve belief truth.
- The function updates the memory object in-place by deleting outdated beliefs and adding new eternal beliefs.
## _function Memory_inject_commands(RET_DICT, inp, buf, currentTime, memory, atoms, cmd, userQuestion, userGoal, PrintAnswer, PrintMemoryUpdates, PrintTruthValues, QuestionPriming, TimeHandling, ImportGPTKnowledge, atomCreationThreshold)
**Memory_inject_commands**: The function of Memory_inject_commands is to process a list of commands and update the memory based on the information extracted from each command. It iterates over the commands, performs various checks and operations, and calls other functions to handle specific cases.

**parameters**:
- RET_DICT: A dictionary that stores the merged contents.
- inp: A string representing the input data.
- buf: A list that stores the buffer items.
- currentTime: An integer representing the current time.
- memory: A dictionary that stores the memory items.
- atoms: A dictionary containing the existing atoms and their embeddings.
- cmd: A list of strings representing the commands to be processed.
- userQuestion: A boolean indicating whether the commands are user questions.
- userGoal: A boolean indicating whether the commands are user goals.
- PrintAnswer: A boolean indicating whether to print the answers.
- PrintMemoryUpdates: A boolean indicating whether to print memory updates.
- PrintTruthValues: A boolean indicating whether to print truth values.
- QuestionPriming: A boolean indicating whether to prime the memory with questions.
- TimeHandling: A boolean indicating whether to handle time-related information.
- ImportGPTKnowledge: A boolean indicating whether GPT knowledge should be imported.
- atomCreationThreshold: The threshold value for creating a new atom.

**Code Description**:
The Memory_inject_commands function takes a list of commands and processes each command one by one. It starts by initializing a set called AlreadyExecuted to keep track of the commands that have already been executed.

Next, it iterates over the commands using a for loop. For each command, it performs several checks and operations. If the length of the command is less than 3, it skips the current iteration. If the command starts with a dot (".") followed by a space, it removes the dot and space from the command. If the command contains a "#" character, it removes everything after the "#" character. If the command is already in the AlreadyExecuted set or contains certain keywords ("hasproperty none", "isa none", "none hasproperty", "none isa"), it skips the current iteration.

If the command passes all the checks, it adds the command to the AlreadyExecuted set. It then checks if the command is a system question or a user question based on its prefix. If PrintAnswer is enabled, it prints the command.

The function also checks if the command is a negated relation claim or negated property claim. If it is, it sets the isNegated flag to True, removes the prefix, and updates the truth value accordingly.

Next, the function checks if the command is a relation claim or property claim. If it is, it removes the prefix.

The function then checks if the command is an input command (relation claim or property claim) and if it contains a closing parenthesis. If both conditions are met, it extracts the sentence from the command, removes any quotes or periods, and converts it to lowercase. It then calls the Memory_digest_sentence function to process the sentence and update the memory. The function also checks if the sentence was successfully processed and, if PrintAnswer is enabled, prints the processed sentence.

After processing all the commands, the function checks if userQuestion is True and QuestionPriming is enabled. If both conditions are met, it calls the Memory_QuestionPriming function to prime the memory with the commands.

Finally, the function returns the current time.

**Note**: 
- The Memory_inject_commands function relies on the Memory_digest_sentence and Memory_QuestionPriming functions to process the commands and update the memory. It is important to ensure that these functions are implemented and accessible within the scope of the Memory_inject_commands function.
- The Memory_inject_commands function assumes that the AlreadyExecuted set, RET_DICT, inp, buf, currentTime, memory, atoms, cmd, userQuestion, userGoal, PrintAnswer, PrintMemoryUpdates, PrintTruthValues, QuestionPriming, TimeHandling, ImportGPTKnowledge, and atomCreationThreshold parameters are defined and accessible within the scope of the function.
- The Memory_inject_commands function assumes that the Memory_digest_sentence and Memory_QuestionPriming functions are compatible with the specified input parameters and return the expected results.
- The Memory_inject_commands function assumes that the RET_DICT, memory, and atoms dictionaries are initialized and accessible within the scope of the function.
- The Memory_inject_commands function assumes that the PrintAnswer, PrintMemoryUpdates, PrintTruthValues, QuestionPriming, TimeHandling, and ImportGPTKnowledge flags are boolean values indicating whether to perform the corresponding actions.
- The Memory_inject_commands function assumes that the atomCreationThreshold parameter is a threshold value for creating a new atom.

**Output Example**: If the commands are successfully processed and the PrintAnswer flag is enabled, the Memory_inject_commands function will print the processed sentences.

