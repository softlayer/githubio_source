---
title: "SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader"
description: "The SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader data type contains informatio... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader"
---

# SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_ModifyResponseHeader data type contains information for specific responses from the modify response header API. 





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
[delimiter]: #delimiter
#### [delimiter]
Specifies the delimiter to be used when indicating multiple values for a header. Valid delimiter is, a <space>, , (comma), ; (semicolon), ,<space> (comma and space), or ;<space> (semicolon and space).   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
The description of modify response header.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[headers]: #headers
#### [headers]
A collection of key value pairs that specify the headers and associated values to be modified. The header name and header value must be separated by colon (:). Example: ['header1:value1','header2:Value2']   
<span class="type-label">Type: </span>**array of strings**


</div>
<div class="prop-row">

-----
[modResHeaderUniqueId]: #modresheaderuniqueid
#### [modResHeaderUniqueId]
The uniqueId of the modify response header to which the existing behavior belongs.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[path]: #path
#### [path]
The path, relative to the domain that is accessed via modify response header.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of the modify response header, could be append/modify/delete. Set this to append to add a given header value to a header name set in the headerList. Set this to delete to remove a given header value from a header name set in the headerList. Set this to overwrite to match on a specified header name and replace its existing header value with a new one you specify.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[uniqueId]: #uniqueid
#### [uniqueId]
The uniqueId of the mapping to which the existing behavior belongs.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


