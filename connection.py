#!/usr/bin/env python3

from ncclient import manager

def connection(host, netconfport, user, password, terminal2):
	conn = manager.connect(
		host = host,
		port = netconfport,
		username = user,
		password = password,
		timeout = 100,
		device_params = {'name':'junos'},
		hostkey_verify = False)
	#print (terminal2)
	result = conn.command(terminal2, format='xml')
	conn.close_session()
	return result
