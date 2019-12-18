---
title: "SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration"
description: "SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration specifies the protocol, port, maximum number of allowed connec... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration"
---

# SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Network_LBaaS_LoadBalancerProtocolConfiguration specifies the protocol, port, maximum number of allowed connections and session stickiness for load balancer's front- and backend. 





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
[backendPort]: #backendport
#### [backendPort]
Backends port  
<span class="type-label">Type: </span>**integer**

-----
[backendProtocol]: #backendprotocol
#### [backendProtocol]
<<EOT  
<span class="type-label">Type: </span>**string**

-----
[frontendPort]: #frontendport
#### [frontendPort]
Frontends port  
<span class="type-label">Type: </span>**integer**

-----
[frontendProtocol]: #frontendprotocol
#### [frontendProtocol]
<<EOT  
<span class="type-label">Type: </span>**string**

-----
[listenerUuid]: #listeneruuid
#### [listenerUuid]
Listeners UUID, required for update only  
<span class="type-label">Type: </span>**string**

-----
[loadBalancingMethod]: #loadbalancingmethod
#### [loadBalancingMethod]
<<EOT  
<span class="type-label">Type: </span>**string**

-----
[maxConn]: #maxconn
#### [maxConn]
Maximum number of allowed connections  
<span class="type-label">Type: </span>**integer**

-----
[sessionCookieName]: #sessioncookiename
#### [sessionCookieName]
Sessions cookie name  
<span class="type-label">Type: </span>**string**

-----
[sessionType]: #sessiontype
#### [sessionType]
Session stickiness type. Valid values are "SOURCE_IP" "HTTP_COOKIE"  
<span class="type-label">Type: </span>**string**

-----
[tlsCertificateId]: #tlscertificateid
#### [tlsCertificateId]
ssl/tls certificate id  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

</div>


