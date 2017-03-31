---
title: "Reload with SSH keys"
description: "Reloads a server with an image template and some ssh keys"
date: "2016-01-28"
classes: ["SoftLayer_Hardware_Server"]
tags:
    - "reloadOperatingSystem"
    - "reload"
    - "server"
---


```python
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):
        """
        Will reload the operating system with a new imageTemplate, 
        along with a set of sshKeys. This will erease all data.
        """
        # Change these IDs
        imageId = 1234567
        sshKey1 = 123
        sshKey2 = 456
        serverId = 102938
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
