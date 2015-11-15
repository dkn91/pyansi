#!/usr/bin/env python
import paramiko
from getpass import getpass

ip='50.76.53.27'
user='pyclass'
pwd=getpass('88newclass')
port=22

remote_conn =paramiko.SSHClient()
remote_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn.connect(ip,username=user,password=pwd,look_for_keys=False,allow_agent=False,port=port)

rtr_conn = remote_conn.invoke_shell()
rtr_conn.send('show ver\n')
op = rtr_conn.recv(1000)
print op

