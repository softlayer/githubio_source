---
title: "SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem"
description: "SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem models a single Microsoft Update as reported by... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem"
---

# SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_UpdateItem models a single Microsoft Update as reported by SoftLayer's private Windows Server Update Services (WSUS) services. All servers purchased with Microsoft Windows retrieve updates from SoftLayer's WSUS servers by default.

### External Links


* [Windows Server Update Services (WSUS) Home](http://technet.microsoft.com/en-us/wsus/default.aspx)


* [Microsoft Help and Support](http://support.microsoft.com/)



### associatedMethods

*  [SoftLayer_Hardware_Server::getWindowsUpdateAvailableUpdates](/reference/services/SoftLayer_Hardware_Server/getWindowsUpdateAvailableUpdates )
*  [SoftLayer_Hardware_Server::getWindowsUpdateInstalledUpdates](/reference/services/SoftLayer_Hardware_Server/getWindowsUpdateInstalledUpdates )



### seeAlso

* [SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status](/reference/datatypes/SoftLayer_Container_Utility_Microsoft_Windows_UpdateServices_Status )




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
[description]: #description
#### [description]
A short description of a Microsoft Windows Update.  
<span class="type-label">Type: </span>**string**

-----
[failed]: #failed
#### [failed]
Flag indicating that this patch failed to properly install  
<span class="type-label">Type: </span>**boolean**

-----
[kbArticleNumber]: #kbarticlenumber
#### [kbArticleNumber]
A Windows Update's knowledge base article number. Every Windows Update can be referenced on the Microsoft Help and Support site at the URL <nowiki>http://support.microsoft.com/kb/<article number></nowiki>.   
<span class="type-label">Type: </span>**integer**

-----
[optional]: #optional
#### [optional]
Flag indicating that the update is entirely optionals  
<span class="type-label">Type: </span>**boolean**

-----
[requiresReboot]: #requiresreboot
#### [requiresReboot]
Flag indicating that a reboot is needed for this update to be fully applied  
<span class="type-label">Type: </span>**boolean**

</div>
<!-- LOCAL PROPERTY END -->

</div>


