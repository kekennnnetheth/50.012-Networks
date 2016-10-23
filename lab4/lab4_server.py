# Tan Shun Yu 1001171, Nigel Leong 1001095
import socket
import sys

# Run-once application
count = 0

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

# Bind the socket to the port
server_address = ('10.0.0.2', 5555)
sock.bind(server_address)

boolean = True

def runServer():
	try:
		count = 0
		while True:
		    print ('\nwaiting to receive message')		    
		    data, address = sock.recvfrom(100000)
		    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
		    if data:
			segidarr = data.split(',')
			segid = segidarr[0]
			print('segment '+segid+' received.')
		 	count += 1
	except socket.timeout:
		print ('no of packets received: %s' % str(count))
		if count != 5:
			print('WARNING: missing datagrams.')


while (boolean == True):	
	runServer()
	reset = raw_input("Do you want to try again? (y/n) ")
	if reset == 'n' or reset == 'N':
		boolean = False



