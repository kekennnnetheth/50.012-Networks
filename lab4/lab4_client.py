# Tan Shun Yu 1001171, Nigel Leong 1001095
import socket
import sys
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('10.0.0.2', 5555)
message = 'a' # 1 byte = 8 bits
count = 1
packet = raw_input("Enter your preferred bandwidth in Mbit/s: ")

try:
    while (count<=5):
        # Send data
	sock.sendto(str(count) + "," + message*int(float(packet)*25000), server_address)
        print('sent segment '+str(count))
        count += 1

finally:
    time.sleep(1) #sleep for 1 second
    print >>sys.stderr, 'closing socket'
   
    sock.close()
