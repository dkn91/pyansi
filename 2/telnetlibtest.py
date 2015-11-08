#!/usr/bin/env python

import telnetlib
import time
import socket
import sys

tport = 23
ttimeout = 6

def send_cmd(remote_conn, cmd):
    cmd=cmd.rstrip()
    print cmd
    remote_conn.write(cmd+"\n")
    time.sleep(1)
    return remote_conn.read_very_eager()    
     
def login(remote_conn, user, password):
    op = remote_conn.read_until('username:', ttimeout)
    remote_conn.write(user+'\n')
    op = remote_conn.read_until('password:', ttimeout)
    remote_conn.write(password+'\n' )

def telnet_connect(ip):
    try:
        return telnetlib.Telnet(ip, tport, ttimeout)
    except socket.error:
        sys.exit('Connection timedout')
 
def main():
    ip = '50.76.53.27'
    user= 'pyclass'
    password='88newclass'
    
    remote_conn = telnet_connect(ip)
    login(remote_conn, user, password)

    op=send_cmd(remote_conn,'term len 0')
    op=send_cmd(remote_conn,'show inter desc')    
    print op
    op=send_cmd(remote_conn,'config') 
    print op
    send_cmd(remote_conn,'')
    send_cmd(remote_conn,'interface loopback 99')    
    op =send_cmd(remote_conn,"description created_by_deepak")    
    print op
    op=send_cmd(remote_conn,'exit')    
    print op
    send_cmd(remote_conn,'exit')    
    op=send_cmd(remote_conn,'show inter desc')    
    print op
    remote_conn.close()

if __name__ == '__main__':
    main()
