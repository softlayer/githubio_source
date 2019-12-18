---
title: "SoftLayer_Container_Product_Order_Attribute_Address"
description: "This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. The SoftLayer_Container... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Product_Order_Attribute_Address"
---

# SoftLayer_Container_Product_Order_Attribute_Address
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Product_Order_Attribute_Address' >Datatype</a></li>
    </ul>
</div>

## Description 
This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. The SoftLayer_Container_Product_Order_Attribute_Address datatype contains the address information. 





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
[addressLine1]: #addressline1
#### [addressLine1]
The physical street address.  
<span class="type-label">Type: </span>**string**

-----
[addressLine2]: #addressline2
#### [addressLine2]
The second line in the address. Information such as suite number goes here.  
<span class="type-label">Type: </span>**string**

-----
[city]: #city
#### [city]
The city name  
<span class="type-label">Type: </span>**string**

-----
[countryCode]: #countrycode
#### [countryCode]
The 2-character Country code. (i.e. US)  
<span class="type-label">Type: </span>**string**

-----
[nonUsState]: #nonusstate
#### [nonUsState]
State, Region or Province not part of the U.S. or Canada.  
<span class="type-label">Type: </span>**string**

-----
[postalCode]: #postalcode
#### [postalCode]
The Zip or Postal Code.  
<span class="type-label">Type: </span>**string**

-----
[state]: #state
#### [state]
U.S. State, Region or Canadian Province.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


