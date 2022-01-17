---
title: "Create Storage Snapshot"
description: "Initiate a manual snapshot of an Endurance or Performance Block storage volume."
date: "2016-08-11"
classes: ["SoftLayer_Network_Storage_Iscsi"]
tags:
    - "iscsi"
    - "blockstorage"
    - "objectmask"
---

Operation: `POST`

Method: [`SoftLayer_Network_Storage_Iscsi::.createSnapshot()`]http://sldn.softlayer.com/reference/services/SoftLayer_Network_Storage_Iscsi/createSnapshot)

URL: SoftLayer_Network_Storage_Iscsi/createSnapshot

Example CURL:
```
curl -s --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" "https://api.softlayer.com/rest/v3/SoftLayer_Network_Storage_Iscsi/8744521/createSnapshot"
```

Example Response
```
{
    "accountId": xxxxx,
    "capacityGb": 20,
    "createDate": "2016-08-11T13:45:39-06:00",
    "guestId": null,
    "hardwareId": null,
    "hostId": null,
    "id": 13430037,
    "nasType": "SNAPSHOT",
    "properties": [
        {
            "createDate": "2016-08-11T13:45:39-06:00",
            "modifyDate": null,
            "type": {
                "description": "Determines whether the volume is currently mountable",
                "keyname": "MOUNTABLE",
                "name": "Mountable"
            },
            "value": "0",
            "volumeId": 13430037
        },
        {
            "createDate": "2016-08-11T13:45:39-06:00",
            "modifyDate": null,
            "type": {
                "description": "Volume name",
                "keyname": "VOLUME_NAME",
                "name": "Volume Name"
            },
            "value": "manual.2016-08-11_1445",
            "volumeId": 13430037
        },
        {
            "createDate": "2016-08-11T13:45:39-06:00",
            "modifyDate": null,
            "type": {
                "description": "The amount of space used by snapshots.",
                "keyname": "SNAPSHOT_SPACE_USED",
                "name": "Snapshot Used"
            },
            "value": "88000",
            "volumeId": 13430037
        },
        {
            "createDate": "2016-08-11T13:45:39-06:00",
            "modifyDate": null,
            "value": "2016-08-11T14:45:39-05:00",
            "volumeId": 13430037
        }
    ],
    "serviceProviderId": 1,
    "serviceResourceBackendIpAddress": "nfshou0201b-fz.service.softlayer.com",
    "serviceResourceName": "PerfStor Aggr aggr_staashou0201_pc01",
    "storageTypeId": "16",
    "upgradableFlag": true,
    "username": "SL01SEVCxxxxx_2"
}
```

You can get the current snapshots by issuing the following command:

Example CURL:
```
curl -s --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" "https://api.softlayer.com/rest/v3/SoftLayer_Network_Storage_Iscsi/1234567/getSnapshotsForVolume"
```

Example Response
```
[
    {
        "accountId": xxxxx,
        "capacityGb": 20,
        "createDate": "2016-08-11T13:09:41-06:00",
        "guestId": null,
        "hardwareId": null,
        "hostId": null,
        "id": 13429199,
        "nasType": "SNAPSHOT",
        "propertyCount": 0,
        "serviceProviderId": 1,
        "serviceResourceBackendIpAddress": "nfshou0201b-fz.service.softlayer.com",
        "serviceResourceName": "PerfStor Aggr aggr_staashou0201_pc01",
        "storageTypeId": "16",
        "upgradableFlag": true,
        "username": "SL01SEVCxxxxx_2"
    },
    {
        "accountId": xxxxx,
        "capacityGb": 20,
        "createDate": "2016-08-11T11:09:00-06:00",
        "guestId": null,
        "hardwareId": null,
        "hostId": null,
        "id": 13427035,
        "nasType": "SNAPSHOT",
        "propertyCount": 0,
        "serviceProviderId": 1,
        "serviceResourceBackendIpAddress": "nfshou0201b-fz.service.softlayer.com",
        "serviceResourceName": "PerfStor Aggr aggr_staashou0201_pc01",
        "storageTypeId": "16",
        "upgradableFlag": true,
        "username": "SL01SEVCxxxxx_2"
    },
    {
        "accountId": xxxxx,
        "capacityGb": 20,
        "createDate": "2016-08-10T11:09:10-06:00",
        "guestId": null,
        "hardwareId": null,
        "hostId": null,
        "id": 13402009,
        "nasType": "SNAPSHOT",
        "propertyCount": 0,
        "serviceProviderId": 1,
        "serviceResourceBackendIpAddress": "nfshou0201b-fz.service.softlayer.com",
        "serviceResourceName": "PerfStor Aggr aggr_staashou0201_pc01",
        "storageTypeId": "16",
        "upgradableFlag": true,
        "username": "SL01SEVCxxxxx_2"
    }
]
```
