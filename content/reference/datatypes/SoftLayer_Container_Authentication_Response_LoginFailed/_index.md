---
title: "SoftLayer_Container_Authentication_Response_LoginFailed"
description: "The SoftLayer_Container_Authentication_Response_LOGIN_FAILED data type contains information for specific responses from... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Authentication_Response_LoginFailed"
---

# SoftLayer_Container_Authentication_Response_LoginFailed
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Authentication_Response_LoginFailed' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Authentication_Response_LOGIN_FAILED data type contains information for specific responses from the getPortalLogin API. This class is indicative of a request where there was an inability to login based on the information that was provided. 





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
[accounts]: #accounts
#### [accounts]
The list of linked accounts for the authenticated SoftLayer customer portal user.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Authentication_Response_Account'>SoftLayer_Container_Authentication_Response_Account[] </a>**


</div>
<div class="prop-row">

-----
[errorMessage]: #errormessage
#### [errorMessage]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[statusKeyName]: #statuskeyname
#### [statusKeyName]
  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


