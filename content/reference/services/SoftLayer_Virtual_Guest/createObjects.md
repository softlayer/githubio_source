---
title: "createObjects"
description: "
createObjects() enables the creation of multiple computing instances on an account in a single call. This 
method is a simplified alternative to interacting with the ordering system directly. 


In order to create a computing instance a set of template objects must be sent in with a few required 
values. 


<b>Warning:</b> Computing instances created via this method will incur charges on your account. 


See [SoftLayer_Virtual_Guest::createObject](/reference/services/SoftLayer_Virtual_Guest/createObject) for specifics on the requirements of each template object. 


<h1>Example</h1> 
<http title='Request'>curl -X POST -d '{ 
 'parameters':[ 
     [ 
         { 
             'hostname': 'host1', 
             'domain': 'example.com', 
             'startCpus': 1, 
             'maxMemory': 1024, 
             'hourlyBillingFlag': true, 
             'localDiskFlag': true, 
             'operatingSystemReferenceCode': 'UBUNTU_LATEST' 
         }, 
         { 
             'hostname': 'host2', 
             'domain': 'example.com', 
             'startCpus': 1, 
             'maxMemory': 1024, 
             'hourlyBillingFlag': true, 
             'localDiskFlag': true, 
             'operatingSystemReferenceCode': 'UBUNTU_LATEST' 
         } 
     ] 
 ] 
}' https://api.softlayer.com/rest/v3/SoftLayer_Virtual_Guest/createObjects.json 
</http> 
<http title='Response'>HTTP/1.1 200 OK 


[ 
    { 
        'accountId': 232298, 
        'createDate': '2012-11-30T23:56:48-06:00', 
        'dedicatedAccountHostOnlyFlag': false, 
        'domain': 'softlayer.com', 
        'hostname': 'ubuntu1', 
        'id': 1301456, 
        'lastPowerStateId': null, 
        'lastVerifiedDate': null, 
        'maxCpu': 1, 
        'maxCpuUnits': 'CORE', 
        'maxMemory': 1024, 
        'metricPollDate': null, 
        'modifyDate': null, 
        'privateNetworkOnlyFlag': false, 
        'startCpus': 1, 
        'statusId': 1001, 
        'globalIdentifier': 'fed4c822-48c0-45d0-85e2-90476aa0c542' 
    }, 
    { 
        'accountId': 232298, 
        'createDate': '2012-11-30T23:56:49-06:00', 
        'dedicatedAccountHostOnlyFlag': false, 
        'domain': 'softlayer.com', 
        'hostname': 'ubuntu2', 
        'id': 1301457, 
        'lastPowerStateId': null, 
        'lastVerifiedDate': null, 
        'maxCpu': 1, 
        'maxCpuUnits': 'CORE', 
        'maxMemory': 1024, 
        'metricPollDate': null, 
        'modifyDate': null, 
        'privateNetworkOnlyFlag': false, 
        'startCpus': 1, 
        'statusId': 1001, 
        'globalIdentifier': 'bed4c686-9562-4ade-9049-dc4d5b6b200c' 
    } 
] 
</http> "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

# [REST Example](#createObjects-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#createObjects-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Virtual_Guest]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/createObjects'
```
