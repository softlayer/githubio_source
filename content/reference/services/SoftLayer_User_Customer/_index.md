---
title: "SoftLayer_User_Customer"
description: "Every SoftLayer account has one or more portal users which are defined by the SoftLayer_User_Customer service. Every Sof... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer"
---
# SoftLayer_User_Customer
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_User_Customer' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_User_Customer' >Datatype</a></li>
    </ul>
</div>

## Description
Every SoftLayer account has one or more portal users which are defined by the SoftLayer_User_Customer service. Every SoftLayer customer account has a master user account whose name corresponds to their account id preceded by the letters "SL". Users exist in a parent-child relationship. Child users inherit the properties and permissions of their parent user while conversely a user may have more than one child users. 

API users have full access to their own portal user account and they could also have access to other users under their SoftLayer customer account, if they have "Manage Users" permission in the customer portal. 



        
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

#### [acknowledgeSupportPolicy](/reference/services/SoftLayer_User_Customer/acknowledgeSupportPolicy)


#### [addApiAuthenticationKey](/reference/services/SoftLayer_User_Customer/addApiAuthenticationKey)
Create a user's API authentication key.

#### [addBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addBulkDedicatedHostAccess)
Grant access to the user for one or more dedicated hosts devices.

#### [addBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/addBulkHardwareAccess)
Add multiple hardware to a portal user's hardware access list.

#### [addBulkPortalPermission](/reference/services/SoftLayer_User_Customer/addBulkPortalPermission)
Add multiple permissions to a portal user's permission set.

#### [addBulkRoles](/reference/services/SoftLayer_User_Customer/addBulkRoles)


#### [addBulkVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/addBulkVirtualGuestAccess)
Add multiple CloudLayer Computing Instances to a portal user's access list.

#### [addDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addDedicatedHostAccess)
Grant access to the user for a single dedicated host device.

#### [addExternalBinding](/reference/services/SoftLayer_User_Customer/addExternalBinding)


#### [addHardwareAccess](/reference/services/SoftLayer_User_Customer/addHardwareAccess)
Add hardware to a portal user's hardware access list.

#### [addNotificationSubscriber](/reference/services/SoftLayer_User_Customer/addNotificationSubscriber)
Create a notification subscription record for the user.

#### [addPortalPermission](/reference/services/SoftLayer_User_Customer/addPortalPermission)
Add a permission to a portal user's permission set.

#### [addRole](/reference/services/SoftLayer_User_Customer/addRole)


#### [addVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/addVirtualGuestAccess)
Add a CloudLayer Computing Instance to a portal user's access list.

#### [assignNewParentId](/reference/services/SoftLayer_User_Customer/assignNewParentId)
Assign a different parent to this user. 

#### [changePreference](/reference/services/SoftLayer_User_Customer/changePreference)
Change preference values for the current user

#### [checkExternalAuthenticationStatus](/reference/services/SoftLayer_User_Customer/checkExternalAuthenticationStatus)
Checks if an external authentication is complete or not

#### [checkPhoneFactorAuthenticationForPasswordSet](/reference/services/SoftLayer_User_Customer/checkPhoneFactorAuthenticationForPasswordSet)
Check the status of an outstanding Phone Factor Authentication for Password Set

#### [createNotificationSubscriber](/reference/services/SoftLayer_User_Customer/createNotificationSubscriber)
Create a new subscriber for a given resource.

#### [createObject](/reference/services/SoftLayer_User_Customer/createObject)
Create a new user record.

#### [createSubscriberDeliveryMethods](/reference/services/SoftLayer_User_Customer/createSubscriberDeliveryMethods)
Create delivery methods for the subscriber.

#### [deactivateNotificationSubscriber](/reference/services/SoftLayer_User_Customer/deactivateNotificationSubscriber)
Delete a subscriber for a given resource.

#### [editObject](/reference/services/SoftLayer_User_Customer/editObject)
Update a user's information.

