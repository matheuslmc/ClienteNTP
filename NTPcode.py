from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct, time, sched
import datetime
 


def getNTPTime(host = "pool.ntp.org"):
        port = 123
        buf = 1024
        address = (host,port)
        msg = '\x1b' + 47 * '\0'
 
        # Criando tempo de agora...
        ct = datetime.datetime.now()
        
 
        #Conectar num servidor
        client = socket.socket( AF_INET, SOCK_DGRAM)
        client.sendto(msg.encode('utf-8'), address)
        msg, address = client.recvfrom( buf )
 
        t = struct.unpack( "!12I", msg )[10]
        t -= ct
        return time.ctime(t).replace("  "," ")
	
	while True:
		time.sleep(600)
		print("O horário agora é de:", ct)
	
 
if _name_ == "_main_":
        print(getNTPTime())


