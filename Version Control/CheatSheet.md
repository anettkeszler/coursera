# Version Control Chaet Sheet 

## Software Collaboration

**Version Control:** is a system for tracking and managing changes to files over time, commonly used in software development to record every modification to source code. It allows teams to collaborate efficiently, revert to previous versions if errors occur, and compare changes, ensuring code integrity and project history is maintained. 

Primary goal is to keep track of changes. <br>
VCS allows developers access to the entire change history with the ability to revert or roll back to a previous state.

**Why is version control so important?**<br>
Version control (or source control or revision control) serves as a safety net to protect the source code from irreparable harm, giving the development team the freedom to experiment without fear of causing damage or creating code conflicts.

Benefits of using VC: 
- revision history: it provides a record of all changes in a project, it has the ability to revert to a stable point in time in case of issues or bugs.So the team can work faster and deliver code with more confident. 
- identity: All changes were made with the identity of the user
- collaboration: a developer works with many people on the same project, everyone can submit their own code and review other's code (peer review) to provide feedback
- automation
- efficiency

**Version Control Systems** are sowtware tools, like Git, that automate this process by creating snapshots of files in a central repository. 

**Effective using of Version Control** leads to better team collaborating because it helps you understand why certain changes were made if you look at commits. Also helps you context switch between different features or projects that you're working on. Effective collaboration led to a better outcome on the recent project.

### Types of Version Control Systems:

**Centralized VCSs (CVCS):**  Contains a central server where the complete project history is stored and clients as users. Developers must connect to this server to access and update the code.

Pros: 
- easier to learn
- give more access control to user

Cons:
- slower (needs to estabilish a connection to the server to perform any actions)

**Distributed Version Control System (DVCS)**: similar to CVCS, you still need to pull code down from the server to view the latest changes. The key difference is that every user is essentially a server and not a client. This means that every time you pull down code from the distributed model, you have the entire history of changes on your local system. <br>
Each developer has a full copy of the project history on their local machine, enabling offline work and faster operations.

Pros:
- it allows users to work in an offline state (you don't need to be connected to the server to add your changes or view a file's history, users can work in an offline state, you only have to connect to server when you pull down or push back the changes)
- speed and performance is better 
- better software developement life cycle

**Version Control Systems examples:**
- Git (D)
- Mercurial (D)

- Subversion
- Perforce
- AWS Code Commit


### Version control in professional software development 
- Version Control plays a crucial part in software development. 
- Developers work together to deliver software to customers. 
- VC must be completed by other tools and procedures to ensure quality and efficiency throughout the process. 
- **Common tools and startegies to complete VC**: 
    - **Workflow**:     
        - a good workflow is a must, to **avoid/resolve merge conflicts** (when developers work on the same files). 
        - **Peer reviews** - another developer review the code before it is merged

     - **Continuos Integration (CI)**: is used to automate the integration of code changes from multiple developers into a single main stream. Small changes are merged frequently will reduce the number of merge conflicts. This process is widespread in test-driven software development strategies. CI is used to automatically compile the project and run tests on every code change to ensure that the build remain stable. 

     - **Continous Delivery (CD)**: is build on top of CI. When changes are merged into the main codebase, a Continous Delivery pipeline automates the process of preparing the application for deployment. This process includes tasks like building the apllication, running tests, preparing it for deployment to production-like environment. The main goal of Continuous Delivery is to ensure that the application is always in a deployable state. Continuous Delivery requires manual approval to release the application to the production environment. Although this gives teams greater control over when and how changes are deployed to live systems, Continuous Delivery is slower than Continuous Deployment because of this manual step.

     - **Continuos Deployment**: Continuous Deployment takes Continuous Delivery a step further by automating the actual deployment of the application to production. <br>
    With this practice, every change that passes through automated tests and validations in the pipeline is automatically deployed to production without the need for manual intervention. Unlike Continuous Delivery, Continuous Deployment eliminates the manual approval step, making it faster and more efficient. This approach ensures that updates, features, and fixes are delivered to customers as soon as they are ready, fostering rapid and iterative delivery. 

    - The Continuous Delivery steps ensure the code is production-ready after passing all tests and reviews. The Continuous Deployment then automates the final step of deploying production-ready code without manual intervention. Using them together in a production environment provides an additional safety layer but also increases the time required.

Continuous Integration is used to automatically integrate code changes.<br> 
Continuous Delivery automatically packages the application and prepares it for deployment.<br>
Continuous Deployment helps to deploy the application to customers frequently.

### Revision History:
Revision History is a record of all changes within a project. It allows you to pinpoint who made the changes, when they were made and what was changed. 

The revision history will record the essential data points so any developer or team member can walk through the entire project from start to its current state.

