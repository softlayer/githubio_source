---
title: "SoftLayer_Network_Security_Scanner_Request"
description: "SoftLayer gives customers the ability to manage vulnerability scans for each of their servers.  This service provides th... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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
SoftLayer gives customers the ability to manage vulnerability scans for each of their servers.  This service provides the ability to create a new scan request, view the status of a current request, and finally view the report of a finished scan. 

A vulnerability scan attempts to find potential security problems on a server by first searching for open ports and the services that run on them.  If any services are found the scanner will then check for version and patch information of each service found.  Lastly, the scanner will use the information gathered to search its database of known vulnerabilities and generate a report. Reports typically take five to ten minutes to run but allow for up to thirty minutes in rare cases. 

A vulnerability report will typically include the following information: 
*Number of security holes and warnings.
*The hosts that were scanned.
*The port/service and the corresponding issue.
*Detailed information about the issue, risk factor, and possible fixes.


If you have a firewall, SoftLayer's administrative networks need to be allowed for the vulnerability scan to be effective.  If a firewall is blocking all ports, the report may not show any problems even if some exist.  In addition you may have some indication in your firewall logs of the scan taking place as ports on your system are investigated. 

### External Links


* [Vulnerability scanner at Wikipedia](http://en.wikipedia.org/wiki/Vulnerability_scanner)




### seeAlso

* [SoftLayer_Network_Security_Scanner_Request_Status](/reference/datatypes/SoftLayer_Network_Security_Scanner_Request_Status )


        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_Network_Security_Scanner_Request/createObject)
Create a new vulnerability scan request.
</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_Security_Scanner_Request/getAccount)
Retrieve the account associated with a security scan request.
</div>

<div class="method-row">

#### [getGuest](/reference/services/SoftLayer_Network_Security_Scanner_Request/getGuest)
Retrieve the virtual guest a security scan is run against.
</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_Network_Security_Scanner_Request/getHardware)
Retrieve the hardware a security scan is run against.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Security_Scanner_Request/getObject)
Retrieve a SoftLayer_Network_Security_Scanner_Request record.
</div>

<div class="method-row">

#### [getReport](/reference/services/SoftLayer_Network_Security_Scanner_Request/getReport)
Get the vulnerability report for a scan request.
</div>

<div class="method-row">

#### [getRequestorOwnedFlag](/reference/services/SoftLayer_Network_Security_Scanner_Request/getRequestorOwnedFlag)
Retrieve flag whether the requestor owns the hardware the scan was run on. This flag will  return for hardware servers only, virtual servers will result in a null return even if you have  a request out for them.
</div>

<div class="method-row">

#### [getStatus](/reference/services/SoftLayer_Network_Security_Scanner_Request/getStatus)
Retrieve a security scan request's status.
</div>
</div>

</div>

