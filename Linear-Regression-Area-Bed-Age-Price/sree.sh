
SreeMacMin16GB-1215:Log-Reg-Iris sree$ time ./train-save.py 
[2]
[2 0]

real	0m3.514s
user	0m1.384s
sys	0m0.491s
SreeMacMin16GB-1215:Log-Reg-Iris sree$ time ./load.py 
[2 0]

real	0m2.063s
user	0m1.173s
sys	0m0.316s
SreeMacMin16GB-1215:Log-Reg-Iris sree$ 

SreeMacMin16GB-1215:Linear-Regression-Area-Bed-Age-Price sree$ python3 train-save.py 
   area  bedrooms  age   price
0  2600       3.0   20  550000
1  3000       4.0   15  565000
2  3200       NaN   18  610000
3  3600       3.0   30  595000
4  4000       5.0    8  760000
5  4100       6.0    8  810000
[498408.25158031]
SreeMacMin16GB-1215:Linear-Regression-Area-Bed-Age-Price sree$ python3 load.py 3000 3 40
[498408.25158031]
[498408.25158031]


