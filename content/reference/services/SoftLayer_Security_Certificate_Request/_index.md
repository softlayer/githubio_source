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

To create an SSL certificate order, pass a completed [[SoftLayer_Container_Product_Order_Security_Certificate|SSL order container]] to the [[SoftLayer_Product_Order::placeOrder|SoftLayer ordering service]]. 
        
        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/cancelSslOrder'> cancelSslOrder</a> </span>
            <div class='views-field-body'>Cancels a pending SSL certificate order at the Certificate Authority</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account to which a SSL certificate request belongs.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/getAdministratorEmailDomains'> getAdministratorEmailDomains</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/getAdministratorEmailPrefixes'> getAdministratorEmailPrefixes</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/getCertificateAuthorityName'> getCertificateAuthorityName</a> </span>
            <div class='views-field-body'>Retrieve the Certificate Authority name</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Security_Certificate_Request record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/getOrder'> getOrder</a> </span>
            <div class='views-field-body'>Retrieve the order contains the information related to a SSL certificate request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/getOrderItem'> getOrderItem</a> </span>
            <div class='views-field-body'>Retrieve the associated order item for this SSL certificate request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/getPreviousOrderData'> getPreviousOrderData</a> </span>
            <div class='views-field-body'>Returns previous SSL certificate order data.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/getSslCertificateRequests'> getSslCertificateRequests</a> </span>
            <div class='views-field-body'>Returns all the SSL certificate requests</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/getStatus'> getStatus</a> </span>
            <div class='views-field-body'>Retrieve the status of a SSL certificate request.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/resendEmail'> resendEmail</a> </span>
            <div class='views-field-body'>Have the Certificate Authority send various emails</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Security_Certificate_Request/validateCsr'> validateCsr</a> </span>
            <div class='views-field-body'>Validates a Certificate Signing Request (CSR) with the certificate authority (CA). </div>
        </div>
        </div>
</div>

