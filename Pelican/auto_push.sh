#!/bin/bash

# Run Pelican command
pelican content -o .. -s pelicanconf.py

# Check if there are any changes to commit
if [[ `git status --porcelain` ]]; then
  # Add all changes
  git add .

  # Commit changes with a message
  git commit -m "Update site content"

  # Push changes to the remote repository
  git push origin main
else
  echo "No changes to commit."
fi

