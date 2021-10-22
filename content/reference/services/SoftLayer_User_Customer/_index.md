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

There are two relational properties that contain the permissions assigned to a customer user; permissions and actions.  These are simply two different representations of the same information. The permissions ORM key creates a SoftLayer_Container_Collection_Permissions collection from SoftLayer_User_Customer_CustomerPermission_Permission objects which is populated from the same data source as the actions ORM key which creates a SoftLayer_Container_Collection_Permissions collection from SoftLayer_User_Permission_Action objects. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [acknowledgeSupportPolicy](/reference/services/SoftLayer_User_Customer/acknowledgeSupportPolicy)

</div>

<div class="method-row">

#### [addApiAuthenticationKey](/reference/services/SoftLayer_User_Customer/addApiAuthenticationKey)
Create a user's API authentication key.
</div>

<div class="method-row">

#### [addBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addBulkDedicatedHostAccess)
Grant access to the user for one or more dedicated hosts devices.
</div>

<div class="method-row">

#### [addBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/addBulkHardwareAccess)
Add multiple hardware to a portal user's hardware access list.
</div>

<div class="method-row">

#### [addBulkPortalPermission](/reference/services/SoftLayer_User_Customer/addBulkPortalPermission)
Add multiple permissions to a portal user's permission set.
</div>

<div class="method-row">

#### [addBulkRoles](/reference/services/SoftLayer_User_Customer/addBulkRoles)

</div>

<div class="method-row">

#### [addBulkVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/addBulkVirtualGuestAccess)
Add multiple CloudLayer Computing Instances to a portal user's access list.
</div>

<div class="method-row">

#### [addDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/addDedicatedHostAccess)
Grant access to the user for a single dedicated host device.
</div>

<div class="method-row">

#### [addExternalBinding](/reference/services/SoftLayer_User_Customer/addExternalBinding)

</div>

<div class="method-row">

#### [addHardwareAccess](/reference/services/SoftLayer_User_Customer/addHardwareAccess)
Add hardware to a portal user's hardware access list.
</div>

<div class="method-row">

#### [addNotificationSubscriber](/reference/services/SoftLayer_User_Customer/addNotificationSubscriber)
Create a notification subscription record for the user.
</div>

<div class="method-row">

#### [addPortalPermission](/reference/services/SoftLayer_User_Customer/addPortalPermission)
Add a permission to a portal user's permission set.
</div>

<div class="method-row">

#### [addRole](/reference/services/SoftLayer_User_Customer/addRole)

</div>

<div class="method-row">

#### [addVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/addVirtualGuestAccess)
Add a CloudLayer Computing Instance to a portal user's access list.
</div>

<div class="method-row">

#### [assignNewParentId](/reference/services/SoftLayer_User_Customer/assignNewParentId)
Assign a different parent to this user. 
</div>

<div class="method-row">

#### [changePreference](/reference/services/SoftLayer_User_Customer/changePreference)
Change preference values for the current user
</div>

<div class="method-row">

#### [checkExternalAuthenticationStatus](/reference/services/SoftLayer_User_Customer/checkExternalAuthenticationStatus)
Checks if an external authentication is complete or not
</div>

<div class="method-row">

#### [checkPhoneFactorAuthenticationForPasswordSet](/reference/services/SoftLayer_User_Customer/checkPhoneFactorAuthenticationForPasswordSet)
Check the status of an outstanding Phone Factor Authentication for Password Set
</div>

<div class="method-row">

#### [createNotificationSubscriber](/reference/services/SoftLayer_User_Customer/createNotificationSubscriber)
Create a new subscriber for a given resource.
</div>

<div class="method-row">

#### [createObject](/reference/services/SoftLayer_User_Customer/createObject)
Create a new user record.
</div>

<div class="method-row">

#### [createSubscriberDeliveryMethods](/reference/services/SoftLayer_User_Customer/createSubscriberDeliveryMethods)
Create delivery methods for the subscriber.
</div>

<div class="method-row">

