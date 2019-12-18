---
title: "SoftLayer_Notification_Occurrence_User"
description: "This type contains general information relating to a user that may be impacted by a [SoftLayer_Notification_Occurrence_E... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Occurrence_User"
---

# SoftLayer_Notification_Occurrence_User
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Notification_Occurrence_User' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_Occurrence_User' >Datatype</a></li>
    </ul>
</div>

## Description 
This type contains general information relating to a user that may be impacted by a [SoftLayer_Notification_Occurrence_Event]({{<ref "reference/datatypes/SoftLayer_Notification_Occurrence_Event">}}). 





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
[acknowledgedFlag]: #acknowledgedflag
#### [acknowledgedFlag]
  
<span class="type-label">Type: </span>**integer**

-----
[active]: #active
#### [active]
  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
  
<span class="type-label">Type: </span>**integer**

-----
[usrRecordId]: #usrrecordid
#### [usrRecordId]
  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[impactedResources]: #impactedresources
#### [impactedResources]
A collection of resources impacted by the associated event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Resource'>SoftLayer_Notification_Occurrence_Resource[] </a>**

-----
[notificationOccurrenceEvent]: #notificationoccurrenceevent
#### [notificationOccurrenceEvent]
The associated event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event </a>**

-----
[user]: #user
#### [user]
The impacted user.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


## Count

-----
[impactedResourceCount]: #impactedresourcecount
#### [impactedResourceCount]
A count of a collection of resources impacted by the associated event.   
<span class="type-label">Type: </span>**unsigned long**

</div>


