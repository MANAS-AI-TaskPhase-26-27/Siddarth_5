# BASIC GIT COMMANDS

## LOCAL REPOSITORY COMMANDS :-
```bash
git commit
"saves snapshot"
```
```bash
git branch <name>
"creates new branch"
```
```bash
git checkout <name>
"switches to the branch"
```
```bash
git checkout -b  <name>
"creates and switches to the new branch"
```
```bash
git merge
"combines different branches"
```
```bash
git rebase
"Moves the commit base"
```


### HEAD - points to most recent commit

```bash
git checkout HEAD^
"points above ancestor"
```
##### ^  Caret operator

```bash
git checkout HEAD~<number>
"points ancestor upto given number"
```
##### ~ Tilde operator

```bash
git branch-f <branchname> HEAD~<number>
"branch forcing"
```
```bash
git reset
"reversing local branches (not shared with others)"
```
```bash
git revert
"reversing remote branches (shared with others)"
```
```bash
git cherry-pick <commit1> <commit2> <...>
"copies series of commits below HEAD (main does not move)"
```
```bash
git rebase -i HEAD~<number>
"allows to copy and arrange commits (main does move)"
```
```bash
git add filename
git commit
"saves changes with respect to file"
```
```bash
git add
"saves changes of all files"
```
```bash
.gitignore
"ignores files that you never wanted to commit"
```
```bash
git restore --staged<file_name>
"unstage a file keeping edits"
```
```bash
git restore <file_name>
"discards your edits"
```
```bash
git commit --ammend
"to make slight modification"
```
```bash
git tag <tag_name> <commit>
"marks commit as milestone"
```
