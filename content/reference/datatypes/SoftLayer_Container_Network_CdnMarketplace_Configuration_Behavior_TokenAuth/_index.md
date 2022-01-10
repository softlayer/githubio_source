---
title: "SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth"
description: "The SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth data type contains information for speci... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth"
---

# SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Container_Network_CdnMarketplace_Configuration_Behavior_TokenAuth data type contains information for specific responses from the Token Authentication API. 





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
[aclDelimiter]: #acldelimiter
#### [aclDelimiter]
Specifies a single character to separate access control list (ACL) fields. The default value is '!'.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[escapeTokenInputs]: #escapetokeninputs
#### [escapeTokenInputs]
Possible values '0' and '1'. If set to '1', input values are escaped before adding them to the token. Default value is '1'.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[hmacAlgorithm]: #hmacalgorithm
#### [hmacAlgorithm]
Specifies the algorithm to use for the token's hash-based message authentication code (HMAC) field. Valid entries are 'SHA256', 'SHA1', or 'MD5'. The default value is 'SHA256'.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[ignoreQueryString]: #ignorequerystring
#### [ignoreQueryString]
Possible values '0' and '1'. If set to '1', query strings are removed from a URL when computing the token's HMAC algorithm. Default value is '0'.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The token name. If this value is empty, then it is set to the default value '__token__'.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[path]: #path
#### [path]
The path, relative to the domain that is accessed via token authentication.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[tokenDelimiter]: #tokendelimiter
#### [tokenDelimiter]
Specifies a single character to separate the individual token fields. The default value is '~'.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[tokenKey]: #tokenkey
#### [tokenKey]
The token encryption key, which specifies an even number of hex digits for the token key. An entry can be up to 64 characters in length.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[transitionKey]: #transitionkey
#### [transitionKey]
The token transition key, which specifies an even number of hex digits for the token transition key. An entry can be up to 64 characters in length.   
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


