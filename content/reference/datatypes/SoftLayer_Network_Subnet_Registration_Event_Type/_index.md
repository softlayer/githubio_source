---
title: "SoftLayer_Network_Subnet_Registration_Event_Type"
description: "Subnet Registration Event Type objects describe the nature of a [SoftLayer_Network_Subnet_Registration_Event]({{<ref 're... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Subnet_Registration_Event_Type"
---

# SoftLayer_Network_Subnet_Registration_Event_Type
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Subnet_Registration_Event_Type' >Datatype</a></li>
    </ul>
</div>

## Description 


Subnet Registration Event Type objects describe the nature of a [SoftLayer_Network_Subnet_Registration_Event]({{<ref "reference/datatypes/SoftLayer_Network_Subnet_Registration_Event">}}) 

The standard values for these objects are as follows: <ul> <li><strong>REGISTRATION_CREATED</strong> - Indicates that the registration has been created</li> <li><strong>REGISTRATION_UPDATED</strong> - Indicates that the registration has been updated</li> <li><strong>REGISTRATION_CANCELLED</strong> - Indicates that the registration has been cancelled</li> <li><strong>RIR_RESPONSE</strong> - Indicates that an action taken against the RIR has produced a response. More details will be provided in the event message.</li> <li><strong>ERROR</strong> - Indicates that an error has been encountered. More details will be provided in the event message.</li> <li><strong>NOTE</strong> - An employee or other system has entered a note regarding the registration. The note content will be provided in the event message.</li> </ul> 





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
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
Unique numeric ID of the event type object   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
Code-friendly string name of the event type   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Human-readable name of the event type   
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


