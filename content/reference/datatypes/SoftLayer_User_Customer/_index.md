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





<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
    <div id="localProperties" class="prop-content" >
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountId" name=accountId>accountId</a>
            </span>
            <div class='views-field-body'>A portal user's associated [[SoftLayer_Account|customer account]] id. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#address1" name=address1>address1</a>
            </span>
            <div class='views-field-body'>The first line of the mailing address belonging to a portal user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#address2" name=address2>address2</a>
            </span>
            <div class='views-field-body'>The second line of the mailing address belonging to a portal user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#aim" name=aim>aim</a>
            </span>
            <div class='views-field-body'>A portal user's AOL Instant Messenger screen name. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#alternatePhone" name=alternatePhone>alternatePhone</a>
            </span>
            <div class='views-field-body'>A portal user's secondary phone number. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#authenticationToken" name=authenticationToken>authenticationToken</a>
            </span>
            <div class='views-field-body'>The authentication token used for logging into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Container_User_Authentication_Token'>SoftLayer_Container_User_Authentication_Token </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#city" name=city>city</a>
            </span>
            <div class='views-field-body'>The city of the mailing address belonging to a portal user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#companyName" name=companyName>companyName</a>
            </span>
            <div class='views-field-body'>A portal user's associated company. This may not be the same company as the customer that owns this portal user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#country" name=country>country</a>
            </span>
            <div class='views-field-body'>A two-letter abbreviation of the country in the mailing address belonging to a portal user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The date a portal user's record was created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#daylightSavingsTimeFlag" name=daylightSavingsTimeFlag>daylightSavingsTimeFlag</a>
            </span>
            <div class='views-field-body'>Whether a portal user's time zone is affected by Daylight Savings Time. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#denyAllResourceAccessOnCreateFlag" name=denyAllResourceAccessOnCreateFlag>denyAllResourceAccessOnCreateFlag</a>
            </span>
            <div class='views-field-body'>Flag used to deny access to all hardware and cloud computing instances upon user creation. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#displayName" name=displayName>displayName</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#email" name=email>email</a>
            </span>
            <div class='views-field-body'>A portal user's email address. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#firstName" name=firstName>firstName</a>
            </span>
            <div class='views-field-body'>A portal user's first name. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#forumPasswordHash" name=forumPasswordHash>forumPasswordHash</a>
            </span>
            <div class='views-field-body'>A user's password for the SoftLayer forums, hashed for auto-login capability from the SoftLayer customer portal </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#iamAuthorizationFlag" name=iamAuthorizationFlag>iamAuthorizationFlag</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#iamId" name=iamId>iamId</a>
            </span>
            <div class='views-field-body'>The IAMid (realm-identifier) of the user being created by PaaS </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#icq" name=icq>icq</a>
            </span>
            <div class='views-field-body'>A portal user's ICQ UIN. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A portal user's internal identifying number. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ipAddressRestriction" name=ipAddressRestriction>ipAddressRestriction</a>
            </span>
            <div class='views-field-body'>The IP addresses or IP ranges from which a user may login to the SoftLayer customer portal. Specify subnets in CIDR format and separate multiple addresses and subnets by commas. You may combine IPv4 and IPv6 addresses and subnets, for example: 192.168.0.0/16,fe80:021b::0/64. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#isMasterUserFlag" name=isMasterUserFlag>isMasterUserFlag</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#lastName" name=lastName>lastName</a>
            </span>
            <div class='views-field-body'>A portal user's last name. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#linkedAccountIntegrationMode" name=linkedAccountIntegrationMode>linkedAccountIntegrationMode</a>
            </span>
            <div class='views-field-body'>The linked account integration mode </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#localeId" name=localeId>localeId</a>
            </span>
            <div class='views-field-body'>A portal user's associated [[SoftLayer_Locale|locale]] id. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#managedByFederationFlag" name=managedByFederationFlag>managedByFederationFlag</a>
            </span>
            <div class='views-field-body'>Determines if this portal user is managed by SAML federation. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#managedByOpenIdConnectFlag" name=managedByOpenIdConnectFlag>managedByOpenIdConnectFlag</a>
            </span>
            <div class='views-field-body'>Determines if this portal user is managed by IBMid federation. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The date a portal user's record was last modified. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#msn" name=msn>msn</a>
            </span>
            <div class='views-field-body'>A portal user's MSN address. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#nameId" name=nameId>nameId</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#officePhone" name=officePhone>officePhone</a>
            </span>
            <div class='views-field-body'>A portal user's office phone number. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#openIdConnectUserName" name=openIdConnectUserName>openIdConnectUserName</a>
            </span>
            <div class='views-field-body'>The BlueID username associated to with this user, if the account is managed by OpenIDConnect / BlueID federation </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#parentId" name=parentId>parentId</a>
            </span>
            <div class='views-field-body'>A portal user's parent user. Id a users parentId is ''null'' then it doesn't have a parent user in the customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#passwordExpireDate" name=passwordExpireDate>passwordExpireDate</a>
            </span>
            <div class='views-field-body'>The expiration date for the user's password </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#postalCode" name=postalCode>postalCode</a>
            </span>
            <div class='views-field-body'>The postal code of the mailing address belonging to an portal user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#pptpVpnAllowedFlag" name=pptpVpnAllowedFlag>pptpVpnAllowedFlag</a>
            </span>
            <div class='views-field-body'>Whether a portal user may connect to the SoftLayer private network via PPTP VPN or not. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#savedId" name=savedId>savedId</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#secondaryLoginManagementFlag" name=secondaryLoginManagementFlag>secondaryLoginManagementFlag</a>
            </span>
            <div class='views-field-body'>Whether a user may change their security options (IP restriction, password expiration, or enforce security questions on login) which were pre-selected by their account's master user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#secondaryLoginRequiredFlag" name=secondaryLoginRequiredFlag>secondaryLoginRequiredFlag</a>
            </span>
            <div class='views-field-body'>Whether a user is required to answer a security question when logging into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#secondaryPasswordModifyDate" name=secondaryPasswordModifyDate>secondaryPasswordModifyDate</a>
            </span>
            <div class='views-field-body'>The date when a user's password was last updated. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#secondaryPasswordTimeoutDays" name=secondaryPasswordTimeoutDays>secondaryPasswordTimeoutDays</a>
            </span>
            <div class='views-field-body'>The number of days for which a user's password is active. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sms" name=sms>sms</a>
            </span>
            <div class='views-field-body'>A phone number that can receive SMS text messages for this portal user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sslVpnAllowedFlag" name=sslVpnAllowedFlag>sslVpnAllowedFlag</a>
            </span>
            <div class='views-field-body'>Whether a portal user may connect to the SoftLayer private network via SSL VPN or not. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#state" name=state>state</a>
            </span>
            <div class='views-field-body'>A two-letter abbreviation of the state in the mailing address belonging to a portal user. If a user does not reside in a province then this is typically blank. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#statusDate" name=statusDate>statusDate</a>
            </span>
            <div class='views-field-body'>The date a portal users record's last status change. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#timezoneId" name=timezoneId>timezoneId</a>
            </span>
            <div class='views-field-body'>A portal user's time zone. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userStatusId" name=userStatusId>userStatusId</a>
            </span>
            <div class='views-field-body'>A number reflecting the state of a portal user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#username" name=username>username</a>
            </span>
            <div class='views-field-body'>A portal user's username. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#verificationCode" name=verificationCode>verificationCode</a>
            </span>
            <div class='views-field-body'>The verification code from Bluemix BSS to save in the invitation </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#vpnManualConfig" name=vpnManualConfig>vpnManualConfig</a>
            </span>
            <div class='views-field-body'>Whether a portal user vpn subnets have been manual configured. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#yahoo" name=yahoo>yahoo</a>
            </span>
            <div class='views-field-body'>A portal user's Yahoo! Chat name. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The customer account that a user belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#actions" name=actions>actions</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Permission_Action'>SoftLayer_User_Permission_Action[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#additionalEmails" name=additionalEmails>additionalEmails</a>
            </span>
            <div class='views-field-body'>A portal user's additional email addresses. These email addresses are contacted when updates are made to support tickets. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_AdditionalEmail'>SoftLayer_User_Customer_AdditionalEmail[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#apiAuthenticationKeys" name=apiAuthenticationKeys>apiAuthenticationKeys</a>
            </span>
            <div class='views-field-body'>A portal user's API Authentication keys. There is a max limit of two API keys per user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_ApiAuthentication'>SoftLayer_User_Customer_ApiAuthentication[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#cdnAccounts" name=cdnAccounts>cdnAccounts</a>
            </span>
            <div class='views-field-body'>The CDN accounts associated with a portal user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_ContentDelivery_Account'>SoftLayer_Network_ContentDelivery_Account[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#childUsers" name=childUsers>childUsers</a>
            </span>
            <div class='views-field-body'>A portal user's child users. Some portal users may not have child users. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#closedTickets" name=closedTickets>closedTickets</a>
            </span>
            <div class='views-field-body'>An user's associated closed tickets. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#dedicatedHosts" name=dedicatedHosts>dedicatedHosts</a>
            </span>
            <div class='views-field-body'>The dedicated hosts to which the user has been granted access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Virtual_DedicatedHost'>SoftLayer_Virtual_DedicatedHost[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#externalBindings" name=externalBindings>externalBindings</a>
            </span>
            <div class='views-field-body'>The external authentication bindings that link an external identifier to a SoftLayer user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_External_Binding'>SoftLayer_User_External_Binding[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardware" name=hardware>hardware</a>
            </span>
            <div class='views-field-body'>A portal user's accessible hardware. These permissions control which hardware a user has access to in the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareNotifications" name=hardwareNotifications>hardwareNotifications</a>
            </span>
            <div class='views-field-body'>Hardware notifications associated with this user. A hardware notification links a user to a piece of hardware, and that user will be notified if any monitors on that hardware fail, if the monitors have a status of 'Notify User'. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_Notification_Hardware'>SoftLayer_User_Customer_Notification_Hardware[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hasAcknowledgedSupportPolicyFlag" name=hasAcknowledgedSupportPolicyFlag>hasAcknowledgedSupportPolicyFlag</a>
            </span>
            <div class='views-field-body'>Whether or not a user has acknowledged the support policy. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hasFullDedicatedHostAccessFlag" name=hasFullDedicatedHostAccessFlag>hasFullDedicatedHostAccessFlag</a>
            </span>
            <div class='views-field-body'>Permission granting the user access to all Dedicated Host devices on the account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hasFullHardwareAccessFlag" name=hasFullHardwareAccessFlag>hasFullHardwareAccessFlag</a>
            </span>
            <div class='views-field-body'>Whether or not a portal user has access to all hardware on their account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hasFullVirtualGuestAccessFlag" name=hasFullVirtualGuestAccessFlag>hasFullVirtualGuestAccessFlag</a>
            </span>
            <div class='views-field-body'>Whether or not a portal user has access to all hardware on their account. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ibmIdLink" name=ibmIdLink>ibmIdLink</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_Link'>SoftLayer_User_Customer_Link </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#layoutProfiles" name=layoutProfiles>layoutProfiles</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Layout_Profile'>SoftLayer_Layout_Profile[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#locale" name=locale>locale</a>
            </span>
            <div class='views-field-body'>A user's locale. Locale holds user's language and region information. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Locale'>SoftLayer_Locale </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#loginAttempts" name=loginAttempts>loginAttempts</a>
            </span>
            <div class='views-field-body'>A user's attempts to log into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_Access_Authentication'>SoftLayer_User_Customer_Access_Authentication[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#mobileDevices" name=mobileDevices>mobileDevices</a>
            </span>
            <div class='views-field-body'>A portal user's associated mobile device profiles. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_MobileDevice'>SoftLayer_User_Customer_MobileDevice[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notificationSubscribers" name=notificationSubscribers>notificationSubscribers</a>
            </span>
            <div class='views-field-body'>Notification subscription records for the user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_Subscriber'>SoftLayer_Notification_Subscriber[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#openTickets" name=openTickets>openTickets</a>
            </span>
            <div class='views-field-body'>An user's associated open tickets. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#overrides" name=overrides>overrides</a>
            </span>
            <div class='views-field-body'>A portal user's vpn accessible subnets. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Service_Vpn_Overrides'>SoftLayer_Network_Service_Vpn_Overrides[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#parent" name=parent>parent</a>
            </span>
            <div class='views-field-body'>A portal user's parent user. If a SoftLayer_User_Customer has a null parentId property then it doesn't have a parent user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#permissions" name=permissions>permissions</a>
            </span>
            <div class='views-field-body'>A portal user's permissions. These permissions control that user's access to functions within the SoftLayer customer portal and API. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_CustomerPermission_Permission'>SoftLayer_User_Customer_CustomerPermission_Permission[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#preferences" name=preferences>preferences</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Preference'>SoftLayer_User_Preference[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#roles" name=roles>roles</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Permission_Role'>SoftLayer_User_Permission_Role[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#salesforceUserLink" name=salesforceUserLink>salesforceUserLink</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_Link'>SoftLayer_User_Customer_Link </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#securityAnswers" name=securityAnswers>securityAnswers</a>
            </span>
            <div class='views-field-body'>A portal user's security question answers. Some portal users may not have security answers or may not be configured to require answering a security question on login. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_Security_Answer'>SoftLayer_User_Customer_Security_Answer[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#subscribers" name=subscribers>subscribers</a>
            </span>
            <div class='views-field-body'>A user's notification subscription records. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Notification_User_Subscriber'>SoftLayer_Notification_User_Subscriber[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#successfulLogins" name=successfulLogins>successfulLogins</a>
            </span>
            <div class='views-field-body'>A user's successful attempts to log into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_Access_Authentication'>SoftLayer_User_Customer_Access_Authentication[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#supportPolicyAcknowledgementRequiredFlag" name=supportPolicyAcknowledgementRequiredFlag>supportPolicyAcknowledgementRequiredFlag</a>
            </span>
            <div class='views-field-body'>Whether or not a user is required to acknowledge the support policy for portal access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#surveyRequiredFlag" name=surveyRequiredFlag>surveyRequiredFlag</a>
            </span>
            <div class='views-field-body'>Whether or not a user must take a brief survey the next time they log into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#surveys" name=surveys>surveys</a>
            </span>
            <div class='views-field-body'>The surveys that a user has taken in the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Survey'>SoftLayer_Survey[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#tickets" name=tickets>tickets</a>
            </span>
            <div class='views-field-body'>An user's associated tickets. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Ticket'>SoftLayer_Ticket[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#timezone" name=timezone>timezone</a>
            </span>
            <div class='views-field-body'>A portal user's time zone. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Locale_Timezone'>SoftLayer_Locale_Timezone </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#unsuccessfulLogins" name=unsuccessfulLogins>unsuccessfulLogins</a>
            </span>
            <div class='views-field-body'>A user's unsuccessful attempts to log into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_Access_Authentication'>SoftLayer_User_Customer_Access_Authentication[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userLinks" name=userLinks>userLinks</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_Link'>SoftLayer_User_Customer_Link[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userStatus" name=userStatus>userStatus</a>
            </span>
            <div class='views-field-body'>A portal user's status, which controls overall access to the SoftLayer customer portal and VPN access to the private network. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_User_Customer_Status'>SoftLayer_User_Customer_Status </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#virtualGuests" name=virtualGuests>virtualGuests</a>
            </span>
            <div class='views-field-body'>A portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing Instances a user has access to in the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest[] </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#actionCount" name=actionCount>actionCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#additionalEmailCount" name=additionalEmailCount>additionalEmailCount</a>
            </span>
            <div class='views-field-body'>A count of a portal user's additional email addresses. These email addresses are contacted when updates are made to support tickets. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#apiAuthenticationKeyCount" name=apiAuthenticationKeyCount>apiAuthenticationKeyCount</a>
            </span>
            <div class='views-field-body'>A count of a portal user's API Authentication keys. There is a max limit of two API keys per user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#cdnAccountCount" name=cdnAccountCount>cdnAccountCount</a>
            </span>
            <div class='views-field-body'>A count of the CDN accounts associated with a portal user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#childUserCount" name=childUserCount>childUserCount</a>
            </span>
            <div class='views-field-body'>A count of a portal user's child users. Some portal users may not have child users. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#closedTicketCount" name=closedTicketCount>closedTicketCount</a>
            </span>
            <div class='views-field-body'>A count of an user's associated closed tickets. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#dedicatedHostCount" name=dedicatedHostCount>dedicatedHostCount</a>
            </span>
            <div class='views-field-body'>A count of the dedicated hosts to which the user has been granted access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#externalBindingCount" name=externalBindingCount>externalBindingCount</a>
            </span>
            <div class='views-field-body'>A count of the external authentication bindings that link an external identifier to a SoftLayer user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareCount" name=hardwareCount>hardwareCount</a>
            </span>
            <div class='views-field-body'>A count of a portal user's accessible hardware. These permissions control which hardware a user has access to in the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#hardwareNotificationCount" name=hardwareNotificationCount>hardwareNotificationCount</a>
            </span>
            <div class='views-field-body'>A count of hardware notifications associated with this user. A hardware notification links a user to a piece of hardware, and that user will be notified if any monitors on that hardware fail, if the monitors have a status of 'Notify User'. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#layoutProfileCount" name=layoutProfileCount>layoutProfileCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#loginAttemptCount" name=loginAttemptCount>loginAttemptCount</a>
            </span>
            <div class='views-field-body'>A count of a user's attempts to log into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#mobileDeviceCount" name=mobileDeviceCount>mobileDeviceCount</a>
            </span>
            <div class='views-field-body'>A count of a portal user's associated mobile device profiles. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#notificationSubscriberCount" name=notificationSubscriberCount>notificationSubscriberCount</a>
            </span>
            <div class='views-field-body'>A count of notification subscription records for the user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#openTicketCount" name=openTicketCount>openTicketCount</a>
            </span>
            <div class='views-field-body'>A count of an user's associated open tickets. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#overrideCount" name=overrideCount>overrideCount</a>
            </span>
            <div class='views-field-body'>A count of a portal user's vpn accessible subnets. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#permissionCount" name=permissionCount>permissionCount</a>
            </span>
            <div class='views-field-body'>A count of a portal user's permissions. These permissions control that user's access to functions within the SoftLayer customer portal and API. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#preferenceCount" name=preferenceCount>preferenceCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#roleCount" name=roleCount>roleCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#securityAnswerCount" name=securityAnswerCount>securityAnswerCount</a>
            </span>
            <div class='views-field-body'>A count of a portal user's security question answers. Some portal users may not have security answers or may not be configured to require answering a security question on login. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#subscriberCount" name=subscriberCount>subscriberCount</a>
            </span>
            <div class='views-field-body'>A count of a user's notification subscription records. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#successfulLoginCount" name=successfulLoginCount>successfulLoginCount</a>
            </span>
            <div class='views-field-body'>A count of a user's successful attempts to log into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#surveyCount" name=surveyCount>surveyCount</a>
            </span>
            <div class='views-field-body'>A count of the surveys that a user has taken in the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ticketCount" name=ticketCount>ticketCount</a>
            </span>
            <div class='views-field-body'>A count of an user's associated tickets. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#unsuccessfulLoginCount" name=unsuccessfulLoginCount>unsuccessfulLoginCount</a>
            </span>
            <div class='views-field-body'>A count of a user's unsuccessful attempts to log into the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#userLinkCount" name=userLinkCount>userLinkCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#virtualGuestCount" name=virtualGuestCount>virtualGuestCount</a>
            </span>
            <div class='views-field-body'>A count of a portal user's accessible CloudLayer Computing Instances. These permissions control which CloudLayer Computing Instances a user has access to in the SoftLayer customer portal. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


