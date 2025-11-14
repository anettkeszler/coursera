# Version Control Course 

Source: Version Control: https://www.coursera.org/learn/introduction-to-version-control?specialization=meta-full-stack-developer

## Module3 - Working With Git (1-30)

### 1. What is Git and GitHub? 

**Git** is a version control system for tracking changes of projects

**GitHub** is a cloud-based hosting service that manages git repositories

A **git repository** is used to track all changes to files in a specific folder, and keep a history of all changes. 

### 5. Connecting to GitHub via HTTPS

### 6. Connecting to GitHub via SSH

If you plan to use Github from your local device, the recommended way to authenticate is using Secure Shell, or SSH for short. This requires the creation of keys: a public and a private key. The advantage of using SSH is that you don't need to enter in your credentials when interacting with the remote repository. The keys are generated and stored on your local machine and then the public key is copied to the Github server. After you finish setting up, every operation will be authenticated using the keys.

### 7. Creating and cloning a repository

- Repostory name: my-first-repo
- Description: Practice account for learning Git
- add README.md file
- create 

- md is short for markdown
- every repository you create will have a single main branch at the start (main line)

- clone the repository via HTTPS:<br>
    - copy the url under HTTPS 
    - go to Terminal, and paste the url: ```git clone https://....``` 
    (this works only if you are connected to GitHub via HTTPS)

### 8. How git works

- when I clone the repository, and check the content of it, there is a '.git' folder. It is a hidden folder (ls -la) used to track all of the changes. This folder is automatically created when you create a repository. It is initialized by running the 'git init' command. As the repository was created on GitHub, it is not required to run the 'git init'. GitHub handled all of this as part of its create new repo flow. 

Git workflow: modified, staged, committed <br>

**Working directory / Modified**: adding, removing or updating files. Git knows the file has changed, but does not track it. 

**Staging area / Staged:** in order for Git to track a file, it needs to be put in the staged area (by 'git add' command )

**Committed**: committing a file in Git is a save point in many ways. Git will save the file, and have a snapshot of the current changes. 

**Remote repository**: we push our commits into the remote repository (on GitHub)

### 9. Add and commit 

```
git add .
git add test.txt
```

Git add marks a file to be included as part of a code commit, it will let git knows that I want to track this file. 

- To untrack a file (which was mistakenly tracked)
```
git restore --staged test.txt
```

### 10. Branches

- before creating a new branch, make sure that your branch is up to date with the 'origen/main', and nothing to commit, working tree clean 
```
git status

git branch feature/lesson               - it will create the new branch 
git checkout -b feature/lesson          - it will create and checkout to this new branch

git branch                              - it shows all of my branches, and my current stay
```

Git branches exist in isolation. <br>
Changes need to be merged back to the main branch. 

- Pull request: the purpose is to obtain a peer review of changes made to the branch, to validate that the changes are correct

- Use git push to push your changes from the local repository to the remote repo. 
```
git push -u origin feature/lesson
```
- '-u' - it's a good practice to specify -u, this means that I'm only going to get updates from the upstream, which is the main branch in this case. The result of this is that the origin won't be my main branch anymore. Instead, it's the fearue/lesson.

- On GitHub I can create the Pull Request to merge feature/lesson branch into main.  A Pull Request lets the team know that I've made new changes that I want them to review and that I also want to approve or request changes to the actual PR itself. 

Once PR is approved, you can merge the changes into main branch. 

Having independent branches makes the project easier to manage.
This is cleaner than everyone working on the main branch, which could likely cause a lot of isses / merge conflicts.
Also there is no limit how many branches you can have. 

When you create a pull request you are asking the other developers to review your work and approve it to be merged with the repository.

Naming convention: 
when working on a new feature: feature/...
when bug fixing: fix/..

Once you pushed your changes from feature into main on GitHub UI, go back to your Terminal. 
```
git status                  - you are still on feature, chackout to main
git checkout main
git pull                    - you will recieve the latest changes from your main remote repository 
```

### 11. Remote vs Local 

Remote repository where any developer can push their changes.  

The remote code is accessed through a URI which is unique and only accessible to those who have permission.

Local refers to your machine which can be a laptop, desktop or mobile device, and it is only accessible to you

One advantage is using git that you can work offline and commit your changes when you are ready. 

- Let's create a new local repository with git init:
```
mkdir my-first-repo
cd my-first-repo
git init                    - an empty git repository has been initialized
git remote                  - it comes back as blank 
```

- git remote comes back blank, the reason for that is that I've only initialized a local repository which has no connection to a central repository yet. Right now it's only available locally on my machine. 

### 12. Push and Pull 

- You need internet connection to push or pull the changes between local and remote. 

```
git push origin <main>            - I want to push my changes into main

git pull                        - This will get the latest changes from the remote repo to your local repo
```

### 13. Add, commit and push

Lab work

### 16. Resolving conflicts

Conflicts will normally occur when you try to merge a branch that may have competing changes. Git will normally try to automatically merge (auto-merge), but in the case of a conflict, it will need some confirmation. 

