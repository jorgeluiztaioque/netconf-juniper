#!/usr/bin/env python3

import sys
import os

sys.path.append(os.path.abspath("../"))
from connection import *

def subscriber(host, netconfport, user, password):

	terminal = "show subscriber summary"
	result = (connection(host, netconfport, user, password, terminal))

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

def vlanPppoe(host, netconfport, user, password):

	terminal = "show subscriber"
	result = (connection(host, netconfport, user, password, terminal))

	size = len(result.xpath('subscribers-information/subscriber/vlan-id'))
	for i in range(size):
		subVlan = result.xpath('subscribers-information/subscriber/vlan-id')
		subscriberVlan = (subVlan[i].text).strip()
		print (subscriberVlan.replace('0x8100.',''))
	print ('Total numbers of vlans is = '+str(size))

def numSubscriberForVlan(host, netconfport, user, password, vlan):

	terminal = ('show subscribers vlan-id '+str(vlan))
	result = (connection(host, netconfport, user, password, terminal))

	#subscribers-information/subscriber/user-name
	size = len(result.xpath('subscribers-information/subscriber/ip-address'))
	print ('Total Subscribers on vlan '+str(vlan)+' = '+str(size))

def numSubscriberForVlanCount(host, netconfport, user, password, vlan):

	terminal = ('show subscribers vlan-id '+str(vlan))
	result2 = (connection(host, netconfport, user, password, terminal))

	#subscribers-information/subscriber/user-name
	size = len(result2.xpath('subscribers-information/subscriber/ip-address'))
	return vlan, size
	#print ('Total Subscriber on vlan '+str(vlan)+' = '+str(size))

def vlanPppoeCount(host, netconfport, user, password):

	terminal = "show subscriber"
	result = (connection(host, netconfport, user, password, terminal))
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

def interfacePsPppoe(host, netconfport, user, password):

	terminal = "show interface ps*"

	result = (connection(host, netconfport, user, password, terminal))

	size = len(result.xpath('interface-information/physical-interface/name'))
	for i in range(size):
	  interfaces = result.xpath('interface-information/physical-interface/name')
	  interface = (interfaces[i].text).strip()
	  terminal2 = ('show subscribers summary physical-interface '+str(interface))
	  result2 = (connection(host, netconfport, user, password, terminal2))
	  numSubscriber = result2.xpath('subscribers-summary-information/counters/session-type-pppoe')
	  if numSubscriber:
	    totalSubscriber = (numSubscriber[0].text).strip()
	    print ('Interface = '+interface+' pppoe = '+totalSubscriber)