#### [deactivateNotificationSubscriber](/reference/services/SoftLayer_User_Customer/deactivateNotificationSubscriber)
Delete a subscriber for a given resource.
</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_User_Customer/editObject)
Update a user's information.
</div>

<div class="method-row">

#### [editObjects](/reference/services/SoftLayer_User_Customer/editObjects)
Update a collection of users' information
</div>

<div class="method-row">

#### [findUserPreference](/reference/services/SoftLayer_User_Customer/findUserPreference)

</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_User_Customer/getAccount)
Retrieve the customer account that a user belongs to.
</div>

<div class="method-row">

#### [getActions](/reference/services/SoftLayer_User_Customer/getActions)

</div>

<div class="method-row">

#### [getActiveExternalAuthenticationVendors](/reference/services/SoftLayer_User_Customer/getActiveExternalAuthenticationVendors)
Get a list of active external authentication vendors for a SoftLayer user.
</div>

<div class="method-row">

#### [getAdditionalEmails](/reference/services/SoftLayer_User_Customer/getAdditionalEmails)
Retrieve a portal user's additional email addresses. These email addresses are contacted when updates are made to support tickets.
</div>

<div class="method-row">

#### [getAgentImpersonationToken](/reference/services/SoftLayer_User_Customer/getAgentImpersonationToken)

</div>

<div class="method-row">

#### [getAllowedDedicatedHostIds](/reference/services/SoftLayer_User_Customer/getAllowedDedicatedHostIds)

</div>

<div class="method-row">

#### [getAllowedHardwareIds](/reference/services/SoftLayer_User_Customer/getAllowedHardwareIds)

</div>

<div class="method-row">

#### [getAllowedVirtualGuestIds](/reference/services/SoftLayer_User_Customer/getAllowedVirtualGuestIds)

</div>

<div class="method-row">

#### [getApiAuthenticationKeys](/reference/services/SoftLayer_User_Customer/getApiAuthenticationKeys)
Retrieve a portal user's API Authentication keys. There is a max limit of one API key per user.
</div>

<div class="method-row">

#### [getAuthenticationToken](/reference/services/SoftLayer_User_Customer/getAuthenticationToken)

</div>

<div class="method-row">

#### [getChildUsers](/reference/services/SoftLayer_User_Customer/getChildUsers)
Retrieve a portal user's child users. Some portal users may not have child users.
</div>

<div class="method-row">

#### [getClosedTickets](/reference/services/SoftLayer_User_Customer/getClosedTickets)
Retrieve an user's associated closed tickets.
</div>

<div class="method-row">

#### [getDedicatedHosts](/reference/services/SoftLayer_User_Customer/getDedicatedHosts)
Retrieve the dedicated hosts to which the user has been granted access.
</div>

<div class="method-row">

#### [getDefaultAccount](/reference/services/SoftLayer_User_Customer/getDefaultAccount)
This method should never be invoked as it is not applicable to legacy SoftLayer-authenticated users. See SoftLayer_User_Customer_OpenIdConnect::getDefaultAccount instead. 
</div>

<div class="method-row">

#### [getExternalBindings](/reference/services/SoftLayer_User_Customer/getExternalBindings)
Retrieve the external authentication bindings that link an external identifier to a SoftLayer user.
</div>

<div class="method-row">

#### [getHardware](/reference/services/SoftLayer_User_Customer/getHardware)
Retrieve a portal user's accessible hardware. These permissions control which hardware a user has access to in the SoftLayer customer portal.
</div>

<div class="method-row">

#### [getHardwareCount](/reference/services/SoftLayer_User_Customer/getHardwareCount)
Retrieve the current number of servers a portal user has access to.
</div>

<div class="method-row">

#### [getHardwareNotifications](/reference/services/SoftLayer_User_Customer/getHardwareNotifications)
Retrieve hardware notifications associated with this user. A hardware notification links a user to a piece of hardware, and that user will be notified if any monitors on that hardware fail, if the monitors have a status of 'Notify User'.
</div>

<div class="method-row">

