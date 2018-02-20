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
### external links
        Array
(
    [url] => http://en.wikipedia.org/wiki/Vulnerability_scanner
    [description] => Vulnerability scanner at Wikipedia
)
1        
### seeAlso
        SoftLayer_Network_Security_Scanner_Request_Status1                
        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Security_Scanner_Request/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a new vulnerability scan request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Security_Scanner_Request/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account associated with a security scan request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Security_Scanner_Request/getGuest'> getGuest</a> </span>
            <div class='views-field-body'>Retrieve the virtual guest a security scan is run against.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Security_Scanner_Request/getHardware'> getHardware</a> </span>
            <div class='views-field-body'>Retrieve the hardware a security scan is run against.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Security_Scanner_Request/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Security_Scanner_Request record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Security_Scanner_Request/getReport'> getReport</a> </span>
            <div class='views-field-body'>Get the vulnerability report for a scan request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Security_Scanner_Request/getRequestorOwnedFlag'> getRequestorOwnedFlag</a> </span>
            <div class='views-field-body'>Retrieve flag whether the requestor owns the hardware the scan was run on. This flag will  return for hardware servers only, virtual servers will result in a null return even if you have  a request out for them.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Security_Scanner_Request/getStatus'> getStatus</a> </span>
            <div class='views-field-body'>Retrieve a security scan request's status.</div>
        </div>
        </div>
</div>

