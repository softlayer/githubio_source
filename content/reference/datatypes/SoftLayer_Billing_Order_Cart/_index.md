---
title: "SoftLayer_Billing_Order_Cart"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Cart"
---

# SoftLayer_Billing_Order_Cart
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Billing_Order_Cart' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Billing_Order_Cart' >Datatype</a></li>
    </ul>
</div>

## Description 






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
[accountId]: #accountid
#### [accountId]
Identification Number of the account record tied to the quote  
<span class="type-label">Type: </span>**integer**

-----
[completedPurchaseDataId]: #completedpurchasedataid
#### [completedPurchaseDataId]
Identification Number of the order record tied to the quote.  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
Holds the date the quote record was created  
<span class="type-label">Type: </span>**dateTime**

-----
[expirationDate]: #expirationdate
#### [expirationDate]
This property holds the date of expiration of a quote, after that date the quote would be deem expired  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
The id use to identify a quote.  
<span class="type-label">Type: </span>**integer**

-----
[modifyDate]: #modifydate
#### [modifyDate]
Holds the date when the quote record was modified with reference to its creation date  
<span class="type-label">Type: </span>**dateTime**

-----
[name]: #name
#### [name]
The name given to quote by the initiator  
<span class="type-label">Type: </span>**string**

-----
[publicNote]: #publicnote
#### [publicNote]
This property Holds system generated notes. In our case if a quote is tied to an order where one of the order item has an inactive promotion code, the quote will be considered invalid.  
<span class="type-label">Type: </span>**string**

-----
[quoteKey]: #quotekey
#### [quoteKey]
Holds system generated hash password for the Quote  
<span class="type-label">Type: </span>**string**

-----
[status]: #status
#### [status]
This property Holds the current status of a Quote: pending,expired, saved or deleted  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
A quote's corresponding account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[doNotContactFlag]: #donotcontactflag
#### [doNotContactFlag]
Indicates whether the owner of the quote chosen to no longer be contacted.  
<span class="type-label">Type: </span>**boolean**

-----
[order]: #order
#### [order]
This order contains the records for which products were selected for this quote.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order </a>**

-----
[ordersFromQuote]: #ordersfromquote
#### [ordersFromQuote]
These are all the orders that were created from this quote.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Order'>SoftLayer_Billing_Order[] </a>**


## Count

-----
[ordersFromQuoteCount]: #ordersfromquotecount
#### [ordersFromQuoteCount]
A count of these are all the orders that were created from this quote.   
<span class="type-label">Type: </span>**unsigned long**

</div>


