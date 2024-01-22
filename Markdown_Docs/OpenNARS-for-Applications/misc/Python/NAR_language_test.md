## _function Test1
**Test1**: The function of Test1 is to perform a series of actions and tests in the OpenNARS-for-Applications project.

**parameters**: None

**Code Description**:
The Test1 function is a key component in the OpenNARS-for-Applications project. It performs a series of actions and tests to demonstrate the functionality of the project. 

The function starts by printing the message "//Test1:" to indicate the start of the Test1 function.

Next, it calls the TrainStart function to initiate the training process. This function sets the global variable "Training" to True and prints the message "//Training Start" to indicate that the training process has begun.

The Test1 function then proceeds to call the processInput function multiple times with different input strings. The processInput function is responsible for processing user input and performing various actions based on the input type. The specific behavior and usage of the processInput function may vary depending on the calling object and the input parameters provided.

After processing the input strings, the Test1 function calls the TrainEnd function to mark the end of the training process. This function sets the global variable "Training" to False and prints the message "//Training End" to indicate that the training process has ended.

Finally, the Test1 function performs a series of queries using the Query function. The Query function is used to perform a query matching operation on a given term. It searches the memory for the best matching term based on the given parts and returns the result. The specific behavior and usage of the Query function may vary depending on the input term and the isRelation parameter.

The Test1 function prints the results of the queries using the print() function. The output examples provided in the code comments demonstrate the expected output of the queries.

From a functional perspective, the Test1 function serves as a test case for the OpenNARS-for-Applications project. It demonstrates the usage of various functions and their interactions to perform actions and retrieve information from the memory.

**Note**: 
- The Test1 function does not take any parameters.
- The TrainStart, processInput, TrainEnd, and Query functions are assumed to be defined and accessible from within the Test1 function.
- The specific behavior and output of the Test1 function may vary depending on the content of the memory and the implementation of the project.
- The Test1 function can be modified or extended to include additional actions or tests as needed for the project.
## _function Test2
**Test2**: The function of Test2 is to execute a series of predefined actions and perform queries on the memory.

**parameters**:
- None

**Code Description**:
The Test2 function is a high-level function that executes a series of predefined actions and performs queries on the memory. It serves as a test case for the OpenNARS-for-Applications project.

The function starts by printing the message "//Test2:" to indicate the start of the Test2 function.

Next, it calls the TrainStart function to initiate the training process.

The function then proceeds to execute a series of processInput function calls with predefined input strings. These input strings represent various actions and statements that are processed by the NAR_language module.

After executing the processInput function calls, the function calls the TrainEnd function to mark the end of the training process.

Following the training phase, the function performs three queries on the memory using the Query function. Each query is constructed as a string and passed as an argument to the Query function. The results of the queries are printed using the print() function.

Finally, the function calls the processInput function twice with additional input strings.

From a functional perspective, the Test2 function serves as a test case for the NAR_language module. It demonstrates the usage of the TrainStart, TrainEnd, processInput, and Query functions. By executing a series of predefined actions and queries, the Test2 function verifies the functionality and correctness of the NAR_language module.

**Note**: 
- The Test2 function does not take any parameters.
- It is important to call the TrainStart function before executing any training-related tasks to ensure that the training process is properly initialized.
- The processInput function is responsible for processing user input and performing various actions based on the input type.
- The Query function is used to perform a query matching operation on a given term and retrieve relevant information from the memory.
