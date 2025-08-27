#!/usr/bin/env python3

import json

def get_inventory_data():
    return {
        "local": {                          #inventory group name
            "hosts": ["local"],                #list of hosts in group
            "vars": {                          #group vars that apply to all hosts in this group
                "ansible_host": "192.168.1.9",
                "ansible_user": "ayush",
                #"ansible_ssh_pass": ""
            }
        },
        "azure": {
            "hosts": ["azure_vm"],
            "vars": {
                "ansible_host": "172.171.236.12",
                "ansible_user": "ayush",
                #"ansible_ssh_pass": ""
            }
        },
        "demo": {
            "children": ["local","azure"],
            "vars": {
                
            }
        }
    }

if __name__ == "__main__":
    inventory_data = get_inventory_data()
    print(json.dumps(inventory_data))