---
title: "Get storage credentials for Block Storage"
description: "Retrieving the username and password for Performance/Endurance Block storage"

date: "2016-08-08"
classes: ["SoftLayer_Network_Storage_Iscsi"]
tags:
  - "Iscsi"
  - "BlockStorage"
  - "getObject"
---

Operation: `GET`

Method: [`SoftLayer_Network_Storage_Iscsi::getObject()`](http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage_Iscsi/getObject)

URL: SoftLayer_Network_Storage_Iscsi/getObject

Example CURL:
```
curl -s --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" "https://api.softlayer.com/rest/v3/SoftLayer_Network_Storage_Iscsi/1234567/getObject.json?objectMask=mask[allowedHardware[allowedHost[credential]],allowedVirtualGuests[allowedHost[credential]]]"
```

Example Response:
```json
{
    "accountId": 12345,
    "allowedHardware": [
        {
            "accountId": 12345,
            "allowedHost": {
                "credential": {
                    "accountId": "12345",
                    "createDate": "2016-04-13T13:10:40-06:00",
                    "id": 324649,
                    "modifyDate": null,
                    "nasCredentialTypeId": 2,
                    "password": "xxxxxxxxxxxxxxxxx",
                    "username": "SL0xxxxx-xxxxxx"
                },
                "credentialId": 324649,
                "id": 429811,
                "name": "iqn.2005-05.com.softlayer:SL0xxxxx-xxxxxx",
                "resourceTableId": 882187,
                "resourceTableName": "HARDWARE"
            },
            "bareMetalInstanceFlag": 0,
            "domain": "example.com",
            "fullyQualifiedDomainName": "esxi.example.com",
            "globalIdentifier": "xxxxxx",
            "hardwareFunction": {
                "code": "WEBSVR",
                "description": "Web Server",
                "id": 3
            },
            "hardwareStatus": {
                "id": 5,
                "status": "ACTIVE"
            },
            "hardwareStatusId": 5,
            "hostname": "esxi",
            "id": 882187,
            "manufacturerSerialNumber": "C819UAE45B00720",
            "networkManagementIpAddress": "10.x.x.149",
            "notes": "",
            "primaryBackendIpAddress": "10.x.x.144",
            "primaryIpAddress": "184.x.x.209",
            "privateIpAddress": "10.x.x.144",
            "provisionDate": "2016-04-13T10:54:55-06:00",
            "serialNumber": "SL01C9M1",
            "serviceProviderId": 1,
            "serviceProviderResourceId": null
        }
    ],
    "allowedVirtualGuests": [],
    "capacityGb": 20,
    "createDate": "2016-01-25T09:41:08-06:00",
    "guestId": null,
    "hardwareId": null,
    "hostId": null,
    "id": 8744521,
    "nasType": "ISCSI",
    "serviceProviderId": 1,
    "serviceResourceName": "PerfStor Aggr aggr_staashou0201_pc01",
    "storageTypeId": "7",
    "upgradableFlag": true,
    "username": "SL0xxxxxxxx-3"
}
```
