---
title: "SoftLayer_Security_Certificate_Request"
description: "SoftLayer_Security_Certificate_Request holds your SSL certificate request data. This data is used to place an SSL certif... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate_Request"
---
# SoftLayer_Security_Certificate_Request
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Security_Certificate_Request' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Security_Certificate_Request' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer_Security_Certificate_Request holds your SSL certificate request data. This data is used to place an SSL certificate order with a Certificate Authority. 

To create an SSL certificate order, pass a completed [SoftLayer_Container_Product_Order_Security_Certificate]({{<ref "reference/datatypes/SoftLayer_Container_Product_Order_Security_Certificate">}}). 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [cancelSslOrder](/reference/services/SoftLayer_Security_Certificate_Request/cancelSslOrder)
Cancels a pending SSL certificate order at the Certificate Authority

#### [getAccount](/reference/services/SoftLayer_Security_Certificate_Request/getAccount)
Retrieve the account to which a SSL certificate request belongs.

#### [getAdministratorEmailDomains](/reference/services/SoftLayer_Security_Certificate_Request/getAdministratorEmailDomains)


#### [getAdministratorEmailPrefixes](/reference/services/SoftLayer_Security_Certificate_Request/getAdministratorEmailPrefixes)


#### [getObject](/reference/services/SoftLayer_Security_Certificate_Request/getObject)
Retrieve a SoftLayer_Security_Certificate_Request record.

#### [getOrder](/reference/services/SoftLayer_Security_Certificate_Request/getOrder)
Retrieve the order contains the information related to a SSL certificate request.

#### [getOrderItem](/reference/services/SoftLayer_Security_Certificate_Request/getOrderItem)
Retrieve the associated order item for this SSL certificate request.

#### [getPreviousOrderData](/reference/services/SoftLayer_Security_Certificate_Request/getPreviousOrderData)
Returns previous SSL certificate order data.

#### [getSslCertificateRequests](/reference/services/SoftLayer_Security_Certificate_Request/getSslCertificateRequests)
Returns all the SSL certificate requests

#### [getStatus](/reference/services/SoftLayer_Security_Certificate_Request/getStatus)
Retrieve the status of a SSL certificate request.

#### [resendEmail](/reference/services/SoftLayer_Security_Certificate_Request/resendEmail)
Have the Certificate Authority send various emails

#### [validateCsr](/reference/services/SoftLayer_Security_Certificate_Request/validateCsr)
Validates a Certificate Signing Request (CSR) with the certificate authority (CA). 

</div>

