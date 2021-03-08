# Useful Github commands

This is a markdown file to help keep track of useful github commands. 

## Table of contents

- [First Time Setup](#first-time-setup)
    - [Migrate from URL to SSH keys](#migrate-from-url-to-ssh-keys)
- [General Use](#general-use)
    - [Bread and Butter Commands](#bread-and-butter-commands)
    - [Branch Setup](#branch-setup)
    - [Branch Management](#branch-management)
    - [Commits](#commits)
    - [Push n Pull](#push-n-pull)
    - [Others](#others)
- [Resets](#resets)
    - [Web Resources](#web-resources)
- [Revert Branch Walkthrough](#revert-branch-walkthrough)
    - [Pushed to wrong branch](#pushed-to-wrong-branch)
    - [Copy specific files from another branch](#copy-specific-files-from-another-branch)
    - [Update remote to another branch](#update-remote-to-another-branch)
- [Config](#config)
- [Web resources](#web-resources)

## First Time Setup

Run the folowing to set up github the first time. 
In a directory that you want to set up github perform the folowing. 
The first two commands below *should* be run. 
One of the seccond two should be run to push a repo to the remote, or pull a remote to local. 

> Example directory `/home/acobb/git`.

> More info for Cloaning can be fond later on.

You can find the url requested below by going to the main repo page. 
On the right there is a green button `Clone or download`. 
After clicking on the green button, copy the url. 

> Enterprise url structure `https://<enterprise>/<platform>/<repo_name>.git`

If you are creating a repo from a directory run `git init`. 
If you are cloaning a repo from remote use `git clone <ssh or html url>`. 

### Migrate from username/password to SSH keys

If you happen to still be using username/password I highly reccomend changing to ssh. 
Each account needs to save ssh keys, and your local branches need to have the url updated. 
When you copy in your ssh keys make sure you only copy the public key. 

#### Updating your account

- Copy the contents of the id_rsa.pub file to your clipboard `~/.ssh/id_rsa.pub`. 
    This is your public key so its fine if people see it. 
    If you are lazy you can try this cmd `xclip -sel clip < ~/.ssh/id_rsa.pub`. 

- Go to Settings

![a](image_dir/userbar-account-settings1.png)

- In the user settings sidebar, click SSH and GPG keys.

![b](image_dir/settings-sidebar-ssh-keys2.png)

- Click New SSH key or Add SSH key.

![c](image_dir/ssh-add-ssh-key3.png)

- In the "Title" field, add a descriptive label for the new key. For example, if you're using a Kepler VDI, you might call this key "KVDI".

![d](image_dir/ssh-key-paste4.png)

- Paste your key into the "Key" field.

![e](image_dir/ssh-add-key5.png)

- Click Add SSH key.

> If you have questions follow this link: https://help.github.com/en/enterprise/2.18/user/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account

#### Updating your local repo

You can check to see if you are set up for URL pushes by running `git remote -v`:

```
git remote -v
origin  https://github.<enterprise>.com/<platform>/<repo_name>.git (fetch)
origin  https://github.<enterprise>.com/<platform>/<repo_name>.git (push)
```

Set the new url:

```
git remote set-url origin git@github.com:PROJECT/REPOSITORY.git
```
```
git remote set-url origin git@github.com:USERNAME/REPOSITORY.git
```

> git remote set-url origin git@github.digitalglobe.com:p20-20-mcs/MCS-toolbox.git

> USERNAME/PROJECT depending on the use case

Verify that they are now set correctly:

```
git remote -v
origin  git@github.<enterprise>.com:<platform>/<repo_name>.git (fetch)
origin  git@github.<enterprise>.com:<platform>/<repo_name>.git (push)
```

---

## General Use

### Bread and Butter Commands

Of all the commands in this file, the following are most likely to be the most useful. 
The commands are somewhat oriented with most often used on top to least often on bottom. 

| Command | Description |
| --- | --- |
| `git commit`                      | Stage updates and give them a description.                                            |
| `git push`                        | Push updates to the remote repo.                                                      |
| `git status`                      | See what is and isnt statged.                                                         |
| `git add <file_name>`             | Add a file to the next commit (`git add .` adds everything in that directory down).   |
| `git branch`                      | Lists active branches in your local repo.                                             |
| `git pull`                        | Pull the remote branch changes.                                                       |
| `git checkout -b <branch name>`   | Creates a new branch and checks it out.                                               |

---

### Branch Setup

Use this to create a local copy of a remote repo. 
You can find the url requested below by going to the main repo page. 
On the right there is a green button `Clone or download`. 
After clicking on the green button, copy the url. 

> Enterprise url structure `https://github.<enterprise>.com/<platform>/<repo_name>.git`

| Command | Description |
| --- | --- |
| `git clone <url from remote repo>`                                | Create a local copy of a remote repository.   |
| `git checkout -b <new_branch_name> origin/<remote_branch_name>`   | To create a local copy of a remote branch.    |

---

### Branch Management

| Command | Description |
| --- | --- |
| `git branch`                                          | List branches (the asterisk denotes the current branch)   |
| `git branch <branch name>`                            | Create a new branch                                       |
| `git branch -d <branch name>`                         | Delete a branch                                           |
| `git branch -D <branch name>`                         | Delete a branch that has un pushed commits                |
| `git checkout <branch name>`                          | Switch to a branch                                        |
| `git checkout -b <branch name>`                       | Create a new branch and switch to it                      |
| `git checkout -b <branch name> origin/<branch name>`  | Clone a remote branch and switch to it                    |
| `git checkout -`                                      | Switch to the branch last checked out                     |
| `git checkout --track origin/<repo_name>`             | Pull a remote branch that is not in your local repo       |
| `git fetch`                                           | Pulls the most current from remote repo                   |
| `git rebase <branchname>`                             | Sync _local only_ branch up with remote master            |
| `git merge <branch name>`                             | Merge a branch into the active branch                     |
| `git merge <source branch> <target branch>`           | Merge a branch into a target branch                       |
| `git stash`                                           | Stash changes in a dirty working directory                |
| `git stash clear`                                     | Remove all stashed entries                                |
| `git rm -- cached <filename>`                         | Stop tracking file but dont delete it in remote           |

To update a single file to what remote has use this:
```bash
git fetch
git checkout origin/<branch> <file_path>
```

If you need to bring a branch up to speed with another like master, use this (update local with master updates):
```bash
git checkout master
git pull
git checkout <branchname>
git merge master
```

---

### Commits

Commit to stage an upodate and title the stage. 
Once you have staged sufficient commits you can push them to the remote repo. 
If the branch has not been added to the remote repo, git will prompt you to update remote. 
To add untracked files you need to use `git add`. 

| Command | Description |
| --- | --- |
| `git add <file_name>`                 | Add a specific file or list to the next commit.                   |
| `git add .`                           | Add all new and changed files to the next commit.                 |
| `git add -A`                          | Add all new and changed files to the next commit.                 |
| `git commit -a`                       | Commit changes, will prompt for message in a _vi_ text editer.    |
| `git commit -m "<commit message>"`    | Commit changes.                                                   |
| `git commit --amend`                  | Appends the previous commit.                                      |
| `git rm --cached <file>`              | Tel git to stop tracking a file but dont delete the file.         |
| `git rm -r --cached <directory>`       | Tel git to stop tracking a direcotry                              |

---

### Push n Pull

Pushes are used to push to the remote. 
Pulls are used to pull from the remote to local or one branch to another.

| Command | Description |
| --- | --- |
| `git push`                                            | Push changes to remote repo. |
| `git push --set-upstream origin <new_branch_name>`    | Push local branch to the remote if it does not exist yet |
| `git pull`                                            | Update local repository to the remote |

---

## Others

| Command | Description |
| ------- | ----------- |
| `git log` | View changes |
| `git log --summary` | View changes (detailed) |
| `git diff [source branch] [target branch]` | Preview changes before merging |
| `git diff --name-status [source branch]..[target branch]` | Show file differences between two branches |

---

## Resets

**I dont keep this completely up to date because I dont use these commands very often.**

#### Revert a push/commit

This is super useful if you happen to push to the wrong branch (specifically master or dev). 
Make sure that you are on the branch of concern. 
Find the commit you would like to roll back to and run the following command. 
The process creates a new commit that reverts the previous commit. 
There are ways to delete the commit, but this is easiest. 

```tcsh
git revert <commit_id>
git push
```

I needed to roll back the top commit: 
![one](image_dir/revert_commit1.png)

So I ran: 

```tcsh
git revert 815d0bc
git push
```

> UPDATE: It is better to run `git log` and use the ~40 char code as the revert commit id

> Note: I had to pull from master first to update my local repo with the commit. 

#### Reset

**Caution**, this section is potentially dangerous, only attempt it if you have to and have thought it through.
This section is numbered least dangerous to most dangerous. 
It is highly reccomended to attempt 1 first and only keep trying if the issue is not fixed. 
For a better explanation, follow the `Doing a hard reset` link below

When doing resets, a `~` refers to pushes and `^` refers to commits, see reference below for a better explanation. 
Note: You do not need to give a number, no number assumes most recent. 

A hard reset `--hard` is rather dangerous. 
If you do a hard reset against your current HEAD, it will erase all changes in your working tree, so that your current files match the contents of HEAD.

For any process below, it is reccomended to stash your current changes `git stash`. 
This saves the changes but not to a branch. 
If you want to rever the changes, run `git stash apply`.


1. Head back in time 

```tcsh
git checkout -b <new-branch> HEAD~<#>
```

2. Wipe out differences in working tree

```tcsh
git reset --hard origin/<branch>
```

3. Set HEAD to point to an earlier commit

```tcsh
git reset --soft HEAD~<#>
```

4. Go back in time, throwing away changes

```tcsh
git reset --hard HEAD~<#>
```

---

## Revert Branch Walkthrough

Enevetably we all break things. 
Commiting to the wrong branch or the wrong thing tends to be the most common. 
Hopefully the walkthrough below will help. 

- [Pushed to wrong branch](#pushed-to-wrong-branch)
- [Copy specific files from another branch](#copy-specific-files-from-another-branch)
- [Update remote to another branch](#update-remote-to-another-branch)

### Pushed to wrong branch

If you push to the wrong branch, the easiest thing to do is to move the commits to the correct branch. 
This is done with `cherry-pick`. 
Cherry pick will uncommit from the wrong branch and commit to the correct branch. 
There are two ways to do it, either cherry pick each commit, or batch cherry pick. 

  **Moving a few commits**

  Branch A has commits (X,Y) that also need to be in Branch B.  
  The cherry-pick operations should be done in the same chronological order that the commits appear in Branch A.  
  cherry-pick does support a range of commits, but if you have merge commits in that range, it gets really complicated. 

  ``` 
  git checkout branch-B
  git cherry-pick X
  git cherry-pick Y
  ``` 

  **Moving many commits**

  Branch A has a series of commits (X..Y) that need to be moved to branch B. 
  You will need to specify the commit before the initial commit you are interested in order for it to be included. 
  Example: you want commits B..D from (...A->B->C->D-E->...) you would use "A" as the starting commit. 
  You will also need the commit SHA for the HEAD of the branch you are transferring to. 

  ``` 
  git checkout branch-B
  git log  # Note the SHA of most recent commit (M) 
  git rebase --onto M <commit before X> Y
  git rebase HEAD branch-B
  ``` 

  When you are done you still need to push the changes so that the remote is up to date. 

### Copy specific files from another branch

  Branch A has files (X,Y) that need to be in Branch B. 
  From branch B, checkout branch A with a list of files as arguments. 
  The files will be copied over. 
  Commit the files or they will not be saved. 
  (If you try to switch back to branch A, the files will not be saved to branch B). 
  This works for multiple files and filepaths but does not work for wildcard searches. 
  
  ```
  git checkout branch-B
  git checkout branch-A X y
  git commit
  ```

### Update remote to another branch

  If you have updates to branch A that you want in branch B, you need to rebase branch B.

  ```
  git checkout branch-B
  git rebase branch-A
  ```

  For a good visual:
  
  ```
        A---B---C branch-B
       /
  D---E---F---G master
  ```
  
  ```
  git checkout branch-B
  git rebase master
  ```
  
  ```
                A'--B'--C' topic
               /
  D---E---F---G master
  ```

---

### Config

Each users github config file is found in `/home/user/.gitconfig`. 
The default looks something like this: 

```tcsh
[user]
      email = 
      name = 
[push]
      default = 
```

Further categories can be added by following this link: 
https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration

| Command | Description |
| --- | --- |
| `git config --global credential.helper cache`                     | set up your git config file                                           |
| `git config --global credential.helper 'cache --timeout=86400'`   | set up your password timeout to 24hrs from 0                          |
| `git config --global core.editor <default code editor>`           | Change the default editor from `vi`                                   |
| `git config --list`                                               | Lists out the contents of a users config file                         |
| `git config --unset-all`                                          | I believe this unsets the config, but I have not tried it to confirm  |

---

###### References

> [~ vs ^](https://stackoverflow.com/questions/2221658/whats-the-difference-between-head-and-head-in-git)

> [Doing a hard reset](https://jwiegley.github.io/git-from-the-bottom-up/3-Reset/4-doing-a-hard-reset.html)

## Web Resources

You will have a hard time accessing any of these while in MCS Gold. 
Feel free to try if you dont believe me. 

 - [Basic markdown](https://guides.github.com/features/mastering-markdown/)

 - [More markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

 - [Even mroe markdown](https://help.github.com/en/articles/basic-writing-and-formatting-syntax#headings)

 - [Emoji markdown](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)

 - [Hard reset](https://jwiegley.github.io/git-from-the-bottom-up/3-Reset/4-doing-a-hard-reset.html)

 - [~ vs ^](https://stackoverflow.com/questions/2221658/whats-the-difference-between-head-and-head-in-git)
 
 - [Cherry Pick](https://gist.github.com/unbracketed/889c844473bcca1917e2)
