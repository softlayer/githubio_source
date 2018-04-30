---
title: "SoftLayer_Virtual_Host"
description: "The virtual host represents the platform on which virtual guests reside. At times a virtual host has no allocations on t... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Host"
---

# SoftLayer_Virtual_Host
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Virtual_Host' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Host' >Datatype</a></li>
    </ul>
</div>

## Description 
The virtual host represents the platform on which virtual guests reside. At times a virtual host has no allocations on the physical server, however with many modern platforms it is a virtual machine with small CPU and Memory allocations that runs in the Control Domain. 





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
                <a href="#accountId" name=accountId>accountId</a>
            </span>
            <div class='views-field-body'>A virtual host's associated account id  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The date a virtual host was created.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#description" name=description>description</a>
            </span>
            <div class='views-field-body'>A virtual host's description.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#enabledFlag" name=enabledFlag>enabledFlag</a>
            </span>
            <div class='views-field-body'>The enabled flag specifies whether a virtual host can run guests.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareId" name=hardwareId>hardwareId</a>
            </span>
            <div class='views-field-body'>A hardware device which a virtual host resides.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>Unique ID for a virtual host.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The date a virtual host was last modified.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>A virtual host's name.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#physicalMemoryCapacity" name=physicalMemoryCapacity>physicalMemoryCapacity</a>
            </span>
            <div class='views-field-body'>The amount of memory physically available for a virtual host.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#uuid" name=uuid>uuid</a>
            </span>
            <div class='views-field-body'>Unique ID for a virtual host's record on a virtualization platform.  </div>
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
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The account which a virtual host belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billedPerGuestFlag" name=billedPerGuestFlag>billedPerGuestFlag</a>
            </span>
            <div class='views-field-body'>Boolean flag indicating whether this virtualization platform gets billed per guest rather than at a fixed rate. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billedPerMemoryUsageFlag" name=billedPerMemoryUsageFlag>billedPerMemoryUsageFlag</a>
            </span>
            <div class='views-field-body'>Boolean flag indicating whether this virtualization platform gets billed per memory usage rather than at a fixed rate. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#guests" name=guests>guests</a>
            </span>
            <div class='views-field-body'>The guests associated with a virtual host. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardware" name=hardware>hardware</a>
            </span>
            <div class='views-field-body'>The hardware record which a virtual host resides on. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware_Server'>SoftLayer_Hardware_Server </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#metricTrackingObject" name=metricTrackingObject>metricTrackingObject</a>
            </span>
            <div class='views-field-body'>The metric tracking object for this virtual host. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Metric_Tracking_Object'>SoftLayer_Metric_Tracking_Object </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#guestCount" name=guestCount>guestCount</a>
            </span>
            <div class='views-field-body'>A count of the guests associated with a virtual host. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


