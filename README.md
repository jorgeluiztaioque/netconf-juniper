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
## Configuring Juniper devices - Enable Netconf
```
set system services netconf ssh port 830
```
Ps. Do not forget of allow tcp port 830 on Router-Engine protection or in outbox firewall

## Download
```
On bash
wget https://github.com/jorgeluiztaioque/netconf-juniper.git
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

### Runing examples
```
./netconf-juniper-api.py -H 10.10.10.1 -u netconf -p 123456789 -n 830 -f subscriber
Numbers of VLANS = 111
Numbers of PPPOE = 14339
Numbers of DHCPV6 = 11744
Total of Sessions = 26193
```

```
./netconf-juniper-api.py -H 10.10.10.1 -u netconf -p 123456789 -f subscriberforonevlan -v 1661
Total Subscribers on vlan 1661 = 19
```

```
./netconf-juniper-api.py -H 10.10.10.1 -u netconf -p 123456789 -f subscriberforvlan
Total Subscribers on vlan 836 = 478
Total Subscribers on vlan 831 = 391
Total Subscribers on vlan 834 = 301
Total Subscribers on vlan 838 = 192
Total Subscribers on vlan 830 = 303
Total Subscribers on vlan 835 = 338
Total Subscribers on vlan 833 = 384
Total Subscribers on vlan 829 = 270
Total Subscribers on vlan 837 = 212
Total of Subscribers = 2869

```

```
./netconf-juniper-api.py -H 10.10.10.1 -u netconf -p 123456789 -f vlanpppoe
836
831
834
838
830
835
833
829
837
832
839
840
Total numbers of vlans is = 12
```
