---
title: "SoftLayer_Network_LBaaS_L7Rule"
description: "The SoftLayer_Network_LBaaS_L7Rule represents the Rules that can be attached to a a L7 policy."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Rule"
---

# SoftLayer_Network_LBaaS_L7Rule
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_L7Rule' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Rule' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_LBaaS_L7Rule represents the Rules that can be attached to a a L7 policy. 





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
[comparisonType]: #comparisontype
#### [comparisonType]
Comparision type for the Rule, It should any of the following values : REGEX, STARTS_WITH, ENDS_WITH, CONTAINS, EQUAL_TO.   
<span class="type-label">Type: </span>**string**

-----
[createDate]: #createdate
#### [createDate]
Specifies when a Rule was created  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
The ID of a Rule.  
<span class="type-label">Type: </span>**integer**

-----
[invert]: #invert
#### [invert]
Inverts the result of the value if set, i.e. True will be inverted to False and vice-versa   
<span class="type-label">Type: </span>**integer**

-----
[key]: #key
#### [key]
Key for Rule type HEADER and COOKIE.  
<span class="type-label">Type: </span>**string**

-----
[modifyDate]: #modifydate
#### [modifyDate]
Specifies when a Rule was updated previously.  
<span class="type-label">Type: </span>**dateTime**

-----
[type]: #type
#### [type]
Type of the Rule. It  should have any of the following values: HOST_NAME, FILE_TYPE, HEADER, COOKIE, PATH.   
<span class="type-label">Type: </span>**string**

-----
[uuid]: #uuid
#### [uuid]
The UUID of a Rule.  
<span class="type-label">Type: </span>**string**

-----
[value]: #value
#### [value]
Value for Rule . For type HEADER and COOKIE, this value is compared against the value of the key from HEADER or COOKIE.   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


