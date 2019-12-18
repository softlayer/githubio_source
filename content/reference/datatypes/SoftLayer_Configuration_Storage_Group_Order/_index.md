---
title: "SoftLayer_Configuration_Storage_Group_Order"
description: "Single storage group(array) used for a hardware server order. 

If a raid configuration is required this object will des... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Configuration"
classes:
    - "SoftLayer_Configuration_Storage_Group_Order"
---

# SoftLayer_Configuration_Storage_Group_Order
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Order' >Datatype</a></li>
    </ul>
</div>

## Description 
Single storage group(array) used for a hardware server order. 

If a raid configuration is required this object will describe a single array that will be configured on the server. If the server requires more than one array, a storage group will need to be created for each array. 





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
[arrayNumber]: #arraynumber
#### [arrayNumber]
  
<span class="type-label">Type: </span>**integer**

-----
[arraySize]: #arraysize
#### [arraySize]
  
<span class="type-label">Type: </span>**decimal**

-----
[arrayTypeId]: #arraytypeid
#### [arrayTypeId]
  
<span class="type-label">Type: </span>**integer**

-----
[billingOrderItemId]: #billingorderitemid
#### [billingOrderItemId]
  
<span class="type-label">Type: </span>**integer**

-----
[controller]: #controller
#### [controller]
  
<span class="type-label">Type: </span>**integer**

-----
[hardDrives]: #harddrives
#### [hardDrives]
  
<span class="type-label">Type: </span>**array of integers**

-----
[hotSpareDrives]: #hotsparedrives
#### [hotSpareDrives]
  
<span class="type-label">Type: </span>**array of integers**

-----
[lvmFlag]: #lvmflag
#### [lvmFlag]
  
<span class="type-label">Type: </span>**boolean**

-----
[partitionData]: #partitiondata
#### [partitionData]
  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[arrayType]: #arraytype
#### [arrayType]
Raid mode for the storage group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Configuration_Storage_Group_Array_Type'>SoftLayer_Configuration_Storage_Group_Array_Type </a>**

-----
[billingOrderItem]: #billingorderitem
#### [billingOrderItem]
The order item that relates to this storage group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order_Item'>SoftLayer_Billing_Order_Item </a>**


## Count
</div>


