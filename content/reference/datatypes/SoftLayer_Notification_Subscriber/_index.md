---
title: "SoftLayer_Notification_Subscriber"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Subscriber"
---

# SoftLayer_Notification_Subscriber
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_Subscriber' >Datatype</a></li>
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
[active]: #active
#### [active]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[notificationId]: #notificationid
#### [notificationId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[notificationSubscriberTypeId]: #notificationsubscribertypeid
#### [notificationSubscriberTypeId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[notificationSubscriberTypeResourceId]: #notificationsubscribertyperesourceid
#### [notificationSubscriberTypeResourceId]
  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[deliveryMethods]: #deliverymethods
#### [deliveryMethods]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Subscriber_Delivery_Method'>SoftLayer_Notification_Subscriber_Delivery_Method[] </a>**  



</div>
<div class="prop-row">

-----
[notification]: #notification
#### [notification]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification'>SoftLayer_Notification </a>**  



</div>

## Count
<div class="prop-row">

-----
[deliveryMethodCount]: #deliverymethodcount
#### [deliveryMethodCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


