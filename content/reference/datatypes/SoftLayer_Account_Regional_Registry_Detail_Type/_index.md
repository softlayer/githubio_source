---
title: "SoftLayer_Account_Regional_Registry_Detail_Type"
description: "Subnet Registration Detail Type objects describe the nature of a [SoftLayer_Account_Regional_Registry_Detail]({{<ref 're... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail_Type"
---

# SoftLayer_Account_Regional_Registry_Detail_Type
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Regional_Registry_Detail_Type' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Type' >Datatype</a></li>
    </ul>
</div>

## Description 
Subnet Registration Detail Type objects describe the nature of a [SoftLayer_Account_Regional_Registry_Detail]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail">}}) object. 

The standard values for these objects are as follows: <ul> <li><strong>NETWORK</strong> - The detail object represents the information for a [SoftLayer_Network_Subnet]({{<ref "reference/datatypes/SoftLayer_Network_Subnet">}})</li> <li><strong>PERSON</strong> - The detail object represents the information for a customer with the RIR</li> </ul> 





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
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
Unique numeric ID of the detail type object   
<span class="type-label">Type: </span>**integer**

-----
[keyName]: #keyname
#### [keyName]
Code-friendly string name of the detail type   
<span class="type-label">Type: </span>**string**

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
Human-readable name of the detail type   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


