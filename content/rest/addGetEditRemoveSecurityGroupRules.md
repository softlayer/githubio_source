---
title: "Add, get, edit and remove Security Group rules"
description: "Examples of how to add, get, edit and remove Security Group rules."
date: "2017-10-02"
classes: ["SoftLayer_Network_SecurityGroup"]
tags:
  - "securitygroups"
  - "addRules"
  - "editRules"
  - "removeRules"
---

### Add rules

Operation: `POST`

URL: `SoftLayer_Network_SecurityGroup/{securitygroup_id}/addRules`

Example CURL:
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -X POST 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup/136741/addRules' -d '{"parameters": [[{"direction": "ingress","portRangeMin":100,"portRangeMax":101,"protocol":"tcp"}]]}'
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
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -X PUT 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup/123456/editRules' -d '{"parameters": [[{"id": 11111,"portRangeMin": 99},{"id": 22222,"portRangeMin": 199}]]}'
```

---

### Remove Rules

Operation: `PUT`

URL: `SoftLayer_Network_SecurityGroup/{securitygroup_id}/removeRules`

Example CURL:
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -X PUT 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup/123456/removeRules' -d '{"parameters": [[11111]]}'
```

