#!/usr/bin/env python3

from texttable import Texttable
import sys
import os

sys.path.append(os.path.abspath("../"))
from connection import *

def system(host, netconfport, user, password):

	terminal = "show system information"
	result = (connection(host, netconfport, user, password, terminal))

	hardware = result.xpath('system-information/hardware-model')
	osName = result.xpath('system-information/os-name')
	osVersion = result.xpath('system-information/os-version')
	serial = result.xpath('system-information/serial-number')
	hostName = result.xpath('system-information/host-name')

	res = Texttable()
	res.add_rows([['Hostname', (hostName[0].text).strip()], ['Hardware',(hardware[0].text).strip()], ['OS Name', (osName[0].text).strip()], ['OS Version', (osVersion[0].text).strip()], ['Serial Number', (serial[0].text).strip()]])
	print (res.draw())
