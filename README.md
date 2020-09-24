# AFTS
this is an AutoFillTemperatueSystem  
build docker image : docker build -t aftsimg --no-cache .    
run container : docker run -t -d --name afts aftsimg  
exec with sh : docker exec -it afts /bin/sh  
run script : cd /app;python autoFill.py  

## when reboot gce cron will run runService.sh to exec python code
docker start afts; docker exec -t afts python  /app/autoFill.py > /home/cubemail88/xx.log
