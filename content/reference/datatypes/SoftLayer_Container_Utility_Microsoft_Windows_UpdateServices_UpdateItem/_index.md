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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>A short description of a Microsoft Windows Update. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#failed" name=failed>failed</a>
            </span>
            <div class='views-field-body'>Flag indicating that this patch failed to properly install </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#kbArticleNumber" name=kbArticleNumber>kbArticleNumber</a>
            </span>
            <div class='views-field-body'>A Windows Update's knowledge base article number. Every Windows Update can be referenced on the Microsoft Help and Support site at the URL <nowiki>http://support.microsoft.com/kb/<article number></nowiki>.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#optional" name=optional>optional</a>
            </span>
            <div class='views-field-body'>Flag indicating that the update is entirely optionals </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#requiresReboot" name=requiresReboot>requiresReboot</a>
            </span>
            <div class='views-field-body'>Flag indicating that a reboot is needed for this update to be fully applied </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
            </div>
    </div>