#### [getHasAcknowledgedSupportPolicyFlag](/reference/services/SoftLayer_User_Customer/getHasAcknowledgedSupportPolicyFlag)
Retrieve whether or not a user has acknowledged the support policy.
</div>

<div class="method-row">

#### [getHasFullDedicatedHostAccessFlag](/reference/services/SoftLayer_User_Customer/getHasFullDedicatedHostAccessFlag)
Retrieve permission granting the user access to all Dedicated Host devices on the account.
</div>

<div class="method-row">

#### [getHasFullHardwareAccessFlag](/reference/services/SoftLayer_User_Customer/getHasFullHardwareAccessFlag)
Retrieve whether or not a portal user has access to all hardware on their account.
</div>

<div class="method-row">

#### [getHasFullVirtualGuestAccessFlag](/reference/services/SoftLayer_User_Customer/getHasFullVirtualGuestAccessFlag)
Retrieve whether or not a portal user has access to all virtual guests on their account.
</div>

<div class="method-row">

#### [getIbmIdLink](/reference/services/SoftLayer_User_Customer/getIbmIdLink)
Retrieve specifically relating the Customer instance to an IBMid. A Customer instance may or may not have an IBMid link.
</div>

<div class="method-row">

#### [getImpersonationToken](/reference/services/SoftLayer_User_Customer/getImpersonationToken)

</div>

<div class="method-row">

#### [getLayoutProfiles](/reference/services/SoftLayer_User_Customer/getLayoutProfiles)
Retrieve contains the definition of the layout profile.
</div>

<div class="method-row">

#### [getLocale](/reference/services/SoftLayer_User_Customer/getLocale)
Retrieve a user's locale. Locale holds user's language and region information.
</div>

<div class="method-row">

#### [getLoginAttempts](/reference/services/SoftLayer_User_Customer/getLoginAttempts)
Retrieve a user's attempts to log into the SoftLayer customer portal.
</div>

<div class="method-row">

#### [getLoginToken](/reference/services/SoftLayer_User_Customer/getLoginToken)
Authenticate a user for the SoftLayer customer portal
</div>

<div class="method-row">

#### [getMappedAccounts](/reference/services/SoftLayer_User_Customer/getMappedAccounts)
Retrieve a list of all the accounts that belong to this customer.
</div>

<div class="method-row">

#### [getMobileDevices](/reference/services/SoftLayer_User_Customer/getMobileDevices)
Retrieve a portal user's associated mobile device profiles.
</div>

<div class="method-row">

#### [getNotificationSubscribers](/reference/services/SoftLayer_User_Customer/getNotificationSubscribers)
Retrieve notification subscription records for the user.
</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_User_Customer/getObject)
Retrieve a SoftLayer_User_Customer record.
</div>

<div class="method-row">

#### [getOpenIdConnectMigrationState](/reference/services/SoftLayer_User_Customer/getOpenIdConnectMigrationState)
Get the OpenId migration state
</div>

<div class="method-row">

#### [getOpenTickets](/reference/services/SoftLayer_User_Customer/getOpenTickets)
Retrieve an user's associated open tickets.
</div>

<div class="method-row">

#### [getOverrides](/reference/services/SoftLayer_User_Customer/getOverrides)
Retrieve a portal user's vpn accessible subnets.
</div>

<div class="method-row">

#### [getParent](/reference/services/SoftLayer_User_Customer/getParent)
Retrieve a portal user's parent user. If a SoftLayer_User_Customer has a null parentId property then it doesn't have a parent user.
</div>

<div class="method-row">

#### [getPasswordRequirements](/reference/services/SoftLayer_User_Customer/getPasswordRequirements)

</div>

<div class="method-row">

#### [getPermissions](/reference/services/SoftLayer_User_Customer/getPermissions)
Retrieve a portal user's permissions. These permissions control that user's access to functions within the SoftLayer customer portal and API.
</div>

<div class="method-row">

#### [getPortalLoginToken](/reference/services/SoftLayer_User_Customer/getPortalLoginToken)
Authenticate a user for the SoftLayer customer portal
</div>