Managing merge conflicts:<br>
After commit, the developer will push their changes to the repository and create a pull request. Other developers will then peer review the pull request to approve the changes or decline.
When working on a single project, there's usually some level of crossover between the developers. When this does occur, the history of revisions can help aid the developers in seeing the full life cycle of changes that have occurred. It is also essential for merging conflicts where multiple developers have made changes that may need to be resolved prior to the code being approved. The history will show who made the change, for what reason, the code itself and its changes, and the date and time of when they occurred. 

### Staging vs. Production

**Deployment environments**: before a team release their new feature or changes, they need to verify that the code is not going to cause any issues or bugs. So they set up multiple environments for testing and verifying. (UAT, QA and staging environments). The more ways to test the changes the less likely bugs will be introduced.

**Staging:** this should mimic the production environment. This allows teams to find any potential issues prior going production. 
Areas that benefit from staging environments:
- New features: developers submitting new features with feature flags for turning them on and off in staging environment. The team can verify that the feature works as expected and does not break other functionalities. 
- Testing:  staging mimics the production, so testing is a must at this point. QA teams will apply Unit testing, Integration tests and Performance test. 
- Migrations: Snapshots can be taken from production and used to test your migration scripts to confirm your changes will not break anything.
- Configuration changes

**Production**: Production is live. It's out there for people to see. Any issues or problems should have been caught and fixed in the staging environments. 

- Downtime: if users can not access your website or app to its full capabilities, it will most likely have a cost involved
- Vulnerabilities: Cyber-security should also play a big role in what gets released in production.  Any updates to software such as patching or moving to the latest version should be checked and verified. This is also the same rule for not upgrading software when critical updates are released.
- Reputation: Downtime or issues in production is damaging for a company as it does not instill confidence in end users. If something is down or broken it can cause the company to lose potential customers.

## Command Line

**Graphical User Interfaces (GUIs)**: a system for interacting with electronic devices using visual elements like icons, buttons, and menus instead of text-based commands. They offer an easy way to interact with devices, but they limit the scope of human-computer interaction.
You interact with your phone and computer through a graphical user interface, which is just a layer above underlying commands that tells the device what to do.

**Command line**: its an alternative of GUI. It allows to perform tasks, such as creating directories, files, copying, moving files, performing advanced searches, writing scripts to automate processes, start and stop programs, etc... Usage is limitless.

**Unix commands** are simply a layer below the normal actions. 
Each Unix command has a set of helper instructions, which give detailed information about how the commands can run and which 'flags' can be passed to that command.

```
cd ~/Desktop        - change directory to (~)Home/Desktop
touch example.txt   - create a new empty file or to update a timestamp on a file
mkdir html          - make directory with the name of html
history             - to view the history of the most recently typed commands
code example.js     - it will open the file in VSCode

man                 - manual, it's a  helper command, it will display a detailed manual instructions of that given command. 

man ls              - detailed manual of instructions of list command 
ls                  - list the contents of the current working directory 
ls -l               - '-l' is a flag, it gives a detailed list of content of the current directory (gives an ordered list, shows the read and write permissions and owners)
ls -a               - list all files, even the hidden ones 
pwd                 - present working directory, shows the full path of the current directory 
cp                  - copy, copies files or folders from one destination to another 
mv                  - move files from one directory to another
rm                  - remove a file or directory
cat                 - Allows reading or concatenation of a file
less                - Displays the contents of a file one page at a time
grep                - Global regular expression, allows for searching contents of files or folders
```

#### Editing files: 
**VI or VIM**. <br>
**VI** stands for **Visual Editor**. <br>
**VIM** is better version of VI - **Visual Editor iMproved**<br>
When you open a file, you can navigate through text, search words, delete or copy lines, etc. 

```
h, j, k, l          - Move left, down, up and right
/search_term        - search for a word or phrase
:w                  - save the file
:q                  - quit the editor
:wq                 - save and quit the file
```

- Insert mode: Allows the contents of the files to be edited directly. It can be entered by pressing i (insert), a (append), or o (open new line).

- Command line mode:  It can be entered by typing colon : in Normal mode.


### Using Bash in practice

#### Let's create a simple script and make it executable!
```
cd ~
ls -la
vim testshell.sh

insert this: 

#!/bin/bash                   - this lets the operating system know that this is a bash script 
echo "Hello World!"
```
- press 'escape' from get out insert mode, than press ':wq', which saves and quit the file. 
```
ls -la                       -rw-r--r--   1 anettkeszler  staff     32 Nov  7 13:20 testshell.sh
```
This file can't be run at the moment, it's not executable, it's just a read-write file. To be able to run the file, you can make it executable by adding the proper permission. 
```
chmod 755 testshell.sh      -rwxr-xr-x   1 anettkeszler  staff     32 Nov  7 13:20 testshell.sh
```
Now I can run the file from the command line. 
```
./testshell.sh
Hello World!
```

