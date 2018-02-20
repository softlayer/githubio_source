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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Software_Component/getAverageInstallationDuration'> getAverageInstallationDuration</a> </span>
            <div class='views-field-body'>Retrieve the average amount of time that a software component takes to install.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Software_Component/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the billing item for a software component.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Software_Component/getHardware'> getHardware</a> </span>
            <div class='views-field-body'>Retrieve the hardware this Software Component is installed upon.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Software_Component/getLicenseFile'> getLicenseFile</a> </span>
            <div class='views-field-body'>Get the license file for a software component if it is supported.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Software_Component/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Software_Component record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Software_Component/getPasswordHistory'> getPasswordHistory</a> </span>
            <div class='views-field-body'>Retrieve history Records for Software Passwords.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Software_Component/getPasswords'> getPasswords</a> </span>
            <div class='views-field-body'>Retrieve username/Password pairs used for access to this Software Installation.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Software_Component/getSoftwareDescription'> getSoftwareDescription</a> </span>
            <div class='views-field-body'>Retrieve the Software Description of this Software Component.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Software_Component/getSoftwareLicense'> getSoftwareLicense</a> </span>
            <div class='views-field-body'>Retrieve the License this Software Component uses.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Software_Component/getVendorSetUpConfiguration'> getVendorSetUpConfiguration</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Software_Component/getVirtualGuest'> getVirtualGuest</a> </span>
            <div class='views-field-body'>Retrieve the virtual guest this software component is installed upon.</div>
        </div>
        </div>
</div>

