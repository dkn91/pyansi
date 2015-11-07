#!/usr/bin/env python

import telnetlib
import time


def send_cmd(remote_conn, cmd):
    cmd=cmd.rstrip()
    remote_conn.write(cmd+"\n")
    time.sleep(1)
    return remote_conn.read_very_eager()    
     

def main():
    print 'hello'
    ip = '50.76.53.27'
    user= 'pyclass'
    password='88newclass'
    tport = 23
    ttimeout = 6
    remote_conn = telnetlib.Telnet(ip, tport, ttimeout)
    op = remote_conn.read_until('username:', ttimeout)
    remote_conn.write(user+'\n')
    op = remote_conn.read_until('password:', ttimeout)
    remote_conn.write(password+'\n' )

    op=send_cmd(remote_conn,'term len 0')
    op=send_cmd(remote_conn,'show ver')    
    print op
    remote_conn.close()


if __name__ == '__main__':
    main()
