---
title: "Authenticating to the SoftLayer API"
description: "Authenticating to the SoftLayer API"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
---



''username'' which contains your portal/API username, and ''apiKey'' which contains your API access key. If you don't provide the authenticate header the API returns the [[exception]] "No valid authentication headers found.", and if you provide an invalid username and apiKey combination the API returns the exception "Invalid API Token".

A SOAP representation of the ''authenticate'' header looks like this:
<xml>
<authenticate xsi:type="slt:authenticate" xmlns:slt="http://api.service.softlayer.com/soap/v3/SLTypes/">
    <username xsi:type="xsd:string">MY_USERNAME</username>
    <apiKey xsi:type="xsd:string">MY_API_ACCESS_KEY</apiKey>
</authenticate>
</xml>
while it's XML-RPC counterpart looks like this:
<xml>
<struct>
    <member>
        <name>authenticate</name>
        <value>
            <struct>
                <member>
                    <name>username</name>
                    <value>
                        <string>MY_USERNAME</string>
                    </value>
                </member>
                <member>
                    <name>apiKey</name>
                    <value>
                        <string>MY_API_ACCESS_KEY</string>
                    </value>
                </member>
            </struct>
        </value>
    </member>
</struct>
</xml>
## Generating Your API Key
There are two ways to generate an API access key, via the portal or by direct API calls. To generate your own API access key in the customer portal:

1. Log into the [https://manage.softlayer.com/ SoftLayer customer portal] with your customer account master user's username and portal password.
2. Click the ''administrative'' then ''API Access'' links.
3. Select the user you wish to generate a key for and click ''Generate API Access Key''

To generate an API access key via API calls invoke the [[SoftLayer_User_Customer::addApiAuthenticationKey|addApiAuthenticationKey]] method in the [[SoftLayer_User_Customer]] service. To remove a user's API access key execute the [[SoftLayer_User_Customer::removeApiAuthenticationKey|removeApiAuthenticationKey]] method in the same service. Be careful when removing API access keys. Removing these keys will remove that user's ability to use the SoftLayer API.

## Temporary API Key
It is possible to get a short lived API key using a username/password combination with [[SoftLayer_User_Customer::getPortalLoginToken]]. This token can be used in place of an API key during calls and will expire after 48 hours.

## Associated Methods

* [[SoftLayer_User_Customer::getApiAuthenticationKeys]]
* [[SoftLayer_User_Customer::addApiAuthenticationKey]]
* [[SoftLayer_User_Customer::removeApiAuthenticationKey]]
## See Also

* [[SoftLayer_User_Customer_ApiAuthentication]]

## External Links

* The [https://manage.softlayer.com/UserManagement/apiKeychain API keychain] page at the [https://manage.softlayer.com/ SoftLayer customer portal]