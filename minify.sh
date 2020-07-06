for file in `find . -name *.js`
do
	npx terser $file -cmo ${file/.js/.min.js}
done