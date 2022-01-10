---
title: "SoftLayer_Network_LoadBalancer_Service"
description: "The SoftLayer_Network_LoadBalancer_Service data type contains all the information relating to a specific service (destin... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LoadBalancer_Service"
---

# SoftLayer_Network_LoadBalancer_Service
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LoadBalancer_Service' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_Service' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_LoadBalancer_Service data type contains all the information relating to a specific service (destination) on a particular load balancer. 

Information retained on the object itself is the the source and destination of the service, routing type, weight, and whether or not the service is currently enabled. 


### associatedMethods

*  [SoftLayer_Network_LoadBalancer_Service::getObject](/reference/services/SoftLayer_Network_LoadBalancer_Service/getObject )





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
[connectionLimit]: #connectionlimit
#### [connectionLimit]
Connection limit on this service.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
Creation Date of this service  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[destinationIpAddress]: #destinationipaddress
#### [destinationIpAddress]
The IP Address of the real server you wish to direct traffic to.  Your account must own this IP  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[destinationPort]: #destinationport
#### [destinationPort]
The port on the real server to direct the traffic.  This can be different than the source port.  If you wish to obfuscate your HTTP traffic, you can accept requests on port 80 on the load balancer, then redirect them to port 932 on your real server.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[enabled]: #enabled
#### [enabled]
A flag (either true or false) that determines if this particular service should be enabled on the load balancer.  Set to false to bring the server out of rotation without losing your configuration  
<span class="type-label">Type: </span>**boolean**  



</div>
<div class="prop-row">

-----
[healthCheck]: #healthcheck
#### [healthCheck]
The health check type for this service.  If one is supplied, the load balancer will occasionally ping your server to determine if it is still up.  Servers that are down are removed from the queue and will not be used to handle requests until their status returns to "up".  The value of the health check is determined directly by what option you have selected for the routing type. 

{| 
|-
! Type
! Valid Health Checks
|-
| HTTP
| HTTP, TCP, ICMP
|-
| TCP
| HTTP, TCP, ICMP
|-
| FTP
| TCP, ICMP
|-
| DNS
| DNS, ICMP
|-
| UDP
| None
|}

  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[healthCheckURL]: #healthcheckurl
#### [healthCheckURL]
The URL provided here (starting with /) is what the load balancer will request in order to perform a custom HTTP health check.  You must specify either "GET /location/of/file.html" or "HEAD /location/of/file.php"  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[healthResponse]: #healthresponse
#### [healthResponse]
The expected response from the custom HTTP health check.  If the requested page contains this response, the check succeeds.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique ID for this object, used for the getObject method, and must be set if you are editing this object.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Last modification date of this service  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Name of the load balancer service  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
Holds whether this server is up or down.  Does not affect load balancer configuration at all, just for the customer's informational purposes  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[peakConnections]: #peakconnections
#### [peakConnections]
Peak historical connections since the creation of this service.  Is reset any time you make a configuration change  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[sourcePort]: #sourceport
#### [sourcePort]
The port on the load balancer that this service maps to.  This is the port for incoming traffic, it needs to be shared with other services to form a group.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The connection type of this service.  Valid values are HTTP, FTP, TCP, UDP, and DNS.  The value of this variable affects available values of healthCheck, listed in that variable's description  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[vipId]: #vipid
#### [vipId]
Unique ID for this object's parent.  Probably not useful in the API, as this object will always be a child of a VirtualIpAddress anyway.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[weight]: #weight
#### [weight]
Weight affects the choices the load balancer makes between your services.  The weight of each service is expressed as a percentage of the TOTAL CONNECTION LIMIT on the virtual IP Address.  All services draw from the same pool of connections, so if you expect to have 4 times as much HTTP traffic as HTTPS, your weights for the above example routes would be 40%, 40%, 10%, 10% respectively.  The weights should add up to 100%  If you go over 100%, an exception will be thrown.  Weights must be whole numbers, no fractions or decimals are accepted.   
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[vip]: #vip
#### [vip]
The load balancer that this service belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LoadBalancer_VirtualIpAddress'>SoftLayer_Network_LoadBalancer_VirtualIpAddress </a>**  



</div>

## Count
</div>


