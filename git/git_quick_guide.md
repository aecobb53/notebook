# Useful Github commands

This is a markdown file to help keep track of useful github commands. 

## Table of contents

- [First Time Setup](#first-time-setup)
  - [Migrate from URL to SSH keys](#migrate-from-url-to-ssh-keys)
- [General Use](#general-use)
- [Commands](#commands)
  - [Branch Setup](#branch-setup)
  - [Commits n Pushes](#commits-n-pushes)
  - [Branch Management](#branch-management)
  - [Push n Pull](#push-n-pull)
  - [Others](#others)
  - [Resets](#resets)
  - [Web Resources](#web-resources)
- [Revert Branch Walkthrough](#revert-branch-walkthrough)
  - [Pushed to wrong branch](#pushed-to-wrong-branch)
  - [Copy specific files from another branch](#copy-specific-files-from-another-branch)
  - [Update remote to another branch](#update-remote-to-another-branch)
- [Config](#config)

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

> DG url structure `https://github.digitalglobe.com/<platform>/<repo_name>.git`

```tcsh
git config --global credential.helper 'cache --timeout=86400'
git init
git clone <url from remote repo>
```

| Command | Description |
| ------- | ----------- |
| `git config --global credential.helper 'cache --timeout=86400'` | set up your password timeout to 24hrs from 0 |
| `git init` | Initialize a local Git repository |
| `git clone <url from remote repo>` | Create a local copy of a remote repository |

### Migrate from URL to SSH keys

By default github is set up to use URLs to push commits to the remote branch. 
I find using ssh keys to authenticate to be much easier than the URL. 
Another reason to switch are the issues with the two factor authentication. 
Each account needs to have ssh keys, and your local branches need to have the url updated. 

#### Updating your account

- Copies the contents of the id_rsa.pub file to your clipboard `~/.ssh/id_rsa.pub`. 
  This is your public key so its fine if people see it. 

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

#### Updating your local branch

You can check to see if you are set up for URL pushes by running `git remote -v`:

```
git remote -v
origin  https://github.digitalglobe.com/p20-20-mcs/MCS-toolbox.git (fetch)
origin  https://github.digitalglobe.com/p20-20-mcs/MCS-toolbox.git (push)
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
origin  git@github.digitalglobe.com:p20-20-mcs/MCS-toolbox.git (fetch)
origin  git@github.digitalglobe.com:p20-20-mcs/MCS-toolbox.git (push)
```

---

## General Use

### Commands

Of all the commands in this file, the following are most likely to be the most useful. 
Memorizing the following list would be worthwile. 
The commands are somewhat oriented with most often used on top to least often on bottom. 

| Command | Description | Reason it is useful |
| --- | --- | --- |
| `git commit` | Commit changes | Small updates to a script can be saved |
| `git push` | Push changes to remote repository (remembered branch) | Save to the remote |
| `git status` | Check status | Check for mismatches between local and remote before pushes |
| `git add <file_name>` | Add a file to the staging area | Add files to save to git |
| `git branch` | List branches (the asterisk denotes the current branch) | Verify you are on the branch you thought, or see other branches |
| `git checkout -b <branch name>` | Create a new branch and switch to it | Create a new feature branch |
| `git pull origin <branch name>` | Pull changes from remote repository | Updates your local repo if the remote changed |

---

### Branch Setup

Use this to set your local host to a remote repo. 
You can find the url requested below by going to the main repo page. 
On the right there is a green button `Clone or download`. 
After clicking on the green button, copy the url. 

> DG url structure `https://github.digitalglobe.com/<platform>/<repo_name>.git`

```tcsh
git clone <url from remote repo>
```

| Command | Description |
| ------- | ----------- |
| `git clone <url from remote repo>` | Create a local copy of a remote repository |

To add a remote branch to your local branch run the following command:

```tcsh
git checkout --track origin/<branch name>
```

---

### Commits n Pushes

The git remove function is not needed if you remove the file/directory and commit. 
If you do not like to use the command line. 
You can run `git commit` and then type your mesage and save the file. 

```tcsh
git status
git add <file_name>
git add .
git add -A
git commit
git commit -m "<commit message>"
git commit --amend
git rm -r <file-name.txt>
```

| Command | Description |
| ------- | ----------- |
| `git status` | Check general status and status of local vs remote |
| `git add <file_name>` | Add a file to the staging area |
| `git add .` | Add all new and changed files to the staging area |
| `git add -A` | Add all new and changed files to the staging area |
| `git commit ` | Commit changes, will prompt for message in a *vi* text editer |
| `git commit -m "<commit message>"` | Commit changes |
| `git commit --amend` | Appends the previous commit |
| `git rm -r <file-name.txt>` | Remove a file/directory |

---

### Branch Management

The folowing commands are useful for branch management

```tcsh
git branch
git branch <branch name>
git branch -d <branch name>
git checkout -b <branch name>
git checkout -b <branch name> origin/<branch name>
git checkout <branch name>
git checkout -
git checkout -- <file-name.txt>
git checkout --track origin/<repo_name>
git fetch
git fetch -p origin
git merge <branch name>
git merge <source branch> <target branch>
git stash
git stash clear
git rm -- cached <filename>
```

| Command | Description |
| ------- | ----------- |
| `git branch` | List branches (the asterisk denotes the current branch) |
| `git branch <branch name>` | Create a new branch |
| `git branch -d <branch name>` | Delete a branch |
| `git checkout -b <branch name>` | Create a new branch and switch to it |
| `git checkout -b <branch name> origin/<branch name>` | Clone a remote branch and switch to it |
| `git checkout <branch name>` | Switch to a branch |
| `git checkout -` | Switch to the branch last checked out |
| `git checkout -- <file-name.txt>` | Discard changes to a file |
| `git checkout --track origin/<repo_name>` | Pull a remote branch that is not in your local repo |
| `git fetch` | Pulls the most current from remote repo |
| `git fetch -p origin` | Pulls the most current master from the remote repo |
| `git merge <branch name>` | Merge a branch into the active branch |
| `git merge <source branch> <target branch>` | Merge a branch into a target branch |
| `git stash` | Stash changes in a dirty working directory |
| `git stash clear` | Remove all stashed entries |
| `git rm -- cached <filename>` | Stop tracking file but dont delete it in remote |

To add a remote branch to your local branch run the following command:

```tcsh
git checkout --track origin/<branch name>
```

---

### Push n Pull

Pushes are used to push to the remote. 
Pulls are used to pull from the remote to local or one branch to another.

```tcsh
git push
git push origin <branch name>
git push -u origin <branch name>
git push origin --delete <branch name>
git push --set-upstream origin <new_branch_name>
git pull
git pull origin <branch name>
```

| Command | Description |
| ------- | ----------- |
| `git push` | Push changes to remote repository (remembered branch) |
| `git push origin [branch name]` | Push a branch to your remote repository |
| `git push -u origin [branch name]` | Push changes to remote repository (and remember the branch) |
| `git push origin --delete [branch name]` | Delete a remote branch |
| `git push --set-upstream origin <new_branch_name>` | Push local branch to the remote if it does not exist yet |
| `git pull` | Update local repository to the newest commit |
| `git pull origin [branch name]` | Pull changes from remote repository |

---

## Others

| Command | Description |
| ------- | ----------- |
| `git log` | View changes |
| `git log --summary` | View changes (detailed) |
| `git diff [source branch] [target branch]` | Preview changes before merging |

---

## Resets

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

Config commands
```tcsh
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=86400'
git config --global core.editor <default code editor>
git config --list
git config --unset-all
```

| Command | Description |
| ------- | ----------- |
| `git config --global credential.helper cache` | set up your git config file |
| `git config --global credential.helper 'cache --timeout=86400'` | set up your password timeout to 24hrs from 0 |
| `git config --global core.editor <default code editor>` | Change the default editor from `vi` |
| `git config --list` | Lists out the contents of a users config file |
| `git config --unset-all` | I believe this unsets the config, but I have not tried it to confirm |

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
