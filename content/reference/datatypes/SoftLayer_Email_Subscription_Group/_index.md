---
title: "SoftLayer_Email_Subscription_Group"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Email"
classes:
    - "SoftLayer_Email_Subscription_Group"
---

# SoftLayer_Email_Subscription_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Email_Subscription_Group' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Email_Subscription_Group' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Email subscription group name.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[subscriptions]: #subscriptions
#### [subscriptions]
All email subscriptions associated with this group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Email_Subscription'>SoftLayer_Email_Subscription[] </a>**


</div>

## Count
<div class="prop-row">

-----
[subscriptionCount]: #subscriptioncount
#### [subscriptionCount]
A count of all email subscriptions associated with this group.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


