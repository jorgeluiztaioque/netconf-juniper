#!/usr/bin/env python3

__author__ = 'Jorge Luiz Taioque'
__version__= 0.1

from ncclient import manager
import argparse
import sys

#Shot config
defaultnetconfport = 2222

class CommandLine:
	def __init__(self):
		parser = argparse.ArgumentParser(description = "Description for my parser")
		parser.add_argument("-H", "--Host", help = "Example: Help argument", required = True, default = "")
		parser.add_argument("-u", "--user", help = "Example: Save argument", required = True, default = "")
		parser.add_argument("-p", "--password", help = "Example: Print argument", required = True, default = "")
		parser.add_argument("-n", "--netconfport", help = "Example: Output argument", required = False, default = "")
		parser.add_argument("-f", "--function", help = "Example: Output argument", required = False, default = "")
		parser.add_argument("-v", "--vlan", help = "Example: Output argument", required = False, default = "")

		argument = parser.parse_args()
		status = False

		if argument.Host:
			global host
			host = (argument.Host)
			status = True
		if argument.user:
			global user
			user = (argument.user)
			status = True
		if argument.password:
			global password
			password = (argument.password)
			status = True
		if argument.netconfport:
			global netconfport
			netconfport = (argument.netconfport)
			status = True
		else:
			netconfport = defaultnetconfport
		if argument.vlan:
			global vlan
			vlan = (argument.vlan)
			status = True
		else:
			vlan = ''
		'''
		FUNCTION SELECT
		'''
		if argument.function:
			global function
			function = (argument.function)
			status = True
			if function == 'interfaceterse':
				interfaceterse()
			if function == 'subscriber':
				subiscriber()
			if function == 'vlanpppoe':
				vlanPppoe()
			if function == 'subscriberforonevlan':
				if vlan:
					numSubscriberForVlan(vlan)
				else:
					print ('You must declare vlan with -v VLAN_NUMBER')
			if function == 'subscriberforvlan':
				vlanPppoeCount()
			if function == 'interfacepspppoe':
				interfacePsPppoe()

		if not status:
			print("Maybe you want to use -H or -u or -p or -n or -f or -v as arguments ?")

def connection(terminal2):
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

def interfaceterse():

	terminal = "show interface terse"
	result = (connection(terminal))
	size = len(result.xpath('interface-information/physical-interface/name'))
	for i in range(size):
		interface = result.xpath('interface-information/physical-interface/name')
		oper = result.xpath('interface-information/physical-interface/oper-status')
		interfaceName = (interface[i].text).strip()
		operStatus = (oper[i].text).strip()
		print (interfaceName+' '+operStatus)

def subiscriber():

	terminal = "show subscriber summary"
	result = (connection(terminal))

	vlan = result.xpath('subscribers-summary-information/counters/session-type-vlan')
	pppoe = result.xpath('subscribers-summary-information/counters/session-type-pppoe')
	dhcp = result.xpath('subscribers-summary-information/counters/session-type-dhcp')
	total = result.xpath('subscribers-summary-information/counters/session-state-active')

	if len(vlan):
		vlanPppoe = (vlan[0].text).strip()
		print ('Numbers of VLANS = '+vlanPppoe)
	if len(pppoe):
		pppoeCount = (pppoe[0].text).strip()
		print ('Numbers of PPPOE = '+pppoeCount)
	if len(dhcp):
		dhcpCount = (dhcp[0].text).strip()
		print ('Numbers of DHCPV6 = '+dhcpCount)

	totalCount = (total[0].text).strip()

	print ('Total of Sessions = '+totalCount)


def vlanPppoe():

	terminal = "show subscriber"
	result = (connection(terminal))

	size = len(result.xpath('subscribers-information/subscriber/vlan-id'))
	for i in range(size):
		subVlan = result.xpath('subscribers-information/subscriber/vlan-id')
		subscriberVlan = (subVlan[i].text).strip()
		print (subscriberVlan.replace('0x8100.',''))
	print ('Total numbers of vlans is = '+str(size))

def numSubscriberForVlan(vlan):

	terminal = ('show subscribers vlan-id '+str(vlan))
	result = (connection(terminal))

	#subscribers-information/subscriber/user-name
	size = len(result.xpath('subscribers-information/subscriber/ip-address'))
	print ('Total Subscribers on vlan '+str(vlan)+' = '+str(size))

def numSubscriberForVlanCount(vlan):

	terminal = ('show subscribers vlan-id '+str(vlan))
	result2 = (connection(terminal))

	#subscribers-information/subscriber/user-name
	size = len(result2.xpath('subscribers-information/subscriber/ip-address'))
	return vlan, size
	#print ('Total Subscriber on vlan '+str(vlan)+' = '+str(size))

def vlanPppoeCount():

	terminal = "show subscriber"
	result = (connection(terminal))
	total = 0
	size = len(result.xpath('subscribers-information/subscriber/vlan-id'))
	for i in range(size):
		subVlan = result.xpath('subscribers-information/subscriber/vlan-id')
		subscriberVlan = (subVlan[i].text).strip()
		vlan, size = numSubscriberForVlanCount(subscriberVlan.replace('0x8100.',''))
		print ('Total Subscribers on vlan '+str(vlan)+' = '+str(size))
		total = total+size
	print ('Total of subscribers = '+str(total))
	subiscriber()

def interfacePsPppoe():

	terminal = "show interface ps*"

	result = (connection(terminal))

	size = len(result.xpath('interface-information/physical-interface/name'))
	for i in range(size):
	  interfaces = result.xpath('interface-information/physical-interface/name')
	  interface = (interfaces[i].text).strip()
	  terminal2 = ('show subscribers summary physical-interface '+str(interface))
	  result2 = (connection(terminal2))
	  numSubscriber = result2.xpath('subscribers-summary-information/counters/session-type-pppoe')
	  if numSubscriber:
	    totalSubscriber = (numSubscriber[0].text).strip()
	    print ('Interface = '+interface+' pppoe = '+totalSubscriber)


if __name__ == '__main__':
    app = CommandLine()
