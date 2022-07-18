// Tek Raj Joshi
// Superset ID: 1368453

#!/bin/sh
echo "What absolute directory do you want to count?"
read DIR
cd $DIR
files=`ls`
file=0;
dir=0;
bdf=0;
cdf=0;
for d in $files
do
dir=`expr $dir + 1`
done
for f in $files
do
file=`expr $file + 1`
done
for b in $files
do
bdf=`expr $bdf + 1`
done
for c in $files
do
cdf=`expr $cdf + 1`
done
echo "Files $file"
echo "Directories $dir"
echo "Block Device files $bdf"
echo "Character special files $cdf"