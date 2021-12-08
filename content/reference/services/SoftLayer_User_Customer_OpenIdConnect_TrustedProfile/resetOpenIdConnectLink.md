---
title: "resetOpenIdConnectLink"
description: "This method will change the IBMid that a SoftLayer user is linked to, if we need to do that for some reason. It will do... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect_TrustedProfile"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect_trustedprofile/resetOpenIdConnectLink"
---
# [SoftLayer_User_Customer_OpenIdConnect_TrustedProfile](/reference/services/SoftLayer_User_Customer_OpenIdConnect_TrustedProfile)::resetOpenIdConnectLink


Change the link of a user for OpenIdConnect managed accounts, provided the


## Overview 
This method will change the IBMid that a SoftLayer user is linked to, if we need to do that for some reason. It will do this by modifying the link to the desired new IBMid. NOTE:  This method cannot be used to "un-link" a SoftLayer user.  Once linked, a SoftLayer user can never be un-linked. Also, this method cannot be used to reset the link if the user account is already Bluemix linked. To reset a link for the Bluemix-linked user account, use resetOpenIdConnectLinkUnifiedUserManagementMode. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| The provider type. Currently only 'IBMid' is considered a valid value.|
|newIbmIdUsername| string| The new IBMid the user is trying to switch to.|
|removeSecuritySettings| boolean| Flag to indicate if the security settings for the user should be|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnect_TrustedProfileInitParameters


### Return Values
* void




