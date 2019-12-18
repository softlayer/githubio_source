---
title: "SoftLayer_Auxiliary_Notification_Emergency"
description: "A SoftLayer_Auxiliary_Notification_Emergency data object represents a notification event being broadcast to the SoftLaye... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Auxiliary"
classes:
    - "SoftLayer_Auxiliary_Notification_Emergency"
---

# SoftLayer_Auxiliary_Notification_Emergency
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Auxiliary_Notification_Emergency' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Auxiliary_Notification_Emergency' >Datatype</a></li>
    </ul>
</div>

## Description 
A SoftLayer_Auxiliary_Notification_Emergency data object represents a notification event being broadcast to the SoftLayer customer base. It is used to provide information regarding outages or current known issues. 


### associatedMethods

*  [SoftLayer_Auxiliary_Notification_Emergency::getObject](/reference/services/SoftLayer_Auxiliary_Notification_Emergency/getObject )



### seeAlso

* [SoftLayer_Auxiliary_Notification_Emergency_Status](/reference/datatypes/SoftLayer_Auxiliary_Notification_Emergency_Status )


* [SoftLayer_Auxiliary_Notification_Emergency_Signature](/reference/datatypes/SoftLayer_Auxiliary_Notification_Emergency_Signature )




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
The date this event was created.  
<span class="type-label">Type: </span>**dateTime**

-----
[device]: #device
#### [device]
The device (if any) effected by this event.  
<span class="type-label">Type: </span>**string**

-----
[duration]: #duration
#### [duration]
The duration of this event.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
The device (if any) effected by this event.  
<span class="type-label">Type: </span>**integer**

-----
[location]: #location
#### [location]
The location effected by this event.  
<span class="type-label">Type: </span>**string**

-----
[message]: #message
#### [message]
A message describing this event.  
<span class="type-label">Type: </span>**string**

-----
[modifyDate]: #modifydate
#### [modifyDate]
The last date this event was modified.  
<span class="type-label">Type: </span>**dateTime**

-----
[servicesAffected]: #servicesaffected
#### [servicesAffected]
The service(s) (if any) effected by this event.  
<span class="type-label">Type: </span>**string**

-----
[startDate]: #startdate
#### [startDate]
The date this event will start.  
<span class="type-label">Type: </span>**dateTime**

-----
[statusId]: #statusid
#### [statusId]
Current status record for this event.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[signature]: #signature
#### [signature]
The signature of the SoftLayer employee department associated with this notification.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Notification_Emergency_Signature'>SoftLayer_Auxiliary_Notification_Emergency_Signature </a>**

-----
[status]: #status
#### [status]
The status of this notification.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Notification_Emergency_Status'>SoftLayer_Auxiliary_Notification_Emergency_Status </a>**


## Count
</div>


