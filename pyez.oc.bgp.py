#USAGE: python python.pyez.oc.bgp.py my_list_of_devices.yml

from jinja2 import Template
from yaml import load
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.op.bgp import BGPNeighborTable
import time
import sys

''' 
argv[1] is the first command-line argument. 
my_list_of_devices.yml is a yaml file with the list of devices. my_list_of_devices is a python variable (python list).
'''
f=open(sys.argv[1])
data=f.read()
my_list_of_devices=load(data)
f.close()

#bgp.j2 is a jinja2 template to build BGP OC configuration file. template is object (instance of the class Template)
f=open('bgp.j2')
data=f.read()
template=Template(data)
f.close()

# build from a jinja2 template the configuration file for each device
print '\nBuilding the configuration file for each device from a jinja2 template:'
for item in my_list_of_devices:
    # get the variables definition for this item. item_vars is a python variable (dictionary) 
    f=open('host_vars/'+item["host_name"]+'/bgp.yml')
    data=f.read()
    item_vars=load(data)
    f.close()
    # build the configuration file from a jinja2 template for this item using the variable item_vars
    print item["host_name"]+'.oc.bgp.conf'
    conffile=open(item["host_name"]+'.oc.bgp.conf','w')
    conffile.write(template.render(item_vars))
    conffile.close()
print 'Done for all the devices!\n'

# load and commit the configuration file for each device
print 'Pushing and Committing the configuration files to the devices ...'
for item in my_list_of_devices:
    dev = Device(host=item["management_ip"], user='tiaddemo', password='OpenConfig')
    dev.open()
    cfg=Config(dev)
    cfg.load(path=item["host_name"]+'.oc.bgp.conf', format='text')
    if cfg.commit(comment="from PyEZ") == True:
        print ('Configuration commited successfully on ' + item["host_name"])
    else:
        print ('Commit failed on ' + item["host_name"])
    dev.close()
print 'Done for all the devices!\n'

# Wait for 20 seconds. so BGP sessions will be established.  
print 'Waiting 20 seconds before auditing BGP sessions state ...\n'
time.sleep(20)


'''
audit BGP states with tables and view
Please add table and view for bgp before as it is not provided by PyEZ.
'''
print 'Auditing the BGP states using PyEZ Tables and Views:'
for device in my_list_of_devices:
    dev = Device(host=device["management_ip"], user='tiaddemo', password='OpenConfig') 
    dev.open()
    bgp=BGPNeighborTable (dev)
    bgp.get()
    print "\nStatus of BGP sessions for device " + device["host_name"] + ':'
    for item in bgp:
        print item.neighbor + " is " + item.state
    dev.close()
print '\nDone for all the devices!\n'

print 'auditing the BGP states using NetConf standard operations to pull state data (config false of OpenConfig YANG modules)'
from lxml import etree
from lxml.builder import E
rpc = E('get', E('filter', {'type': 'xpath', 'source': '/bgp'}))
for item in my_list_of_devices:
    dev = Device(host=item["management_ip"], user='tiaddemo', password='OpenConfig')
    dev.open()
    op = dev.execute(rpc)
    print op.findtext("bgp/neighbors/neighbor/state/session-state")
    assert(op.findtext("bgp/neighbors/neighbor/state/session-state")=="ESTABLISHED"), "BGP OC Neighbor is not established"
    dev.close()



