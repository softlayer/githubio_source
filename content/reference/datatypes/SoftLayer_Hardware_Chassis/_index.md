---
title: "SoftLayer_Hardware_Chassis"
description: "Every piece of hardware in SoftLayer's datacenters, including customer servers, are housed in one of many hardware chass... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Chassis"
---

# SoftLayer_Hardware_Chassis
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Chassis' >Datatype</a></li>
    </ul>
</div>

## Description 
Every piece of hardware in SoftLayer's datacenters, including customer servers, are housed in one of many hardware chassis. The SoftLayer_Hardware_Chassis data type defines these chassis. 


### associatedMethods

*  [SoftLayer_Hardware::getHardwareChassis](/reference/services/SoftLayer_Hardware/getHardwareChassis )



### seeAlso

* [SoftLayer_Hardware (type)](/reference/datatypes/SoftLayer_Hardware (type) )


* [SoftLayer_Hardware_Server (type)](/reference/datatypes/SoftLayer_Hardware_Server (type) )




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
                <a href="#formFactorId" name=formFactorId>formFactorId</a>
            </span>
            <div class='views-field-body'>A hardware form factor internal identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A hardware chassis' internal identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#manufacturer" name=manufacturer>manufacturer</a>
            </span>
            <div class='views-field-body'>A hardware chassis' manufacturer. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>A hardware chassis' name. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#unitSize" name=unitSize>unitSize</a>
            </span>
            <div class='views-field-body'>The physical size of a hardware chassis.  Currently this relates to the 'U' size of a chassis buy default. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#version" name=version>version</a>
            </span>
            <div class='views-field-body'>A hardware chassis' revision number. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#backplaneCapacity" name=backplaneCapacity>backplaneCapacity</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#bayCapacity" name=bayCapacity>bayCapacity</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#driveCapacity" name=driveCapacity>driveCapacity</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#driveControllerCapacity" name=driveControllerCapacity>driveControllerCapacity</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#gpuCapacity" name=gpuCapacity>gpuCapacity</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareFunction" name=hardwareFunction>hardwareFunction</a>
            </span>
            <div class='views-field-body'>A hardware's function. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware_Function'>SoftLayer_Hardware_Function </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#moduleCapacity" name=moduleCapacity>moduleCapacity</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#powerCapacity" name=powerCapacity>powerCapacity</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


