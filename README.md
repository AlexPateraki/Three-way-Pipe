# Three-way-Pipe
Three-way pipes are pipes where there is a parent process that receives (in our case, reads from a tuple) messages as input and pipes them to its two children. In this case, the parent process is on the write end of the pipe, and its two children are on the read end of the pipe. Whatever the parent process writes as the contents of the tuple (one element of the tuple at a time), is transferred intact to each of its children (meaning both children read exactly the same content).
![image](https://github.com/AlexPateraki/Three-way-Pipe/assets/25749228/b4958223-c40e-4ef8-a915-4c6ce03956ae)
Proper exception handling is performed in the program, and file descriptors are opened and closed at appropriate points in the code. The parent process will print on the screen the elements it reads from a tuple and will write to one end of the pipe. The children will print the messages they read from the pipe. In your program, corresponding lines should be printed, similar to what is shown in the above description for parent and children.

Help: See the `dup2` function (https://docs.python.org/3/library/os.html)

Restrictions: Your implementation is allowed to import only the `os` and `sys` modules. No other modules are allowed.