<div class="method-row">

#### [getPreference](/reference/services/SoftLayer_User_Customer/getPreference)
Get a preference value for the current user
</div>

<div class="method-row">

#### [getPreferenceTypes](/reference/services/SoftLayer_User_Customer/getPreferenceTypes)
Get all available preference types
</div>

<div class="method-row">

#### [getPreferences](/reference/services/SoftLayer_User_Customer/getPreferences)
Retrieve data type contains a single user preference to a specific preference type.
</div>

<div class="method-row">

#### [getRequirementsForPasswordSet](/reference/services/SoftLayer_User_Customer/getRequirementsForPasswordSet)
Retrieve the authentication requirements for a user when attempting
</div>

<div class="method-row">

#### [getRoles](/reference/services/SoftLayer_User_Customer/getRoles)

</div>

<div class="method-row">

#### [getSalesforceUserLink](/reference/services/SoftLayer_User_Customer/getSalesforceUserLink)
Retrieve [DEPRECATED]
</div>

<div class="method-row">

#### [getSecurityAnswers](/reference/services/SoftLayer_User_Customer/getSecurityAnswers)
Retrieve a portal user's security question answers. Some portal users may not have security answers or may not be configured to require answering a security question on login.
</div>

<div class="method-row">

#### [getSubscribers](/reference/services/SoftLayer_User_Customer/getSubscribers)
Retrieve a user's notification subscription records.
</div>

<div class="method-row">

#### [getSuccessfulLogins](/reference/services/SoftLayer_User_Customer/getSuccessfulLogins)
Retrieve a user's successful attempts to log into the SoftLayer customer portal.
</div>

<div class="method-row">

#### [getSupportPolicyAcknowledgementRequiredFlag](/reference/services/SoftLayer_User_Customer/getSupportPolicyAcknowledgementRequiredFlag)
Retrieve whether or not a user is required to acknowledge the support policy for portal access.
</div>

<div class="method-row">

#### [getSupportPolicyDocument](/reference/services/SoftLayer_User_Customer/getSupportPolicyDocument)

</div>

<div class="method-row">

#### [getSupportPolicyName](/reference/services/SoftLayer_User_Customer/getSupportPolicyName)

</div>

<div class="method-row">

#### [getSupportedLocales](/reference/services/SoftLayer_User_Customer/getSupportedLocales)
Returns all supported locales for the current user
</div>

<div class="method-row">

#### [getSurveyRequiredFlag](/reference/services/SoftLayer_User_Customer/getSurveyRequiredFlag)
Retrieve whether or not a user must take a brief survey the next time they log into the SoftLayer customer portal.
</div>

<div class="method-row">

#### [getSurveys](/reference/services/SoftLayer_User_Customer/getSurveys)
Retrieve the surveys that a user has taken in the SoftLayer customer portal.
</div>

<div class="method-row">

#### [getTickets](/reference/services/SoftLayer_User_Customer/getTickets)
Retrieve an user's associated tickets.
</div>

<div class="method-row">

#### [getTimezone](/reference/services/SoftLayer_User_Customer/getTimezone)
Retrieve a portal user's time zone.
</div>

<div class="method-row">

#### [getUnsuccessfulLogins](/reference/services/SoftLayer_User_Customer/getUnsuccessfulLogins)
Retrieve a user's unsuccessful attempts to log into the SoftLayer customer portal.
</div>

<div class="method-row">

#### [getUserIdForPasswordSet](/reference/services/SoftLayer_User_Customer/getUserIdForPasswordSet)
Retrieve a user id using a password request key
</div>

<div class="method-row">

#### [getUserLinks](/reference/services/SoftLayer_User_Customer/getUserLinks)
Retrieve user customer link with IBMid and IAMid.
</div>

<div class="method-row">

#### [getUserPreferences](/reference/services/SoftLayer_User_Customer/getUserPreferences)

</div>

<div class="method-row">

