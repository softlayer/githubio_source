---
title: "Spare Pool Servers"
description: "How to interact with the Spare Pool"

date: "2017-10-09"
classes: 
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Account"
tags:
  - "spare pool"
  - "server"
  - "objectFilter"
---

Operation: `GET`

Method: [`SoftLayer_Hardware_Server::sparepool()`](http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/sparePool)

Example CURL:
```
curl -su userid:api_key https://api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/<hardware_id>/sparepool/add

curl -su userid:api_key  "https://api.softlayer.com/rest/v3/SoftLayer_Hardware_Server/<hardware_id>/sparePool/activate"
```

Will return True if the action was successful, or throw an exception otherwise

Exceptions:
```
This server (hostname.domain.name) is not in a status that allows it to be added to spare pool.
This server (hostname.domain.name) is not in a status that allows it to be removed from spare pool.
```
The server is likely already in a spare pool.


### View Spare Pool Servers
Filtering by hardwareStatus->status doesn't work, you will need to filter by the status id only.

Status id 23 is SPARE_POOL
Status id 5 is ACTIVE
```
curl -su userid:api_key 'https://api.softlayer.com/rest/v3/SoftLayer_Account/getHardware?objectMask=mask[id,hostname,hardwareStatus[status,id]]&objectFilter={"hardware":{"hardwareStatus":{"id":{"operation":23}}}}'
```
