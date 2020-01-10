---
title: "SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status"
description: "SoftLayer customer servers that are purchased with the Microsoft Windows operating system are configured by default to r... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status"
---

# SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer customer servers that are purchased with the Microsoft Windows operating system are configured by default to retrieve updates from SoftLayer's local Windows Server Update Services (WSUS) server. Periodically, these servers synchronize and check for new updates from their local WSUS server. SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status models the results of a server's last synchronization attempt as queried from SoftLayer's WSUS servers. 

### External Links


* [Windows Server Update Services (WSUS) Home](http://technet.microsoft.com/en-us/wsus/default.aspx)



### associatedMethods

*  [SoftLayer_Hardware_Server::getWindowsUpdateStatus](/reference/services/SoftLayer_Hardware_Server/getWindowsUpdateStatus )



### seeAlso

* [SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem](/reference/datatypes/SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem )




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
[lastRebootDate]: #lastrebootdate
#### [lastRebootDate]
The last time a server rebooted due to a Windows Update.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[lastStatusDate]: #laststatusdate
#### [lastStatusDate]
The last time that SoftLayer's local WSUS server received a status update from a customer server.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[lastSyncDate]: #lastsyncdate
#### [lastSyncDate]
The last time a server synchronized with SoftLayer's local WSUS server.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[privateIPAddress]: #privateipaddress
#### [privateIPAddress]
This is the private IP address for this server.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[syncStatus]: #syncstatus
#### [syncStatus]
The status message returned from a server's last synchronization with SoftLayer's local WSUS server.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[updateStatus]: #updatestatus
#### [updateStatus]
A server's update status, as retrieved form SoftLayer's local WSUS server.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


