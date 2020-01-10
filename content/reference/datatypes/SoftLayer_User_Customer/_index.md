---
title: "SoftLayer_User_Customer"
description: "The SoftLayer_User_Customer data type contains general information relating to a single SoftLayer customer portal user.... "
layout: "datatype"
tags:
    - "datatype"
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
The SoftLayer_User_Customer data type contains general information relating to a single SoftLayer customer portal user. Personal information in this type such as names, addresses, and phone numbers are not necessarily associated with the customer account the user is assigned to. 


### associatedMethods

*  [SoftLayer_User_Customer::getObject](/reference/services/SoftLayer_User_Customer/getObject )
*  [SoftLayer_Account::getUsers](/reference/services/SoftLayer_Account/getUsers )





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[accountId]: #accountid
#### [accountId]
A portal user's associated [SoftLayer_Account]({{<ref "reference/datatypes/SoftLayer_Account">}}) id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[address1]: #address1
#### [address1]
The first line of the mailing address belonging to a portal user.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[address2]: #address2
#### [address2]
The second line of the mailing address belonging to a portal user.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[aim]: #aim
#### [aim]
A portal user's AOL Instant Messenger screen name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[alternatePhone]: #alternatephone
#### [alternatePhone]
A portal user's secondary phone number.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[authenticationToken]: #authenticationtoken
#### [authenticationToken]
The authentication token used for logging into the SoftLayer customer portal.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_User_Authentication_Token'>SoftLayer_Container_User_Authentication_Token </a>**


</div>
<div class="prop-row">

-----
[city]: #city
#### [city]
The city of the mailing address belonging to a portal user.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[companyName]: #companyname
#### [companyName]
A portal user's associated company. This may not be the same company as the customer that owns this portal user.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[country]: #country
#### [country]
A two-letter abbreviation of the country in the mailing address belonging to a portal user.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date a portal user's record was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[daylightSavingsTimeFlag]: #daylightsavingstimeflag
#### [daylightSavingsTimeFlag]
Whether a portal user's time zone is affected by Daylight Savings Time.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[denyAllResourceAccessOnCreateFlag]: #denyallresourceaccessoncreateflag
#### [denyAllResourceAccessOnCreateFlag]
Flag used to deny access to all hardware and cloud computing instances upon user creation.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[displayName]: #displayname
#### [displayName]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[email]: #email
#### [email]
A portal user's email address.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[firstName]: #firstname
#### [firstName]
A portal user's first name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[forumPasswordHash]: #forumpasswordhash
#### [forumPasswordHash]
A user's password for the SoftLayer forums, hashed for auto-login capability from the SoftLayer customer portal  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[iamAuthorizationStatus]: #iamauthorizationstatus
#### [iamAuthorizationStatus]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[iamId]: #iamid
#### [iamId]
The IAMid (realm-identifier) of the user being created by PaaS  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[icq]: #icq
#### [icq]
A portal user's ICQ UIN.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A portal user's internal identifying number.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[ipAddressRestriction]: #ipaddressrestriction
#### [ipAddressRestriction]
The IP addresses or IP ranges from which a user may login to the SoftLayer customer portal. Specify subnets in CIDR format and separate multiple addresses and subnets by commas. You may combine IPv4 and IPv6 addresses and subnets, for example: 192.168.0.0/16,fe80:021b::0/64.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[isMasterUserFlag]: #ismasteruserflag
#### [isMasterUserFlag]
  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[lastName]: #lastname
#### [lastName]
A portal user's last name.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[linkedAccountIntegrationMode]: #linkedaccountintegrationmode
#### [linkedAccountIntegrationMode]
The linked account integration mode  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[localeId]: #localeid
#### [localeId]
A portal user's associated [SoftLayer_Locale]({{<ref "reference/datatypes/SoftLayer_Locale">}}) id.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[managedByFederationFlag]: #managedbyfederationflag
#### [managedByFederationFlag]
Determines if this portal user is managed by SAML federation.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[managedByOpenIdConnectFlag]: #managedbyopenidconnectflag
#### [managedByOpenIdConnectFlag]
Determines if this portal user is managed by IBMid federation.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[minimumPasswordLifeHours]: #minimumpasswordlifehours
#### [minimumPasswordLifeHours]
The minimum number of hours that must pass between password resets.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a portal user's record was last modified.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[msn]: #msn
#### [msn]
A portal user's MSN address.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[nameId]: #nameid
#### [nameId]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[officePhone]: #officephone
#### [officePhone]
A portal user's office phone number.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[openIdConnectUserName]: #openidconnectusername
#### [openIdConnectUserName]
The BlueID username associated to with this user, if the account is managed by OpenIDConnect / BlueID federation  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[parentId]: #parentid
#### [parentId]
A portal user's parent user. Id a users parentId is ''null'' then it doesn't have a parent user in the customer portal.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[passwordExpireDate]: #passwordexpiredate
#### [passwordExpireDate]
The expiration date for the user's password  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[postalCode]: #postalcode
#### [postalCode]
The postal code of the mailing address belonging to an portal user.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[pptpVpnAllowedFlag]: #pptpvpnallowedflag
#### [pptpVpnAllowedFlag]
Whether a portal user may connect to the SoftLayer private network via PPTP VPN or not.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[preventPreviousPasswords]: #preventpreviouspasswords
#### [preventPreviousPasswords]
  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[savedId]: #savedid
