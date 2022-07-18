// Tek Raj Joshi
// Superset ID: 1368453

#!/bin/sh
echo "Select a option"
echo "1. Disk free statisitcs"
echo "2. Virtual Memory Statistics"
echo "3. Real Time Processes"
echo "4. exit"
echo -n "Enter your choice [1-4]: "

while :
do

read choice

case $choice in
1) df;;
2) vmstat;;
3) top;;
4) echo "exiting"
    exit;;
*) echo "invalid choice";;
esac 
    echo -n "Enter your choice [1-4]: "
done
