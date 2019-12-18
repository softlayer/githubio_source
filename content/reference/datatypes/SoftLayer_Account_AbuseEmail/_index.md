---
title: "SoftLayer_Account_AbuseEmail"
description: "An unfortunate facet of the hosting business is the necessity of with legal and network abuse inquiries. As these types... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_AbuseEmail"
---

# SoftLayer_Account_AbuseEmail
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_AbuseEmail' >Datatype</a></li>
    </ul>
</div>

## Description 
An unfortunate facet of the hosting business is the necessity of with legal and network abuse inquiries. As these types of inquiries frequently contain sensitive information SoftLayer keeps a separate account contact email address for direct contact about legal and abuse matters, modeled by the SoftLayer_Account_AbuseEmail data type. SoftLayer will typically email an account's abuse email addresses in these types of cases, and an email is automatically sent to an account's abuse email addresses when a legal or abuse ticket is created or updated. 

### External Links


* [Legal info at the SoftLayer website](http://www.softlayer.com/legal)






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
[email]: #email
#### [email]
A valid email address.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account associated with an abuse email address.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


## Count
</div>


