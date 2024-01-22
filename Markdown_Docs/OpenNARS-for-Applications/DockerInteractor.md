## _class DockerInteractor
**DockerInteractor**: The function of DockerInteractor is to interact with a Docker container by executing commands and receiving output from the container.

**attributes**:
- process: A subprocess object representing the Docker container process.
- stdout_queue: A queue to store the standard output from the container.
- stderr_queue: A queue to store the standard error from the container.

**Code Description**: The DockerInteractor class provides methods to send commands to a Docker container and receive the output from it. 

The class constructor initializes the process attribute by creating a subprocess using the provided command. The subprocess is configured to redirect the standard input, standard output, and standard error to pipes. The bufsize parameter is set to 1 to enable line buffering, and universal_newlines is set to True to ensure that the input and output are treated as text.

Two reader threads are started to read the output from the container. The reader method is a static method that reads lines from a given stream and puts them into the specified queue.

The send method writes a message to the standard input of the container and flushes the input stream.

The recv method retrieves the next line of output from the container's standard output queue. It can optionally accept a timeout parameter to wait for a specified amount of time for the output to become available.

The recv_err method retrieves the next line of output from the container's standard error queue. It also accepts an optional timeout parameter.

The execute_command method sends a command to the container and receives the output until a specified delimiter is seen. It uses the send method to send the command and then reads lines from the container's standard output queue until either the delimiter is found or there is no more output. The output is accumulated in a string and returned after removing the delimiter.

The shutdown method closes the standard input stream of the container, terminates the container process, and waits for the process to terminate.

**Note**: 
- The DockerInteractor class requires the subprocess and queue modules to be imported.
- The send, recv, and recv_err methods are non-blocking, meaning they will return immediately even if there is no output available. It is the responsibility of the caller to handle the case where no output is received.
- The execute_command method is blocking and will not return until the specified delimiter is seen or there is no more output from the container.

**Output Example**:
```python
interactor = DockerInteractor("docker exec -it my_container")
interactor.send("ls")
output = interactor.recv()
print(output)
```
Output:
```
file1.txt
file2.txt
```
### _class_function __init__(self, command)
**__init__**: The function of __init__ is to initialize an instance of the DockerInteractor class.

**parameters**:
- command: The command to be executed as a subprocess.

**Code Description**:
The `__init__` function is the constructor of the DockerInteractor class. It takes a command as a parameter and initializes the instance by creating a subprocess using the `subprocess.Popen` function. The subprocess is executed with the specified command.

The `subprocess.Popen` function creates a new process and returns a Popen object that represents the process. The Popen object has attributes and methods that allow interaction with the process. In this case, the Popen object is assigned to the `self.process` attribute of the DockerInteractor instance.

The `subprocess.Popen` function takes several arguments:
- `command`: The command to be executed as a subprocess. This can be a string or a sequence of strings.
- `stdin`: The input stream for the subprocess. In this case, it is set to `subprocess.PIPE`, which means that the subprocess will receive input from the parent process through a pipe.
- `stdout`: The output stream for the subprocess. It is set to `subprocess.PIPE`, which means that the subprocess output will be captured and made available for reading.
- `stderr`: The error stream for the subprocess. It is set to `subprocess.PIPE`, which means that the subprocess error output will be captured and made available for reading.
- `bufsize`: The buffer size for the input and output streams. It is set to 1, which means that the streams will be line-buffered.
- `universal_newlines`: This parameter is set to True, which means that the input and output streams will be opened in text mode and use universal newlines.

After creating the subprocess, the `__init__` function initializes two queue objects, `stdout_queue` and `stderr_queue`, using the `queue.Queue` class. These queues will be used to store the lines read from the stdout and stderr streams of the subprocess.

The function then starts two reader threads using the `threading.Thread` class. The `reader` function is used as the target function for both threads. The first thread reads lines from the stdout stream of the subprocess and puts them into the `stdout_queue`, while the second thread reads lines from the stderr stream of the subprocess and puts them into the `stderr_queue`. The `reader` function is called with the respective streams and queues as arguments.

