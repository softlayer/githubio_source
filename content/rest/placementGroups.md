---
title: "Working with Placement Groups"
description: "Collection of examples on how to work with placement groups."
date: "2019-02-14"
classes:
    - "Virtual_PlacementGroup"
    - "Virtual_PlacementGroup_Rule"
tags:
  - "virtualguest"
---

## [Placement Groups](https://console.bluemix.net/docs/vsi/vsi_placegroup.html#placement-groups)


### Creation
To create a group, we need to know a few pieces of information. With the slcli this can all be obtained with `slcli vs placementgroup create-options`

1. Router (Pod in a datacenter) the group should be located behind.

```bash
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" 'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_PlacementGroup/getAvailableRouters.json'
```

[Virtual_PlacementGroup::getAvailableRouters()](/reference/services/SoftLayer_Virtual_PlacementGroup/getAvailableRouters) will print a list of all routers that support placement groups. You will need the router ID listed.

2. Rule which the group should enforce

```bash
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" 'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_PlacementGroup_Rule/getAllObjects.json'
```
[SoftLayer_Virtual_PlacementGroup_Rule::getAllObjects()](/reference/services/SoftLayer_Virtual_PlacementGroup_Rule/getAllObjects/) will print a list of rules useable, keep track of the Id. At the moment there is only the 'SPREAD' rule which ensures each VSI is on a different host. 

3. Name that we want to give the group.
This is always the hardest part, sadly we don't have an API to generate a name for you.


Next, create the instance.

[SoftLayer_Virtual_PlacementGroup::createObject()](/reference/services/SoftLayer_Virtual_PlacementGroup/createObject/) takes as an argument a [SoftLayer_Virtual_PlacementGroup](/reference/datatypes/SoftLayer_Virtual_PlacementGroup/) datatype. You only need to supply `backendRouterId`, `name`, `ruleId`. 

`slcli vs placementgroup create --name test1234 -b bcr01.wdc01 -r SPREAD`

```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [{"name": "test1234", "backendRouterId": 16358, "ruleId": 1}]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_PlacementGroup/createObject.json'
```


### Listing
`slcli vs placementgroup list`

To list out all the placement groups, we use [SoftLayer_Account/getPlacementGroups](/reference/services/SoftLayer_Account/getPlacementGroups/)
with the mask `mask[id, name, createDate, rule, guestCount, backendRouter[id, hostname]]` 

```bash
curl -u $SL_USER:$SL_APIKEY -X GET 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getPlacementGroups.json?objectMask=mask%5Bid%2C+name%2C+createDate%2C+rule%2C+guestCount%2C+backendRouter%5Bid%2C+hostname%5D%5D'
```

### Deleting
`slcli -vvv  vs placementgroup delete test1234`

Deleting is pretty easy, first you will need the PlacementGroup id, then just call [SoftLayer_Virtual_PlacementGroup::deleteObject()](/reference/services/SoftLayer_Virtual_PlacementGroup/deleteObject/)

```bash
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_PlacementGroup/81435/deleteObject.json
```


To delete a PlacementGroup, it is required all servers in that group be delete. You can use `slcli -vvv  vs placementgroup delete test1234 --purge` for that, or simply delete each VSI beforehand.

### Adding VSIs to a group.
To create a VSI in a placement group, you need to supply the placementGroupId in your [SoftLayer_Container_Product_Order_Virtual_Guest](/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Guest/) container. This information is added at the same level hostname and domain are set. 

`slcli vs create -H test12345 -D test.com -f  B1_1X2X25 -d mex01 -o DEBIAN_LATEST --placementgroup test12345`

```bash
curl -u $SL_USER:$SL_APIKEY -X POST  -d '
{"parameters": [{
    "imageTemplateId": null,
    "location": "449600",
    "packageId": 1035,
    "presetId": 583,
    "prices": [{
        "hourlyRecurringFee": "0",
        "id": 202563,
        "recurringFee": "0",
        "item": {
            "description": "Debian GNU/Linux 9.x Stretch/Stable - Minimal Install (64 bit) "
        }
    }, {
        "hourlyRecurringFee": "0",
        "id": 2202,
        "recurringFee": "0",
        "item": {
            "description": "25 GB (SAN)"
        }
    }, {
        "hourlyRecurringFee": "0",
        "id": 905,
        "recurringFee": "0",
        "item": {
            "description": "Reboot / Remote Console"
        }
    }, {
        "hourlyRecurringFee": "0",
        "id": 210301,
        "recurringFee": "0",
        "item": {
            "description": "100 Mbps Public & Private Network Uplinks"
        }
    }, {
        "hourlyRecurringFee": "0",
        "id": 1800,
        "item": {
            "description": "0 GB Bandwidth Allotment"
        }
    }, {
        "hourlyRecurringFee": "0",
        "id": 21,
        "recurringFee": "0",
        "item": {
            "description": "1 IP Address"
        }
    }, {
        "hourlyRecurringFee": "0",
        "id": 210349,
        "recurringFee": "0",
        "item": {
            "description": "Host Ping and TCP Service Monitoring"
        }
    }, {
        "hourlyRecurringFee": "0",
        "id": 57,
        "recurringFee": "0",
        "item": {
            "description": "Email and Ticket"
        }
    }, {
        "hourlyRecurringFee": "0",
        "id": 210353,
        "recurringFee": "0",
        "item": {
            "description": "Automated Reboot from Monitoring"
        }
    }, {
        "hourlyRecurringFee": "0",
        "id": 420,
        "recurringFee": "0",
        "item": {
            "description": "Unlimited SSL VPN Users & 1 PPTP VPN User per account"
        }
    }, {
        "hourlyRecurringFee": "0",
        "id": 418,
        "recurringFee": "0",
        "item": {
            "description": "Nessus Vulnerability Assessment & Reporting"
        }
    }],
    "quantity": 1,
    "sourceVirtualGuestId": null,
    "sshKeys": [],
    "useHourlyPricing": true,
    "virtualGuests": [{
        "domain": "test.com",
        "hostname": "test12345",
        "placementGroupId": 12345
    }],
    "complexType": "SoftLayer_Container_Product_Order_Virtual_Guest"
}]} 'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/placeOrder.json'
```


