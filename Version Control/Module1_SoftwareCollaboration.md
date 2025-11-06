# Version Control Course 

## Module1 - Software Collaboration (1-17)

### 1. Introduction to the Course (video)

- **Version Control**: is a practice of tracking and managing changes to files over time. It allows teams to collaborate by separating work into different versions, compare changes, and revert to previous states if error comes up. It is essential to the daily development activities. 

- **Version Control Systems** are sowtware tools, like Git, that automate this process by creating snapshots of files in a central repository. 

### 2. How do developers collaborate in the real world? (video)

Effective collaboration is important especially on large projects. Developers sometimes work on the same feature paralell.
Communication is the most important skill for working with other developers. 
Prioritize your work is also very important to unblock other developers.

Effective using of Version Control leads to better collaborating because it helps you understand why certain changes were made if you look at commit. Also helps you context switch between different feature or projects that you're working on. 
Effective collaboration led to a better outcome on the recent project. 

### 3. Course Syllabus (reading)

**After completing this course, you will be able to**:

- Implement Version Control systems.

- Navigate and configure using the command line.

- Manage code revisions.

- Create and use a GitHub repository.

**Module 1: Software Collaboration**

After completing this module, you will be able to: 
- Describe how modern software teams collaborate and work on the same codebase.
- List different version control systems and methodologies. 
- Illustrate a standard software development workflow.

**Module 2: Command Line**

After completing this module, you will be able to: 
- Describe what the command line is and how it is used to execute command in Linux.
- Practice traversing your hard drive via the command line.
- Create, rename and delete files and folders on your hard drive using Unix commands.
- Use pipes and redirection.


**Module 3: Git**

After completing this module, you will be able to: 
- Outline the Git principles.
- Use a GitHub repository.
- Describe the steps in a standard GitHub workflow.
- Create branches and merge different branches and sources.
- Describe how code goes from local development to version control and then to live production.

**Module 4: Graded Assessment**

- Recap on all of the topics covered throughout the course.
- Apply all the skills you have learned in a graded project.

### 4. How to be successful in this course (reading)

Here are some general tips that can help you stay focused and on track: 

- Set daily goals for studying 
- Create a dedicated study space
- Schedule time to study on your calendar 
- Keep yourself accountable 
- Actively take notes 
- Join the discussion 
- Do one thing at a time
- Take breaks 

### 5. Why Every Developer Needs Collaboration Tools (dialog)

- **Universal Collaboration Challenges**: Identify problems that occur in any development team when multiple developers work on the same project: 
    - overwriting work: they might overwrite each other's work when multiple people edit the same file 
    - conflicting implementation: different approaches to implementation can lead to conflicts or inconsistencies in the codebase, this highlights the need for clear communication and agreed upon standards

- **Cross-Platform Teamwork**: Explore how mixed teams coordinate on the same project using shared collaboration principles.(like frontend, backend, and mobile developers):
    -  They use Version Control softwares for tracking their changes on files and ensuring everyone is on the same page

- **Version Control Softwares and Techniques**: Explore different version control software, why it's important for conflict resolution, and introduce Git and GitHub:
    - Git is a version controle software which tracking changes, enabling collaboration through different versions, comparing changes, and enabling to revert to previous states.
    - GitHub is a platform to handeling projects with git

- **Version Control as a Universal Tool**: Analyze how version control systems serve as an essential "time machine" for all types of developers:
    - Git allows us to revert our changes or go back to a previous version. 
    - commit history acts like a detailed logbook, explaining what and why chanes were made. 


### 6. What is version control? (video)
**Version control** is a system that records all changes and modification to files for tracking purposes. Primary goal is to keep track of changes. 
VCS allows developers access to the entire change history with the ability to revert or roll back to a previous state. 

Benefits of using VC: 
- revision history: it provides a record of all changes in a project, it has the ability to revert to a stable point in time in case of issues or bugs.So the team can work faster and deliver code with more confident. 
- identity: All changes were made with the identity of the user
- collaboration: a developer works with many people on the same project, everyone can submit their own code and review other's code (peer review) to provide feedback
- automation
- efficiency

DevOps is a set of practices, philosophies and tools that increase an organization's ability to deliver applications or services to a hight quality and velocity. VC is a key tool in this process.

Agile methodology: 
- Planning 
- Requirement analysis
- Design
- Developement
- Testing
- Deployment

 In an agile process planning and working is usually a 2 weeks duration, it is an iteration. Each iteration has a list of tasks.

 ### 7. Case study: how Meta engineers collaborate (video)

### 8. Version Control Git terminology (cheat sheet, pdf)

![alt text](img/git1.png)
![alt text](img/git2.png)
![alt text](img/git3.png)
![alt text](img/git4.png)

### 9. Systems of Version control and tool
Version Control Systems examples: 
- Git
- Subversion
- Perforce
- AWS Code Commit
- Mercurial

VCSs can be **Centralized or Distributed** 

**Centralized VCSs (CVCS):** contain a server and a client. The server contains the main repository that keeps the full history of versions of the code base. Developers working on projects using CVCS need to pull down the code from the server to their local machine, so they have their own working copy of the code base. The cliant has the latest code. After making changes to the code, the developer needs to push the changes to the central server so that other developers can see them. 

Pros: 
- easier to learn
- give more access control to user

Cons:
- slower (needs to estabilish a connection to the server to perform any actions)

**Distributed Version Control System (DVCS)**: similar to CVCS, you still need to pull code down from the server to view the latest changes. The key difference is that every user is essentially a server and not a client. This means that every time you pull down code from the distributed model, you have the entire history of changes on your local system. 

Pros:
- you don't need to be connected to the server to add your changes or view a file's history (users can work in an offline state)
- speed and performance is better 
- better software developement life cycle