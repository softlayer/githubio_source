---
title: "Edit IP address note"
description: "Shows how to get and set the notes for individual IP addresses."
date: "2015-12-11"
classes:
  - "SoftLayer_Account"
  - "SoftLayer_Network_Subnet"
  - "SoftLayer_Network_Subnet_IpAddress"
tags:
  - "subnet"
  - "notes"
  - "ip address"
---



```python
import SoftLayer

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def getSubnets(self):
        subnets = self.client['SoftLayer_Account'].getSubnets()
        for subnet in subnets:
            print("%s - %s/%s - %s" % 
                (   subnet['id'],
                    subnet['gateway'],
                    subnet['cidr'],
                    subnet['networkVlanId']
                )
            )

    def getIpInSubnet(self, subnet_id):
        mask = "mask[virtualGuest,hardware]"
        subnet = self.client['SoftLayer_Network_Subnet']
        ips = subnet.getIpAddresses(id=subnet_id,mask=mask)
        for ip in ips:
            status = "Free"
            if ip['subnet']['subnetType'] == "PRIMARY":
                status = "Reserved"
            elif ip['isNetwork']:
                status = "Network Ip"
            elif ip['isGateway']:
                status = "Gateway Ip"
            try: 
                status = ip['virtualGuest']['fullyQualifiedDomainName']
            except KeyError:
                pass
            try:
                status = ip['hardware']['fullyQualifiedDomainName']
            except KeyError:
                pass

            try:
                note = ip['note']
            except KeyError:
                note = "none"
            print("%s: %s - %s - %s" % (ip['id'],ip['ipAddress'],status, note))

    def editNote(self, ip_id, note):
        """
            With editObject on SoftLayer_Network_Subnet_IpAddress you can only 
            edit the note, everything else will get ignored silently.
        """
        ip = {
            'id': ip_id,
            'note': note,
        }
        self.client['SoftLayer_Network_Subnet_IpAddress'].editObject(ip,id=ip_id)

if __name__ == "__main__":
    # CHANGE ME
    subnet_ip = 1234
    # CHANGE ME
    ip_id = 4567
    main = example()
    # List all subnets, find the ID of the one you want to work with
    main.getSubnets()
    # List all the IPs and their notes, find the id of the one you want to edit
    main.getIpInSubnet(subnet_ip)
    # Edit the note
    main.editNote(ip_id,"Hello World22")
```