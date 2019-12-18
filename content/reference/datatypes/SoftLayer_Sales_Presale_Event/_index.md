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
    <li id='service'> <a href='/reference/services/SoftLayer_Sales_Presale_Event' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Sales_Presale_Event' >Datatype</a></li>
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

## Local
-----
[description]: #description
#### [description]
Description of the presale event.  
<span class="type-label">Type: </span>**string**

-----
[endDate]: #enddate
#### [endDate]
End date of the presale event. Orders can be approved and provisioned after this date.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
Presale event unique identifier.  
<span class="type-label">Type: </span>**integer**

-----
[itemId]: #itemid
#### [itemId]
[SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}}) id associated with the presale event.  
<span class="type-label">Type: </span>**integer**

-----
[locationId]: #locationid
#### [locationId]
[SoftLayer_Location]({{<ref "reference/datatypes/SoftLayer_Location">}}) id for the presale event.  
<span class="type-label">Type: </span>**integer**

-----
[startDate]: #startdate
#### [startDate]
Start date of the presale event. Orders cannot be approved before this date.  
<span class="type-label">Type: </span>**dateTime**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[activeFlag]: #activeflag
#### [activeFlag]
A flag to indicate that the presale event is currently active. A presale event is active if the current time is between the start and end dates.  
<span class="type-label">Type: </span>**boolean**

-----
[expiredFlag]: #expiredflag
#### [expiredFlag]
A flag to indicate that the presale event is expired. A presale event is expired if the current time is after the end date.  
<span class="type-label">Type: </span>**boolean**

-----
[item]: #item
#### [item]
The [SoftLayer_Product_Item]({{<ref "reference/datatypes/SoftLayer_Product_Item">}}) associated with the presale event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Product_Item'>SoftLayer_Product_Item </a>**

-----
[location]: #location
#### [location]
The [SoftLayer_Location]({{<ref "reference/datatypes/SoftLayer_Location">}}) associated with the presale event.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**

-----
[orders]: #orders
#### [orders]
The orders ([SoftLayer_Billing_Order]({{<ref "reference/datatypes/SoftLayer_Billing_Order">}})) associated with this presale event that were created for the customer's account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order[] </a>**


## Count

-----
[orderCount]: #ordercount
#### [orderCount]
A count of the orders ([SoftLayer_Billing_Order]({{<ref "reference/datatypes/SoftLayer_Billing_Order">}})) associated with this presale event that were created for the customer's account.   
<span class="type-label">Type: </span>**unsigned long**

</div>