#### [savedId]
  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[secondaryLoginManagementFlag]: #secondaryloginmanagementflag
#### [secondaryLoginManagementFlag]
Whether a user may change their security options (IP restriction, password expiration, or enforce security questions on login) which were pre-selected by their account's master user.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[secondaryLoginRequiredFlag]: #secondaryloginrequiredflag
#### [secondaryLoginRequiredFlag]
Whether a user is required to answer a security question when logging into the SoftLayer customer portal.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[secondaryPasswordModifyDate]: #secondarypasswordmodifydate
#### [secondaryPasswordModifyDate]
The date when a user's password was last updated.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[secondaryPasswordTimeoutDays]: #secondarypasswordtimeoutdays
#### [secondaryPasswordTimeoutDays]
The number of days for which a user's password is active.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[sms]: #sms
#### [sms]
A phone number that can receive SMS text messages for this portal user.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[sslVpnAllowedFlag]: #sslvpnallowedflag
#### [sslVpnAllowedFlag]
Whether a portal user may connect to the SoftLayer private network via SSL VPN or not.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[state]: #state
#### [state]
A two-letter abbreviation of the state in the mailing address belonging to a portal user. If a user does not reside in a province then this is typically blank.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[statusDate]: #statusdate
#### [statusDate]
The date a portal users record's last status change.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[timezoneId]: #timezoneid
#### [timezoneId]
A portal user's time zone.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[userStatusId]: #userstatusid
#### [userStatusId]
A number reflecting the state of a portal user.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[username]: #username
#### [username]
A portal user's username.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[verificationCode]: #verificationcode
#### [verificationCode]
The verification code from Bluemix BSS to save in the invitation  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[vpnManualConfig]: #vpnmanualconfig
#### [vpnManualConfig]
Whether a portal user vpn subnets have been manual configured.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[yahoo]: #yahoo
#### [yahoo]
A portal user's Yahoo! Chat name.  
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The customer account that a user belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[actions]: #actions
#### [actions]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Permission_Action'>SoftLayer_User_Permission_Action[] </a>**


</div>
<div class="prop-row">

-----
[additionalEmails]: #additionalemails
#### [additionalEmails]
A portal user's additional email addresses. These email addresses are contacted when updates are made to support tickets.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_AdditionalEmail'>SoftLayer_User_Customer_AdditionalEmail[] </a>**


</div>
<div class="prop-row">

-----
[apiAuthenticationKeys]: #apiauthenticationkeys
#### [apiAuthenticationKeys]
A portal user's API Authentication keys. There is a max limit of one API key per user.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_ApiAuthentication'>SoftLayer_User_Customer_ApiAuthentication[] </a>**


</div>
<div class="prop-row">

-----
[childUsers]: #childusers
#### [childUsers]
A portal user's child users. Some portal users may not have child users.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a>**


</div>
<div class="prop-row">

-----
[closedTickets]: #closedtickets
#### [closedTickets]
An user's associated closed tickets.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[dedicatedHosts]: #dedicatedhosts
#### [dedicatedHosts]
The dedicated hosts to which the user has been granted access.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost[] </a>**


</div>
<div class="prop-row">

-----
[externalBindings]: #externalbindings
#### [externalBindings]
The external authentication bindings that link an external identifier to a SoftLayer user.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_External_Binding'>SoftLayer_User_External_Binding[] </a>**


</div>
<div class="prop-row">

-----
[hardware]: #hardware
#### [hardware]
A portal user's accessible hardware. These permissions control which hardware a user has access to in the SoftLayer customer portal.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hardwareNotifications]: #hardwarenotifications
#### [hardwareNotifications]
Hardware notifications associated with this user. A hardware notification links a user to a piece of hardware, and that user will be notified if any monitors on that hardware fail, if the monitors have a status of 'Notify User'.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Hardware'>SoftLayer_User_Customer_Notification_Hardware[] </a>**


</div>
<div class="prop-row">

