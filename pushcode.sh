#!/bin/bash

# Initialize repository if not already initialized
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit: Solar System Explorer project"

# Rename the default branch to main
git branch -M main

# Add the remote repository
git remote add origin https://github.com/arrhenius975/Solar_System_Explorer.git

# Push to GitHub with force flag to overwrite any existing history
git push -u origin main --force
