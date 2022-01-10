---
title: "SoftLayer_Security_Certificate_Request_Status"
description: "SoftLayer_Security_Certificate_Request_Status indicates the status of your SSL certificate request. When you submit an SSL certificate order, the associated certificate request will be in the 'Pending CA Approval' status. This is the only status in which can cancel your order. 

Once the certificate authority (CA) approves your order, the status will change to 'Approved'. Once your order is approved, you will receive your fulfillment email from the CA. The email will contain your SSL certificate. SoftLayer does not store your SSL certificate in our system. If you lose the email from your CA, you can have the fulfillment email sent again via the SoftLayer customer portal or by using [SoftLayer_Security_Certificate_Request::resendEmail](reference/services/SoftLayer_Security_Certificate_Request/resendEmail). Your approved order will be picked up by SoftLayer's billing system and it will complete the payment process. Finally, your order will change to 'Complete' status when the payment process is successful. 

There might be a chance that your SSL certificate order could rejected by a CA. Our automated system will put a rejected order into 'Canceled' status. You can contact SoftLayer Support for more details. "
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "Security"
classes:
    - "SoftLayer_Security_Certificate_Request_Status"
type: "reference"
layout: "service"
mainService : "SoftLayer_Security_Certificate_Request_Status"
---