#### [editObjects](/reference/services/SoftLayer_User_Customer/editObjects)
Update a collection of users' information

#### [findUserPreference](/reference/services/SoftLayer_User_Customer/findUserPreference)


#### [getAccount](/reference/services/SoftLayer_User_Customer/getAccount)
Retrieve the customer account that a user belongs to.

#### [getActions](/reference/services/SoftLayer_User_Customer/getActions)


#### [getActiveExternalAuthenticationVendors](/reference/services/SoftLayer_User_Customer/getActiveExternalAuthenticationVendors)
Get a list of active external authentication vendors for a SoftLayer user.

#### [getAdditionalEmails](/reference/services/SoftLayer_User_Customer/getAdditionalEmails)
Retrieve a portal user's additional email addresses. These email addresses are contacted when updates are made to support tickets.

#### [getAllowedDedicatedHostIds](/reference/services/SoftLayer_User_Customer/getAllowedDedicatedHostIds)


#### [getAllowedHardwareIds](/reference/services/SoftLayer_User_Customer/getAllowedHardwareIds)


#### [getAllowedVirtualGuestIds](/reference/services/SoftLayer_User_Customer/getAllowedVirtualGuestIds)


#### [getApiAuthenticationKeys](/reference/services/SoftLayer_User_Customer/getApiAuthenticationKeys)
Retrieve a portal user's API Authentication keys. There is a max limit of one API key per user.

#### [getAuthenticationToken](/reference/services/SoftLayer_User_Customer/getAuthenticationToken)


#### [getChildUsers](/reference/services/SoftLayer_User_Customer/getChildUsers)
Retrieve a portal user's child users. Some portal users may not have child users.

#### [getClosedTickets](/reference/services/SoftLayer_User_Customer/getClosedTickets)
Retrieve an user's associated closed tickets.

#### [getDedicatedHosts](/reference/services/SoftLayer_User_Customer/getDedicatedHosts)
Retrieve the dedicated hosts to which the user has been granted access.

#### [getDefaultAccount](/reference/services/SoftLayer_User_Customer/getDefaultAccount)
Retrieve the default account for the current for the OpenIdConnect identity that is linked to the current SoftLayer user identity

#### [getExternalBindings](/reference/services/SoftLayer_User_Customer/getExternalBindings)
Retrieve the external authentication bindings that link an external identifier to a SoftLayer user.

#### [getHardware](/reference/services/SoftLayer_User_Customer/getHardware)
Retrieve a portal user's accessible hardware. These permissions control which hardware a user has access to in the SoftLayer customer portal.

#### [getHardwareCount](/reference/services/SoftLayer_User_Customer/getHardwareCount)
Retrieve the current number of servers a portal user has access to.

#### [getHardwareNotifications](/reference/services/SoftLayer_User_Customer/getHardwareNotifications)
Retrieve hardware notifications associated with this user. A hardware notification links a user to a piece of hardware, and that user will be notified if any monitors on that hardware fail, if the monitors have a status of 'Notify User'.

#### [getHasAcknowledgedSupportPolicyFlag](/reference/services/SoftLayer_User_Customer/getHasAcknowledgedSupportPolicyFlag)
Retrieve whether or not a user has acknowledged the support policy.

#### [getHasFullDedicatedHostAccessFlag](/reference/services/SoftLayer_User_Customer/getHasFullDedicatedHostAccessFlag)
Retrieve permission granting the user access to all Dedicated Host devices on the account.

#### [getHasFullHardwareAccessFlag](/reference/services/SoftLayer_User_Customer/getHasFullHardwareAccessFlag)
Retrieve whether or not a portal user has access to all hardware on their account.

#### [getHasFullVirtualGuestAccessFlag](/reference/services/SoftLayer_User_Customer/getHasFullVirtualGuestAccessFlag)
Retrieve whether or not a portal user has access to all hardware on their account.

#### [getIbmIdLink](/reference/services/SoftLayer_User_Customer/getIbmIdLink)


