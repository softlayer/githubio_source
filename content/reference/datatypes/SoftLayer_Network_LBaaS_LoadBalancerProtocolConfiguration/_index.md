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





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[backendPort]: #backendport
#### [backendPort]
Backends port  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[backendProtocol]: #backendprotocol
#### [backendProtocol]
Backends protocol. Valid values are "TCP", "HTTP"   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[clientTimeout]: #clienttimeout
#### [clientTimeout]
maximum idle time in seconds(Range: 1 to 7200), after which the load balancer brings down the client-side connection  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[frontendPort]: #frontendport
#### [frontendPort]
Frontends port  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[frontendProtocol]: #frontendprotocol
#### [frontendProtocol]
Frontends protocol. Valid values are "TCP", "HTTP" and "HTTPS"   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[listenerUuid]: #listeneruuid
#### [listenerUuid]
Listeners UUID, required for update only  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[loadBalancingMethod]: #loadbalancingmethod
#### [loadBalancingMethod]
Load balancing method. Valid values are "ROUNDROBIN", "WEIGHTED_RR" and "LEASTCONNECTION"   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[maxConn]: #maxconn
#### [maxConn]
Maximum number of allowed connections  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[serverTimeout]: #servertimeout
#### [serverTimeout]
maximum idle time in seconds(Range: 1 to 7200), after which the load balancer brings down the server-side connection  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[sessionCookieName]: #sessioncookiename
#### [sessionCookieName]
Sessions cookie name  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[sessionType]: #sessiontype
#### [sessionType]
Session stickiness type. Valid values are "SOURCE_IP" "HTTP_COOKIE"  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[tlsCertificateId]: #tlscertificateid
#### [tlsCertificateId]
ssl/tls certificate id  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


