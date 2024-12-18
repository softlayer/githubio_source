---
title: "resetOpenIdConnectLink"
description: "This method will change the IBMid that a SoftLayer user is linked to, if we need to do that for some reason. It will do this by modifying the link to the desired new IBMid. NOTE:  This method cannot be used to 'un-link' a SoftLayer user.  Once linked, a SoftLayer user can never be un-linked. Also, this method cannot be used to reset the link if the user account is already Bluemix linked. To reset a link for the Bluemix-linked user account, use resetOpenIdConnectLinkUnifiedUserManagementMode. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
type: "reference"
layout: "method"
mainService : "SoftLayer_User_Customer"
---

### [REST Example](#resetOpenIdConnectLink-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#resetOpenIdConnectLink-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string, string, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/{SoftLayer_User_CustomerID}/resetOpenIdConnectLink'
```