#### [getUserStatus](/reference/services/SoftLayer_User_Customer/getUserStatus)
Retrieve a portal user's status, which controls overall access to the SoftLayer customer portal and VPN access to the private network.
</div>

<div class="method-row">

#### [getVirtualGuestCount](/reference/services/SoftLayer_User_Customer/getVirtualGuestCount)
Retrieve the current number of CloudLayer Computing Instances a portal user has access to.
</div>

<div class="method-row">

#### [getVirtualGuests](/reference/services/SoftLayer_User_Customer/getVirtualGuests)
Retrieve a portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing Instances a user has access to in the SoftLayer customer portal.
</div>

<div class="method-row">

#### [inTerminalStatus](/reference/services/SoftLayer_User_Customer/inTerminalStatus)

</div>

<div class="method-row">

#### [initiateExternalAuthentication](/reference/services/SoftLayer_User_Customer/initiateExternalAuthentication)
Initiates an external authentication using the given authentication container.
</div>

<div class="method-row">

#### [initiatePortalPasswordChange](/reference/services/SoftLayer_User_Customer/initiatePortalPasswordChange)
Request email to allow user to change their password
</div>

<div class="method-row">

#### [initiatePortalPasswordChangeByBrandAgent](/reference/services/SoftLayer_User_Customer/initiatePortalPasswordChangeByBrandAgent)
Allows a Brand Agent to request password reset email to be sent to
</div>

<div class="method-row">

#### [inviteUserToLinkOpenIdConnect](/reference/services/SoftLayer_User_Customer/inviteUserToLinkOpenIdConnect)
Send email invitation to a user to join a SoftLayer account and authenticate with OpenIdConnect.
</div>

<div class="method-row">

#### [isMasterUser](/reference/services/SoftLayer_User_Customer/isMasterUser)
Determine if a portal user is a master user.
</div>

<div class="method-row">

#### [isValidPortalPassword](/reference/services/SoftLayer_User_Customer/isValidPortalPassword)
Determine if a string is a user's portal password.
</div>

<div class="method-row">

#### [performExternalAuthentication](/reference/services/SoftLayer_User_Customer/performExternalAuthentication)
Perform an external authentication using the given authentication container. 
</div>

<div class="method-row">

#### [processPasswordSetRequest](/reference/services/SoftLayer_User_Customer/processPasswordSetRequest)
Set the password for a user who has a valid password request key
</div>

<div class="method-row">

#### [removeAllDedicatedHostAccessForThisUser](/reference/services/SoftLayer_User_Customer/removeAllDedicatedHostAccessForThisUser)
Revoke access to all dedicated hosts on the account for this user.
</div>

<div class="method-row">

#### [removeAllHardwareAccessForThisUser](/reference/services/SoftLayer_User_Customer/removeAllHardwareAccessForThisUser)
Remove all hardware from a portal user's hardware access list.
</div>

<div class="method-row">

#### [removeAllVirtualAccessForThisUser](/reference/services/SoftLayer_User_Customer/removeAllVirtualAccessForThisUser)
Remove all cloud computing instances from a portal user's instance access list.
</div>

<div class="method-row">

#### [removeApiAuthenticationKey](/reference/services/SoftLayer_User_Customer/removeApiAuthenticationKey)
Remove a user's API authentication key.
</div>

<div class="method-row">

#### [removeBulkDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeBulkDedicatedHostAccess)
Revoke access for the user for one or more dedicated hosts devices.
</div>

<div class="method-row">

#### [removeBulkHardwareAccess](/reference/services/SoftLayer_User_Customer/removeBulkHardwareAccess)
Remove multiple hardware from a portal user's hardware access list.
</div>

<div class="method-row">

#### [removeBulkPortalPermission](/reference/services/SoftLayer_User_Customer/removeBulkPortalPermission)
Remove multiple permissions from a portal user's permission set.
</div>

<div class="method-row">

#### [removeBulkRoles](/reference/services/SoftLayer_User_Customer/removeBulkRoles)

</div>

<div class="method-row">

#### [removeBulkVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/removeBulkVirtualGuestAccess)
Remove multiple CloudLayer Computing Instances from a portal user's access list.
</div>

