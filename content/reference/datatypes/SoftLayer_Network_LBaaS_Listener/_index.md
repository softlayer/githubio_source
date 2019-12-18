---
title: "SoftLayer_Network_LBaaS_Listener"
description: "The SoftLayer_Network_LBaaS_Listener type presents a data structure for a load balancers listener, also called frontend."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_Listener"
---

# SoftLayer_Network_LBaaS_Listener
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_Listener' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_Listener' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_LBaaS_Listener type presents a data structure for a load balancers listener, also called frontend. 





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
[connectionLimit]: #connectionlimit
#### [connectionLimit]
Limit of connections a listener can accept  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
Specifies when the listener was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
Specifies when the listener was updated previously.  
<span class="type-label">Type: </span>**dateTime**

-----
[protocol]: #protocol
#### [protocol]
Listeners protocol, one of "TCP", "HTTP", "HTTPS".  
<span class="type-label">Type: </span>**string**

-----
[protocolPort]: #protocolport
#### [protocolPort]
Listeners protocol port number.  
<span class="type-label">Type: </span>**integer**

-----
[provisioningStatus]: #provisioningstatus
#### [provisioningStatus]
The provisioning status of listener.  
<span class="type-label">Type: </span>**string**

-----
[tlsCertificateId]: #tlscertificateid
#### [tlsCertificateId]
This references to SSL/TLS certificate (optional) for a listener  
<span class="type-label">Type: </span>**integer**

-----
[uuid]: #uuid
#### [uuid]
The UUID of a listener.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[defaultPool]: #defaultpool
#### [defaultPool]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_Pool'>SoftLayer_Network_LBaaS_Pool </a>**

-----
[l7Policies]: #l7policies
#### [l7Policies]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Policy'>SoftLayer_Network_LBaaS_L7Policy[] </a>**


## Count

-----
[l7PolicyCount]: #l7policycount
#### [l7PolicyCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


