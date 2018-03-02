---
title: "SoftLayer_Sales_Presale_Event"
description: "The presale event data types indicate the information regarding an individual presale event. The '''locationId''' will i... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Sales"
classes:
    - "SoftLayer_Sales_Presale_Event"
---

# SoftLayer_Sales_Presale_Event
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Sales_Presale_Event' >Datatype</a></li>
    </ul>
</div>

## Description 
The presale event data types indicate the information regarding an individual presale event. The '''locationId''' will indicate the datacenter associated with the presale event. The '''itemId''' will indicate the product item associated with a particular presale event - however these are more rare. The '''startDate''' and '''endDate''' will provide information regarding when the presale event is available for use. At the end of the presale event, the server or services purchased will be available once approved and provisioned. 


### associatedMethods

*  [SoftLayer_Sales_Presale_Event::getObject](/reference/services/SoftLayer_Sales_Presale_Event/getObject )





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
            <span class='views-field-title'><a href="#description" name=description>description</a></span>
            <div class='views-field-body'>Description of the presale event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#endDate" name=endDate>endDate</a></span>
            <div class='views-field-body'>End date of the presale event. Orders can be approved and provisioned after this date. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>Presale event unique identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#itemId" name=itemId>itemId</a></span>
            <div class='views-field-body'>[[SoftLayer_Product_Item]] id associated with the presale event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#locationId" name=locationId>locationId</a></span>
            <div class='views-field-body'>[[SoftLayer_Location]] id for the presale event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#startDate" name=startDate>startDate</a></span>
            <div class='views-field-body'>Start date of the presale event. Orders cannot be approved before this date. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#activeFlag" name=activeFlag>activeFlag</a></span>
            <div class='views-field-body'>A flag to indicate that the presale event is currently active. A presale event is active if the current time is between the start and end dates. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#expiredFlag" name=expiredFlag>expiredFlag</a></span>
            <div class='views-field-body'>A flag to indicate that the presale event is expired. A presale event is expired if the current time is after the end date. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#item" name=item>item</a></span>
            <div class='views-field-body'>The [[SoftLayer_Product_Item]] associated with the presale event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#location" name=location>location</a></span>
            <div class='views-field-body'>The [[SoftLayer_Location]] associated with the presale event. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orders" name=orders>orders</a></span>
            <div class='views-field-body'>The orders ([[SoftLayer_Billing_Order]]) associated with this presale event that were created for the customer's account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#orderCount" name=orderCount>orderCount</a></span>
            <div class='views-field-body'>A count of the orders ([[SoftLayer_Billing_Order]]) associated with this presale event that were created for the customer's account. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


