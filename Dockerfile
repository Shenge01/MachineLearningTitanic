# initialise a base image
FROM python:3.6.15-bullseye
ENV FLASK_APP app.py
# define the present working directory
WORKDIR /MachineLearningTitanic
# copy the contents into the working directory
ADD . /MachineLearningTitanic
# run pip to install the dependencies on the flask app
RUN pip3 install -r requirements.txt 
# define the command to start the container
CMD ["flask", "run"]