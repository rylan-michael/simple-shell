# Simple Shell

The goal for this exercise is to create a simple shell in python that runs select OS processes.
Write a program that implements a simple shell. The shell takes a use command as input and executes the command. When the shell is started, it should take a use command as input, execute it and display the output. The following example shows an execution of the shell. It displays the command prompt 'uofmsh' and takes the use command 'ls' as input from STDIN. It then executes the command 'ls' and prints the output to STDOUT. Basically, your shell launches a program and coordinates the input and output of the program.

* Implement command parsing in your shell. You do not need to write a full parser in yacc/lex to parse commands. Using plain string funcitons such as strok (for C/C++) should suffice. Once a command is parsed, the parsed command should be executed.
* Built-in command **exit**: Your shell should terminate when the exit command is parsed and executed in your shell.
* Built-in command **stat**: Your shell should display the history of commands received from the user along with the system time when it was input by the user. EX: 11:34 exit
* Your shell should execute a program specified by the user input. To execute a program, a new process should be forked and its memory space should be replaced by the user specific program. Test you shell with programs with different numbers of arguments. System call programs.
* Add support for changing the working directory. Implement the command **cd** in your shell using the **chdir(2)** system call. More information available [here](http://man7.org/linux/man-pages/man2/chdir.2.html)
* Make sure that **‘cd -‘** should change the directory to the last directory that the user was in, and **‘cd’** with no arguments should change the directory to the user home directory. Also make sure to implement **‘cd .’** that leaves you in the current directory and **‘cd ..’** that moves up one directory.
* Verify that the cd command works correctly by using the ‘pwd’command which displays the currentworking directory.
* Display the current working directory in your shell prompt. For example \tmp\homework1> pwd.

* Redirection is one of the most powerful features of Linux/UNIX systems. Special characters (i.e., ‘<’, ’>’ ,’|’) are used to accomplish redirection. Read more information about the redirection [here](https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection).
* Review the following system calls related to file management: [open()](http://man7.org/linux/man-pages/man2/open.2.html), [close()](http://man7.org/linux/man-pages/man2/close.2.html), [read()](http://man7.org/linux/man-pages/man2/read.2.html), [write()](http://man7.org/linux/man-pages/man2/write.2.html), [dup()/dup2()](http://man7.org/linux/man-pages/man2/dup.2.html).
* To implement support for redirection, you should modify your parsing code such that these three special characters are identified and shell-level directives are individually parsed, rather than passing the entire command to **exec()**. For example, given a command ‘ls > file’, your shell 
should parse this command into ‘ls’, ‘>’, and ‘newfile’. The output of ‘ls’ will be saved in a file ‘newfile’. If the file ‘newfile’ does not exist, your shell will create this file using a system call.
