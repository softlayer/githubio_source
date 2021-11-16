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





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[accountId]: #accountid
#### [accountId]
The account id of the shipment.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[courierId]: #courierid
#### [courierId]
The courier id of the shipment.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[courierName]: #couriername
#### [courierName]
The courier name of the shipment.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[createUserId]: #createuserid
#### [createUserId]
The create user id of the shipment.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[destinationAddressId]: #destinationaddressid
#### [destinationAddressId]
The destination address id of the shipment.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[destinationDate]: #destinationdate
#### [destinationDate]
The destination date of the shipment.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique id of the shipment.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyUserId]: #modifyuserid
#### [modifyUserId]
The modify user id of the shipment.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[note]: #note
#### [note]
The shipment note (special handling instructions).  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[originationAddressId]: #originationaddressid
#### [originationAddressId]
The origination address id of the shipment.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[originationDate]: #originationdate
#### [originationDate]
The origination date of the shipment.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[statusId]: #statusid
#### [statusId]
The status id of the shipment.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[typeId]: #typeid
#### [typeId]
The type id of the shipment.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[viaAddressId]: #viaaddressid
#### [viaAddressId]
The via address id of the shipment.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account to which the shipment belongs.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**  



</div>
<div class="prop-row">

-----
[courier]: #courier
#### [courier]
The courier handling the shipment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Auxiliary_Shipping_Courier'>SoftLayer_Auxiliary_Shipping_Courier </a>**  



</div>
<div class="prop-row">

-----
[createEmployee]: #createemployee
#### [createEmployee]
The employee who created the shipment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**  



</div>
<div class="prop-row">

-----
[createUser]: #createuser
#### [createUser]
The customer user who created the shipment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>
<div class="prop-row">

-----
[currency]: #currency
#### [currency]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Currency'>SoftLayer_Billing_Currency </a>**  



</div>
<div class="prop-row">

-----
[destinationAddress]: #destinationaddress
#### [destinationAddress]
The address at which the shipment is received.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address </a>**  



</div>
<div class="prop-row">

-----
[masterTrackingData]: #mastertrackingdata
#### [masterTrackingData]
The one master tracking data for the shipment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Shipment_Tracking_Data'>SoftLayer_Account_Shipment_Tracking_Data </a>**  



</div>
<div class="prop-row">

-----
[modifyEmployee]: #modifyemployee
#### [modifyEmployee]
The employee who last modified the shipment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Employee'>SoftLayer_User_Employee </a>**  



</div>
<div class="prop-row">

-----
[modifyUser]: #modifyuser
#### [modifyUser]
The customer user who last modified the shipment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**  



</div>
<div class="prop-row">

-----
[originationAddress]: #originationaddress
#### [originationAddress]
The address from which the shipment is sent.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address </a>**  



</div>
<div class="prop-row">

-----
[shipmentItems]: #shipmentitems
#### [shipmentItems]
The items in the shipment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Shipment_Item'>SoftLayer_Account_Shipment_Item[] </a>**  



</div>
<div class="prop-row">

-----
[status]: #status
#### [status]
The status of the shipment.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Shipment_Status'>SoftLayer_Account_Shipment_Status </a>**  



</div>
<div class="prop-row">

-----
[trackingData]: #trackingdata
#### [trackingData]
All tracking data for the shipment and packages.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Shipment_Tracking_Data'>SoftLayer_Account_Shipment_Tracking_Data[] </a>**  



</div>
<div class="prop-row">

-----
[type]: #type
#### [type]
The type of shipment (e.g. for Data Transfer Service or Colocation Service).  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Shipment_Type'>SoftLayer_Account_Shipment_Type </a>**  



</div>
<div class="prop-row">

-----
[viaAddress]: #viaaddress
#### [viaAddress]
The address at which the shipment is received.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account_Address'>SoftLayer_Account_Address </a>**  



</div>

## Count
<div class="prop-row">

-----
[shipmentItemCount]: #shipmentitemcount
#### [shipmentItemCount]
A count of the items in the shipment.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[trackingDataCount]: #trackingdatacount
#### [trackingDataCount]
A count of all tracking data for the shipment and packages.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