The `reader` function is responsible for reading lines from a stream and putting them into a queue. It uses a `for` loop with the `iter` function to iterate over the lines of the stream until an empty line is encountered. This ensures that the function continues reading lines until the stream is closed or no more lines are available. After all the lines have been read, the stream is closed using the `close` method.

In the context of the project, the `__init__` function is called when an instance of the DockerInteractor class is created. It sets up the subprocess and the reader threads for capturing the output and error streams of the subprocess. This allows the DockerInteractor instance to interact with the subprocess and retrieve its output and error messages.

**Note**: It is important to ensure that the command passed to the `__init__` function is a valid command that can be executed as a subprocess. Additionally, the queues (`stdout_queue` and `stderr_queue`) should be thread-safe if used in a multi-threaded environment to avoid potential race conditions.
### _class_function reader(stream, queue)
**reader**: The function of reader is to read lines from a stream and put them into a queue.
**parameters**:
- stream: The input stream from which the lines will be read.
- queue: The queue where the lines will be put.

**Code Description**: 
The `reader` function takes in a stream and a queue as parameters. It reads lines from the stream using the `readline` method and puts them into the queue using the `put` method. The function uses a `for` loop with the `iter` function to iterate over the lines of the stream until an empty line is encountered. This ensures that the function continues reading lines until the stream is closed or no more lines are available. After all the lines have been read, the stream is closed using the `close` method.

This function is typically used in a multi-threaded or multi-process environment where one thread or process is responsible for reading lines from a stream and another thread or process is responsible for processing those lines. By using a queue, the lines can be efficiently passed from the reader to the processor without the need for explicit synchronization between the threads or processes.

In the context of the project, the `reader` function is called by the `__init__` method of the `DockerInteractor` class. The `__init__` method creates a subprocess using the `subprocess.Popen` function and initializes two queues (`stdout_queue` and `stderr_queue`) for capturing the output and error streams of the subprocess. It then starts two reader threads, one for reading lines from the stdout stream of the subprocess and putting them into the `stdout_queue`, and another for reading lines from the stderr stream of the subprocess and putting them into the `stderr_queue`. The `reader` function is used as the target function for both reader threads, with the respective streams and queues passed as arguments.

**Note**: It is important to ensure that the stream passed to the `reader` function is properly opened and accessible. Additionally, the queue passed to the function should be thread-safe if used in a multi-threaded environment to avoid potential race conditions.
### _class_function send(self, message)
**send**: The function of send is to send a message to the process.

**parameters**:
- message: The message to be sent to the process.

**Code Description**:
The `send` function is responsible for sending a message to the process. It takes a single parameter, `message`, which represents the message to be sent.

Inside the function, the `write` method of the `stdin` attribute of the `self.process` object is called to write the message to the input stream of the process. The message is appended with a newline character ('\n') to ensure proper formatting. The `flush` method is then called to ensure that the message is immediately sent to the process.

**Note**:
- It is important to note that the `self.process` object must be initialized and running before calling the `send` function.
- The `send` function does not return any value.
### _class_function recv(self, timeout)
**recv**: The function of recv is to receive data from the stdout_queue.

**parameters**:
- timeout (optional): The maximum time to wait for data to be received from the stdout_queue. If no data is received within the specified timeout, None is returned.

**Code Description**:
The recv function is used to retrieve data from the stdout_queue. It first attempts to get data from the queue using the get method with the specified timeout. If data is available within the timeout period, it is returned. If the queue is empty or no data is received within the specified timeout, None is returned.

This function is called by the execute_command method in the DockerInteractor class. The execute_command method sends a command and then waits for the output until a delimiter is seen. It calls the recv function repeatedly with a timeout of 1 second to receive the output line by line. Each received line is appended to the output string. The loop continues until either no more data is received or the delimiter is found in the received line. Finally, the output string is returned after replacing the delimiter with an empty string.

**Note**:
- The recv function relies on the stdout_queue attribute, which should be populated with data before calling this function.
- The timeout parameter can be used to control the maximum waiting time for data to be received. If not specified, the function will wait indefinitely until data is available.

**Output Example**:
If data is available in the stdout_queue, the recv function will return the received data as a string. For example, if the stdout_queue contains the string "Hello, World!", calling recv() will return "Hello, World!".

