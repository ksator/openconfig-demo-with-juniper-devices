from jinja2 import Template
from yaml import load
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

# my_list_of_devices.yml yaml file has the list of devices. my_list_of_devices is a python variable (python list).
f=open('my_list_of_devices.yml')
data=f.read()
my_list_of_devices=load(data)
f.close()

#bgp.j2 is a jinja2 template to build BGP OC configuration file. template is object (instance of the class Template)
f=open('bgp.j2')
data=f.read()
template=Template(data)
f.close()

# build from a jinja2 template the configuration file for each device
print '\nbuild the configuration file for each device from a jinja2 template:'
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
print 'done for all the devices\n'

# load and commit the configuration file for each device
print 'applying the configuration files to the devices ...'
for item in my_list_of_devices:
    dev = Device(host=item["management_ip"], user='tiaddemo', password='OpenConfig')
    dev.open()
    cfg=Config(dev)
    cfg.load(path=item["host_name"]+'.oc.bgp.conf', format='text')
    if cfg.commit(comment="from PyEZ") == True:
        print ('configuration commited on ' + item["host_name"])
    else:
        print ('commit failed on ' + item["host_name"])
    dev.close()
print ('done for all the devices\n')
