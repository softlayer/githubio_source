---
title: "SoftLayer_Container_Authentication_Response_2FactorAuthenticationNeeded"
description: "The SoftLayer_Container_Authentication_Response_2FactorAuthenticationNeeded data type contains information for specific... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Authentication_Response_2FactorAuthenticationNeeded"
---

# SoftLayer_Container_Authentication_Response_2FactorAuthenticationNeeded
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Authentication_Response_2FactorAuthenticationNeeded' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_Authentication_Response_2FactorAuthenticationNeeded data type contains information for specific responses from the getPortalLogin API. This class is indicative of a request that is missing the appropriate 2FA information. 





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
[additionalData]: #additionaldata
#### [additionalData]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Authentication_Response_Common'>SoftLayer_Container_Authentication_Response_Common </a>**


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


