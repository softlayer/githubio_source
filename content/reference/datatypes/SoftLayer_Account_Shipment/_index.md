---
title: "SoftLayer_Account_Shipment"
description: "The SoftLayer_Account_Shipment data type contains information relating to a shipment. Basic information such as addresse... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Shipment"
---

# SoftLayer_Account_Shipment
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_Shipment' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_Shipment' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Account_Shipment data type contains information relating to a shipment. Basic information such as addresses, the shipment courier, and any tracking information for as shipment is accessible with this data type. 





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
            <div class='views-field-body'>The account id of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#courierId" name=courierId>courierId</a>
            </span>
            <div class='views-field-body'>The courier id of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#courierName" name=courierName>courierName</a>
            </span>
            <div class='views-field-body'>The courier name of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createUserId" name=createUserId>createUserId</a>
            </span>
            <div class='views-field-body'>The create user id of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#destinationAddressId" name=destinationAddressId>destinationAddressId</a>
            </span>
            <div class='views-field-body'>The destination address id of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#destinationDate" name=destinationDate>destinationDate</a>
            </span>
            <div class='views-field-body'>The destination date of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The unique id of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyUserId" name=modifyUserId>modifyUserId</a>
            </span>
            <div class='views-field-body'>The modify user id of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#note" name=note>note</a>
            </span>
            <div class='views-field-body'>The shipment note (special handling instructions). </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#originationAddressId" name=originationAddressId>originationAddressId</a>
            </span>
            <div class='views-field-body'>The origination address id of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#originationDate" name=originationDate>originationDate</a>
            </span>
            <div class='views-field-body'>The origination date of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#statusId" name=statusId>statusId</a>
            </span>
            <div class='views-field-body'>The status id of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#typeId" name=typeId>typeId</a>
            </span>
            <div class='views-field-body'>The type id of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The account to which the shipment belongs. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#courier" name=courier>courier</a>
            </span>
            <div class='views-field-body'>The courier handling the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Auxiliary_Shipping_Courier'>SoftLayer_Auxiliary_Shipping_Courier </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createEmployee" name=createEmployee>createEmployee</a>
            </span>
            <div class='views-field-body'>The employee who created the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createUser" name=createUser>createUser</a>
            </span>
            <div class='views-field-body'>The customer user who created the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#destinationAddress" name=destinationAddress>destinationAddress</a>
            </span>
            <div class='views-field-body'>The address at which the shipment is received. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyEmployee" name=modifyEmployee>modifyEmployee</a>
            </span>
            <div class='views-field-body'>The employee who last modified the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyUser" name=modifyUser>modifyUser</a>
            </span>
            <div class='views-field-body'>The customer user who last modified the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#originationAddress" name=originationAddress>originationAddress</a>
            </span>
            <div class='views-field-body'>The address from which the shipment is sent. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#shipmentItems" name=shipmentItems>shipmentItems</a>
            </span>
            <div class='views-field-body'>The items in the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Shipment_Item'>SoftLayer_Account_Shipment_Item[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#status" name=status>status</a>
            </span>
            <div class='views-field-body'>The status of the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Shipment_Status'>SoftLayer_Account_Shipment_Status </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#trackingData" name=trackingData>trackingData</a>
            </span>
            <div class='views-field-body'>The tracking data for the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Shipment_Tracking_Data'>SoftLayer_Account_Shipment_Tracking_Data[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#type" name=type>type</a>
            </span>
            <div class='views-field-body'>The type of shipment (e.g. for Data Transfer Service or Colocation Service). </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account_Shipment_Type'>SoftLayer_Account_Shipment_Type </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#shipmentItemCount" name=shipmentItemCount>shipmentItemCount</a>
            </span>
            <div class='views-field-body'>A count of the items in the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#trackingDataCount" name=trackingDataCount>trackingDataCount</a>
            </span>
            <div class='views-field-body'>A count of the tracking data for the shipment. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


