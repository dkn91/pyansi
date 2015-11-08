#!/usr/bin/env python
from snmp_helper import snmp_get_oid,snmp_extract

oid1='1.3.6.1.2.1.1.5.0'
oid2='1.3.6.1.2.1.1.1.0'
comm = 'galileo'
port_rtr1 = 7961
port_rtr2 = 8061

def snmp_poll(ip,comm,port,oid):
    _conn=(ip,comm,port)
    data = snmp_get_oid(_conn,oid)
    return snmp_extract(data)+'\n'



def main():
    #main method
    ip = '50.76.53.27'
    op= snmp_poll(ip,comm,port_rtr1,oid1)
    op+= snmp_poll(ip,comm,port_rtr1,oid2)
    op+= snmp_poll(ip,comm,port_rtr2,oid1)
    op+= snmp_poll(ip,comm,port_rtr2,oid2)

    print op

if __name__=='__main__':
    main()