#### [getImpersonationToken](/reference/services/SoftLayer_User_Customer/getImpersonationToken)


#### [getLayoutProfiles](/reference/services/SoftLayer_User_Customer/getLayoutProfiles)


#### [getLocale](/reference/services/SoftLayer_User_Customer/getLocale)
Retrieve a user's locale. Locale holds user's language and region information.

#### [getLoginAttempts](/reference/services/SoftLayer_User_Customer/getLoginAttempts)
Retrieve a user's attempts to log into the SoftLayer customer portal.

#### [getLoginToken](/reference/services/SoftLayer_User_Customer/getLoginToken)
Authenticate a user for the SoftLayer customer portal

#### [getMappedAccounts](/reference/services/SoftLayer_User_Customer/getMappedAccounts)
Retrieve a list of all the accounts that belong to this customer.

#### [getMobileDevices](/reference/services/SoftLayer_User_Customer/getMobileDevices)
Retrieve a portal user's associated mobile device profiles.

#### [getNotificationSubscribers](/reference/services/SoftLayer_User_Customer/getNotificationSubscribers)
Retrieve notification subscription records for the user.

#### [getObject](/reference/services/SoftLayer_User_Customer/getObject)
Retrieve a SoftLayer_User_Customer record.

#### [getOpenIdConnectMigrationState](/reference/services/SoftLayer_User_Customer/getOpenIdConnectMigrationState)
Get the OpenId migration state

#### [getOpenTickets](/reference/services/SoftLayer_User_Customer/getOpenTickets)
Retrieve an user's associated open tickets.

#### [getOverrides](/reference/services/SoftLayer_User_Customer/getOverrides)
Retrieve a portal user's vpn accessible subnets.

#### [getParent](/reference/services/SoftLayer_User_Customer/getParent)
Retrieve a portal user's parent user. If a SoftLayer_User_Customer has a null parentId property then it doesn't have a parent user.

#### [getPasswordRequirements](/reference/services/SoftLayer_User_Customer/getPasswordRequirements)


#### [getPermissions](/reference/services/SoftLayer_User_Customer/getPermissions)
Retrieve a portal user's permissions. These permissions control that user's access to functions within the SoftLayer customer portal and API.

#### [getPortalLoginToken](/reference/services/SoftLayer_User_Customer/getPortalLoginToken)
Authenticate a user for the SoftLayer customer portal

#### [getPreference](/reference/services/SoftLayer_User_Customer/getPreference)
Get a preference value for the current user

#### [getPreferenceTypes](/reference/services/SoftLayer_User_Customer/getPreferenceTypes)
Get all available preference types

#### [getPreferences](/reference/services/SoftLayer_User_Customer/getPreferences)


#### [getRequirementsForPasswordSet](/reference/services/SoftLayer_User_Customer/getRequirementsForPasswordSet)
Retrieve the authentication requirements for a user when attempting

#### [getRoles](/reference/services/SoftLayer_User_Customer/getRoles)


#### [getSalesforceUserLink](/reference/services/SoftLayer_User_Customer/getSalesforceUserLink)
Retrieve [DEPRECATED]

#### [getSecurityAnswers](/reference/services/SoftLayer_User_Customer/getSecurityAnswers)
Retrieve a portal user's security question answers. Some portal users may not have security answers or may not be configured to require answering a security question on login.

#### [getSubscribers](/reference/services/SoftLayer_User_Customer/getSubscribers)
Retrieve a user's notification subscription records.

#### [getSuccessfulLogins](/reference/services/SoftLayer_User_Customer/getSuccessfulLogins)
Retrieve a user's successful attempts to log into the SoftLayer customer portal.

#### [getSupportPolicyAcknowledgementRequiredFlag](/reference/services/SoftLayer_User_Customer/getSupportPolicyAcknowledgementRequiredFlag)
Retrieve whether or not a user is required to acknowledge the support policy for portal access.

