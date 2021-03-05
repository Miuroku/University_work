FROM python:3.9

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

# Copies all the stuff from current dir on machine to dir inside conteiner.
COPY . /usr/src/app/ 

# Executes those script in shell inside conteiner.
CMD ["python", "first_script.py"]