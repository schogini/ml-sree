
#CLASS/codebasics-py-git

fol=CLASS/codebasics-py-git/ML

old=$(pwd)
cd $fol

#echo "<html><body><pre>" > index.tmp

for ff in $(find . -type f -name "*.ipynb")
do
 echo $ff
 f=$(basename $ff)
 d=$(dirname $ff)
 docker run -v $(pwd)/$d:/data schogini/jp jupyter nbconvert --to html --execute \
 /data/$f --output /data/$f.html --ExecutePreprocessor.kernel_name=python3

done

#There is also other format : markdown, html, pdf, ipynb, etc

cd $old
sh index-html.sh $fol

