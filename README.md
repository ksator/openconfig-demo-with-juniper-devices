# About this project:   
Automation content about Openconfig on Juniper devices.

## Openconfig repository
The published versions of OpenConfig modules can be found at https://github.com/openconfig/public/tree/master/release/models 

## Lab topology
There are two Juniper routers. There are directly connected between them.  
The Openconfig modules and the corrsponding translation scripts are alreday installed on the two devices. 

## Automation

### Ansible
Ansible to interact with the Juniper routers.

##### Ansible Inventory file:  
The default 'hosts' file is supposed to live in /etc/ansible/hosts  
The inventory file we are using in this repository is **hosts**. It is at the root of the repository (https://github.com/ksator/openconfig-demo/blob/master/hosts), so it is not at the default place.  
There are 2 devices in the inventory file: **MX240-04** and **FR-MX80-214**.  They belong to the group **Openconfig_Routers**.   
This file also defines the ip address of each device with the variable **junos_host**. This variable is used in the playbooks.     

##### Ansible config file for ansible:   
There is an **ansible.cfg** file at the root of the repository (https://github.com/ksator/openconfig-demo/blob/master/ansible.cfg).  
It refers to our inventory file (**hosts**): So, despite the inventory file is not /etc/ansible/hosts, there is no need to add -i hosts to the ansible-playbook commands: the playbooks will find automatically the inventory file.      

#### Ansible variables:   
**group_vars** and **host_vars** directories at the root of this repository define the variables. 
**group_vars** defines the variables for the groups, **host_vars** defines the variables for the hosts.  
The inventory file (**hosts** file at the root of the repository) also defines some variables (**junos_host**).     
Ansible can find automatically the variables defined in the **group_vars** and **host_vars** directories and the **hosts** file.  

##### Ansible playbooks:  
All playbooks are named **pb.*.yml**. They are at the root of the repository.    
- **pb.oc.bgp.yaml** -This playbook uses the junja2 template **bgp.j2** to render an Openconfig BGP configuration file for each device (**MX240-04.conf** and **FR-MX80-214.conf**). It then configures the devices. It then checks on the configured devices if the actual new  operationnal state is equal to the expected operationnal state.    
- **pb.rollback.yml** -This playbook rollbacks the configuration on the devices.  

##### Usage:

##### Continuous integration with Travis CI
The playbooks in  this repository are tested automatically by Travis CI (https://travis-ci.org/ksator/openconfig-demo).    
The files **.travis.yml** and **requirements.txt** at the root of this repository are used for this.  
ansible-playbook has a built in option to check only the playbook's syntax (--syntax-check). This is how Travis is testing our playbooks that interact with Junos. If there are any syntax error, Travis will fail the build and output the errors in the log. Travis CI doesnt actually connect to the devices. 

##### More examples on of how to use Ansible with Juniper devices:   
For more examples, you can visit this repository https://github.com/ksator/ansible-training-for-junos

### Python

#### Pyang

#### Pyangbind

#### PyEZ

#### ncclient


## Contributions, bugs, questions, enhancement requests:      
Please submit github issues or pull requests.  

