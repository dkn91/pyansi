#!/usr/bin/env python
from snmp_helper import snmp_get_oid,snmp_extract

oid='1.3.6.1.2.1.1.5.0'
comm = 'galileo'
port = 7961
  
def main():
    #main method
    ip = '50.76.53.27'
    _conn=(ip,comm,port)
    data = snmp_get_oid(_conn,oid)
    print snmp_extract(data)

if __name__=='__main__':
    main()