-----
[hasAcknowledgedSupportPolicyFlag]: #hasacknowledgedsupportpolicyflag
#### [hasAcknowledgedSupportPolicyFlag]
Whether or not a user has acknowledged the support policy.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[hasFullDedicatedHostAccessFlag]: #hasfulldedicatedhostaccessflag
#### [hasFullDedicatedHostAccessFlag]
Permission granting the user access to all Dedicated Host devices on the account.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[hasFullHardwareAccessFlag]: #hasfullhardwareaccessflag
#### [hasFullHardwareAccessFlag]
Whether or not a portal user has access to all hardware on their account.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[hasFullVirtualGuestAccessFlag]: #hasfullvirtualguestaccessflag
#### [hasFullVirtualGuestAccessFlag]
Whether or not a portal user has access to all hardware on their account.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[ibmIdLink]: #ibmidlink
#### [ibmIdLink]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_Link'>SoftLayer_User_Customer_Link </a>**


</div>
<div class="prop-row">

-----
[layoutProfiles]: #layoutprofiles
#### [layoutProfiles]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Layout_Profile'>SoftLayer_Layout_Profile[] </a>**


</div>
<div class="prop-row">

-----
[locale]: #locale
#### [locale]
A user's locale. Locale holds user's language and region information.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Locale'>SoftLayer_Locale </a>**


</div>
<div class="prop-row">

-----
[loginAttempts]: #loginattempts
#### [loginAttempts]
A user's attempts to log into the SoftLayer customer portal.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_Access_Authentication'>SoftLayer_User_Customer_Access_Authentication[] </a>**


</div>
<div class="prop-row">

-----
[mobileDevices]: #mobiledevices
#### [mobileDevices]
A portal user's associated mobile device profiles.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_MobileDevice'>SoftLayer_User_Customer_MobileDevice[] </a>**


</div>
<div class="prop-row">

-----
[notificationSubscribers]: #notificationsubscribers
#### [notificationSubscribers]
Notification subscription records for the user.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_Subscriber'>SoftLayer_Notification_Subscriber[] </a>**


</div>
<div class="prop-row">

-----
[openTickets]: #opentickets
#### [openTickets]
An user's associated open tickets.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[overrides]: #overrides
#### [overrides]
A portal user's vpn accessible subnets.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Service_Vpn_Overrides'>SoftLayer_Network_Service_Vpn_Overrides[] </a>**


</div>
<div class="prop-row">

-----
[parent]: #parent
#### [parent]
A portal user's parent user. If a SoftLayer_User_Customer has a null parentId property then it doesn't have a parent user.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a>**


</div>
<div class="prop-row">

-----
[permissions]: #permissions
#### [permissions]
A portal user's permissions. These permissions control that user's access to functions within the SoftLayer customer portal and API.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission'>SoftLayer_User_Customer_CustomerPermission_Permission[] </a>**


</div>
<div class="prop-row">

-----
[preferences]: #preferences
#### [preferences]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Preference'>SoftLayer_User_Preference[] </a>**


</div>
<div class="prop-row">

-----
[roles]: #roles
#### [roles]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Permission_Role'>SoftLayer_User_Permission_Role[] </a>**


</div>
<div class="prop-row">

-----
[salesforceUserLink]: #salesforceuserlink
#### [salesforceUserLink]
[DEPRECATED]  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_Link'>SoftLayer_User_Customer_Link </a>**


</div>
<div class="prop-row">

-----
[securityAnswers]: #securityanswers
#### [securityAnswers]
A portal user's security question answers. Some portal users may not have security answers or may not be configured to require answering a security question on login.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_Security_Answer'>SoftLayer_User_Customer_Security_Answer[] </a>**


</div>
<div class="prop-row">

-----
[subscribers]: #subscribers
#### [subscribers]
A user's notification subscription records.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber[] </a>**


</div>
<div class="prop-row">

-----
[successfulLogins]: #successfullogins
#### [successfulLogins]
A user's successful attempts to log into the SoftLayer customer portal.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_Access_Authentication'>SoftLayer_User_Customer_Access_Authentication[] </a>**


</div>
<div class="prop-row">

-----
[supportPolicyAcknowledgementRequiredFlag]: #supportpolicyacknowledgementrequiredflag
#### [supportPolicyAcknowledgementRequiredFlag]
Whether or not a user is required to acknowledge the support policy for portal access.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[surveyRequiredFlag]: #surveyrequiredflag
#### [surveyRequiredFlag]
Whether or not a user must take a brief survey the next time they log into the SoftLayer customer portal.  
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[surveys]: #surveys
#### [surveys]
The surveys that a user has taken in the SoftLayer customer portal.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Survey'>SoftLayer_Survey[] </a>**


</div>
<div class="prop-row">

