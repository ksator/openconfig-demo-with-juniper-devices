### Parse native configuration and return and OpenConfig object

from napalm_base import get_network_driver
import napalm_yang
from json import dumps

junos_driver = get_network_driver('junos')
junos_device = {'username': 'pytraining', 'password': 'Poclab123', 'hostname': '172.30.179.95'}

with junos_driver(**junos_device) as d:
  running_config = napalm_yang.base.Root()
  running_config.add_model(napalm_yang.models.openconfig_interfaces)
  running_config.parse_config(device=d)

print dumps(running_config.get(filter=True), indent=4)

"""
# python ./native_to_openconfig.py
{
    "interfaces": {
        "interface": {
            "lo0": {
                "name": "lo0",
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
                                        "192.179.0.95": {
                                            "ip": "192.179.0.95",
                                            "config": {
                                                "ip": "192.179.0.95",
                                                "prefix-length": 32
                                            }
                                        },
                                        "127.0.0.1": {
                                            "ip": "127.0.0.1",
                                            "config": {
                                                "ip": "127.0.0.1",
                                                "prefix-length": 32
                                            }
                                        }
                                    }
                                }
                            },
                            "config": {
                                "enabled": True,
                                "name": "0"
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
                    "type": "softwareLoopback",
                    "enabled": True,
                    "name": "lo0"
                }
            },
            "me0": {
                "name": "me0",
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
                                        "172.30.179.95": {
                                            "ip": "172.30.179.95",
                                            "config": {
                                                "ip": "172.30.179.95",
                                                "prefix-length": 24
                                            }
                                        }
                                    }
                                }
                            },
                            "config": {
                                "enabled": True,
                                "name": "0"
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
                    "name": "me0"
                }
            },
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
"""
