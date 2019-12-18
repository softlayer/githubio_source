---
title: "SoftLayer_Security_Certificate_Request_Status"
description: "SoftLayer_Security_Certificate_Request_Status indicates the status of your SSL certificate request. When you submit an S... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate_Request_Status"
---
# SoftLayer_Security_Certificate_Request_Status
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Security_Certificate_Request_Status' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Security_Certificate_Request_Status' >Datatype</a></li>
    </ul>
</div>

## Description
SoftLayer_Security_Certificate_Request_Status indicates the status of your SSL certificate request. When you submit an SSL certificate order, the associated certificate request will be in the "Pending CA Approval" status. This is the only status in which can cancel your order. 

Once the certificate authority (CA) approves your order, the status will change to "Approved". Once your order is approved, you will receive your fulfillment email from the CA. The email will contain your SSL certificate. SoftLayer does not store your SSL certificate in our system. If you lose the email from your CA, you can have the fulfillment email sent again via the SoftLayer customer portal or by using [SoftLayer_Security_Certificate_Request::resendEmail]({{<ref "reference/services/SoftLayer_Security_Certificate_Request/resendEmail">}}). Your approved order will be picked up by SoftLayer's billing system and it will complete the payment process. Finally, your order will change to "Complete" status when the payment process is successful. 

There might be a chance that your SSL certificate order could rejected by a CA. Our automated system will put a rejected order into "Canceled" status. You can contact SoftLayer Support for more details. 



        
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

#### [getObject](/reference/services/SoftLayer_Security_Certificate_Request_Status/getObject)
Retrieve a SoftLayer_Security_Certificate_Request_Status record.

#### [getSslRequestStatuses](/reference/services/SoftLayer_Security_Certificate_Request_Status/getSslRequestStatuses)
Returns all SSL certificate request status objects

</div>

