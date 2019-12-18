---
title: "SoftLayer_Container_Product_Order_Billing_Information"
description: "This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This datatype has every... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Product_Order_Billing_Information"
---

# SoftLayer_Container_Product_Order_Billing_Information
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Product_Order_Billing_Information' >Datatype</a></li>
    </ul>
</div>

## Description 
This is the datatype that needs to be populated and sent to SoftLayer_Product_Order::placeOrder. This datatype has everything required to place an order with SoftLayer. 





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
[billingAddressLine1]: #billingaddressline1
#### [billingAddressLine1]
The physical street address. Reserve information such as "apartment #123" or "Suite 2" for line 1.  
<span class="type-label">Type: </span>**string**

-----
[billingAddressLine2]: #billingaddressline2
#### [billingAddressLine2]
The second line in the address. Information such as suite number goes here.  
<span class="type-label">Type: </span>**string**

-----
[billingCity]: #billingcity
#### [billingCity]
The city in which a customer's account resides.  
<span class="type-label">Type: </span>**string**

-----
[billingCountryCode]: #billingcountrycode
#### [billingCountryCode]
The 2-character Country code for an account's address. (i.e. US)  
<span class="type-label">Type: </span>**string**

-----
[billingEmail]: #billingemail
#### [billingEmail]
The email address associated with a customer account.  
<span class="type-label">Type: </span>**string**

-----
[billingNameCompany]: #billingnamecompany
#### [billingNameCompany]
the company name for an account.  
<span class="type-label">Type: </span>**string**

-----
[billingNameFirst]: #billingnamefirst
#### [billingNameFirst]
The first name of the customer account owner.  
<span class="type-label">Type: </span>**string**

-----
[billingNameLast]: #billingnamelast
#### [billingNameLast]
The last name of the customer account owner  
<span class="type-label">Type: </span>**string**

-----
[billingPhoneFax]: #billingphonefax
#### [billingPhoneFax]
The fax number associated with a customer account.  
<span class="type-label">Type: </span>**string**

-----
[billingPhoneVoice]: #billingphonevoice
#### [billingPhoneVoice]
The phone number associated with a customer account.  
<span class="type-label">Type: </span>**string**

-----
[billingPostalCode]: #billingpostalcode
#### [billingPostalCode]
The Zip or Postal Code for the billing address on an account.  
<span class="type-label">Type: </span>**string**

-----
[billingState]: #billingstate
#### [billingState]
The State for the account.  
<span class="type-label">Type: </span>**string**

-----
[cardAccountNumber]: #cardaccountnumber
#### [cardAccountNumber]
The credit card number to use.  
<span class="type-label">Type: </span>**string**

-----
[cardExpirationMonth]: #cardexpirationmonth
#### [cardExpirationMonth]
The payment card expiration month  
<span class="type-label">Type: </span>**integer**

-----
[cardExpirationYear]: #cardexpirationyear
#### [cardExpirationYear]
The payment card expiration year  
<span class="type-label">Type: </span>**integer**

-----
[creditCardVerificationNumber]: #creditcardverificationnumber
#### [creditCardVerificationNumber]
The Card Verification Value Code (CVV) number  
<span class="type-label">Type: </span>**string**

-----
[euSupported]: #eusupported
#### [euSupported]
1 = opted in,  0 = not opted in. Select the EU Supported option if you use IBM Bluemix Infrastructure services to process EU citizens' personal data. This option limits Level 1 and Level 2 support to the EU. However, IBM Bluemix and SoftLayer teams outside the EU perform processing activities when they are not resolved at Level 1 or 2. These activities are always at your instruction and do not impact the security or privacy of your data. As with our standard services, you must review the impact these cross-border processing activities have on your services and take any necessary measures, including review of IBM's US-EU Privacy Shield registration and Data Processing Addendum.  If you select products, services, or locations outside the EU, all processing activities will be performed outside of the EU. If you select other IBM services in addition to Bluemix IaaS (IBM or a third party), determine the service location in order to meet any additional data protection or processing requirements that permit cross-border transfers.   
<span class="type-label">Type: </span>**boolean**

-----
[isBusinessFlag]: #isbusinessflag
#### [isBusinessFlag]
If true, order is being placed by a business.   
<span class="type-label">Type: </span>**boolean**

-----
[taxExempt]: #taxexempt
#### [taxExempt]
Tax exempt status. 1 = exempt (not taxable),  0 = not exempt (taxable)  
<span class="type-label">Type: </span>**integer**

-----
[vatId]: #vatid
#### [vatId]
The VAT ID entered at checkout  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

</div>


