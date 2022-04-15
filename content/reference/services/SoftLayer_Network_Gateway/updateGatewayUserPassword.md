---
title: "updateGatewayUserPassword"
description: "The method updates the Gateway password for the provided username.  It does not perform any synchronization with the Gateway to update the credentials.  The method only updates the IMS db with the username / password record for the Gateway. 

The 'username' and 'password' in the record template are required. 'username' must not be blank and must exist in the Gateway password records 'password' must not be blank 

Returns true if password change is successful, false if not successful 

"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Gateway"
---
