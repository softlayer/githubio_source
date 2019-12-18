---
title: "SoftLayer_Network_Monitor_Version1_Query_ResponseType"
description: "The ResponseType type stores only an ID and a description of the response type.  The only use for this object is in refe... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_ResponseType"
---

# SoftLayer_Network_Monitor_Version1_Query_ResponseType
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_ResponseType' >Datatype</a></li>
    </ul>
</div>

## Description 
The ResponseType type stores only an ID and a description of the response type.  The only use for this object is in reference.  The user chooses a response action that would be appropriate for a monitoring instance, and sets the ResponseTypeId to the SoftLayer_Network_Monitor_Version1_Query_Host->responseActionId value. 

The user can retrieve all available ResponseTypes with the getAllObjects method on this service. 


### associatedMethods

*  [SoftLayer_Network_Monitor_Version1_Query_ResponseType::getAllObjects](/reference/services/SoftLayer_Network_Monitor_Version1_Query_ResponseType/getAllObjects )





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
[actionDescription]: #actiondescription
#### [actionDescription]
The description of the action the monitoring system will take on failure  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
The unique identifier for this object  
<span class="type-label">Type: </span>**integer**

-----
[level]: #level
#### [level]
The level of this response.  The level the customer has access to is determined by values in SoftLayer_Network_Monitor_Version1_Query_Host_Stratum  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

</div>


