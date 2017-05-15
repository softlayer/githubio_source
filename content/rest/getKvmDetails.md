---
title: "Get Virtual Console Virtual Guest"
description: "Retrieve the IP, username, and password needed to access the KVM console for a Virtual Guest."
date: "2017-05-04"
classes: ["SoftLayer_Virtual_Guest"]
tags:
    - "objectMask"
    - "getObject"
---

Operation: `GET`

Method: [`SoftLayer_Virtual_Guest::getObject()`](http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getObject)

URL: SoftLayer_Virtual_Guest/getObject

Example CURL:

```
https://$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY@api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/[device_id]/getObject?objectMask=mask[consoleIpAddressRecord[ipAddress[ipAddress],port],operatingSystem[passwords]]
```

Example Response:

```json
{
    "accountId": xxxxx,
    "consoleIpAddressRecord": {
        "ipAddress": {
            "ipAddress": "10.3.2.143"
        },
        "port": 5902
    },
    "createDate": "2017-05-02T11:00:54-06:00",
    "dedicatedAccountHostOnlyFlag": false,
    "domain": "cdetest.info",
    "fullyQualifiedDomainName": "kube.cdetest.info",
    "globalIdentifier": "1c02e7d5-7a4e-4324-9ff2-xxxxxxxx",
    "hostname": "kube",
    "id": 31678643,
    "lastPowerStateId": null,
    "lastVerifiedDate": null,
    "managedResourceFlag": false,
    "maxCpu": 2,
    "maxCpuUnits": "CORE",
    "maxMemory": 4096,
    "metricPollDate": null,
    "modifyDate": "2017-05-02T11:10:50-06:00",
    "operatingSystem": {
        "hardwareId": null,
        "id": 15948205,
        "manufacturerLicenseInstance": "",
        "passwords": [
            {
                "createDate": "2017-05-02T11:04:32-06:00",
                "id": 17502747,
                "modifyDate": "2017-05-02T11:04:32-06:00",
                "password": "redacted",
                "port": null,
                "software": null,
                "softwareId": 15948205,
                "username": "root"
            }
```
