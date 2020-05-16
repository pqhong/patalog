for file in `ls *.js`
do
	npx terser $file -cmo ${file/.js/.min.js}
done