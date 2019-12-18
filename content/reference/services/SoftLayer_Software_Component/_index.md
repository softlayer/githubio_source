---
title: "SoftLayer_Software_Component"
description: "Every installed piece of software is represented in the API as a 'Software Component.'  This is the base class for softw... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component"
---
# SoftLayer_Software_Component
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Software_Component' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Software_Component' >Datatype</a></li>
    </ul>
</div>

## Description
Every installed piece of software is represented in the API as a "Software Component."  This is the base class for software components, exposing basic functionality for software components.  From any Software Component, through this service, you can get the hardware a component is installed upon, the license that this component is governed by, the current access passwords for a component, and the history of previous passwords for a component. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [getAverageInstallationDuration](/reference/services/SoftLayer_Software_Component/getAverageInstallationDuration)
Retrieve the average amount of time that a software component takes to install.

#### [getBillingItem](/reference/services/SoftLayer_Software_Component/getBillingItem)
Retrieve the billing item for a software component.

#### [getHardware](/reference/services/SoftLayer_Software_Component/getHardware)
Retrieve the hardware this Software Component is installed upon.

#### [getLicenseFile](/reference/services/SoftLayer_Software_Component/getLicenseFile)
Get the license file for a software component if it is supported.

#### [getObject](/reference/services/SoftLayer_Software_Component/getObject)
Retrieve a SoftLayer_Software_Component record.

#### [getPasswordHistory](/reference/services/SoftLayer_Software_Component/getPasswordHistory)
Retrieve history Records for Software Passwords.

#### [getPasswords](/reference/services/SoftLayer_Software_Component/getPasswords)
Retrieve username/Password pairs used for access to this Software Installation.

#### [getSoftwareDescription](/reference/services/SoftLayer_Software_Component/getSoftwareDescription)
Retrieve the Software Description of this Software Component.

#### [getSoftwareLicense](/reference/services/SoftLayer_Software_Component/getSoftwareLicense)
Retrieve the License this Software Component uses.

#### [getVendorSetUpConfiguration](/reference/services/SoftLayer_Software_Component/getVendorSetUpConfiguration)


#### [getVirtualGuest](/reference/services/SoftLayer_Software_Component/getVirtualGuest)
Retrieve the virtual guest this software component is installed upon.

</div>

