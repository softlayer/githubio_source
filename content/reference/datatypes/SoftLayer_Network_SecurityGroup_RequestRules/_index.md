---
title: "SoftLayer_Network_SecurityGroup_RequestRules"
description: "The SoftLayer_Network_SecurityGroup_RequestRules data type contains the ID of a specific request sent to the API, as wel... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_SecurityGroup_RequestRules"
---

# SoftLayer_Network_SecurityGroup_RequestRules
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_RequestRules' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_SecurityGroup_RequestRules data type contains the ID of a specific request sent to the API, as well as an associative array of the rules that were created, edited, or removed by the request. 





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
[requestId]: #requestid
#### [requestId]
The unique ID for a request.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[rules]: #rules
#### [rules]
Whether the API call was valid or not.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_SecurityGroup_Rule'>SoftLayer_Network_SecurityGroup_Rule[] </a>**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


