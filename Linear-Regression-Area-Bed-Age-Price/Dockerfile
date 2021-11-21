FROM python:3.8-slim-buster

RUN mkdir /app
WORKDIR /app
RUN mkdir -p ../lib
RUN mkdir -p data
RUN pip3 install -t ../lib numpy pandas 
RUN pip3 install -t ../lib -U scikit-learn
RUN pip3 install -t ../lib -U matplotlib

ADD *.py .
ADD *.dat data
ADD *.csv data
CMD ["python3","load.py","3300","3","40"]


#docker build -t tmp .
#docker run tmp ls -l ../lib

#SreeMacMin16GB-1215:Linear-Regression-Area-Price sree$ ls -l data/
#total 16
#-rw-r--r--@ 1 sree  staff   71 Nov  7 17:38 homeprices.csv
#-rw-r--r--  1 sree  staff  568 Nov  7 17:52 model.dat


# SreeMacMin16GB-1215:Linear-Regression-Area-Bed-Age-Price sree$ docker run -v $(pwd)/data:/app/data tmp python train-save.py
#    area  bedrooms  age   price
# 0  2600       3.0   20  550000
# 1  3000       4.0   15  565000
# 2  3200       NaN   18  610000
# 3  3600       3.0   30  595000
# 4  4000       5.0    8  760000
# 5  4100       6.0    8  810000
# [498408.25158031]
# SreeMacMin16GB-1215:Linear-Regression-Area-Bed-Age-Price sree$ docker run -v $(pwd)/data:/app/data tmp python load.py 3300 3 40
# [498408.25158031]
# [532026.98416295]

#SreeMacMin16GB-1215:Linear-Regression-Area-Price sree$ ls -l data/
#total 16
#-rw-r--r--@ 1 sree  staff   71 Nov  7 17:38 homeprices.csv
#-rw-r--r--  1 sree  staff  568 Nov  7 17:57 model.dat
