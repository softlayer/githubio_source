---
title: "SoftLayer_Network_Monitor_Version1_Query_Type"
description: "The MonitorType type stores a name, long description, and default arguments for the monitor types.  The only use for thi... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Monitor_Version1_Query_Type"
---

# SoftLayer_Network_Monitor_Version1_Query_Type
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Type' >Datatype</a></li>
    </ul>
</div>

## Description 
The MonitorType type stores a name, long description, and default arguments for the monitor types.  The only use for this object is in reference.  The user chooses a monitoring type that would be appropriate for their server, and sets the id of the Query_Type to SoftLayer_Network_Monitor_Version1_Query_Host->queryTypeId 

The user can retrieve all available Query Types with the getAllObjects method on this service. 


### associatedMethods

*  [SoftLayer_Network_Monitor_Version1_Query_Type::getAllObjects](/reference/services/SoftLayer_Network_Monitor_Version1_Query_Type/getAllObjects )





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
[argumentDescription]: #argumentdescription
#### [argumentDescription]
The type of parameter sent to the monitoring command.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
Long description of the monitoring type.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique identifier for this object  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[monitorLevel]: #monitorlevel
#### [monitorLevel]
The level of this monitoring type.  The level the customer has access to is determined by values in SoftLayer_Network_Monitor_Version1_Query_Host_Stratum  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Short name of the monitoring type  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


