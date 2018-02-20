---
title: "SoftLayer_Hardware_Component_Ram"
description: "The SoftLayer_Hardware_Component_Ram data type abstracts information related to RAM."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Component_Ram"
---

# SoftLayer_Hardware_Component_Ram
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Component_Ram' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Component_Ram data type abstracts information related to RAM. 
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
            <span class='views-field-title'><a href="#hardwareComponentModelId" name=hardwareComponentModelId>hardwareComponentModelId</a></span>
            <div class='views-field-body'>The internal identifier of a hardware component's component model. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareId" name=hardwareId>hardwareId</a></span>
            <div class='views-field-body'>The internal identifier of the hardware that a hardware component resides inside. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A hardware component's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date that a hardware component was last modified. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The name of this component as referenced by the operating system. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serialNumber" name=serialNumber>serialNumber</a></span>
            <div class='views-field-body'>The component serial number. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serviceProviderId" name=serviceProviderId>serviceProviderId</a></span>
            <div class='views-field-body'>A hardware's internal identification number at its service provider </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#capacity" name=capacity>capacity</a></span>
            <div class='views-field-body'>A component's capacity. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>decimal</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#children" name=children>children</a></span>
            <div class='views-field-body'>A components sub components. Devices that are usually integrated or in some way attached to a component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#componentRevision" name=componentRevision>componentRevision</a></span>
            <div class='views-field-body'>A component's Revision. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#downlinkHardwareComponents" name=downlinkHardwareComponents>downlinkHardwareComponents</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardware" name=hardware>hardware</a></span>
            <div class='views-field-body'>The hardware object that this component belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponentModel" name=hardwareComponentModel>hardwareComponentModel</a></span>
            <div class='views-field-body'>The general group of component models. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model'>SoftLayer_Hardware_Component_Model </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#hardwareComponentType" name=hardwareComponentType>hardwareComponentType</a></span>
            <div class='views-field-body'>A components type. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Type'>SoftLayer_Hardware_Component_Type </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#moduleComponents" name=moduleComponents>moduleComponents</a></span>
            <div class='views-field-body'>The module's hardware components </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#moduleHardwareComponents" name=moduleHardwareComponents>moduleHardwareComponents</a></span>
            <div class='views-field-body'>The module's hardware components </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#moduleNetworkComponents" name=moduleNetworkComponents>moduleNetworkComponents</a></span>
            <div class='views-field-body'>The module's network components </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#networkComponents" name=networkComponents>networkComponents</a></span>
            <div class='views-field-body'>The components local ethernet and remote management interfaces </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Component'>SoftLayer_Network_Component[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#owner" name=owner>owner</a></span>
            <div class='views-field-body'>The account this component belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#parent" name=parent>parent</a></span>
            <div class='views-field-body'>A components parent. Devices that are usually integrated or in some way attached to a component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#parentModule" name=parentModule>parentModule</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#prefixAttribute" name=prefixAttribute>prefixAttribute</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Model_Generic_Attribute'>SoftLayer_Hardware_Component_Model_Generic_Attribute </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#raidMode" name=raidMode>raidMode</a></span>
            <div class='views-field-body'>A RAID controllers RAID mode. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#revision" name=revision>revision</a></span>
            <div class='views-field-body'>The component revision designation. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component_Revision'>SoftLayer_Hardware_Component_Revision </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#serviceProvider" name=serviceProvider>serviceProvider</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Service_Provider'>SoftLayer_Service_Provider </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#uplinkHardwareComponents" name=uplinkHardwareComponents>uplinkHardwareComponents</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Hardware_Component'>SoftLayer_Hardware_Component[] </a></p></div>
        </div>
            </div>
</div>


