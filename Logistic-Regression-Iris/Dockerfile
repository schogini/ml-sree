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
#docker run -v $(pwd)/data:/app/data tmp python train-save.py
#docker run -v $(pwd)/data:/app/data tmp python load.py
#[2 0]