---
title: "Backup and Restore firewall rules"
description: "A quick example on how to backup firewall rules to a file and restore those rules."
date: "2016-03-07"
classes: 
    - "SoftLayer_Network_Vlan_Firewall"
    - "SoftLayer_Network_Firewall_Update_Request"
tags:
    - "firewall"
    - "manager"
---

restoreRules here will clobber any existing rules on the firewall, so be careful with that. 

```

import SoftLayer
from SoftLayer.CLI import firewall
from pprint import pprint as pp
import json
from argparse import ArgumentParser

class ruleSaver():

    def __init__(self, path, fw):
        self.client = SoftLayer.Client()
        self.fw = SoftLayer.FirewallManager(self.client)
        self.path = path
        self.fw_type, self.fw_id = firewall.parse_id(fw)

    def saveRules(self):
        if self.fw_type == 'vlan':
            rules = self.fw.get_dedicated_fwl_rules(self.fw_id)
        else:  
            rules = self.fw.get_standard_fwl_rules(self.fw_id)
        with open(self.path, 'w') as f:
            json.dump(rules,f)
        print("Done saving rules to %s" % self.path)

    def restoreRules(self):
        with open(self.path, 'r') as f:
            rules = json.load(f)
        if self.fw_type == 'vlan':
            result = self.fw.edit_dedicated_fwl_rules(self.fw_id,rules)
        else:  
            result = self.fw.edit_standard_fwl_rules(self.fw_id,rules)
        return result

if __name__ == "__main__":
    
    parser = ArgumentParser(description='Backup/Restore firewall rules')
    parser.add_argument('-f', nargs=1, type=str, required=True, metavar="[/path/to/file]", dest="path",
        help="File to save to / restore from")
    parser.add_argument('-i', nargs=1, type=str, required=True, metavar="[type:id]", dest="fw",
        help="Firewall ID, same format as 'slcli firewall list'. vlan:1234, vs:1234, sever:1234")
    parser.add_argument('-a', nargs=1, type=str, required=True, metavar="[save|restore]", dest="action",
        help="save to file, or restore from file. restore completely overwrites any existing rules")

    args = parser.parse_args()
    main = ruleSaver(args.path[0],args.fw[0])
    action = args.action[0]

    if action == 'restore':
        result = main.restoreRules()
        pp(result)
    else:
        main.saveRules()

```
