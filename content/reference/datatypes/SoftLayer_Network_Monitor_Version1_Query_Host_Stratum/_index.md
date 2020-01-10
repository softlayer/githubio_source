---
title: "SoftLayer_Network_Monitor_Version1_Query_Host_Stratum"
description: "The monitoring stratum type stores the maximum level of the various components of the monitoring system that a particula... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Host_Stratum"
---

# SoftLayer_Network_Monitor_Version1_Query_Host_Stratum
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host_Stratum' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host_Stratum' >Datatype</a></li>
    </ul>
</div>

## Description 
The monitoring stratum type stores the maximum level of the various components of the monitoring system that a particular hardware object has access to.  This object cannot be accessed by ID, and cannot be modified. The user can access this object through Hardware_Server->availableMonitoring. 

There are two values on this object that are important: 
# monitorLevel determines the highest level of SoftLayer_Network_Monitor_Version1_Query_Type object that can be placed in a monitoring instance on this server
# responseLevel determines the highest level of SoftLayer_Network_Monitor_Version1_Query_ResponseType object that can be placed in a monitoring instance on this server


Also note that the query type and response types are available through getAllQueryTypes and getAllResponseTypes, respectively. 





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
[monitorLevel]: #monitorlevel
#### [monitorLevel]
The highest level of a monitoring query type allowed on this server  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[responseLevel]: #responselevel
#### [responseLevel]
The highest level of a monitoring response type allowed on this server  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware object that these monitoring permissions applies to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>

## Count
</div>


