---
title: "Reloading a server with a custom partition scheme"
description: "The script will issue an OS reload on your Bare Metal server with a custom partition scheme."
date: "2017-03-29"
classes: ["Hardware_Server"]
tags:
    - "reloadOperatingSystem"
---

The following code allows you to reload a Bare Metal server with a custom partitioning scheme. You simply need to change the serverId and the partitions to suit your needs. Note that one partition must be marked as the 'grow' partition.

```python
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):
        serverId = 1154505
        config = {
        "upgradeHardDriveFirmware": "0",
        "upgradeBios": "0",
        "hardDrives": [
            {
                "complexType": "SoftLayer_Hardware_Component_HardDrive",
                "partitions": [
                    { "name": "/boot", "minimumSize": ".25"},
                    { "name": "/swap0", "minimumSize": "20"},
                    { "name": "/", "minimumSize": "200"},
                    { "name": "/tmp", "minimumSize": "200"},
                    { "name": "/var", "minimumSize": "200"},
                    { "name": "/remove", "minimumSize": "1", "grow": "1"}
                ]
            }
        ]
     }

        output = self.client['Hardware_Server'].reloadOperatingSystem('FORCE', config, id=serverId)

        pp(config)
        print "RESULT\n"
        pp(output)

if __name__ == "__main__":
    main = example()
    main.main()
```