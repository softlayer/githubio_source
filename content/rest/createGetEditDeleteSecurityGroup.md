---
title: "Create, get, edit and delete Security Groups"
description: "Examples of how to create, get, edit and delete Security Groups."
date: "2017-10-02"
classes: ["SoftLayer_Network_SecurityGroup"]
tags:
  - "securitygroups"
---

### Create Security Group

Operation: `POST`

URL: `SoftLayer_Network_SecurityGroup` 

Example CURL: 
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -k -X POST 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup' -d '{"parameters": [{"name": "some name","description":"some description"}]}'
```

Example Response:
```
{
    "createDate": "2017-10-11T11:04:42-05:00",
    "description": "some description",
    "id": 123456,
    "modifyDate": null,
    "name": "some name"
}
```
---

### Get Security Group

Operation: `GET`

URL: `SoftLayer_Network_SecurityGroup/{securitygroup_id}` 

Example CURL: 
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -k -X GET 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup/123456'
```

Example Response:
```
{
    "createDate": "2017-10-11T11:04:42-05:00",
    "description": "some description",
    "id": 123456,
    "modifyDate": null,
    "name": "some name"
}
```
---

### Edit Security Group

Operation: `PUT`

URL: `SoftLayer_Network_SecurityGroup/{securitygroup_id}` 

Example CURL: 
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -k -X PUT 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup/123456' -d '{"parameters": [{"description": "new description"}]}'
```

Example Response:
```
true
```
---

### Delete Security Group

Operation: `DELETE`

URL: `SoftLayer_Network_SecurityGroup/{securitygroup_id}` 

Example CURL: 
```
$ curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -k -X DELETE 'https://api.softlayer.com/rest/v3/SoftLayer_Network_SecurityGroup/123456'
```

Example Response:
```
true
```
