rmdir output
rm -f log.txt
mkdir output
cd PADAMANJARI/PADAMANJARI
shopt -s nullglob
array=(*.*)
cd ../..

for FILENAME in "${array[@]}"
do
	# conversion
	python preprocess.py 'PADAMANJARI/PADAMANJARI/'$FILENAME
done
