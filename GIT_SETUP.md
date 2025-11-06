# Git Setup Guide

## ✅ Git is Now Configured!

Your repository is initialized and ready to use.

### Current Configuration

```bash
User: nico-
Email: nico-@users.noreply.github.com
Branch: main
Commit: Initial commit completed ✅
```

## 📦 What Was Done

1. **Git Configured**: Set up username and email
2. **Repository Initialized**: Created `.git` directory
3. **Gitignore Created**: Added `.gitignore` to exclude temporary files
4. **Zone.Identifier Files Removed**: Cleaned up Windows metadata files
5. **Initial Commit Created**: All files committed (31 files, 6549 lines)

## 🚀 Connect to GitHub

### Option 1: Using GitHub Desktop (Recommended for You)

Since you have GitHub Desktop installed, you can use it:

1. **Open GitHub Desktop** (your shortcut at `C:\Users\nico-\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\GitHub, Inc\GitHub Desktop.lnk`)

2. **Add this repository**:
   - File → Add Local Repository
   - Browse to: `\\wsl$\Ubuntu\home\onik\proyects\AI\Hello_Britannica`
   - Click "Add Repository"

3. **Publish to GitHub**:
   - Click "Publish repository" button
   - Choose repository name: `Hello_Britannica`
   - Add description: "Test case management for Hello Britannica project"
   - Uncheck "Keep this code private" if you want it public
   - Click "Publish Repository"

### Option 2: Using Command Line

If you prefer command line:

```bash
# Create a new repository on GitHub first (via web browser)
# Then run these commands:

# Add the remote
git remote add origin https://github.com/nico-/Hello_Britannica.git

# Push to GitHub
git push -u origin main
```

### Option 3: Using GitHub CLI

```bash
# Install GitHub CLI (if not already)
# Then authenticate and push:
gh auth login
gh repo create Hello_Britannica --source=. --public --push
```

## 📝 Common Git Commands

### Daily Workflow

```bash
# Check status
git status

# Stage all changes
git add .

# Commit changes
git commit -m "Your commit message"

# Push to GitHub
git push

# Pull latest changes
git pull
```

### Create a New Branch

```bash
# Create and switch to new branch
git checkout -b feature/your-feature-name

# Push new branch to GitHub
git push -u origin feature/your-feature-name
```

### View History

```bash
# Show commit history
git log --oneline

# Show detailed log
git log

# Show changes in last commit
git show
```

## 🔧 Git Configuration

Your Git is configured with:

```bash
# View all config
git config --list

# Change name
git config --global user.name "Your Name"

# Change email
git config --global user.email "your.email@example.com"
```

## 📂 What's Tracked

All project files are now tracked except:
- Python cache files (`__pycache__`, `*.pyc`)
- Virtual environments (`venv/`, `.venv/`)
- IDE files (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`, `Thumbs.db`, `*:Zone.Identifier`)
- Excel temp files (`~$*.xlsx`)
- Backup files (`*.bak`, `*_BACKUP.*`, `*_TEMP.*`)

See `.gitignore` for full list.

## 🔗 GitHub Desktop + WSL

To access your WSL folders in GitHub Desktop:
1. In File Explorer, type: `\\wsl$\Ubuntu\home\onik\proyects\AI\Hello_Britannica`
2. Copy this path
3. Use it in GitHub Desktop's "Add Local Repository"

## 🆘 Troubleshooting

### Issue: "Permission denied"
```bash
# Check SSH keys
ls -la ~/.ssh

# Generate new SSH key (if needed)
ssh-keygen -t ed25519 -C "nico-@users.noreply.github.com"

# Add to GitHub: https://github.com/settings/keys
```

### Issue: "Remote already exists"
```bash
# Remove old remote
git remote remove origin

# Add correct remote
git remote add origin https://github.com/nico-/Hello_Britannica.git
```

### Issue: "Failed to push"
```bash
# Pull first (if remote has changes)
git pull origin main --allow-unrelated-histories

# Then push
git push -u origin main
```

## ✅ Next Steps

1. **Push to GitHub** using GitHub Desktop or command line
2. **Add a README badge** (optional): ![GitHub](https://img.shields.io/github/last-commit/nico-/Hello_Britannica)
3. **Set up branch protection** (optional) for main branch
4. **Enable GitHub Actions** (optional) for automated testing

## 📚 Resources

- [GitHub Desktop Documentation](https://docs.github.com/en/desktop)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [GitHub Guides](https://guides.github.com/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)

---

**Your repository is ready!** 🎉

Just open GitHub Desktop and publish it to start collaborating.
