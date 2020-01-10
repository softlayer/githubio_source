---
title: "SoftLayer_Software_Component_OperatingSystem"
description: "SoftLayer_Software_Component_OperatingSystem extends the [SoftLayer_Software_Component]({{<ref 'reference/datatypes/Soft... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_OperatingSystem"
---

# SoftLayer_Software_Component_OperatingSystem
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Software_Component_OperatingSystem' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Software_Component_OperatingSystem extends the [SoftLayer_Software_Component]({{<ref "reference/datatypes/SoftLayer_Software_Component">}}) data type to include operating system specific properties. 



### seeAlso

* [SoftLayer_Software_Component (type)](/reference/datatypes/SoftLayer_Software_Component (type) )




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
The expected amount of time in minutes that an operating system can be installed.  
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
[licenseExpirationDate]: #licenseexpirationdate
#### [licenseExpirationDate]
The date in which the license for this software expires.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[partitionTemplates]: #partitiontemplates
#### [partitionTemplates]
An operating system's associated [SoftLayer_Hardware_Component_Partition_Template]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Partition_Template">}}) that can be used to configure a hardware drive.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware_Component_Partition_Template'>SoftLayer_Hardware_Component_Partition_Template[] </a>**


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
[reloadTransactionGroup]: #reloadtransactiongroup
#### [reloadTransactionGroup]
An operating systems associated [SoftLayer_Provisioning_Version1_Transaction_Group]({{<ref "reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_Group">}}). A transaction group is a list of operations that will occur during the installment of an operating system.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_Group'>SoftLayer_Provisioning_Version1_Transaction_Group </a>**


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
[partitionTemplateCount]: #partitiontemplatecount
#### [partitionTemplateCount]
A count of an operating system's associated [SoftLayer_Hardware_Component_Partition_Template]({{<ref "reference/datatypes/SoftLayer_Hardware_Component_Partition_Template">}}) that can be used to configure a hardware drive.   
<span class="type-label">Type: </span>**unsigned long**


</div>
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


