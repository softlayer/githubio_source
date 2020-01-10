---
title: "SoftLayer_Notification_Occurrence_Resource_Network_Storage_NetApp_Volume"
description: "This type contains general information related to a [SoftLayer_Network_Storage]({{<ref 'reference/datatypes/SoftLayer_Ne... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Occurrence_Resource_Network_Storage_NetApp_Volume"
---

# SoftLayer_Notification_Occurrence_Resource_Network_Storage_NetApp_Volume
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Resource_Network_Storage_NetApp_Volume' >Datatype</a></li>
    </ul>
</div>

## Description 
This type contains general information related to a [SoftLayer_Network_Storage]({{<ref "reference/datatypes/SoftLayer_Network_Storage">}}) resource that is impacted by a [SoftLayer_Notification_Occurrence_Event]({{<ref "reference/datatypes/SoftLayer_Notification_Occurrence_Event">}}). 





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
[filterLabel]: #filterlabel
#### [filterLabel]
<<< EOT A label which gives some background as to what piece of  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[hostname]: #hostname
#### [hostname]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[notificationOccurrenceEventId]: #notificationoccurrenceeventid
#### [notificationOccurrenceEventId]
<<< EOT The unique identifier for the associated  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[privateIp]: #privateip
#### [privateIp]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[resourceAccountId]: #resourceaccountid
#### [resourceAccountId]
<<< EOT The unique identifier for the [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) associated with  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[resourceName]: #resourcename
#### [resourceName]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
<<< EOT The unique identifier for the physical resource that is associated  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[resourceType]: #resourcetype
#### [resourceType]
  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[notificationOccurrenceEvent]: #notificationoccurrenceevent
#### [notificationOccurrenceEvent]
The associated event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event </a>**


</div>
<div class="prop-row">

-----
[resource]: #resource
#### [resource]
The physical resource.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity </a>**


</div>

## Count
</div>


