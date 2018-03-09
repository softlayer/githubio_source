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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingAddressLine1" name=billingAddressLine1>billingAddressLine1</a>
            </span>
            <div class='views-field-body'>The physical street address. Reserve information such as "apartment #123" or "Suite 2" for line 1. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingAddressLine2" name=billingAddressLine2>billingAddressLine2</a>
            </span>
            <div class='views-field-body'>The second line in the address. Information such as suite number goes here. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCity" name=billingCity>billingCity</a>
            </span>
            <div class='views-field-body'>The city in which a customer's account resides. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingCountryCode" name=billingCountryCode>billingCountryCode</a>
            </span>
            <div class='views-field-body'>The 2-character Country code for an account's address. (i.e. US) </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingEmail" name=billingEmail>billingEmail</a>
            </span>
            <div class='views-field-body'>The email address associated with a customer account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingNameCompany" name=billingNameCompany>billingNameCompany</a>
            </span>
            <div class='views-field-body'>the company name for an account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingNameFirst" name=billingNameFirst>billingNameFirst</a>
            </span>
            <div class='views-field-body'>The first name of the customer account owner. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingNameLast" name=billingNameLast>billingNameLast</a>
            </span>
            <div class='views-field-body'>The last name of the customer account owner </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingPhoneFax" name=billingPhoneFax>billingPhoneFax</a>
            </span>
            <div class='views-field-body'>The fax number associated with a customer account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingPhoneVoice" name=billingPhoneVoice>billingPhoneVoice</a>
            </span>
            <div class='views-field-body'>The phone number associated with a customer account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingPostalCode" name=billingPostalCode>billingPostalCode</a>
            </span>
            <div class='views-field-body'>The Zip or Postal Code for the billing address on an account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingState" name=billingState>billingState</a>
            </span>
            <div class='views-field-body'>The State for the account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#cardAccountNumber" name=cardAccountNumber>cardAccountNumber</a>
            </span>
            <div class='views-field-body'>The credit card number to use. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#cardExpirationMonth" name=cardExpirationMonth>cardExpirationMonth</a>
            </span>
            <div class='views-field-body'>The payment card expiration month </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#cardExpirationYear" name=cardExpirationYear>cardExpirationYear</a>
            </span>
            <div class='views-field-body'>The payment card expiration year </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#creditCardVerificationNumber" name=creditCardVerificationNumber>creditCardVerificationNumber</a>
            </span>
            <div class='views-field-body'>The Card Verification Value Code (CVV) number </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#euSupported" name=euSupported>euSupported</a>
            </span>
            <div class='views-field-body'>1 = opted in,  0 = not opted in. Select the EU Supported option if you use IBM Bluemix Infrastructure services to process EU citizens' personal data. This option limits Level 1 and Level 2 support to the EU. However, IBM Bluemix and SoftLayer teams outside the EU perform processing activities when they are not resolved at Level 1 or 2. These activities are always at your instruction and do not impact the security or privacy of your data. As with our standard services, you must review the impact these cross-border processing activities have on your services and take any necessary measures, including review of IBM's US-EU Privacy Shield registration and Data Processing Addendum.  If you select products, services, or locations outside the EU, all processing activities will be performed outside of the EU. If you select other IBM services in addition to Bluemix IaaS (IBM or a third party), determine the service location in order to meet any additional data protection or processing requirements that permit cross-border transfers.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#taxExempt" name=taxExempt>taxExempt</a>
            </span>
            <div class='views-field-body'>Tax exempt status. 1 = exempt (not taxable),  0 = not exempt (taxable) </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#vatId" name=vatId>vatId</a>
            </span>
            <div class='views-field-body'>The VAT ID entered at checkout </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


