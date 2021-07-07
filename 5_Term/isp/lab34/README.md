# Интернет магазин на Django

## For run project locally : 

**First way**
<br>1.Copy docker-compose-prod.yml
2.Run
```sh
docker-compose -f docker-compose-prod.yml up --build
```

**Second way**
0)  Copy project     

1) Change file 'web-store/my_config.py' и занести туда настройки почты.

2) Run docker container :
    $ docker-compose -f docker-compose.yml up --build


- image from Docker-hub : https://hub.docker.com/r/miuroku/lab34_web

