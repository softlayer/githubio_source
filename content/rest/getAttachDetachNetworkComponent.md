---
title: "Get network components, attach and detach network components"
description: "Examples of how to get a VSI's network components, attach network components to and detach network components from Security Groups."
date: "2017-10-02"
classes: ["SoftLayer_Network_SecurityGroup"]
tags:
  - "securitygroups"
  - "attachNetworkComponents"
  - "detachNetworkComponents"
---

### Get the network component IDs for a VSI

Operation: `GET`

URL: `SoftLayer_Virtual_Guest/{guest_id}/getObject.json?objectMask=mask[networkComponents.port,networkComponents.id]`

Example CURL:
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -g -X GET 'https://api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/39269481/getObject.json?objectMask=mask[networkComponents.port,networkComponents.id]'
```
Example Response:
```
{
    <output omitted>
    "networkComponents": [
        {
            "id": 21781733,
            "port": 0
        },
        {
            "id": 21781731,
            "port": 1
        }
    ],
    <output omitted>
}
```
---

### Attach network component to Security Group

Operation: `POST`

URL: `SoftLayer_Network_SecurityGroup/{securitygroup_id}/attachNetworkComponents`

Example CURL:
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -X POST 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup/461903/attachNetworkComponents' -d '{"parameters": [[21781731]]}'
```

Example Response:
```
{
    "requestId": "3d1bf39a0a0e4d699335c12"
}
```
---

### Detach network component from Security Group

Operation: `POST`

URL: `SoftLayer_Network_SecurityGroup/{securitygroup_id}/detachNetworkComponents`

Example CURL:
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -X POST 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup/461903/detachNetworkComponents' -d '{"parameters": [[21781731]]}'
```

Example Response:
```
{
    "requestId": "12b9e0b9459a1e000bfb169"
}
```
