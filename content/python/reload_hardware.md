---
title: "Reload with SSH keys"
description: "Load server from an image template and add ssh keys"
date: "2016-01-28"
classes: ["SoftLayer_Hardware_Server"]
tags:
    - "reloadOperatingSystem"
    - "reload"
    - "server"
---

Reloading a hardware server from an image template allows users to restore or reconfigure the server based off a pre-existing Flex Image Template that is associated with the account in use. 

### **List Flex Image Templates**
To retrieve the list of available Flex Image Template in the account it is required to use object-filters over the method SoftLayer_Account::getPrivateBlockDeviceTemplateGroups as following

```python
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):        
        # Object-filter which is used to retrieve Flex Images
        _filter = {"privateBlockDeviceTemplateGroups":{"imageTypeKeyName":{"operation":"DISK_CAPTURE"}}}
        
        # object-mask to retrieve only the id and name of the image
        _mask = "mask[id,name]"

        accountService = self.client['Account']
        # Retrieve all Flex Images in the account
        images = accountService.getPrivateBlockDeviceTemplateGroups(filter=_filter, mask=_mask)

        pp(images)
        
if __name__ == "__main__":
    main = example()
    main.main()

```

### **Load Hardware Server from Flex Image Template**
SoftLayer does not perform internal backups of customer devices, so the data in the device cannot be retrieved after the OS Reload is initiated. Back up all data on the device prior to initiating the OS Reload. 

Post Install Script, SSH Keys, Reset IPMI Password, Apply Motherboard BIOS upgrades, Apply firmware updates for all hard drives, etc., are some of the features that can be added in the server configuration, it is recommended to review [Container_Hardware_Server_Configuration](https://softlayer.github.io/reference/datatypes/SoftLayer_Container_Hardware_Server_Configuration) in order know which additional features can be added.

```python
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):
        # ID of server which will be reloaded
        serverId = 102938        
        # Flex Image ID
        imageId = 1234567
        
        sshKey1 = 123
        sshKey2 = 456

        # Build reload configuration        
        config = {
            'imageTemplateId': imageId, 
            'sshKeyIds': [sshKey1, sshKey2]
        }

        output = self.client['Hardware_Server'].reloadOperatingSystem('FORCE', config, id=serverId)

        pp(config)
        print "RESULT\n"
        pp(output)

if __name__ == "__main__":
    main = example()
    main.main()

```
