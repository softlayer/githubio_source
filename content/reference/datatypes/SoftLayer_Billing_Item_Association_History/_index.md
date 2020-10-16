---
title: "SoftLayer_Billing_Item_Association_History"
description: "The SoftLayer_Billing_Item_Association_History type keeps a record of which server billing items an 'orphan' item has be... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Item_Association_History"
---

# SoftLayer_Billing_Item_Association_History
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Item_Association_History' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Billing_Item_Association_History type keeps a record of which server billing items an "orphan" item has been associated with. Orphan billing items are billable items for secondary portable services (such as secondary subnets and StorageLayer accounts) that are not associated with a server and appear at the bottom of a SoftLayer invoice. The [SoftLayer_Billing_Item::setAssociationId]({{<ref "reference/services/SoftLayer_Billing_Item/setAssociationId">}}) method allows you to associate these kinds of items with servers, making them appear as a child item of the server on your invoice. A SoftLayer_Billing_Item_Association_History record is created every time one of these associations are set. 


### associatedMethods

*  [SoftLayer_Billing_Item::getAssociatedBillingItemHistory](/reference/services/SoftLayer_Billing_Item/getAssociatedBillingItemHistory )
*  [SoftLayer_Billing_Item::setAssociationId](/reference/services/SoftLayer_Billing_Item/setAssociationId )
*  [SoftLayer_Billing_Item::removeAssociationId](/reference/services/SoftLayer_Billing_Item/removeAssociationId )



### seeAlso

* [SoftLayer_Billing_Item](/reference/datatypes/SoftLayer_Billing_Item )




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
[associatedBillingItemId]: #associatedbillingitemid
#### [associatedBillingItemId]
The internal identifier of the server billing item that an orphaned billing item was associated with.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[billingItemId]: #billingitemid
#### [billingItemId]
The internal identifier of the billing item that was associated with a server billing item.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date that a billing item association was last changed.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A billing item association history's internal identifier.  
<span class="type-label">Type: </span>**integer**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[associatedBillingItem]: #associatedbillingitem
#### [associatedBillingItem]
The server billing item that an orphaned billing item was associated with.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The billing item that was associated with a server billing item.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>

## Count
</div>