#### Rename a file and move it to another directory in one command: 
```
mv notes.txt ~/Markdown/notes.md
``` 
- Here I renamed the notes.txt files to notes.md and moved it to the Markdown folder. 

#### Check the file content :
```
cat file.txt                - this returns the content of the file
```

#### Count the number of words in a file: 
```
wc file.txt -w              - '-w' flag tells the wc command to return the word count
```
#### Using Piepes:
- Pipes are used to pass the output of one command as input to another command. 
```
ls | wc -w                  output: 2 (there is 2 file in the directory )
cat file.txt | wc -w        output: 181 (there is 181 words in the file1.txt file)
cat file1 file2 | wc -w     output: 362 (there is 362 words in the file1 and file2. 
```

#### Grep - global regular expression print 
- It's used for searching across files and folders as well as the contents of files.
```
grep Sam names.txt          - It searches all of the names starting with 'Sam' in names.txt file.
grep sam names.txt          - It will return a totally different list (grep is case sensitive)

grep -i Sam names.txt       - To ignore case sensitivity we pass in a flag '-i'

grep -w Sam names.txt       - '-w' does exact match, which means it'll match exactly what I'm looking for. Output: Sam 

```
- **Grep is case sensitive**
- '-i' flag ignores case sensitivity 

- Using pipe for combine searches:
```
ls /bin | grep zip 
```
First, I check all the executable files inside the bin directory, than I search for files containing 'zip' in their name. 

### Redirection 

The basic workflow of any Linux command is that it takes an input and gives an output. The standard input device(stdin) is the keyboard, the standard output device(stdout) is the screen. <br>
With redirection you can change the standard input and/or output. <br>
There are 3 types of IO (input/output) redirection:

**1. Standard Input:** - 0

**The standard input redirection gives you the option to record your input and save it to a file either by overwriting or appending the file.**<br>
Taking input usually refers to a user typing information from the keyboard. 
We use '<' sign for user input.
The cat command can be used to record user input and save it to a file. 
But how do we take input and store it in a .txt file? 
```
cat > input.txt
```
- write the input you want, press Enter, than ctr + d 
- to output the content of the file:
```
cat < input.txt         - to display the content of the file 
```

**2. Standard Output** - 1

**The redirection standard output allow you to control where the output goes.**<br>
Output direction is handled with a greater than sign (>). IO allows us to use redirection to control where the output goes. 
To send output to a text file
Every time you run a command like ls, and press Enter, it sends the output of the file to an stdout file. In Linux, if you want to control, where the output goes, you can use a redirection. 
```
ls -l > output.txt
```
We tell to display the result of the 'ls -l' command to the output.txt file (which has not been created yet, but it will be created)
```
less output.txt           - it displays the result of ls -l command 
```

**3. Standard Error** - 2

**The standard error redirect allows you to specify that the error should be written to a file.** <br>
Errors occur when things go wrong. When using redirection, you also have to specify that the error should be written to a file. 
```
ls -l /bin/usr 2> error.txt
less error.txt                  --> 'ls: /bin/usr: No such file or directory' is displayed in the error file
```

You can handle both output and error at once,
```
ls -l /bin/usr > error_output.txt 2>&1
```
```
< input.txt
> output.txt
2> error.txt
```

**Benefits of using the command line:**
- The Command Line Interface (CLI) uses less CPU and memory than a Graphical User Interface (GUI)
- Most cloud providers provide command line access.
- Many tasks can be automated through the command line.


## Git and GitHub

**Git** is a version controle software which tracking changes, enabling collaboration through different versions, comparing changes, and enabling to revert to previous states. <br>
**Git** is a version control system for tracking changes of projects.<br>
Git allows us to revert our changes or go back to a previous version. <br>
Commit history acts like a detailed logbook, explaining what and why changes were made. 

**GitHub** is a platform to handeling projects with git
**GitHub** is a cloud-based hosting service that manages git repositories

A **git repository** is used to track all changes to files in a specific folder, and keep a history of all changes. 

### Connecting to GitHub via HTTPS
When you connect to a repository via HTTPS, its required to authenticate using a **Personal Access Token**. 
A Personal Access Token is a special password that you use instead of your actual account password. When you're finished using the token, you can revoke it so that it can no longer be used. It is also possible to set an expiry time for the token. This helps to keep your account secure.

- **Generate a Personal Access Token:** 
    - Profile --> Settings --> Developer Settings
    - Personal access tokens --> Tokens (classic) --> Generate new token (classic)
    - Set the Name and Expirations date 
    - Select scope: click 'repo' 
    - Generate token 
    - Make sure to copy and keep note of the token, as it will be hidden when you leave the pgae. 
    - This token noe can be used when connectiong to repository over HTTPS. 

