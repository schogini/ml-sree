
cd $1
#CLASS/codebasics-py-git/ML

rm -f index.html
echo "<html><body><pre>" > index.tmp

for ff in $(find . -type f -name "*.html")
do
 echo "<a href=\"$ff\">$ff</a>" >> index.tmp
 #f=$(basename $ff)
 #d=$(dirname $ff)
done

echo "</pre></body></html>" >> index.tmp

mv index.tmp index.html
