#!/usr/bin/env python3

from texttable import Texttable
import sys
import os

sys.path.append(os.path.abspath("../"))
from connection import *

def interfaceterse(host, netconfport, user, password):

	terminal = "show interface terse"
	result = (connection(host, netconfport, user, password, terminal))
	size = len(result.xpath('interface-information/physical-interface/name'))
	for i in range(size):
		interface = result.xpath('interface-information/physical-interface/name')
		oper = result.xpath('interface-information/physical-interface/oper-status')
		interfaceName = (interface[i].text).strip()
		operStatus = (oper[i].text).strip()
		print (interfaceName+' '+operStatus)
