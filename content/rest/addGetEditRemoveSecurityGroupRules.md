---
title: "Add, get, edit and remove Security Group rules"
description: "Examples of how to add, get, edit and remove Security Group rules."
date: "2017-10-02"
classes: ["SoftLayer_Network_SecurityGroup"]
tags:
  - "securitygroups"
  - "addrules"
  - "editrules"
  - "removerules"
---

### Add rules

Operation: `POST`

URL: `SoftLayer_Network_SecurityGroup/{securitygroup_id}/addRules`

Example CURL:
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -X POST 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup/461903/addRules' -d '{"parameters": [[{"direction": "ingress","portRangeMin":100,"portRangeMax":101,"protocol":"tcp"}]]}'
```

Example Response:
```
{
    "requestId": "c0796ae700a8fad97170168",
    "rules": [
        {
            "direction": "ingress",
            "ethertype": "IPv4",
            "id": 789953,
            "portRangeMax": 101,
            "portRangeMin": 100,
            "protocol": "tcp",
            "remoteGroupId": null,
            "securityGroupId": 461903
        }
    ]
}
```
---

### Get rules

Operation: `GET`

URL: `SoftLayer_Network_SecurityGroup/{securitygroup_id}/getObject?objectMask=mask[rules]`

Example CURL:
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -g -X GET 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup/42401/getObject?objectMask=mask[rules]'
```

Example Response:
```
{
    "createDate": "2017-05-19T14:00:15-05:00",
    "description": "VSIs in this group respond to ping requests.",
    "id": 42401,
    "modifyDate": null,
    "name": "allow_ping",
    "rules": [
        {
            "direction": "ingress",
            "ethertype": "IPv4",
            "id": 43001,
            "portRangeMax": 0,
            "portRangeMin": 8,
            "protocol": "icmp",
            "remoteGroupId": null,
            "securityGroupId": 42401
        }
    ]
}

```
---

### Edit Rules

Operation: `PUT`

URL: `SoftLayer_Network_SecurityGroup/{securitygroup_id}/editRules`

Example CURL:
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -X PUT 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup/461903/editRules' -d '{"parameters": [[{"id": 789953,"portRangeMax": 110},{"id": 790219,"portRangeMax": 199}]]}'
```

Example Response:
```
{
    "requestId": "fd56048502cc26e659aacff",
    "rules": [
        {
            "direction": "ingress",
            "ethertype": "IPv4",
            "id": 789953,
            "portRangeMax": 110,
            "portRangeMin": 100,
            "protocol": "tcp",
            "remoteGroupId": null,
            "securityGroupId": 461903
        },
        {
            "direction": "ingress",
            "ethertype": "IPv4",
            "id": 790219,
            "portRangeMax": 199,
            "portRangeMin": 100,
            "protocol": "tcp",
            "remoteGroupId": null,
            "securityGroupId": 461903
        }
    ]
}
```
---

### Remove Rules

Operation: `PUT`

URL: `SoftLayer_Network_SecurityGroup/{securitygroup_id}/removeRules`

Example CURL:
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -X PUT 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup/461903/removeRules' -d '{"parameters": [[789953]]}'
```

Example Response:
```
{
    "requestId": "66cb42be41a2d6a1f82a24b",
    "rules": [
        {
            "direction": "ingress",
            "ethertype": "IPv4",
            "id": 789953,
            "portRangeMax": 110,
            "portRangeMin": 100,
            "protocol": "tcp",
            "remoteGroupId": null,
            "securityGroupId": 461903
        }
    ]
}
```