### Connecting to GitHub via SSH: 
If you plan to use Github from your local device, the recommended way to authenticate is using Secure Shell, or SSH for short. This requires the creation of keys: a public and a private key. The advantage of using SSH is that you don't need to enter in your credentials when interacting with the remote repository. The keys are generated and stored on your local machine and then the public key is copied to the Github server. After you finish setting up, every operation will be authenticated using the keys.

- **Generate SSH keys**:
    - open Terminal, and type: ```ssh-keygen -t ed25519 -C "your@email.com"```
    - it will prompt to enter a password. Hit enter to skip setting a password and do the same for entering the same passphrase again.
    - the keys have been created and stored in the .ssh folder
    - In order to add our key to Github, we need to get a copy of the public key which is always identified as .pub in your local directory
    - then use the below command to copy the file, replacing the <YOUR KEY> with the name of the key file on your device.
    ```
    ls ~/.ssh/
    pbcopy < ~/.ssh/<YOUR KEY>.pub
    ```
- **Adding your keys to GitHub**: <br>
    We now need to add our public key to Github to grant access to the repositories we create:
    - Profile --> Settings --> SSH and GPG keys
    - Click on 'New SSH keys', add title and copy the key
    - You are now ready to access Github via SSH.


### Git workflow:

(When I clone the repository, and check the content of it, there is a '.git' folder. It is a hidden folder (ls -la) and used to track all of the changes. This folder is automatically created when you create a repository. It is initialized by running the 'git init' command. As the repository was created on GitHub, it is not required to run the 'git init'. GitHub handled all of this as part of its 'create new repo' flow.)

**Working directory / Modified**: adding, removing or updating files. Git knows the file has changed, but does not track it. 

**Staging area / Staged:** in order for Git to track a file, it needs to be put in the staged area (use **git add** to add files from untracked to tracked state)

**Committed**: committing a file in Git is a save point in many ways. Git will save the file, and have a snapshot of the current changes. (git commit -m "commit message")

**Remote repository**: we push our commits into the remote repository (on GitHub) (git push)

### Branches:

- Before creating a new branch, make sure that your branch is up to date with the 'origen/main', and nothing to commit, working tree clean 
```
git branch feature/lesson               - it will create the new branch 
git checkout -b feature/lesson          - it will create and checkout to this new branch

git branch                              - it shows all of my branches, and my current stay
```

- Use git push to push your changes from the local repository to the remote repo. 
```
git push -u origin feature/lesson
```

Once you are ready with your feature branch, changes need to be merged back to the main branch. --> You create a PR. 
When you create a **pull request** you are asking the other developers to review (**peer review**) your work and approve it to be merged to the repository.
Once PR is approved, you can merge the changes into main branch.

Having independent branches makes the project easier to manage.
This is cleaner than everyone working on the main branch, which could likely cause a lot of isses / merge conflicts.
Also there is no limit how many branches you can have. 

Once you pushed your changes from feature into main on GitHub UI, go back to your Terminal. 
```
git status                  - you are still on feature, chackout to main
git checkout main
git pull                    - you will recieve the latest changes from your main remote repository 
```

### Remote vs. Local

Remote repository where any developer can push their changes(GitHub). <br>
The remote code is accessed through a URI which is unique and only accessible to those who have permission.

Local refers to your machine which can be a laptop, desktop or mobile device, and it is only accessible to you.

One advantage is using git that you can work offline and commit your changes when you are ready. 
You need internet connection to push or pull the changes between local and remote. 

- Let's create a new local repository with git init:
```
mkdir my-first-repo
cd my-first-repo
git init                    - an empty git repository has been initialized
git remote                  - it comes back as blank 
```

- 'git remote' comes back blank, the reason for that is that I've only initialized a local repository which has no connection to a central repository yet. Right now it's only available locally on my machine. 

### Cloning repository through GitHub CLI

- in Terminal navigate to the folder where you want to clone your repo, than:
```
gh auth login
> GitHub.com
> SSH
> Yes
> How would you like to authenticate GitHub CLI? Login with a web browser

First copy your one-time code: 8963-6140
Press Enter to open github.com in your browser... 
```
- type the one time password, and authenticate yourself through Authentication App



### Resources:

#### Git Cheat Sheet:

file:///Users/anettkeszler/Downloads/github-git-cheat-sheet.pdf

### Further topics:

Check the last section of every module for reading more about topics

DevOps

Agile

Testing

Monolith codebase vs Microservices

More about CI/CD workflow

Relative vs absolute path


