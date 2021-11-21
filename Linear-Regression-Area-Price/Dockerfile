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
CMD ["python3","load.py","3300"]


#docker build -t tmp .
#docker run tmp ls -l ../lib

#SreeMacMin16GB-1215:Linear-Regression-Area-Price sree$ ls -l data/
#total 16
#-rw-r--r--@ 1 sree  staff   71 Nov  7 17:38 homeprices.csv
#-rw-r--r--  1 sree  staff  568 Nov  7 17:52 model.dat
#SreeMacMin16GB-1215:Linear-Regression-Area-Price sree$ docker run -v $(pwd)/data:/app/data tmp python train-save.py
#   area   price
#0  2600  550000
#1  3000  565000
#2  3200  610000
#3  3600  680000
#4  4000  725000
#[628715.75342466]
#SreeMacMin16GB-1215:Linear-Regression-Area-Price sree$ docker run -v $(pwd)/data:/app/data tmp python load.py 3300
#[628715.75342466]
#[628715.75342466]
#SreeMacMin16GB-1215:Linear-Regression-Area-Price sree$ ls -l data/
#total 16
#-rw-r--r--@ 1 sree  staff   71 Nov  7 17:38 homeprices.csv
#-rw-r--r--  1 sree  staff  568 Nov  7 17:57 model.dat
