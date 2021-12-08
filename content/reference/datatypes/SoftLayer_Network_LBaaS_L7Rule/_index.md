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
[comparisonType]: #comparisontype
#### [comparisonType]
Comparision type for the Rule, It should any of the following values : REGEX, STARTS_WITH, ENDS_WITH, CONTAINS, EQUAL_TO.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
Specifies when a Rule was created  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The ID of a Rule.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[invert]: #invert
#### [invert]
Inverts the result of the value if set, i.e. True will be inverted to False and vice-versa   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[key]: #key
#### [key]
Key for Rule type HEADER and COOKIE.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Specifies when a Rule was updated previously.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
Type of the Rule. It  should have any of the following values: HOST_NAME, FILE_TYPE, HEADER, COOKIE, PATH.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[uuid]: #uuid
#### [uuid]
The UUID of a Rule.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[value]: #value
#### [value]
Value for Rule . For type HEADER and COOKIE, this value is compared against the value of the key from HEADER or COOKIE.   
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


