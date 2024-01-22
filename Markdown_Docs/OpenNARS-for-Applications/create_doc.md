## _function AddOutput(line)
**AddOutput**: The function of AddOutput is to append a line to the existing lines.

**parameters**:
- line: A string representing the line to be appended.

**Code Description**:
The AddOutput function is a simple utility function that appends a line to the existing lines. It takes a single parameter, "line", which is a string representing the line to be appended. The function appends the line to the "lines" list.

This function is called by the "Module" function in the "create_doc.py" file. The "Module" function is responsible for creating a new module and adding it to the "modules" list. After adding the module, the "Module" function calls the AddOutput function to append a line to the "lines" list. The line that is appended contains HTML tags for a horizontal rule ("<hr/>") and a heading ("<h1>") with the module name.

**Note**:
- The AddOutput function assumes that the "lines" list is already defined and accessible within the scope of the function.
## _function Module(name)
**Module**: The function of Module is to create a new module and add it to the "modules" list. It also appends a line to the existing lines.

**parameters**:
- name: A string representing the name of the module.

**Code Description**:
The Module function is responsible for creating a new module and adding it to the "modules" list. It takes a single parameter, "name", which is a string representing the name of the module. 

Within the function, the "name" parameter is appended to the "modules" list using the "append" method. This ensures that the newly created module is added to the list of existing modules.

After adding the module to the "modules" list, the function calls the AddOutput function. This function is defined in the "create_doc.py" file and is responsible for appending a line to the existing lines. The line that is appended contains HTML tags for a horizontal rule ("<hr/>") and a heading ("<h1>") with the module name. This helps in visually separating and identifying the newly created module in the output.

**Note**:
- The "modules" list is assumed to be defined and accessible within the scope of the function.
- The AddOutput function is assumed to be defined and accessible within the scope of the function.
- The AddOutput function assumes that the "lines" list is already defined and accessible within the scope of the function.
