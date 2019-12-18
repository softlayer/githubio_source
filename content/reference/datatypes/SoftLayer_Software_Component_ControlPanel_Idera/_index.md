---
title: "SoftLayer_Software_Component_ControlPanel_Idera"
description: "This object specifies a specific type of control panel Software Component:  An Idera instance."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_ControlPanel_Idera"
---

# SoftLayer_Software_Component_ControlPanel_Idera
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Software_Component_ControlPanel_Idera' >Datatype</a></li>
    </ul>
</div>

## Description 
This object specifies a specific type of control panel Software Component:  An Idera instance. 





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
[hardwareId]: #hardwareid
#### [hardwareId]
Hardware Identification Number for the server this Software Component is installed upon.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
An ID number identifying this Software Component (Software Installation)  
<span class="type-label">Type: </span>**integer**

-----
[manufacturerActivationCode]: #manufactureractivationcode
#### [manufacturerActivationCode]
The manufacturer code that is needed to activate a license.  
<span class="type-label">Type: </span>**string**

-----
[manufacturerLicenseInstance]: #manufacturerlicenseinstance
#### [manufacturerLicenseInstance]
A license key for this specific installation of software, if it is needed.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[averageInstallationDuration]: #averageinstallationduration
#### [averageInstallationDuration]
The average amount of time that a software component takes to install.  
<span class="type-label">Type: </span>**unsigned long**

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item for a software component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**

-----
[hardware]: #hardware
#### [hardware]
The hardware this Software Component is installed upon.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**

-----
[passwordHistory]: #passwordhistory
#### [passwordHistory]
History Records for Software Passwords.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component_Password_History'>SoftLayer_Software_Component_Password_History[] </a>**

-----
[passwords]: #passwords
#### [passwords]
Username/Password pairs used for access to this Software Installation.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component_Password'>SoftLayer_Software_Component_Password[] </a>**

-----
[softwareDescription]: #softwaredescription
#### [softwareDescription]
The Software Description of this Software Component.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**

-----
[softwareLicense]: #softwarelicense
#### [softwareLicense]
The License this Software Component uses.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_License'>SoftLayer_Software_License </a>**

-----
[virtualGuest]: #virtualguest
#### [virtualGuest]
The virtual guest this software component is installed upon.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a>**


## Count

-----
[passwordCount]: #passwordcount
#### [passwordCount]
A count of username/Password pairs used for access to this Software Installation.   
<span class="type-label">Type: </span>**unsigned long**


-----
[passwordHistoryCount]: #passwordhistorycount
#### [passwordHistoryCount]
A count of history Records for Software Passwords.   
<span class="type-label">Type: </span>**unsigned long**

</div>


