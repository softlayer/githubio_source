---
title: "SoftLayer_Network_Logging_Syslog"
description: "The Syslog class holds a single line from the Networking Firewall 'Syslog' record, for firewall detected and blocked att... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Logging_Syslog"
---

# SoftLayer_Network_Logging_Syslog
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Logging_Syslog' >Datatype</a></li>
    </ul>
</div>

## Description 


The Syslog class holds a single line from the Networking Firewall "Syslog" record, for firewall detected and blocked attempts on a server. 





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
[createDate]: #createdate
#### [createDate]
Timestamp for when the connection was blocked by the firewall  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[destinationIpAddress]: #destinationipaddress
#### [destinationIpAddress]
The Destination IP Address of the blocked connection (your end)  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[destinationPort]: #destinationport
#### [destinationPort]
The Destination Port of the blocked connection (your end)  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[eventType]: #eventtype
#### [eventType]
This tells you what kind of firewall event this log line is for:  accept or deny.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[message]: #message
#### [message]
Raw syslog message for the event  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[protocol]: #protocol
#### [protocol]
Connection protocol used to make the call that was blocked (tcp, udp, etc)  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[sourceIpAddress]: #sourceipaddress
#### [sourceIpAddress]
The Source IP Address of the call that was blocked (attacker's end)  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[sourcePort]: #sourceport
#### [sourcePort]
The Source Port where the blocked connection was established (attacker's end)  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[totalEvents]: #totalevents
#### [totalEvents]
If this is an aggregation of syslog events, this property shows the total events.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


