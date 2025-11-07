# Version Control Course

Source: Version Control: https://www.coursera.org/learn/introduction-to-version-control?specialization=meta-full-stack-developer

## Module2: Command Line (1-19)

### 1. The Command Line (video)

Graphical User Interfaces (GUIs): a system for interacting with electronic devices using visual elements like icons, buttons, and menus instead of text-based commands. They offer an easy way to interact with devices, but they limit the scope of human-computer interaction. 

Command line: its an alternative of GUI. It allows to perform tasks, such as creating directories, files, copying, moving files, performing advanced searches, writing scripts to automate processes, start and stop programs, etc... Usage is limitless. 

```
cd ~/Desktop        - change directory
touch example.txt   - create a new empty file
mkdir html          - make directory with the name of html
history             - to view the history of the most recently typed commands
code example.js     - it will open the file in VSCode
```

### 2. What are Unix commands? (video)
You interact with your phone and computer through a graphical user interface, which is just a layer above underlying commands that tells the device what to do. Example: creating new folder on your Desktop - you right click with the mouse and push the 'Creating new folder' button. The same in command line: you have to navigate to the Desktop folder and type command to create the folder. 

**Unix commands** are simply a layer below the normal actions. 
Each Unix command has a set of helper instructions, which give detailed information about how the commands can run and which 'flags' can be passed to that command.

```
man         - manual, it's a  helper command, it will display a detailed manual instructions of that given command. 

man ls      - detailed manual of instructions of list command 
ls          - list the contents of the current working directory 
ls -l       - '-l' is a flag, it gives a detailed list of content of the current directory (gives an ordered list, shows the read and write permissions and owners)
ls -a       - list all files, even the hidden ones 
pwd         - present working directory, shows the full path of the current directory 
cp          - copy, copies files or folders from one destination to another 
mv          - move files from one directory to another
```

### 3. Using Bash on Mac Terminal (reading)

Opening Terminal in Mac: 
1. Finder: Finder --> Applications --> Utilities --> Terminal 
2. Launch Pad - Press F4
3. Spotlight Search - Press Command + Space 

![alt text](img/bash_commands.png)


#### <ins>Editing files: </ins>

**VI or VIM**. <br>
VI stands for Visual Editor. <br>
VIM is better version of VI - Visual Editor iMproved<br>
When you open a file, you can navigate through text, search words, delete or copy lines, etc. 

```
h, j, k, l          - Move left, down, up and right
/searc_term         - search for a word or phrase
:w                  - save the file
:q                  - quit the editor
```

- Insert mode: Allows the contents of the files to be edited directly. It can be entered by pressing i (insert), a (append), or o (open new line).

- Command line mode:  It can be entered by typing colon : in Normal mode. 

### Using Bash on Windows
Let's create a simple script and make it executable!
- Open Terminal
- Navigate to the home directory and check the files
```
cd ~
ls -la
```

- create a new file and open it:
```
vim testshell.sh
```
- press 'i' for insert mode and type:
```
#!/bin/bash
```
- this lets the operating system know that this is a bash script 
```
echo "Hello World!"
```
- press 'escape' from get out insert mode, than press ':wq', which saves and quit the file. 

```
-rw-r--r--   1 anettkeszler  staff     32 Nov  7 13:20 testshell.sh
```
This file can't be run at the moment, it's not executable, it's just a read-write file. To be able to run the file, you can make it executable by adding the proper permission. 
```
chmod 755 testshell.sh
```
```
-rwxr-xr-x   1 anettkeszler  staff     32 Nov  7 13:20 testshell.sh
```
Now I can run the file from the command line. 
```
./testshell.sh
Hello World!
```

### 5. Checking the Working Directory (lab)

### 6. Change directories and list contents (video)
Practice pwd, ls, la -l, ls -la, cd, cd .., cd /  to navigate in the file system.

### 7. Creating and moving directories and files (video)
- Create a new directory and working with it 
```
mkdir test
cd test
touch test1.txt
touch test2.txt

cd .. 

mkdir test2
```

- Let's move the test folder into the test2 folder 
```
mv test test2
```
- Now the test folder (and all of its files) are moved into the test2 folder

### 8. Creating and navigating directories and files (dialogue)

- Rename a file and move it to another directory in one command: 
```
mv notes.txt ~/Markdown/notes.md
``` 
- Here I renamed the notes.txt files to notes.md and moved it to the Markdown folder. 