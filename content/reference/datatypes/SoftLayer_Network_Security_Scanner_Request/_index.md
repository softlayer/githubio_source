---
title: "SoftLayer_Network_Security_Scanner_Request"
description: "The SoftLayer_Network_Security_Scanner_Request data type represents a single vulnerability scan request. It provides inf... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Security_Scanner_Request"
---

# SoftLayer_Network_Security_Scanner_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Security_Scanner_Request' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Security_Scanner_Request' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Security_Scanner_Request data type represents a single vulnerability scan request. It provides information on when the scan was created, last updated, and the current status. The status messages are as follows: 
*Scan Pending
*Scan Processing
*Scan Complete
*Scan Cancelled
*Generating Report.


### associatedMethods

*  [SoftLayer_Network_Security_Scanner_Request::getObject](/reference/services/SoftLayer_Network_Security_Scanner_Request/getObject )
*  [SoftLayer_Hardware::getSecurityScanRequests](/reference/services/SoftLayer_Hardware/getSecurityScanRequests )



### seeAlso

* [SoftLayer_Network_Security_Scanner_Request_Status](/reference/datatypes/SoftLayer_Network_Security_Scanner_Request_Status )




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
[accountId]: #accountid
#### [accountId]
A request's associated customer account identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date and time that the request is created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[guestId]: #guestid
#### [guestId]
Virtual Guest Identification Number for the guest this security scanner request belongs to.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hardwareId]: #hardwareid
#### [hardwareId]
The identifier of the hardware item a scan is run on.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[hostId]: #hostid
#### [hostId]
Identification Number for the host this security scanner request belongs to.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A security scan request's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[ipAddress]: #ipaddress
#### [ipAddress]
The IP address that a scan will be performed on.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date and time that the request was last modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
A request status identifier.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account associated with a security scan request.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[guest]: #guest
#### [guest]
The virtual guest a security scan is run against.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**


</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware a security scan is run against.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


</div>
<div class="prop-row">

-----
[requestorOwnedFlag]: #requestorownedflag
#### [requestorOwnedFlag]
Flag whether the requestor owns the hardware the scan was run on. This flag will  return for hardware servers only, virtual servers will result in a null return even if you have  a request out for them.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
A security scan request's status.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Security_Scanner_Request_Status'>SoftLayer_Network_Security_Scanner_Request_Status </a>**


</div>

## Count
</div>