<div class="method-row">

#### [removeDedicatedHostAccess](/reference/services/SoftLayer_User_Customer/removeDedicatedHostAccess)
Revoke access for the user to a single dedicated hosts device.
</div>

<div class="method-row">

#### [removeExternalBinding](/reference/services/SoftLayer_User_Customer/removeExternalBinding)
Remove an external binding from this user.
</div>

<div class="method-row">

#### [removeHardwareAccess](/reference/services/SoftLayer_User_Customer/removeHardwareAccess)
Remove hardware from a portal user's hardware access list.
</div>

<div class="method-row">

#### [removePortalPermission](/reference/services/SoftLayer_User_Customer/removePortalPermission)
Remove a permission from a portal user's permission set.
</div>

<div class="method-row">

#### [removeRole](/reference/services/SoftLayer_User_Customer/removeRole)

</div>

<div class="method-row">

#### [removeSecurityAnswers](/reference/services/SoftLayer_User_Customer/removeSecurityAnswers)

</div>

<div class="method-row">

#### [removeVirtualGuestAccess](/reference/services/SoftLayer_User_Customer/removeVirtualGuestAccess)
Remove a CloudLayer Computing Instance from a portal user's access list.
</div>

<div class="method-row">

#### [resetOpenIdConnectLink](/reference/services/SoftLayer_User_Customer/resetOpenIdConnectLink)
Change the link of a user for OpenIdConnect managed accounts, provided the
</div>

<div class="method-row">

#### [resetOpenIdConnectLinkUnifiedUserManagementMode](/reference/services/SoftLayer_User_Customer/resetOpenIdConnectLinkUnifiedUserManagementMode)
Change the link of a master user for OpenIdConnect managed accounts,
</div>

<div class="method-row">

#### [samlAuthenticate](/reference/services/SoftLayer_User_Customer/samlAuthenticate)

</div>

<div class="method-row">

#### [samlBeginAuthentication](/reference/services/SoftLayer_User_Customer/samlBeginAuthentication)

</div>

<div class="method-row">

#### [samlBeginLogout](/reference/services/SoftLayer_User_Customer/samlBeginLogout)

</div>

<div class="method-row">

#### [samlLogout](/reference/services/SoftLayer_User_Customer/samlLogout)

</div>

<div class="method-row">

#### [selfPasswordChange](/reference/services/SoftLayer_User_Customer/selfPasswordChange)

</div>

<div class="method-row">

#### [setDefaultAccount](/reference/services/SoftLayer_User_Customer/setDefaultAccount)
Sets the default account for the OpenIdConnect identity that is linked to the current SoftLayer user identity.
</div>

<div class="method-row">

#### [silentlyMigrateUserOpenIdConnect](/reference/services/SoftLayer_User_Customer/silentlyMigrateUserOpenIdConnect)
This api is used to migrate a user to IBMid without sending an invitation.
</div>

<div class="method-row">

#### [updateNotificationSubscriber](/reference/services/SoftLayer_User_Customer/updateNotificationSubscriber)
Update the active status for a notification subscription.
</div>

<div class="method-row">

#### [updateSecurityAnswers](/reference/services/SoftLayer_User_Customer/updateSecurityAnswers)
Update portal login security questions and answers.
</div>

<div class="method-row">

#### [updateSubscriberDeliveryMethod](/reference/services/SoftLayer_User_Customer/updateSubscriberDeliveryMethod)
Update a delivery method for the subscriber.
</div>

<div class="method-row">

#### [updateVpnPassword](/reference/services/SoftLayer_User_Customer/updateVpnPassword)
Update a user's VPN password
</div>

<div class="method-row">

#### [updateVpnUser](/reference/services/SoftLayer_User_Customer/updateVpnUser)
Creates or updates a user's VPN access privileges.
</div>

<div class="method-row">

#### [validateAuthenticationToken](/reference/services/SoftLayer_User_Customer/validateAuthenticationToken)

</div>
</div>

</div>