If the stdout_queue is empty or no data is received within the specified timeout, the recv function will return None.
### _class_function recv_err(self, timeout)
**recv_err**: The function of recv_err is to receive an error message from the stderr_queue.

**parameters**:
- timeout: An optional parameter that specifies the maximum time to wait for an error message. If not provided, the function will wait indefinitely until an error message is received.

**Code Description**:
The recv_err function is used to retrieve an error message from the stderr_queue. The function first attempts to get an error message from the queue using the get() method with the specified timeout value. If an error message is available within the specified timeout, it is returned. If the timeout expires before an error message is received, the function returns None.

**Note**:
- This function assumes that the stderr_queue is a valid queue object that has been properly initialized.
- If the timeout parameter is not provided, the function will wait indefinitely until an error message is received. It is important to handle this case appropriately to avoid potential blocking issues.

**Output Example**:
If an error message is available in the stderr_queue, the function will return the error message as a string. For example, if the stderr_queue contains the error message "File not found", the function will return the string "File not found". If the stderr_queue is empty or the timeout expires before an error message is received, the function will return None.
### _class_function execute_command(self, command, delimiter)
**execute_command**: The function of execute_command is to send a command to a process and receive the output until a specified delimiter is seen.

**parameters**:
- command: The command to be sent to the process.
- delimiter: The delimiter used to determine when to stop receiving the output.

**Code Description**:
The `execute_command` function is responsible for sending a command to a process and receiving the output until a specified delimiter is seen. It takes two parameters: `command`, which represents the command to be sent, and `delimiter`, which is the string used to determine when to stop receiving the output.

Inside the function, the `send` method of the `self` object is called to send the command to the process. This method is implemented in the `send` function of the `DockerInteractor` class. The `send` function writes the command to the input stream of the process.

After sending the command, the function enters a loop to receive the output from the process. The `recv` method of the `self` object is called repeatedly with a timeout of 1 second to receive the output line by line. This method is implemented in the `recv` function of the `DockerInteractor` class. The received line is appended to the `output` string.

The loop continues until either no more data is received or the delimiter is found in the received line. If no data is received within the timeout period, the `recv` method returns `None`. If the delimiter is found in the received line, the loop is terminated.

Finally, the function returns the `output` string after replacing the delimiter with an empty string.

**Note**:
- It is important to note that the `self` object must be an instance of the `DockerInteractor` class and the `self.process` object must be initialized and running before calling the `execute_command` function.
- The `execute_command` function assumes that the `send` and `recv` methods of the `self` object are implemented correctly and that the `recv` method returns `None` when no data is received within the specified timeout.
- The `execute_command` function does not handle any exceptions that may occur during the execution of the `send` and `recv` methods. It is recommended to handle exceptions appropriately when using this function.

**Output Example**:
If the output received from the process is "Hello, World!\n", and the delimiter is set to "\n", calling `execute_command("echo Hello, World!", "\n")` will return "Hello, World!".
### _class_function shutdown(self)
**shutdown**: The function of shutdown is to close the stdin stream, terminate the process, and wait for the process to terminate in order to free system resources.

**parameters**:
- None

**Code Description**:
The `shutdown` function is responsible for shutting down the Docker interactor. It performs the following steps:

1. Close the stdin stream: The function first checks if the `stdin` stream of the process is open. If it is, it closes the stream using the `close()` method. This ensures that no further input can be sent to the process.

2. Terminate the process: Next, the function calls the `terminate()` method on the process object. This sends a termination signal to the process, indicating that it should be stopped. The process may not immediately terminate after this signal is sent.

3. Wait for the process to terminate: After terminating the process, the function calls the `wait()` method on the process object. This blocks the execution of the program until the process has completely terminated. This step is important to ensure that all system resources associated with the process are freed.

**Note**:
- It is important to call the `shutdown` function when you are finished using the Docker interactor, in order to properly close the process and free system resources.
- If the `stdin` stream is not closed before terminating the process, it may result in unexpected behavior or resource leaks.
- The `wait()` method is necessary to ensure that the process has completely terminated before continuing with other operations.
