---
title: "SoftLayer_Container_Authentication_Response_Success"
description: "The SoftLayer_Container_Authentication_Response_SUCCESS data type contains information for specific responses from the g... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Authentication_Response_Success"
---

# SoftLayer_Container_Authentication_Response_Success
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Authentication_Response_Success' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Authentication_Response_SUCCESS data type contains information for specific responses from the getPortalLogin API. This class is indicative of a request that was successful in obtaining a portal login token from the getPortalLogin API. 





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
[accounts]: #accounts
#### [accounts]
The list of linked accounts for the authenticated SoftLayer customer portal user.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Authentication_Response_Account'>SoftLayer_Container_Authentication_Response_Account[] </a>**

-----
[statusKeyName]: #statuskeyname
#### [statusKeyName]
  
<span class="type-label">Type: </span>**string**

-----
[token]: #token
#### [token]
The token for interacting with the SoftLayer customer portal.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_User_Authentication_Token'>SoftLayer_Container_User_Authentication_Token </a>**

</div>
<!-- LOCAL PROPERTY END -->

</div>


