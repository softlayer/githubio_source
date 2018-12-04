---
title: "Ordering RAID Through API"
description: "As a SoftLayer user, you have probably seen the beautiful RAID Configurator that greets you when you order a server in the control portal. This API example explains how to build that."
date: "2014-04-22"
author: "hansKristian"
tags:
    - "blog"
    - "baremetalservers"
    - "raid"
---

> See also [orderBareMetal/](/python/orderBareMetal/)

As a SoftLayer user, you have probably seen the beautiful RAID Configurator that greets you when you order a server on the SoftLayer website.

It allows you to do anything you like, from a straight RAID configuration involving all drives in a single disk array, to a much more intricate configuration with nearly any mix of disks and RAID types.

However beautiful and practical the interface, sometimes you want to script this process, and the SoftLayer mantra of "Anything you can do in the Web interface, you can do on the API" also rings true in this case.

## Single RAID group
If all your drives are the same and you simply want a single RAID group, be it RAID 0,1,5 or 10, you can achieve this by ordering the corresponding disk controller.

When building your order template you will see that RAID-enabled servers are listed with multiple disk controllers. Here's an example of the relevant price IDs from package 53 (Intel Xeon 3200 Series):

```
Category "Disk Controller":
     876 -- Non-RAID
     877 -- RAID 0
     878 -- RAID 1
     879 -- RAID 5
     880 -- RAID 10
     22482 -- RAID
```

So ordering an Intel 3260 server with RAID 10 through the API could look like this:

```ruby
require 'rubygems'
require 'softlayer_api'
 
$SL_API_USERNAME = " PLEASE SET ME "
$SL_API_KEY = " PLEASE SET ME TOO "
 
client = SoftLayer::Service.new("SoftLayer_Product_Order");
 
order = {
 :complexType => 'SoftLayer_Container_Product_Order_Hardware_Server',
 :quantity => 1,
 :hardware => [{:hostname => 'raidtest', :domain => 'example.com'}],
 :location => 168642, # San Jose 1
 :packageId => 53, # Intel Xeon 3200 Series
 :prices => [
  {:id => 2050}, # Single Processor Quad Core Xeon 3460 - 2.80GHz (Lynnfield) - 1 x 8MB cache w/HT
  {:id => 17438}, # -- Ubuntu Linux 12.04.0 LTS Precise Pangolin - Minimal Install (64 bit)
  {:id => 21004}, # 4 GB DDR3 Registered 1333
  {:id => 880}, # Disk controller -- RAID 10 
  {:id => 1257}, # First hard drive -- 147GB SA-SCSI 10K RPM
  {:id => 1256}, # Second hard drive -- 147GB SA-SCSI 10K RPM
  {:id => 825}, # Third hard drive -- 147GB SA-SCSI 10K RPM
  {:id => 825}, # Fourth hard drive -- 147GB SA-SCSI 10K RPM
  {:id => 728}, # 0 GB Bandwidth
  {:id => 898}, # 100 Mbps Private Network
  {:id => 906}, # Reboot / KVM over IP  
  {:id => 420}, # Unlimited SSL VPN Users & 1 PPTP VPN User per account
  {:id => 55}, # Host Ping
  {:id => 418}, # Nessus Vulnerability Assessment & Reporting
  {:id => 57}, # Notification -- Email and Ticket
  {:id => 58} # Response -- Automated Notification
 ]
}
 
result = client.verifyOrder(order)
## Uncomment when you are ready to order
# client.placeOrder(order)
```

## Multiple RAID groups
When ordering multiple RAID groups you need to order the Disk Controller type called RAID, and specify your RAID groups in an attribute in the order template called storageGroups.
storageGroups is of the type [SoftLayer_Container_Product_Order_Storage_Group](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Product_Order_Storage_Group) and the most important attributes can be explained as:


