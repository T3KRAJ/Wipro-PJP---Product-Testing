// Tek Raj Joshi
// Superset ID: 1368453

#!/bin/sh
mkdir tmp

func1 () {
        read -p "Enter the directory: " direc
}

func1

func2 () {
        UNDER=$direc"_"
        BACKFILE="$UNDER$(date '+%m_%d_%y').bkp"
}

func2

func3 () {
        cd tmp
        tar --create --file="$BACKFILE" "/root/store"
        echo "Archive created"
}

func3