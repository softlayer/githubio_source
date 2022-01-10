---
title: "resetOpenIdConnectLinkUnifiedUserManagementMode"
description: "This method will change the IBMid that a SoftLayer master user is linked to, if we need to do that for some reason. It w... "
layout: "method"
tags:
    - "method"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_OpenIdConnect"
aliases:
    - "/reference/services/softlayer_user_customer_openidconnect/resetOpenIdConnectLinkUnifiedUserManagementMode"
---
# [SoftLayer_User_Customer_OpenIdConnect](/reference/services/SoftLayer_User_Customer_OpenIdConnect)::resetOpenIdConnectLinkUnifiedUserManagementMode


Change the link of a master user for OpenIdConnect managed accounts,


## Overview 
This method will change the IBMid that a SoftLayer master user is linked to, if we need to do that for some reason. It will do this by unlinking the new owner IBMid from its current user association in this account, if there is one (note that the new owner IBMid is not required to already be a member of the IMS account). Then it will modify the existing IBMid link for the master user to use the new owner IBMid-realm IAMid. At this point, if the new owner IBMid isn't already a member of the PaaS account, it will attempt to add it. As a last step, it will call PaaS to modify the owner on that side, if necessary.  Only when all those steps are complete, it will commit the IMS-side DB changes.  Then, it will clean up the SoftLayer user that was linked to the new owner IBMid (this user became unlinked as the first step in this process).  It will also call BSS to delete the old owner IBMid. NOTE:  This method cannot be used to "un-link" a SoftLayer user.  Once linked, a SoftLayer user can never be un-linked. Also, this method cannot be used to reset the link if the user account is not Bluemix linked. To reset a link for the user account not linked to Bluemix, use resetOpenIdConnectLink. 

-----

### Parameters 
|Name | Type | Description |
| --- | --- | --- |
|providerType| string| The provider type. Currently only 'IBMid' is considered a valid value.|
|newIbmIdUsername| string| The new IBMid (username, *NOT* IBMid-xxx format IAMid) we are trying to switch to.|
|removeSecuritySettings| boolean| Flag to indicate if the security settings for the user should be|


### Required Headers
* authenticate
* SoftLayer_User_Customer_OpenIdConnectInitParameters


### Return Values
* void




