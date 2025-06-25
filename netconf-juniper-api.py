#!/usr/bin/env python3

__author__ = 'Jorge Luiz Taioque'
__version__= 0.1

#from ncclient import manager
from texttable import Texttable
import argparse
import sys
import os

from connection import *
sys.path.append(os.path.abspath("function/"))
from nc_system import *
from subscriber import *
from interface import *


#Shot config
defaultnetconfport = 830

class CommandLine:
	def __init__(self):
		parser = argparse.ArgumentParser(description = "Description for my parser")
		parser.add_argument("-H", "--Host", help = "HOST_NAME or IP_ADDRESS", required = False, default = "")
		parser.add_argument("-u", "--user", help = "NETCONF USERNAME", required = False, default = "")
		parser.add_argument("-p", "--password", help = "NETCONF PASSWORD", required = False, default = "")
		parser.add_argument("-n", "--netconfport", help = "NETCONF PORT", required = False, default = "")
		parser.add_argument("-f", "--function", help = "FUNCTION NAME -f ALL FOR ALL OPTIONS", required = False, default = "")
		parser.add_argument("-v", "--vlan", help = "VLAN-ID NUMBER", required = False, default = "")


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
			if function == 'system':
				system(host, netconfport, user, password)
			if function == 'interfaceterse':
				interfaceterse(host, netconfport, user, password)
			if function == 'subscriber':
				subscriber(host, netconfport, user, password)
			if function == 'vlanpppoe':
				vlanPppoe(host, netconfport, user, password)
			if function == 'subscriberforonevlan':
				if vlan:
					numSubscriberForVlan(host, netconfport, user, password, vlan)
				else:
					print ('You must declare vlan with -v VLAN_NUMBER')
			if function == 'subscriberforvlan':
				vlanPppoeCount(host, netconfport, user, password)
			if function == 'interfacepspppoe':
				interfacePsPppoe(host, netconfport, user, password)

			if function == 'ALL':
				print("Usage ./netconf-juniper-api.py -H 200.200.200.200 -u root -p 1234 -n 2222 -f FUNCTION_NAME")
				printHelp = Texttable()
				printHelp.header(['FUNCTION', 'DESCRIBRE'])
				printHelp.add_row(['system', 'show system information'])
				printHelp.add_row(['interfaceterse', 'show all interface as terse'])
				printHelp.add_row(['subscriber', 'show subscribers connected numers as PPPOE, DHCP and all'])
				printHelp.add_row(['vlanpppoe', 'show all vlans used to connect for customers to conect pppoe'])
				printHelp.add_row(['subscriberforonevlan', 'show number of sbscriber using a specific VLAN'])
				printHelp.add_row(['subscriberforvlan', 'show all vlans and how many subscribers is connected in witch vlan and total'])
				printHelp.add_row(['interfacepspppoe', 'show all interface PS and numer of subscribers is connected using witch interface'])
				print (printHelp.draw())


		if not status:
			print("Usage ./netconf-juniper-api.py -H 200.200.200.200 -u root -p 1234 -n 830 -f FUNCTION_NAME")
			printHelp = Texttable()
			printHelp.header(['FUNCTION', 'DESCRIBRE'])
			printHelp.add_row(['system', 'show system information'])
			printHelp.add_row(['interfaceterse', 'show all interface as terse'])
			printHelp.add_row(['subscriber', 'show subscribers connected numers as PPPOE, DHCP and all'])
			printHelp.add_row(['vlanpppoe', 'show all vlans used to connect for customers to conect pppoe'])
			printHelp.add_row(['subscriberforonevlan', 'show number of sbscriber using a specific VLAN'])
			printHelp.add_row(['subscriverforvlan', 'show all vlans and how many subscribers is connected in witch vlan and total'])
			printHelp.add_row(['interfacepspppoe', 'show all interface PS and numer of subscribers is connected using witch interface'])
			print (printHelp.draw())

if __name__ == '__main__':
    app = CommandLine()
