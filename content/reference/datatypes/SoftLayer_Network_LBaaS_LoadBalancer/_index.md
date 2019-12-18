---
title: "SoftLayer_Network_LBaaS_LoadBalancer"
description: "The SoftLayer_Network_LBaaS_LoadBalancer type presents a structure containing attributes of a load balancer, and its rel... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancer"
---

# SoftLayer_Network_LBaaS_LoadBalancer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_LoadBalancer' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancer' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_LBaaS_LoadBalancer type presents a structure containing attributes of a load balancer, and its related objects including listeners, pools and members. 





<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
-----
[accountId]: #accountid
#### [accountId]
The account this load balancer belongs to.  
<span class="type-label">Type: </span>**integer**

-----
[address]: #address
#### [address]
Address (Host name) of a load balancer.  
<span class="type-label">Type: </span>**string**

-----
[createDate]: #createdate
#### [createDate]
Specifies when a load balancer was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[description]: #description
#### [description]
Description of a load balancer.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
The unique identifier of a load balancer.  
<span class="type-label">Type: </span>**integer**

-----
[isDataLogEnabled]: #isdatalogenabled
#### [isDataLogEnabled]
Specifies whether the data log is enabled for the load balancer.   
<span class="type-label">Type: </span>**integer**

-----
[isPublic]: #ispublic
#### [isPublic]
Specifies whether the load balancer is a public or internal load balancer.   
<span class="type-label">Type: </span>**integer**

-----
[locationId]: #locationid
#### [locationId]
This references to location with type datacenter  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
Specifies when a load balancer was updated last.  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
The load balancer's name.  
<span class="type-label">Type: </span>**string**

-----
[operatingStatus]: #operatingstatus
#### [operatingStatus]
The operation status "ONLINE" or "OFFLINE" of a load balancer.  
<span class="type-label">Type: </span>**string**

-----
[previousErrorText]: #previouserrortext
#### [previousErrorText]
Error message of previous API call in case of failure  
<span class="type-label">Type: </span>**string**

-----
[provisioningStatus]: #provisioningstatus
#### [provisioningStatus]
The provisioning status of a load balancer.  
<span class="type-label">Type: </span>**string**

-----
[type]: #type
#### [type]
Specifies the type of load balancer.   
<span class="type-label">Type: </span>**integer**

-----
[useSystemPublicIpPool]: #usesystempublicippool
#### [useSystemPublicIpPool]
Applicable for public load balancer only. It specifies whether the public IP addresses are allocated from system public IP pool (1, default) or public subnet (null | 0) from the account ordering the load balancer. For internal load balancer, useSystemPublicIpPool will be ignored, and it always defaults to 1.   
<span class="type-label">Type: </span>**integer**

-----
[uuid]: #uuid
#### [uuid]
The UUID of a load balancer.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[datacenter]: #datacenter
#### [datacenter]
Datacenter, where load balancer is located.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[healthMonitors]: #healthmonitors
#### [healthMonitors]
Health monitors for the backend members.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_HealthMonitor'>SoftLayer_Network_LBaaS_HealthMonitor[] </a>**

-----
[l7Pools]: #l7pools
#### [l7Pools]
L7Pools for load balancer.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Pool'>SoftLayer_Network_LBaaS_L7Pool[] </a>**

-----
[listeners]: #listeners
#### [listeners]
Listeners assigned to load balancer.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_Listener'>SoftLayer_Network_LBaaS_Listener[] </a>**

-----
[members]: #members
#### [members]
Members assigned to load balancer.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_Member'>SoftLayer_Network_LBaaS_Member[] </a>**

-----
[sslCiphers]: #sslciphers
#### [sslCiphers]
list of preferred custom ciphers configured for the load balancer.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_SSLCipher'>SoftLayer_Network_LBaaS_SSLCipher[] </a>**


## Count

-----
[healthMonitorCount]: #healthmonitorcount
#### [healthMonitorCount]
A count of health monitors for the backend members.   
<span class="type-label">Type: </span>**unsigned long**


-----
[l7PoolCount]: #l7poolcount
#### [l7PoolCount]
A count of l7Pools for load balancer.   
<span class="type-label">Type: </span>**unsigned long**


-----
[listenerCount]: #listenercount
#### [listenerCount]
A count of listeners assigned to load balancer.   
<span class="type-label">Type: </span>**unsigned long**


-----
[memberCount]: #membercount
#### [memberCount]
A count of members assigned to load balancer.   
<span class="type-label">Type: </span>**unsigned long**


-----
[sslCipherCount]: #sslciphercount
#### [sslCipherCount]
A count of list of preferred custom ciphers configured for the load balancer.   
<span class="type-label">Type: </span>**unsigned long**

</div>


