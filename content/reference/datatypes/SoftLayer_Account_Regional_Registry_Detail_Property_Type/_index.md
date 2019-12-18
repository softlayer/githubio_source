---
title: "SoftLayer_Account_Regional_Registry_Detail_Property_Type"
description: "Subnet Registration Detail Property Type objects describe the nature of a [SoftLayer_Account_Regional_Registry_Detail_Pr... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail_Property_Type"
---

# SoftLayer_Account_Regional_Registry_Detail_Property_Type
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Regional_Registry_Detail_Property_Type' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property_Type' >Datatype</a></li>
    </ul>
</div>

## Description 
Subnet Registration Detail Property Type objects describe the nature of a [SoftLayer_Account_Regional_Registry_Detail_Property]({{<ref "reference/datatypes/SoftLayer_Account_Regional_Registry_Detail_Property">}}) object. These types use [http://php.net/pcre.pattern.php Perl-Compatible Regular Expressions] to validate the value of a property object. 





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
Unique numeric ID of the property type object   
<span class="type-label">Type: </span>**integer**

-----
[keyName]: #keyname
#### [keyName]
Code-friendly string name of the property type   
<span class="type-label">Type: </span>**string**

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
Human-readable name of the property type   
<span class="type-label">Type: </span>**string**

-----
[valueExpression]: #valueexpression
#### [valueExpression]
A Perl-compatible regular expression used to describe the valid format of the property   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


