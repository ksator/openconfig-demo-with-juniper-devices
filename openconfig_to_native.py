### Translate OpenConfig to native configuration

from napalm_base import get_network_driver
import napalm_yang

junos_driver = get_network_driver('junos')
device = junos_driver(hostname = '172.30.179.95', username = 'pytraining', password = 'Poclab123', optional_args = {'profile':["junos"]})

conf = napalm_yang.base.Root()
conf.add_model(napalm_yang.models.openconfig_interfaces())
#type(conf)

oc_config = {
    "interfaces": {
        "interface": {
            "ge-0/0/1": {
                "name": "ge-0/0/1",
                "subinterfaces": {
                    "subinterface": {
                        "0": {
                            "index": "0",
                            "ipv4": {
                                "config": {
                                    "enabled": True
                                },
                                "addresses": {
                                    "address": {
                                        "192.168.0.1": {
                                            "ip": "192.168.0.1",
                                            "config": {
                                                "ip": "192.168.0.1",
                                                "prefix-length": 31
                                            }
                                        }
                                    }
                                }
                            },
                            "config": {
                                "enabled": True,
                                "name": "0",
                                "description": "ex4300-18"
                            }
                        }
                    }
                },
                "routed-vlan": {
                    "ipv4": {
                        "config": {
                            "enabled": False
                        }
                    }
                },
                "config": {
                    "type": "ethernetCsmacd",
                    "enabled": True,
                    "name": "ge-0/0/1"
                }
            },
            "ge-0/0/0": {
                "name": "ge-0/0/0",
                "subinterfaces": {
                    "subinterface": {
                        "0": {
                            "index": "0",
                            "ipv4": {
                                "config": {
                                    "enabled": True
                                },
                                "addresses": {
                                    "address": {
                                        "192.168.0.5": {
                                            "ip": "192.168.0.5",
                                            "config": {
                                                "ip": "192.168.0.5",
                                                "prefix-length": 31
                                            }
                                        }
                                    }
                                }
                            },
                            "config": {
                                "enabled": True,
                                "name": "0",
                                "description": "ex4300-17"
                            }
                        }
                    }
                },
                "routed-vlan": {
                    "ipv4": {
                        "config": {
                            "enabled": False
                        }
                    }
                },
                "config": {
                    "type": "ethernetCsmacd",
                    "enabled": True,
                    "name": "ge-0/0/0"
                }
            }
        }
    }
}

conf.load_dict(oc_config)
print(conf.translate_config(device.profile))

'''
# python openconfig_to_native.py
<configuration>
  <interfaces>
    <interface>
      <name>ge-0/0/1</name>
      <unit>
        <name>0</name>
        <family>
          <inet>
            <address>
              <name>192.168.0.1/31</name>
            </address>
          </inet>
        </family>
        <description>ex4300-18</description>
      </unit>
    </interface>
    <interface>
      <name>ge-0/0/0</name>
      <unit>
        <name>0</name>
        <family>
          <inet>
            <address>
              <name>192.168.0.5/31</name>
            </address>
          </inet>
        </family>
        <description>ex4300-17</description>
      </unit>
    </interface>
  </interfaces>
</configuration>
'''