>arrayTypeId: Integer - Required
Can be retrieved from [SoftLayer_Configuration_Storage_Group_Array_Type::getAllObjects](https://sldn.softlayer.com/reference/services/SoftLayer_Configuration_Storage_Group_Array_Type)[^1]
hardDrives: Array of integers - Required
Array of drives to take part in the given raid array. 0 = first drive, 1 = second drive, etc

>hotSpareDrives: array of integers - Optional
On raid types where hot spare is allowed, you can specify which drives to use as hot spare.
Raid types that allow hot spare can be retrieved from [SoftLayer_Configuration_Storage_Group_Array_Type::getAllObjects](https://sldn.softlayer.com/reference/services/SoftLayer_Configuration_Storage_Group_Array_Type)[^1]

>partitionTemplateId: integer - Optional
To be used on the array where the operating system is to be installed.
Partition Template IDs for the relevant operating system can be retrieved from
[SoftLayer_Hardware_Component_Partition_OperatingSystem::getPartitionTemplates](https://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Component_Partition_OperatingSystem/getPartitionTemplates)
use [SoftLayer_Hardware_Component_Partition_OperatingSystem::getAllObjects](https://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Component_Partition_OperatingSystem)[^1] to get a list of operating system groups that has partition templates

Let's say, for example, you want to have a server with a single SSD drive for the operating system, also hosting a large 12GB swap partition, and a separate RAID array with 3 striped 147GB SAS Drives.

The first thing we'll need to do is specify the controller and drives we want in our order template.

```
{:id => 22482}, # Disk controller -- RAID
{:id => 13756}, # First hard drive -- 50GB SSD
{:id => 1256}, # Second hard drive -- 147GB SA-SCSI 10K RPM
{:id => 825}, # Third hard drive -- 147GB SA-SCSI 10K RPM
{:id => 825}, # Fourth hard drive -- 147GB SA-SCSI 10K RPM
```

To configure the RAID groups we need to populate storageGroups
The disks will be addressed in the order of their placement and template, starting at disk 0.
So for the first disk that we want to be on its own we will use arrayTypeId 9, which is JBOD, and specify partitionTemplateId 226 which specifies a 12GB Swap partition

```ruby
{
        :arrayTypeId => 9, # JBOD -- Other types available from SoftLayer_Configuration_Storage_Group_Array_Type::getAllObjects
        :hardDrives => [0], # First Hard Drive (50GB SSD)
        :partitionTemplateId => 226, # Custom partition template - 12GB Swap
        :arraySize => 50
},
```

For the second group we specify arrayTypeId 1, which is RAID 0 - Striped

```ruby
{
        :arrayTypeId => 1, # RAID 0 -- Other types available from SoftLayer_Configuration_Storage_Group_Array_Type::getAllObjects
        :hardDrives => [1,2,3] # Second, third and fourth hard drives (147GB SAS),
        :arraySize => 147
}
```
All together, the order will look like this:

```ruby
require 'rubygems'
require 'softlayer_api'
 
$SL_API_USERNAME = " PLEASE SET ME "
$SL_API_KEY = " PLEASE SET ME TOO "
 
client = SoftLayer::Service.new("SoftLayer_Product_Order");
 
order = {
 :complexType => 'SoftLayer_Container_Product_Order_Hardware_Server',
 :quantity => 1,
 :hardware => [{:hostname => 'raidtest', :domain => 'example.com'}],
 :location => 168642, # San Jose 1
 :packageId => 53, # Intel Xeon 3200 Series
 :prices => [
  {:id => 2050}, # Single Processor Quad Core Xeon 3460 - 2.80GHz (Lynnfield) - 1 x 8MB cache w/HT
  {:id => 17438}, # -- Ubuntu Linux 12.04.0 LTS Precise Pangolin - Minimal Install (64 bit)
  {:id => 21004}, # 4 GB DDR3 Registered 1333
  {:id => 22482}, # Disk controller -- RAID
  {:id => 13756}, # First hard drive -- 50GB SSD
  {:id => 1256}, # Second hard drive -- 147GB SA-SCSI 10K RPM
  {:id => 825}, # Third hard drive -- 147GB SA-SCSI 10K RPM
  {:id => 825}, # Fourth hard drive -- 147GB SA-SCSI 10K RPM
  {:id => 728}, # 0 GB Bandwidth
  {:id => 898}, # 100 Mbps Private Network
  {:id => 906}, # Reboot / KVM over IP  
  {:id => 420}, # Unlimited SSL VPN Users & 1 PPTP VPN User per account
  {:id => 55}, # Host Ping
  {:id => 418}, # Nessus Vulnerability Assessment & Reporting
  {:id => 57}, # Notification -- Email and Ticket
  {:id => 58} # Response -- Automated Notification
 ],
 
 :storageGroups => [
     { # RAID Array 1
        :arrayTypeId => 9, # JBOD
        :hardDrives => [0], # First Hard Drive (50GB SSD)
        :partitionTemplateId => 226 # Custom partition template - 12GB Swap,
        :arraySize => 50
     },
     { # RAID Array 2
        :arrayTypeId => 1, # RAID 0
        :hardDrives => [1,2,3] # Second, third and fourth hard drives (147GB SAS),
        :arraySize => 147
     }
  ]
}

 
result = client.verifyOrder(order)
## Uncomment when you're ready to order
# client.placeOrder(order)
Links and other useful information
order_multiple_raid_groups.rb
order_single_raid_group.rb
get_package_options.rb (command line tool)
```
//hansKristian

[^1]: These getAllObjects() calls don't show up in the documentation on SLDN, however they do still work. 