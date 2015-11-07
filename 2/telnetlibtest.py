#!/usr/bin/env python

import telnetlib
import time

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
    time.sleep(1)
    remote_conn.write('term len 0\n')
    op = remote_conn.read_very_eager()    
    remote_conn.write('show version\n' )
    
    time.sleep(1)
    op = remote_conn.read_very_eager()    

    print op
    remote_conn.close()


if __name__ == '__main__':
    main()
