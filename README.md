server will run on internal 5000 port only due to docker compose
docker-compose -f docker-compose.yml up -d --build --scale app=3 

then check this URL on browser
http://localhost/test

result should be like this:
container id: 1654f7113cd2 