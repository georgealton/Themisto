import socket

class baseSocket():
    
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
    def closeSocket(self):
        self.socket.close()

class serverSideSocket(baseSocket):
	
	def __init__(self):
	   baseSocket.__init__(self)
	   self.localhost = '127.0.0.1'
	   self.port = 50009
	   self.socket.bind((self.localhost, self.port))
	   print('Bound server socket created')
	   
	def waitForConnection(self):
	    self.socket.listen(1)
	    print('Waiting for incomming connection...')
	    self.conn, addr = self.socket.accept()
	    print('Connection recieved from: ' + self.addr)
	   
		
class clientSideSocket(baseSocket):
	
	def __init__(self):
	   baseSocket.__init__(self)
	   self.localhost = '127.0.0.1'
	   self.port = 50008
	   
	def connectToServer(self, serverIP):
	    self.serverIP = serverIP
	    self.socket.connect((serverIP, self.port))
		
#test
#s = serverSideSocket()
#s.waitForConnection()
#s.closeSocket()
