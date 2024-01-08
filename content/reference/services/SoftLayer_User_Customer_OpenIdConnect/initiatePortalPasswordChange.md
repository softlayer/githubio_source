---
title: "initiatePortalPasswordChange"
description: "Sends password change email to the user containing url that allows the user the change their password. This is the first step when a user wishes to change their password.  The url that is generated contains a one-time use token that is valid for only 24-hours. 

If this is a new master user who has never logged into the portal, then password reset will be initiated. Once a master user has logged into the portal, they must setup their security questions prior to logging out because master users are required to answer a security question during the password reset process.  Should a master user not have security questions defined and not remember their password in order to define the security questions, then they will need to contact support at live chat or Revenue Services for assistance. 

Due to security reasons, the number of reset requests per username are limited within a undisclosed timeframe. "
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

### [REST Example](#initiatePortalPasswordChange-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#initiatePortalPasswordChange-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer_OpenIdConnect/initiatePortalPasswordChange'
```
