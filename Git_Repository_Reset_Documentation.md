# Git Repository Reset Documentation

## Problem Description
The repository was having issues with pushing to GitHub due to large files in the Git history. GitHub has a file size limit of 100MB, and some files in the history were exceeding this limit, causing push operations to fail.

## Solution Steps

### 1. Clean Slate: Remove Git Tracking
```bash
rm -rf .git
```
This command removes the entire Git repository metadata while preserving all local files. It effectively "un-initializes" Git from the project, allowing us to start fresh.

### 2. Initialize New Git Repository
```bash
git init
```
This creates a new Git repository with a clean history. The command creates a new `.git` directory that will store all the version control information.

### 3. Set Up Main Branch
```bash
git branch -M main
```
This renames the default branch to 'main' to align with GitHub's standard naming convention. This is important for consistency with modern Git practices.

### 4. Configure gitignore
Created a `.gitignore` file with rules to exclude:
- Large files (*.mov, *.mp4, *.jar, etc.)
- Build artifacts
- IDE files
- System files
- Virtual environment directories

This prevents Git from tracking files that shouldn't be in version control and helps avoid future issues with large files.

### 5. Initial Commit
```bash
git add .
git commit -m "Initial commit"
```
This creates the first commit with all current files (except those ignored by .gitignore).

### 6. Connect and Push to Remote
```bash
git remote add origin https://github.com/pushpullleg/MS-in-CS.git
git push -f origin main
```
These commands:
- Connect the local repository to the GitHub remote
- Force push the new clean history to GitHub

## Important Notes

### Size Limits
- GitHub has a file size limit of 100MB
- Files larger than this should be added to .gitignore
- Consider using Git LFS for large files if necessary

### Best Practices
1. Always check file sizes before committing
2. Keep build artifacts and dependencies out of Git
3. Use .gitignore proactively
4. Consider using Git LFS for large files that must be version controlled

### Warning
Force pushing (`git push -f`) rewrites history on the remote repository. Only use this command when:
- You're sure you want to overwrite the remote history
- You're the only one working on the repository
- You've backed up any important data

### Troubleshooting Future Issues
If you encounter similar issues in the future:
1. Check for large files: `git ls-tree -r --long main | sort -n -k 4 | tail -n 10`
2. Review .gitignore rules
3. Consider using Git LFS for large files
4. Make sure to commit smaller chunks to avoid large repository size

## Additional Resources
- [GitHub file size limits documentation](https://docs.github.com/en/repositories/working-with-files/managing-large-files)
- [Git LFS documentation](https://git-lfs.github.com/)
- [GitHub .gitignore templates](https://github.com/github/gitignore)
