---
title: "Create Virtual Guest with tags"
description: "Simple sample which creates a VSI with tags"
date: "2019-01-09"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```python
import SoftLayer
from pprint import pprint

class example():

    def __init__(self):
        self.client = SoftLayer.create_client_from_env()
        self.guest = self.client['Virtual_Guest']

    def create_instance(self, object_template, tags=None):
        try:
            instance = self.guest.createObject(object_template)
            
            if tags is not None:
                self.guest.setTags(tags, id=instance['id'])
            
            return self.guest.getObject(mask='mask[tagReferences[id,tag]]', id=instance['id'])
        except SoftLayer.SoftLayerAPIError as e:
            pprint("Exception occurred when creating the instance: "  % (e.faultCode, e.faultString))


if __name__ == "__main__":
    # skeleton of vsi object
    object_template = {
        "datacenter": {"name": "dal05"},
        "hostname": "foobar",
        "domain": "example.com",
        "startCpus": 1,
        "maxMemory": 1024,
        "hourlyBillingFlag": True,
        "localDiskFlag": True,
        "operatingSystemReferenceCode": "UBUNTU_LATEST"
    }

    # tags that will be added to the vsi
    tags = "tag1, tag2"

    main = example()
    guest = main.create_instance(object_template, tags=tags)

    pprint(guest)

```
