# randsomware-chacha20
Uni projekt that should simulate a randsomware attack with the chacha20 cipher

# RUN
cd CC-Server  
docker build -t cc-server .  
docker run ccserver  
    
cd Victim  
docker build -t victim .  
docker run victim  
    
docker exec -it ccserver-id /bin/bash  
docker exec -it victim-id /bin/bash  

    
#in cc-server  
python3 makekey.py  
#in victim  
python3 kenndaten.py  
