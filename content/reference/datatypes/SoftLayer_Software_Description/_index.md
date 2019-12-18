---
title: "SoftLayer_Software_Description"
description: "This class holds a description for a specific installation of a Software Component. 

SoftLayer_Software_Licenses tie a... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Description"
---

# SoftLayer_Software_Description
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Software_Description' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Software_Description' >Datatype</a></li>
    </ul>
</div>

## Description 
This class holds a description for a specific installation of a Software Component. 

SoftLayer_Software_Licenses tie a Software Component (A specific installation on a piece of hardware) to it's description. 

The "Manufacturer" and "Name" properties of a SoftLayer_Software_Description are used by the framework to factory specific objects, objects that may have special methods for that specific piece of software, or objects that contain application specific data, such as default ports.  For example, if you create a SoftLayer_Software_Component who's SoftLayer_Software_License points to the SoftLayer_Software_Description for "Swsoft" "Plesk", you'll actually get a SoftLayer_Software_Component_Swsoft_Plesk object. 



### seeAlso

* [SoftLayer_Software_Component](/reference/services/SoftLayer_Software_Component )


* [SoftLayer_Software_License](/reference/datatypes/SoftLayer_Software_License )




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
[controlPanel]: #controlpanel
#### [controlPanel]
This is set to '1' if this Software Description describes a Control Panel.  
<span class="type-label">Type: </span>**integer**

-----
[id]: #id
#### [id]
An ID number to identify this Software Description.  
<span class="type-label">Type: </span>**integer**

-----
[licenseTermUnit]: #licensetermunit
#### [licenseTermUnit]
The unit of measurement (day, month, or year) for license registration. Used in conjunction with licenseTermValue to determine overall license registration length of a new license.   
<span class="type-label">Type: </span>**string**

-----
[licenseTermValue]: #licensetermvalue
#### [licenseTermValue]
The number of units (licenseTermUnit) a new license is valid for at the time of registration.  
<span class="type-label">Type: </span>**integer**

-----
[longDescription]: #longdescription
#### [longDescription]
The manufacturer, name and version of a piece of software.  
<span class="type-label">Type: </span>**string**

-----
[manufacturer]: #manufacturer
#### [manufacturer]
The name of the manufacturer for this specific piece of software.  This name is used by SoftLayer_Software_Component to tailor make (factory) specific types of Software Components that know details like default ports.   
<span class="type-label">Type: </span>**string**

-----
[name]: #name
#### [name]
The name of this specific piece of software.  This name is used by SoftLayer_Software_Component to tailor make (factory) specific types of Software Components that know details like default ports.   
<span class="type-label">Type: </span>**string**

-----
[operatingSystem]: #operatingsystem
#### [operatingSystem]
This is set to '1' if this Software Description describes an Operating System.  
<span class="type-label">Type: </span>**integer**

-----
[referenceCode]: #referencecode
#### [referenceCode]
A reference code is structured as three tokens separated by underscores. The first token represents the product, the second is the version of the product, and the third is whether the software is 32 or 64bit.   
<span class="type-label">Type: </span>**string**

-----
[upgradeSoftwareDescriptionId]: #upgradesoftwaredescriptionid
#### [upgradeSoftwareDescriptionId]
Contains the ID of the suggested upgrade from this Software_Description to a more powerful software installation.  
<span class="type-label">Type: </span>**integer**

-----
[upgradeSwDescId]: #upgradeswdescid
#### [upgradeSwDescId]
Contains the ID of the suggested upgrade from this Software_Description to a more powerful software installation. (Deprecated - Use upgradeSoftwareDescriptionId)  
<span class="type-label">Type: </span>**integer**

-----
[version]: #version
#### [version]
The version of this specific piece of software.  
<span class="type-label">Type: </span>**string**

-----
[virtualLicense]: #virtuallicense
#### [virtualLicense]
This is set to '1' if this Software Description can be licensed to a Virtual Machine (an IP address).  
<span class="type-label">Type: </span>**integer**

-----
[virtualizationPlatform]: #virtualizationplatform
#### [virtualizationPlatform]
This is set to '1' if this Software Description a platform for hosting virtual servers.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[attributes]: #attributes
#### [attributes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description_Attribute'>SoftLayer_Software_Description_Attribute[] </a>**

-----
[averageInstallationDuration]: #averageinstallationduration
#### [averageInstallationDuration]
The average amount of time that a software description takes to install.  
<span class="type-label">Type: </span>**integer**

-----
[compatibleSoftwareDescriptions]: #compatiblesoftwaredescriptions
#### [compatibleSoftwareDescriptions]
A list of the software descriptions that are compatible with this software description.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description[] </a>**

-----
[features]: #features
#### [features]
The feature attributes of a software description.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description_Feature'>SoftLayer_Software_Description_Feature[] </a>**

-----
[latestVersion]: #latestversion
#### [latestVersion]
The latest version of a software description.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description[] </a>**

-----
[productItems]: #productitems
#### [productItems]
The various product items to which this software description is linked.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item[] </a>**

-----
[provisionTransactionGroup]: #provisiontransactiongroup
#### [provisionTransactionGroup]
This details the provisioning transaction group for this software. This is only valid for Operating System software.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_Group'>SoftLayer_Provisioning_Version1_Transaction_Group </a>**

-----
[reloadTransactionGroup]: #reloadtransactiongroup
#### [reloadTransactionGroup]
The transaction group that a software description belongs to. A transaction group is a sequence of transactions that must be performed in a specific order for the installation of software.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction_Group'>SoftLayer_Provisioning_Version1_Transaction_Group </a>**

-----
[requiredUser]: #requireduser
#### [requiredUser]
The default user created for a given a software description.  
<span class="type-label">Type: </span>**string**

-----
[softwareLicenses]: #softwarelicenses
#### [softwareLicenses]
Software Licenses that govern this Software Description.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_License'>SoftLayer_Software_License[] </a>**

-----
[upgradeSoftwareDescription]: #upgradesoftwaredescription
#### [upgradeSoftwareDescription]
A suggestion for an upgrade path from this Software Description  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**

-----
[upgradeSwDesc]: #upgradeswdesc
#### [upgradeSwDesc]
A suggestion for an upgrade path from this Software Description (Deprecated - Use upgradeSoftwareDescription)  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Description'>SoftLayer_Software_Description </a>**

-----
[validFilesystemTypes]: #validfilesystemtypes
#### [validFilesystemTypes]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Filesystem_Type'>SoftLayer_Configuration_Storage_Filesystem_Type[] </a>**


## Count

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


-----
[compatibleSoftwareDescriptionCount]: #compatiblesoftwaredescriptioncount
#### [compatibleSoftwareDescriptionCount]
A count of a list of the software descriptions that are compatible with this software description.   
<span class="type-label">Type: </span>**unsigned long**


-----
[featureCount]: #featurecount
#### [featureCount]
A count of the feature attributes of a software description.   
<span class="type-label">Type: </span>**unsigned long**


-----
[latestVersionCount]: #latestversioncount
#### [latestVersionCount]
A count of the latest version of a software description.   
<span class="type-label">Type: </span>**unsigned long**


-----
[productItemCount]: #productitemcount
#### [productItemCount]
A count of the various product items to which this software description is linked.   
<span class="type-label">Type: </span>**unsigned long**


-----
[softwareLicenseCount]: #softwarelicensecount
#### [softwareLicenseCount]
A count of software Licenses that govern this Software Description.   
<span class="type-label">Type: </span>**unsigned long**


-----
[validFilesystemTypeCount]: #validfilesystemtypecount
#### [validFilesystemTypeCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**

</div>


