---
title: "Attach and Detach a Block Device to a Virtual_Guest"
description: "Attaching and detaching secondary block devices on Virtual Guests"
date: "2016-03-03"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "attachDiskImage"
    - "detachDiskImage"
    - "getPortableStorageVolumes"
    - "checkHostDiskAvailability"
---

Attaching a currently detached portable block device to a given guest. The disk image will need to be migrated to the host the guest is on, so make sure to check if that host has enough disk space (with checkHostDiskAvailability) before attaching. This is only required for guests with local storage guests. SAN based guests don't need that step.

Running this on a disk that is already attached will move the disk to the new guest. 

```python
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):

        self.client = SoftLayer.Client()

    def main(self, image_id, guest_id):
        my_image = self.getMyImage(image_id)
        size = my_image.get("capacity", 100)
        """
        SAN based guests will throw the following exception:
        SoftLayer.exceptions.SoftLayerAPIError: SoftLayerAPIError(SoftLayer_Exception_Public): This guest is SAN-based, and does not require host migration for disk attachment.
        """
        available = self.client['SoftLayer_Virtual_Guest'].checkHostDiskAvailability(size,id=guest_id)
        # This should be True. False means the host doesn't have enough disk space to attach
        pp(available)

        attach = self.client['SoftLayer_Virtual_Guest'].attachDiskImage(image_id, id=guest_id)
        print("Attaching storage")
        pp(attach)

    def getImages(self):

        mask = "mask[type,blockDevices[guest]]"
        images = self.client['SoftLayer_Account'].getPortableStorageVolumes(mask=mask)

        for image in images:
            desc = image.get('description', "---")
            capacity = image.get('capacity', "0")
            print("%s - %s (%s) - %s " % 
                (image['id'], image['type']['keyName'], capacity ,desc)
            )
            for disk in image['blockDevices']:
                try:
                    hostname = disk['guest']['fullyQualifiedDomainName']
                except KeyError:
                    hostname = "None"
                print("\t%s" % hostname)

    def getMyImage(self,imageId):
        mask = "mask[blockDevices[guest],sourceDiskImage,type]"
        image = self.client['SoftLayer_Virtual_Disk_Image'].getObject(mask=mask,id=imageId)
        pp(image)
        return image


if __name__ == "__main__":
    image_id = 12345
    guest_id = 67890
    main = example()
    main.getImages()
    main.main(image_id, guest_id)
    # The new guest will only show up on the image once the migration transaction is completed
    main.getMyImage(image_id)

```