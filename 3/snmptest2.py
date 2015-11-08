#!/usr/bin/env python
from snmp_helper import snmp_get_oid_v3,snmp_extract


oids=(
    ('sysname','1.3.6.1.2.1.1.5.0','none'),
    ('sysuptime','1.3.6.1.2.1.1.3.0','none'),
    ('ifdesc_fa4','1.3.6.1.2.1.2.2.1.2.5','none'),
    ('ifinoctets_fa4','1.3.6.1.2.1.2.2.1.10.5','none'),
    ('ifinucastpkt_fa4','1.3.6.1.2.1.2.2.1.11.5','none'),
    ('ifoutoctets_fa4','1.3.6.1.2.1.2.2.1.16.5','none'),
    ('ifoutucastpkts_fa4','1.3.6.1.2.1.2.2.1.17.5','none'),
)

port_rtr = (7961, 8061)

def snmp_poll(_conn,_usercred,oid):
    data = snmp_get_oid_v3(_conn,_usercred,oid)
    return snmp_extract(data)+'\n'



def main():
    #main method
    ip = '50.76.53.27'
    _authkey = 'galileo1'
    _encryptkey = 'galileo1'
    _user = 'pysnmp'
    _usercred = (_user,_authkey,_encryptkey)

    for port in port_rtr:
        _conn = (ip, port)
        for desc,oid,val in oids:
            op= snmp_poll(_conn,_usercred,oid)
            print desc, op

if __name__=='__main__':
    main()