n such scenarios, user intervention is required to review and resolve the competing changes. This process is called merging or rebasing. 

To resolve, the the developer must look at the changes on the server and their local repository and validate which changes should be resolved.

Example:<br> 
- Developer1 and Developer 2 pull the main repository on Monday morning and creates their own feature branch
```
git pull
git checkout -b feature1

git pull
git checkout -b feature2
```
- Developer 1 makes their changes to a file called Feature.js and then commits the changes to the repository for approval via a PR (pull request)
```
git add Feature.js
git commit -m 'chore: added feature 1!!'
git pull origin main
git push -u origin feature1
```
The Pull Request (PR) is reviewed and then merged into the main branch. Meanwhile, Developer 2 is working on their feature. They follow a similar process to Developer 1.

Note:  If you look at the code, any reference for HEAD in Git refers to the current branch or commit you're working on.
```
    git add Feature.js
    git commit -m 'chore: added feature 2!!!'
    git pull origin main

From github.com:demo/demo-repo
 * branch            main       -> FETCH_HEAD
   9012934..d3b3cc0  main       -> origin/main
Auto-merging Feature.js
CONFLICT (content): Merge conflict in Feature.js
Automatic merge failed; fix conflicts and then commit the result.
```
At this point, Developer 2 encounters a merge conflict. Git notifies that a merge conflict has occurred and requires resolution before changes can be pushed to the remote repository. Running git status provides additional details about the conflict:
```
 git status
    On branch feature2
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   Feature.js

no changes added to commit (use "git add" and/or "git commit -a")
```

To resolve the issue, Developer 2 must review and compare the changes made by Developer 1. It’s a good practice to first identify the conflicting branch by using the following command:
```
git log --merge

commit 79bca730b68e5045b38b96bec35ad374f44fe4e3 (HEAD -> feature2)
Author: Developer 2 
<developer2@demo.com>
Date:   Sat Jan 29 16:55:40 2022 +0000

    chore: add feature 2

commit 678b0648107b7c53e90682f2eb8103c59f3cb0c0
Author: Developer 1 
<developer1@demo.com>
Date:   Sat Jan 29 16:53:40 2022 +0000

    chore: add feature 1
```
From the log, we can see that conflicting changes occurred in feature1 and feature2. Developer 2 now examines the specific differences causing the conflict:
```
git diff

diff --cc Feature.js
index 1b1136f,c3be92f..0000000
--- a/Feature.js
+++ b/Feature.js
@@@ -1,4 -1,4 +1,8 @@@
  let add = (a, b) => {
++<<<<<<< HEAD
 +  if(a + b > 10) { return 'way too much'}
++=======
+   if(a + b > 10){ return 'too much' }
++>>>>>>> d3b3cc0d9b6b084eef3e0afe111adf9fe612898e
    return a + b;
  }
```
Developer 2 resolves the conflict by editing the file and removing the markers.
```
let add = (a, b) => {
  if(a + b > 10) { return 'way too much'}
  return a + b;
}
```
Developer 2 then stages and commits the resolved changes:

```
 git add Feature.js
 git commit -m 'fix merge conflicts'
 git push -u origin feature2
```

### 18. Example workflow

As a developer working on a project, you first need to pull the project down from a remote repository to your local machine (this is called checking out a project or pulling the project).

Feature branching: you create a new branch from the main line and work on this dedicated branch until the task is complete. 

Pull Request: when you are ready with your developement on your local branch, you push the changes locally, and than you create a PR to merge yout feature into main. 

The PR is compared to the main branch, so developers who peer review the code can see exactly what was changed. Once it's reviewed and approved, it can be merged into the main line. 

### 19. HEAD

how does git know what branch you're currently on? 
It keeps a special pointer called HEAD which is one of the files inside the .git folder. 
This file refers to the current commit you are viewing. 
```
cd .git
cat HEAD                        / ref: refs/heads/master
```

- This file is also exists insode the .git/refs/heads
```
cd .git
cat /ref/heads/main
```
- A single hashed ID appear, which is a reference for the current commit. 

- When you checkout to another branch, we move to HEAD from 'main' to 'feature' branch.  
- Make some changes, and commit. When you run 
```
cat /ref/heads/main
```
- Notice, that the single hashed ID has changed. Whenever a change occurs for a commit, the single hashed ID will update to be the latest commit for that working directory. 

### 20. Diff commands
- Tells you what changes were made exactly
- it used to make comparisons against files on your local repository 
```
git diff HEAD test.txt

git log --pretty=oneline            - it shows it in one line 

git diff main feature/testing
```

### 21. Git blame

- Git blame is used to look at changes of a specific file and show the dates, times and users who made the changes 
 
 ```
 git blame test.txt

 git blame -L 5,15 test.txt                 - from line 5 to 15 , abbreviate the file with -L flag

 git log -p <hash dash ID from git blame>   - shows the actual changes of the file under that commit
 ```






