#!/bin/bash

# Parse Command line arguments
BRANCH=$1
SUBJECT='Weekly Git Log Report'
EMAIL='erik@erikjohnson.ca'
TFILE="/tmp/git-weekly.$$.tmp"

#MAke a temp file if it doesn't exist

if [ ! -e "$TFILE" ] ; then
    touch "$TFILE"
fi

# Update git and get the commit logs of the remote origin for the specific branch
git fetch

echo 'Writing git commit history to temporary storage'
git log origin/$BRANCH --since='last monday' >> $TFILE

echo 'Mailing to' $EMAIL
mail -s "$SUBJECT" --to "$EMAIL" < $TFILE

echo 'Cleaning up'
# Clenaup
if [ -f "$TFILE" ] ; then
    rm "$TFILE"
fi
