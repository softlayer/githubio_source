---
title: "SoftLayer_Notification_Occurrence_Resource"
description: "This type contains general information relating to any hardware or services that may be impacted by a SoftLayer_Notifica... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Notification"
classes:
    - "SoftLayer_Notification_Occurrence_Resource"
---

# SoftLayer_Notification_Occurrence_Resource
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Resource' >Datatype</a></li>
    </ul>
</div>

## Description 
This type contains general information relating to any hardware or services that may be impacted by a SoftLayer_Notification_Occurrence_Event. 





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
[active]: #active
#### [active]
  
<span class="type-label">Type: </span>**integer**

-----
[filterLabel]: #filterlabel
#### [filterLabel]
<<< EOT A label which gives some background as to what piece of  
<span class="type-label">Type: </span>**string**

-----
[notificationOccurrenceEventId]: #notificationoccurrenceeventid
#### [notificationOccurrenceEventId]
<<< EOT The unique identifier for the associated  
<span class="type-label">Type: </span>**integer**

-----
[resourceAccountId]: #resourceaccountid
#### [resourceAccountId]
<<< EOT The unique identifier for the [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) associated with  
<span class="type-label">Type: </span>**integer**

-----
[resourceName]: #resourcename
#### [resourceName]
  
<span class="type-label">Type: </span>**string**

-----
[resourceTableId]: #resourcetableid
#### [resourceTableId]
<<< EOT The unique identifier for the physical resource that is associated  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[notificationOccurrenceEvent]: #notificationoccurrenceevent
#### [notificationOccurrenceEvent]
The associated event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Occurrence_Event'>SoftLayer_Notification_Occurrence_Event </a>**

-----
[resource]: #resource
#### [resource]
The physical resource.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Entity'>SoftLayer_Entity </a>**


## Count
</div>


