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
        
        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/acknowledgeSupportPolicy'> acknowledgeSupportPolicy</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addApiAuthenticationKey'> addApiAuthenticationKey</a> </span>
            <div class='views-field-body'>Create a user's API authentication key.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addBulkDedicatedHostAccess'> addBulkDedicatedHostAccess</a> </span>
            <div class='views-field-body'>Grant access to the user for one or more dedicated hosts devices.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addBulkHardwareAccess'> addBulkHardwareAccess</a> </span>
            <div class='views-field-body'>Add multiple hardware to a portal user's hardware access list.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addBulkPortalPermission'> addBulkPortalPermission</a> </span>
            <div class='views-field-body'>Add multiple permissions to a portal user's permission set.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addBulkRoles'> addBulkRoles</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addBulkVirtualGuestAccess'> addBulkVirtualGuestAccess</a> </span>
            <div class='views-field-body'>Add multiple CloudLayer Computing Instances to a portal user's access list.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addDedicatedHostAccess'> addDedicatedHostAccess</a> </span>
            <div class='views-field-body'>Grant access to the user for a single dedicated host device.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addExternalBinding'> addExternalBinding</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addHardwareAccess'> addHardwareAccess</a> </span>
            <div class='views-field-body'>Add hardware to a portal user's hardware access list.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addNotificationSubscriber'> addNotificationSubscriber</a> </span>
            <div class='views-field-body'>Create a notification subscription record for the user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addPortalPermission'> addPortalPermission</a> </span>
            <div class='views-field-body'>Add a permission to a portal user's permission set.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addRole'> addRole</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/addVirtualGuestAccess'> addVirtualGuestAccess</a> </span>
            <div class='views-field-body'>Add a CloudLayer Computing Instance to a portal user's access list.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/changePreference'> changePreference</a> </span>
            <div class='views-field-body'>Change preference values for the current user</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/checkExternalAuthenticationStatus'> checkExternalAuthenticationStatus</a> </span>
            <div class='views-field-body'>Checks if an external authentication is complete or not</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/checkPhoneFactorAuthenticationForPasswordSet'> checkPhoneFactorAuthenticationForPasswordSet</a> </span>
            <div class='views-field-body'>Check the status of an outstanding Phone Factor Authentication for Password Set</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/createNotificationSubscriber'> createNotificationSubscriber</a> </span>
            <div class='views-field-body'>Create a new subscriber for a given resource.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/createObject'> createObject</a> </span>
            <div class='views-field-body'>Create a new user record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/createSubscriberDeliveryMethods'> createSubscriberDeliveryMethods</a> </span>
            <div class='views-field-body'>Create delivery methods for the subscriber.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/deactivateNotificationSubscriber'> deactivateNotificationSubscriber</a> </span>
            <div class='views-field-body'>Delete a subscriber for a given resource.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/editObject'> editObject</a> </span>
            <div class='views-field-body'>Update a user's information.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/editObjects'> editObjects</a> </span>
            <div class='views-field-body'>Update a collection of users' information</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/findUserPreference'> findUserPreference</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the customer account that a user belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getActions'> getActions</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getActiveExternalAuthenticationVendors'> getActiveExternalAuthenticationVendors</a> </span>
            <div class='views-field-body'>Get a list of active external authentication vendors for a SoftLayer user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getAdditionalEmails'> getAdditionalEmails</a> </span>
            <div class='views-field-body'>Retrieve a portal user's additional email addresses. These email addresses are contacted when updates are made to support tickets.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getAllowedDedicatedHostIds'> getAllowedDedicatedHostIds</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getAllowedHardwareIds'> getAllowedHardwareIds</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getAllowedVirtualGuestIds'> getAllowedVirtualGuestIds</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getApiAuthenticationKeys'> getApiAuthenticationKeys</a> </span>
            <div class='views-field-body'>Retrieve a portal user's API Authentication keys. There is a max limit of two API keys per user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getAuthenticationToken'> getAuthenticationToken</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getCdnAccounts'> getCdnAccounts</a> </span>
            <div class='views-field-body'>Retrieve the CDN accounts associated with a portal user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getChildUsers'> getChildUsers</a> </span>
            <div class='views-field-body'>Retrieve a portal user's child users. Some portal users may not have child users.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getClosedTickets'> getClosedTickets</a> </span>
            <div class='views-field-body'>Retrieve an user's associated closed tickets.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getDedicatedHosts'> getDedicatedHosts</a> </span>
            <div class='views-field-body'>Retrieve the dedicated hosts to which the user has been granted access.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getDefaultAccount'> getDefaultAccount</a> </span>
            <div class='views-field-body'>Retrieve the default account for the current for the OpenIdConnect identity that is linked to the current SoftLayer user identity</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getDefaultSecurityQuestions'> getDefaultSecurityQuestions</a> </span>
            <div class='views-field-body'>Retrieve default security questions.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getExternalBindings'> getExternalBindings</a> </span>
            <div class='views-field-body'>Retrieve the external authentication bindings that link an external identifier to a SoftLayer user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getHardware'> getHardware</a> </span>
            <div class='views-field-body'>Retrieve a portal user's accessible hardware. These permissions control which hardware a user has access to in the SoftLayer customer portal.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getHardwareCount'> getHardwareCount</a> </span>
            <div class='views-field-body'>Retrieve the current number of servers a portal user has access to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getHardwareNotifications'> getHardwareNotifications</a> </span>
            <div class='views-field-body'>Retrieve hardware notifications associated with this user. A hardware notification links a user to a piece of hardware, and that user will be notified if any monitors on that hardware fail, if the monitors have a status of 'Notify User'.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getHasAcknowledgedSupportPolicyFlag'> getHasAcknowledgedSupportPolicyFlag</a> </span>
            <div class='views-field-body'>Retrieve whether or not a user has acknowledged the support policy.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getHasFullDedicatedHostAccessFlag'> getHasFullDedicatedHostAccessFlag</a> </span>
            <div class='views-field-body'>Retrieve permission granting the user access to all Dedicated Host devices on the account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getHasFullHardwareAccessFlag'> getHasFullHardwareAccessFlag</a> </span>
            <div class='views-field-body'>Retrieve whether or not a portal user has access to all hardware on their account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getHasFullVirtualGuestAccessFlag'> getHasFullVirtualGuestAccessFlag</a> </span>
            <div class='views-field-body'>Retrieve whether or not a portal user has access to all hardware on their account.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getImpersonationToken'> getImpersonationToken</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getLayoutProfiles'> getLayoutProfiles</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getLocale'> getLocale</a> </span>
            <div class='views-field-body'>Retrieve a user's locale. Locale holds user's language and region information.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getLoginAttempts'> getLoginAttempts</a> </span>
            <div class='views-field-body'>Retrieve a user's attempts to log into the SoftLayer customer portal.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getLoginToken'> getLoginToken</a> </span>
            <div class='views-field-body'>Authenticate a user for the SoftLayer customer portal</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getMappedAccounts'> getMappedAccounts</a> </span>
            <div class='views-field-body'>Retrieve a list of all the accounts that belong to this customer.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getMobileDevices'> getMobileDevices</a> </span>
            <div class='views-field-body'>Retrieve a portal user's associated mobile device profiles.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getNotificationSubscribers'> getNotificationSubscribers</a> </span>
            <div class='views-field-body'>Retrieve notification subscription records for the user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_User_Customer record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getOpenIdConnectMigrationState'> getOpenIdConnectMigrationState</a> </span>
            <div class='views-field-body'>Get the OpenId migration state</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getOpenTickets'> getOpenTickets</a> </span>
            <div class='views-field-body'>Retrieve an user's associated open tickets.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getOverrides'> getOverrides</a> </span>
            <div class='views-field-body'>Retrieve a portal user's vpn accessible subnets.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getParent'> getParent</a> </span>
            <div class='views-field-body'>Retrieve a portal user's parent user. If a SoftLayer_User_Customer has a null parentId property then it doesn't have a parent user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getPermissions'> getPermissions</a> </span>
            <div class='views-field-body'>Retrieve a portal user's permissions. These permissions control that user's access to functions within the SoftLayer customer portal and API.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getPortalLoginToken'> getPortalLoginToken</a> </span>
            <div class='views-field-body'>Authenticate a user for the SoftLayer customer portal</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getPreference'> getPreference</a> </span>
            <div class='views-field-body'>Get a preference value for the current user</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getPreferenceTypes'> getPreferenceTypes</a> </span>
            <div class='views-field-body'>Get all available preference types</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getPreferences'> getPreferences</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getRequirementsForPasswordSet'> getRequirementsForPasswordSet</a> </span>
            <div class='views-field-body'>Retrieve the authentication requirements for a user when attempting</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getRoles'> getRoles</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getSalesforceUserLink'> getSalesforceUserLink</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getSecurityAnswers'> getSecurityAnswers</a> </span>
            <div class='views-field-body'>Retrieve a portal user's security question answers. Some portal users may not have security answers or may not be configured to require answering a security question on login.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getSubscribers'> getSubscribers</a> </span>
            <div class='views-field-body'>Retrieve a user's notification subscription records.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getSuccessfulLogins'> getSuccessfulLogins</a> </span>
            <div class='views-field-body'>Retrieve a user's successful attempts to log into the SoftLayer customer portal.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getSupportPolicyAcknowledgementRequiredFlag'> getSupportPolicyAcknowledgementRequiredFlag</a> </span>
            <div class='views-field-body'>Retrieve whether or not a user is required to acknowledge the support policy for portal access.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getSupportPolicyDocument'> getSupportPolicyDocument</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getSupportPolicyName'> getSupportPolicyName</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getSupportedLocales'> getSupportedLocales</a> </span>
            <div class='views-field-body'>Returns all supported locales for the current user</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getSurveyRequiredFlag'> getSurveyRequiredFlag</a> </span>
            <div class='views-field-body'>Retrieve whether or not a user must take a brief survey the next time they log into the SoftLayer customer portal.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getSurveys'> getSurveys</a> </span>
            <div class='views-field-body'>Retrieve the surveys that a user has taken in the SoftLayer customer portal.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getTickets'> getTickets</a> </span>
            <div class='views-field-body'>Retrieve an user's associated tickets.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getTimezone'> getTimezone</a> </span>
            <div class='views-field-body'>Retrieve a portal user's time zone.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getUnsuccessfulLogins'> getUnsuccessfulLogins</a> </span>
            <div class='views-field-body'>Retrieve a user's unsuccessful attempts to log into the SoftLayer customer portal.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getUserFromLostPasswordRequest'> getUserFromLostPasswordRequest</a> </span>
            <div class='views-field-body'>Retrieve a user object using a lost password request key</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getUserIdForPasswordSet'> getUserIdForPasswordSet</a> </span>
            <div class='views-field-body'>Retrieve a user object using a password request key</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getUserLinks'> getUserLinks</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getUserPreferences'> getUserPreferences</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getUserStatus'> getUserStatus</a> </span>
            <div class='views-field-body'>Retrieve a portal user's status, which controls overall access to the SoftLayer customer portal and VPN access to the private network.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getVirtualGuestCount'> getVirtualGuestCount</a> </span>
            <div class='views-field-body'>Retrieve the current number of CloudLayer Computing Instances a portal user has access to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/getVirtualGuests'> getVirtualGuests</a> </span>
            <div class='views-field-body'>Retrieve a portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing Instances a user has access to in the SoftLayer customer portal.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/inTerminalStatus'> inTerminalStatus</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/initiateExternalAuthentication'> initiateExternalAuthentication</a> </span>
            <div class='views-field-body'>Initiates an external authentication using the given authentication container.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/initiatePortalPasswordChange'> initiatePortalPasswordChange</a> </span>
            <div class='views-field-body'>Request email to allow user to change their password</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/initiatePortalPasswordChangeByBrandAgent'> initiatePortalPasswordChangeByBrandAgent</a> </span>
            <div class='views-field-body'>Allows a Brand Agent to request password reset email to be sent to</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/inviteUserToLinkOpenIdConnect'> inviteUserToLinkOpenIdConnect</a> </span>
            <div class='views-field-body'>Send email invitation to a user to join a SoftLayer account and authenticate with OpenIdConnect.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/isMasterUser'> isMasterUser</a> </span>
            <div class='views-field-body'>Determine if a portal user is a master user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/isValidForumPassword'> isValidForumPassword</a> </span>
            <div class='views-field-body'>Determine if a string is a user's forum password.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/isValidPortalPassword'> isValidPortalPassword</a> </span>
            <div class='views-field-body'>Determine if a string is a user's portal password.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/lostPassword'> lostPassword</a> </span>
            <div class='views-field-body'>Generate a lost password request</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/performExternalAuthentication'> performExternalAuthentication</a> </span>
            <div class='views-field-body'>Perform an external authentication using the given authentication container.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/processPasswordSetRequest'> processPasswordSetRequest</a> </span>
            <div class='views-field-body'>Set the password for a user who has a valid password request key</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeAllDedicatedHostAccessForThisUser'> removeAllDedicatedHostAccessForThisUser</a> </span>
            <div class='views-field-body'>Revoke access to all dedicated hosts on the account for this user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeAllHardwareAccessForThisUser'> removeAllHardwareAccessForThisUser</a> </span>
            <div class='views-field-body'>Remove all hardware from a portal user's hardware access list.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeAllVirtualAccessForThisUser'> removeAllVirtualAccessForThisUser</a> </span>
            <div class='views-field-body'>Remove all cloud computing instances from a portal user's instance access list.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeApiAuthenticationKey'> removeApiAuthenticationKey</a> </span>
            <div class='views-field-body'>Remove a user's API authentication key.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeBulkDedicatedHostAccess'> removeBulkDedicatedHostAccess</a> </span>
            <div class='views-field-body'>Revoke access for the user for one or more dedicated hosts devices.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeBulkHardwareAccess'> removeBulkHardwareAccess</a> </span>
            <div class='views-field-body'>Remove multiple hardware from a portal user's hardware access list.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeBulkPortalPermission'> removeBulkPortalPermission</a> </span>
            <div class='views-field-body'>Remove multiple permissions from a portal user's permission set.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeBulkRoles'> removeBulkRoles</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeBulkVirtualGuestAccess'> removeBulkVirtualGuestAccess</a> </span>
            <div class='views-field-body'>Remove multiple CloudLayer Computing Instances from a portal user's access list.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeDedicatedHostAccess'> removeDedicatedHostAccess</a> </span>
            <div class='views-field-body'>Revoke access for the user to a single dedicated hosts device.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeExternalBinding'> removeExternalBinding</a> </span>
            <div class='views-field-body'>Remove an external binding from this user.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeHardwareAccess'> removeHardwareAccess</a> </span>
            <div class='views-field-body'>Remove hardware from a portal user's hardware access list.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removePortalPermission'> removePortalPermission</a> </span>
            <div class='views-field-body'>Remove a permission from a portal user's permission set.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeRole'> removeRole</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/removeVirtualGuestAccess'> removeVirtualGuestAccess</a> </span>
            <div class='views-field-body'>Remove a CloudLayer Computing Instance from a portal user's access list.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/resetExpiredPassword'> resetExpiredPassword</a> </span>
            <div class='views-field-body'>Reset a users expired password.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/samlAuthenticate'> samlAuthenticate</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/samlBeginAuthentication'> samlBeginAuthentication</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/samlBeginLogout'> samlBeginLogout</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/samlLogout'> samlLogout</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/setDefaultAccount'> setDefaultAccount</a> </span>
            <div class='views-field-body'>Sets the default account for the OpenIdConnect identity that is linked to the current SoftLayer user identity.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/setPasswordFromLostPasswordRequest'> setPasswordFromLostPasswordRequest</a> </span>
            <div class='views-field-body'>Set a user's password using a password recovery key</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/silentlyMigrateUserOpenIdConnect'> silentlyMigrateUserOpenIdConnect</a> </span>
            <div class='views-field-body'>This api is used to migrate a user to IBMid without sending an invitation.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/updateForumPassword'> updateForumPassword</a> </span>
            <div class='views-field-body'>Update a user's forum password</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/updateNotificationSubscriber'> updateNotificationSubscriber</a> </span>
            <div class='views-field-body'>Update the active status for a notification subscription.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/updatePassword'> updatePassword</a> </span>
            <div class='views-field-body'>Update a user's portal password</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/updateSecurityAnswers'> updateSecurityAnswers</a> </span>
            <div class='views-field-body'>Update portal login security questions and answers.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/updateSubscriberDeliveryMethod'> updateSubscriberDeliveryMethod</a> </span>
            <div class='views-field-body'>Update a delivery method for the subscriber.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/updateVpnPassword'> updateVpnPassword</a> </span>
            <div class='views-field-body'>Update a user's VPN password</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/updateVpnUser'> updateVpnUser</a> </span>
            <div class='views-field-body'>Creates or updates a user's VPN access privileges.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_User_Customer/validateAuthenticationToken'> validateAuthenticationToken</a> </span>
            <div class='views-field-body'></div>
        </div>
        </div>
</div>