#### [getSupportPolicyDocument](/reference/services/SoftLayer_User_Customer/getSupportPolicyDocument)


#### [getSupportPolicyName](/reference/services/SoftLayer_User_Customer/getSupportPolicyName)


#### [getSupportedLocales](/reference/services/SoftLayer_User_Customer/getSupportedLocales)
Returns all supported locales for the current user

#### [getSurveyRequiredFlag](/reference/services/SoftLayer_User_Customer/getSurveyRequiredFlag)
Retrieve whether or not a user must take a brief survey the next time they log into the SoftLayer customer portal.

#### [getSurveys](/reference/services/SoftLayer_User_Customer/getSurveys)
Retrieve the surveys that a user has taken in the SoftLayer customer portal.

#### [getTickets](/reference/services/SoftLayer_User_Customer/getTickets)
Retrieve an user's associated tickets.

#### [getTimezone](/reference/services/SoftLayer_User_Customer/getTimezone)
Retrieve a portal user's time zone.

#### [getUnsuccessfulLogins](/reference/services/SoftLayer_User_Customer/getUnsuccessfulLogins)
Retrieve a user's unsuccessful attempts to log into the SoftLayer customer portal.

#### [getUserIdForPasswordSet](/reference/services/SoftLayer_User_Customer/getUserIdForPasswordSet)
Retrieve a user id using a password request key

#### [getUserLinks](/reference/services/SoftLayer_User_Customer/getUserLinks)


#### [getUserPreferences](/reference/services/SoftLayer_User_Customer/getUserPreferences)


#### [getUserStatus](/reference/services/SoftLayer_User_Customer/getUserStatus)
Retrieve a portal user's status, which controls overall access to the SoftLayer customer portal and VPN access to the private network.

#### [getVirtualGuestCount](/reference/services/SoftLayer_User_Customer/getVirtualGuestCount)
Retrieve the current number of CloudLayer Computing Instances a portal user has access to.

#### [getVirtualGuests](/reference/services/SoftLayer_User_Customer/getVirtualGuests)
Retrieve a portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing Instances a user has access to in the SoftLayer customer portal.

#### [inTerminalStatus](/reference/services/SoftLayer_User_Customer/inTerminalStatus)


#### [initiateExternalAuthentication](/reference/services/SoftLayer_User_Customer/initiateExternalAuthentication)
Initiates an external authentication using the given authentication container.

#### [initiatePortalPasswordChange](/reference/services/SoftLayer_User_Customer/initiatePortalPasswordChange)
Request email to allow user to change their password

#### [initiatePortalPasswordChangeByBrandAgent](/reference/services/SoftLayer_User_Customer/initiatePortalPasswordChangeByBrandAgent)
Allows a Brand Agent to request password reset email to be sent to

#### [inviteUserToLinkOpenIdConnect](/reference/services/SoftLayer_User_Customer/inviteUserToLinkOpenIdConnect)
Send email invitation to a user to join a SoftLayer account and authenticate with OpenIdConnect.

#### [isMasterUser](/reference/services/SoftLayer_User_Customer/isMasterUser)
Determine if a portal user is a master user.

#### [isValidForumPassword](/reference/services/SoftLayer_User_Customer/isValidForumPassword)
Determine if a string is a user's forum password.

#### [isValidPortalPassword](/reference/services/SoftLayer_User_Customer/isValidPortalPassword)
Determine if a string is a user's portal password.

#### [performExternalAuthentication](/reference/services/SoftLayer_User_Customer/performExternalAuthentication)
Perform an external authentication using the given authentication container. 

#### [processPasswordSetRequest](/reference/services/SoftLayer_User_Customer/processPasswordSetRequest)
Set the password for a user who has a valid password request key

#### [removeAllDedicatedHostAccessForThisUser](/reference/services/SoftLayer_User_Customer/removeAllDedicatedHostAccessForThisUser)
Revoke access to all dedicated hosts on the account for this user.

