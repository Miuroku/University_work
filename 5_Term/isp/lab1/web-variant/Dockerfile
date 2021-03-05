FROM python:3.9

# update operating system.
#RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

# set and create work directory.
RUN mkdir -p /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/

# install dependencies
#RUN pip install --upgrade pip
RUN pip install django

# not sure that i need that.
#RUN pip install -r requirements.txt

EXPOSE 8000

# sets where commands'll run.
ENTRYPOINT ["python", "./my_first_dj_project/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]