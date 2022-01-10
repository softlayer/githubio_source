---
title: "SoftLayer_Software_Component_HostIps"
description: "This object specifies a specific type of Software Component:  A Host Intrusion Protection System instance."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_HostIps"
---

# SoftLayer_Software_Component_HostIps
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Software_Component_HostIps' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Software_Component_HostIps' >Datatype</a></li>
    </ul>
</div>

## Description 


This object specifies a specific type of Software Component:  A Host Intrusion Protection System instance. 





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
[hardwareId]: #hardwareid
#### [hardwareId]
Hardware Identification Number for the server this Software Component is installed upon.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
An ID number identifying this Software Component (Software Installation)  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[manufacturerActivationCode]: #manufactureractivationcode
#### [manufacturerActivationCode]
The manufacturer code that is needed to activate a license.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[manufacturerLicenseInstance]: #manufacturerlicenseinstance
#### [manufacturerLicenseInstance]
A license key for this specific installation of software, if it is needed.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[averageInstallationDuration]: #averageinstallationduration
#### [averageInstallationDuration]
The average amount of time that a software component takes to install.  
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a software component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**  



</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
The hardware this Software Component is installed upon.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**  



</div>
<div class="prop-row">

-----
[passwordHistory]: #passwordhistory
#### [passwordHistory]
History Records for Software Passwords.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component_Password_History'>SoftLayer_Software_Component_Password_History[] </a>**  



</div>
<div class="prop-row">

-----
[passwords]: #passwords
#### [passwords]
Username/Password pairs used for access to this Software Installation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component_Password'>SoftLayer_Software_Component_Password[] </a>**  



</div>
<div class="prop-row">

-----
[softwareDescription]: #softwaredescription
#### [softwareDescription]
The Software Description of this Software Component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**  



</div>
<div class="prop-row">

-----
[softwareLicense]: #softwarelicense
#### [softwareLicense]
The License this Software Component uses.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_License'>SoftLayer_Software_License </a>**  



</div>
<div class="prop-row">

-----
[virtualGuest]: #virtualguest
#### [virtualGuest]
The virtual guest this software component is installed upon.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**  



</div>

## Count
<div class="prop-row">

-----
[passwordCount]: #passwordcount
#### [passwordCount]
A count of username/Password pairs used for access to this Software Installation.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[passwordHistoryCount]: #passwordhistorycount
#### [passwordHistoryCount]
A count of history Records for Software Passwords.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