-----
[tickets]: #tickets
#### [tickets]
An user's associated tickets.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a>**


</div>
<div class="prop-row">

-----
[timezone]: #timezone
#### [timezone]
A portal user's time zone.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Locale_Timezone'>SoftLayer_Locale_Timezone </a>**


</div>
<div class="prop-row">

-----
[unsuccessfulLogins]: #unsuccessfullogins
#### [unsuccessfulLogins]
A user's unsuccessful attempts to log into the SoftLayer customer portal.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_Access_Authentication'>SoftLayer_User_Customer_Access_Authentication[] </a>**


</div>
<div class="prop-row">

-----
[userLinks]: #userlinks
#### [userLinks]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_Link'>SoftLayer_User_Customer_Link[] </a>**


</div>
<div class="prop-row">

-----
[userStatus]: #userstatus
#### [userStatus]
A portal user's status, which controls overall access to the SoftLayer customer portal and VPN access to the private network.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_User_Customer_Status'>SoftLayer_User_Customer_Status </a>**


</div>
<div class="prop-row">

-----
[virtualGuests]: #virtualguests
#### [virtualGuests]
A portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing Instances a user has access to in the SoftLayer customer portal.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a>**


</div>

## Count
<div class="prop-row">

-----
[actionCount]: #actioncount
#### [actionCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[additionalEmailCount]: #additionalemailcount
#### [additionalEmailCount]
A count of a portal user's additional email addresses. These email addresses are contacted when updates are made to support tickets.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[apiAuthenticationKeyCount]: #apiauthenticationkeycount
#### [apiAuthenticationKeyCount]
A count of a portal user's API Authentication keys. There is a max limit of one API key per user.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[childUserCount]: #childusercount
#### [childUserCount]
A count of a portal user's child users. Some portal users may not have child users.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[closedTicketCount]: #closedticketcount
#### [closedTicketCount]
A count of an user's associated closed tickets.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[dedicatedHostCount]: #dedicatedhostcount
#### [dedicatedHostCount]
A count of the dedicated hosts to which the user has been granted access.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[externalBindingCount]: #externalbindingcount
#### [externalBindingCount]
A count of the external authentication bindings that link an external identifier to a SoftLayer user.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareCount]: #hardwarecount
#### [hardwareCount]
A count of a portal user's accessible hardware. These permissions control which hardware a user has access to in the SoftLayer customer portal.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[hardwareNotificationCount]: #hardwarenotificationcount
#### [hardwareNotificationCount]
A count of hardware notifications associated with this user. A hardware notification links a user to a piece of hardware, and that user will be notified if any monitors on that hardware fail, if the monitors have a status of 'Notify User'.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[layoutProfileCount]: #layoutprofilecount
#### [layoutProfileCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[loginAttemptCount]: #loginattemptcount
#### [loginAttemptCount]
A count of a user's attempts to log into the SoftLayer customer portal.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[mobileDeviceCount]: #mobiledevicecount
#### [mobileDeviceCount]
A count of a portal user's associated mobile device profiles.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[notificationSubscriberCount]: #notificationsubscribercount
#### [notificationSubscriberCount]
A count of notification subscription records for the user.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[openTicketCount]: #openticketcount
#### [openTicketCount]
A count of an user's associated open tickets.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[overrideCount]: #overridecount
#### [overrideCount]
A count of a portal user's vpn accessible subnets.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[permissionCount]: #permissioncount
#### [permissionCount]
A count of a portal user's permissions. These permissions control that user's access to functions within the SoftLayer customer portal and API.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[preferenceCount]: #preferencecount
#### [preferenceCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[roleCount]: #rolecount
#### [roleCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[securityAnswerCount]: #securityanswercount
#### [securityAnswerCount]
A count of a portal user's security question answers. Some portal users may not have security answers or may not be configured to require answering a security question on login.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[subscriberCount]: #subscribercount
#### [subscriberCount]
A count of a user's notification subscription records.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[successfulLoginCount]: #successfullogincount
#### [successfulLoginCount]
A count of a user's successful attempts to log into the SoftLayer customer portal.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[surveyCount]: #surveycount
#### [surveyCount]
A count of the surveys that a user has taken in the SoftLayer customer portal.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[ticketCount]: #ticketcount
#### [ticketCount]
A count of an user's associated tickets.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[unsuccessfulLoginCount]: #unsuccessfullogincount
#### [unsuccessfulLoginCount]
A count of a user's unsuccessful attempts to log into the SoftLayer customer portal.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[userLinkCount]: #userlinkcount
#### [userLinkCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[virtualGuestCount]: #virtualguestcount
#### [virtualGuestCount]
A count of a portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing Instances a user has access to in the SoftLayer customer portal.   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


