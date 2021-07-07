# Интернет магазин на Django

## For run project locally : 

**First way** <br>
1.Copy docker-compose-prod.yml <br>
2.Run <br>
```sh
docker-compose -f docker-compose-prod.yml up --build
```

**Second way** <br>
0)  Copy project <br>
1) Change file 'web-store/my_config.py' и занести туда настройки почты. <br>
2) Run docker container : <br>
    ```sh
    docker-compose -f docker-compose.yml up --build
    ```
<br>

- image from Docker-hub : https://hub.docker.com/r/miuroku/lab34_web

