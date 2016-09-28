# About this project:   
Openconfig demo with Juniper routers

## Openconfig repository
The repository for publishing OpenConfig models is https://github.com/openconfig/public   
The published versions of OpenConfig modules can be found at https://github.com/openconfig/public/tree/master/release/models 

## Lab topology
There are two Juniper routers. There are directly connected between them.   

## Automation

### Ansible
I used Ansible to interact with the Juniper routers.

##### Ansible Inventory file:  
The default 'hosts' file is supposed to live in /etc/ansible/hosts  
The inventory file we are using in this repository is **hosts**. It is at the root of the repository (https://github.com/ksator/openconfig-demo/blob/master/hosts), so it is not at the default place.  
There are 2 devives in the inventory file: MX240-04 and FR-MX80-214.  They belong to the same group (Openconfig_Routers).   
This file also define the ip address of each device with the variable **junos_host**. This variable is reused in the playbooks.     

##### Ansible config file for ansible:   
There is an **ansible.cfg** file at the root of the repository (https://github.com/ksator/openconfig-demo/blob/master/ansible.cfg).  
It refers to our inventory file (**hosts**): So, despite the inventory file is not /etc/ansible/hosts, there is no need to add -i hosts to the ansible-playbook commands.  

#### Ansible variables:   
**group_vars** and **host_vars** directories at the root of this repository define the variables for the hosts and for the group.  
The inventory file (**hosts** file at the root of the repository) also defines some variables.   

##### Ansible playbooks:  
All playbooks are named **pb.*.yml**. They are at the root of the repository.    
- **pb.oc.bgp.yaml** -This playbook use the template **bgp.j2** to render an Openconfig BGP configuration file for each device (**MX240-04.conf** and **FR-MX80-214.conf**). It then configure the devices. It then checks on the configured devices if the new operationnal state is equal to the desirated/expected operationnal state.    
- **pb.rollback.yml** -This playbook rollbacks the configuration on the devices.  

##### Continuous integration with Travis CI
There is a github webhook with Travis CI (https://travis-ci.org/ksator/openconfig-demo)
The playbooks in  this repository are tested automatically by Travis CI.  
The files **.travis.yml** and **requirements.txt** at the root of this repository are used for this.  
ansible-playbook has a built in option to check only the playbook's syntax (--syntax-check). This is how Travis is testing our playbooks that interact with Junos. If there are any syntax error, Travis will fail the build and output the errors in the log. 


##### More examples on of how to use Ansible with Junos:   
For more examples, you can visit this repository https://github.com/ksator/ansible-training-for-junos

## Contributions, bugs, questions, enhancement requests:      
Please submit github issues or pull requests.  

