# Juniper Netconf API

A simple API using Netconf to get information of Juniper Devices

## Install python and library on ubunt
```
apt install python3
apt install pythin3-pip

pip3 install ncclient
```
### Some ubuntu versions is necessary install ncclient over apt
```
apt install -y python-ncclient
```

## Install pyhon and library on windows
Only downsload and install python3 for windows and install libery using PIP
```
pip3 install ncclient
```

## Download
```
bash
wget
chmod +x netconf-juniper-api-py
```

## How to use

```
./netconf-juniper-api.py argparse
ARGS:
-H = IP or Hostname
-u = username
-p = password
-n = Netconf port, If do not use this argument default port is 2222
-f = Function, select one possivel function
-v = Vlan ID number
```
Working functions:
```
interfaceterce = Show all interface like terse command showing Operational operStatus
subscriber = show subscriber statistic pppoe, dhcp and total of Sessions
vlanpppoe = show all vlans that juniper device recognize and autenticate a subscribers
subscriberforonevlan = show how many subscriber is connected using a especific vlan
subscriberforvlan = show all vlans and how many subscrbers is coonected per vlan, and the total of subscriber souting and sum all vlans
```
