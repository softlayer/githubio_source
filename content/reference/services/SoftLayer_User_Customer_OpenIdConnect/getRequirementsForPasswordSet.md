---
title: "getRequirementsForPasswordSet"
description: "Retrieve the authentication requirements for an outstanding password set/reset request.  The requirements returned in the same SoftLayer_Container_User_Customer_PasswordSet container which is provided as a parameter into this request.  The SoftLayer_Container_User_Customer_PasswordSet::authenticationMethods array will contain an entry for each authentication method required for the user.  See SoftLayer_Container_User_Customer_PasswordSet for more details. 

If the user has required authentication methods, then authentication information will be supplied to the SoftLayer_User_Customer::processPasswordSetRequest method within this same SoftLayer_Container_User_Customer_PasswordSet container.  All existing information in the container must continue to exist in the container to complete the password set/reset process. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer_OpenIdConnect"
---

### [REST Example](#getRequirementsForPasswordSet-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getRequirementsForPasswordSet-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_User_Customer_PasswordSet]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/{SoftLayer_User_Customer_OpenIdConnectID}/getRequirementsForPasswordSet'
```