#### [removeAllHardwareAccessForThisUser](/reference/services/SoftLayer_User_Customer/removeAllHardwareAccessForThisUser)
Remove all hardware from a portal user's hardware access list.

#### [removeAllVirtualAccessForThisUser](/reference/services/SoftLayer_User_Customer/removeAllVirtualAccessForThisUser)
Remove all cloud computing instances from a portal user's instance access list.

#### [removeApiAuthenticationKey](/reference/services/SoftLayer_User_Customer/removeApiAuthenticationKey)
Remove a user's API authentication key.

#### [removeBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeBulkDedicatedHostAccess)
Revoke access for the user for one or more dedicated hosts devices.

#### [removeBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/removeBulkHardwareAccess)
Remove multiple hardware from a portal user's hardware access list.

#### [removeBulkPortalPermission](/reference/services/SoftLayer_User_Customer/removeBulkPortalPermission)
Remove multiple permissions from a portal user's permission set.

#### [removeBulkRoles](/reference/services/SoftLayer_User_Customer/removeBulkRoles)


#### [removeBulkVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/removeBulkVirtualGuestAccess)
Remove multiple CloudLayer Computing Instances from a portal user's access list.

#### [removeDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeDedicatedHostAccess)
Revoke access for the user to a single dedicated hosts device.

#### [removeExternalBinding](/reference/services/SoftLayer_User_Customer/removeExternalBinding)
Remove an external binding from this user.

#### [removeHardwareAccess](/reference/services/SoftLayer_User_Customer/removeHardwareAccess)
Remove hardware from a portal user's hardware access list.

#### [removePortalPermission](/reference/services/SoftLayer_User_Customer/removePortalPermission)
Remove a permission from a portal user's permission set.

#### [removeRole](/reference/services/SoftLayer_User_Customer/removeRole)


#### [removeSecurityAnswers](/reference/services/SoftLayer_User_Customer/removeSecurityAnswers)


#### [removeVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/removeVirtualGuestAccess)
Remove a CloudLayer Computing Instance from a portal user's access list.

#### [samlAuthenticate](/reference/services/SoftLayer_User_Customer/samlAuthenticate)


#### [samlBeginAuthentication](/reference/services/SoftLayer_User_Customer/samlBeginAuthentication)


#### [samlBeginLogout](/reference/services/SoftLayer_User_Customer/samlBeginLogout)


#### [samlLogout](/reference/services/SoftLayer_User_Customer/samlLogout)


#### [selfPasswordChange](/reference/services/SoftLayer_User_Customer/selfPasswordChange)


#### [setDefaultAccount](/reference/services/SoftLayer_User_Customer/setDefaultAccount)
Sets the default account for the OpenIdConnect identity that is linked to the current SoftLayer user identity.

#### [silentlyMigrateUserOpenIdConnect](/reference/services/SoftLayer_User_Customer/silentlyMigrateUserOpenIdConnect)
This api is used to migrate a user to IBMid without sending an invitation.

#### [updateForumPassword](/reference/services/SoftLayer_User_Customer/updateForumPassword)
Update a user's forum password

#### [updateNotificationSubscriber](/reference/services/SoftLayer_User_Customer/updateNotificationSubscriber)
Update the active status for a notification subscription.

#### [updateSecurityAnswers](/reference/services/SoftLayer_User_Customer/updateSecurityAnswers)
Update portal login security questions and answers.

#### [updateSubscriberDeliveryMethod](/reference/services/SoftLayer_User_Customer/updateSubscriberDeliveryMethod)
Update a delivery method for the subscriber.

#### [updateVpnPassword](/reference/services/SoftLayer_User_Customer/updateVpnPassword)
Update a user's VPN password

#### [updateVpnUser](/reference/services/SoftLayer_User_Customer/updateVpnUser)
Creates or updates a user's VPN access privileges.

#### [validateAuthenticationToken](/reference/services/SoftLayer_User_Customer/validateAuthenticationToken)


</div>

