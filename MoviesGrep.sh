# !bin/bash

movies_path="../Movies"
movies_file="./movies.txt"
series_path="../Series"
series_file="./series.txt"

rm -f $movies_file $series_file


if [ ! -d "$movies_path" ]; then
	echo "Folder not found"
	exit 1
fi
if [ ! -d "$series_path" ]; then
	echo "Folder not found"
	exit 1
fi


for subfolder in "$movies_path"/*; do
	if [ -d "$subfolder" ]; then
		name=$(basename "$subfolder")
		echo "$name" >> $movies_file 
	fi
done
echo "File ($movies_file) has been created" 

for subfolder in "$series_path"/*; do
	if [ -d "$subfolder" ]; then
		name=$(basename "$subfolder")
		echo "$name" >> $series_file 
	fi
done
echo "File ($series_file) has been created" 


