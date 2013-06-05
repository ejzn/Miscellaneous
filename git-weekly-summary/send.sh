#!/bin/bash

# Parse Command line arguments
BRANCH=$1
SUBJECT='Weekly Git Log Report'
EMAIL='erik@erikjohnson.ca'

# Update git and get the commit logs of the remote origin for the specific branch
git fetch
/bin/mail -s "$SUBJECT" "$EMAIL" < < git log origin/$BRANCH --since='monday' >> /tmp/git-commit-weekly.txt

# Now let's do the real work on the email front


