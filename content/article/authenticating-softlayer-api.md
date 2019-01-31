---
title: "Authenticating to the SoftLayer API"
description: "Authenticating to the SoftLayer API"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
---

### Note about IBMid
More information about how IBMid works can be found here:
- https://console.bluemix.net/docs/account/softlayerlink.html#unifyingaccounts
- https://console.bluemix.net/docs/customer-portal/cpmanibmid.html#customerportal_ibmid
- https://console.bluemix.net/docs/iam/apikeys.html#manapikey

Currently when an IBMid is linked to SoftLayer, a user record is created in the SoftLayer environment, with a username that matches the email used to login. While you won't be able to login to the SoftLayer control portal directly with your password(instead you will need to authenticate with the IBMid service), you can still follow these steps to create an API key for your SoftLayer Infrastructure

### SoftLayer Users

''username'' which contains your portal/API username, and ''apiKey'' which contains your API access key. If you don't provide the authenticate header the API returns the [[exception]] "No valid authentication headers found.", and if you provide an invalid username and apiKey combination the API returns the exception "Invalid API Token".

### SOAP

A SOAP representation of the ''authenticate'' header looks like this:
<xml>
<authenticate xsi:type="slt:authenticate" xmlns:slt="http://api.service.softlayer.com/soap/v3/SLTypes/">
    <username xsi:type="xsd:string">MY_USERNAME</username>
    <apiKey xsi:type="xsd:string">MY_API_ACCESS_KEY</apiKey>
</authenticate>
</xml>

### XMLRPC

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

### REST
With REST, you can simply use the HTTP Basic Authentication
`curl  -vvv -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getObject'`

## Generating Your API Key
There are two ways to generate an API access key, via the portal or by direct API calls. To generate your own API access key in the customer portal:

1. Log into the [Control Portal](https://control.softlayer.com/) with your customer account master user's username and portal password.
2. In the top menu, go to [Account -> Users -> User List](https://control.softlayer.com/account/users)
3. Find the user you are working with, and there should be a `Generate` button in the `API Key` column. If it says `View` instead, that means the user already has an existing key.

To generate an API access key via API calls invoke the [SoftLayer_User_Customer::addApiAuthenticationKey](https://softlayer.github.io/reference/services/SoftLayer_User_Customer/addApiAuthenticationKey) method in the SoftLayer_User_Customer service. To remove a user's API access key execute the [SoftLayer_User_Customer::removeApiAuthenticationKey](https://softlayer.github.io/reference/services/SoftLayer_User_Customer/removeApiAuthenticationKey) method in the same service. Be careful when removing API access keys. Removing these keys will remove that user's ability to use the SoftLayer API.

[Example](/python/manageUsers/)

## Temporary API Key
It is possible to get a short lived API key using a username/password combination with [SoftLayer_User_Customer::getPortalLoginToken](/reference/services/SoftLayer_User_Customer/getPortalLoginToken/). This token can be used in place of an API key during calls and will expire after 48 hours.

*NOTICE* SoftLayer_User_Customer::getPortalLoginToken does not support the REST endpoint. You will need to send in your request with an XML or SOAP call.

*NOTICE* This method also doesn't work with IBMid username/passwords

## Temporary IBMid Token
It is possible to use the IBMid authentication service to make softlayer API calls.

### Get the IMS_TOKEN
For most users, you will need your username and password, send that to https://iam.ng.bluemix.net/oidc/token, and you will be given a token that can be used to make SoftLayer(IMS) api calls.

```
IBMUSER=myemail@email.com
IBMPASS=123qweasdzxc
curl -s -u 'bx:bx' -k -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d "grant_type=password&response_type=cloud_iam,ims_portal&username=$IBMUSER&password=$IBMPASS" https://iam.ng.bluemix.net/oidc/token
```

For users with an IBM email, you will need to use the SSO endpoint (the above example will also mention this if you try your username/password)

Tokens are retrieved from https://iam-id-1.ng.bluemix.net/identity/passcode
```
TOKEN=qwe124cxzv
curl -s -u 'bx:bx' -k -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d "grant_type=urn:ibm:params:oauth:grant-type:passcode&passcode=$PASSCODE0&response_type=cloud_iam,ims_portal" https://iam.ng.bluemix.net/oidc/token
```

In the response, will be a data field call `ims_token` which will let you authenticate to the SoftLayer API until the token expires (which should also be in the returned data)


The REST endpoint doesn't support authenticating with tokens, so you will need to use the SOAP/XML endpoints.

In the authentication header, you will set `userId` and `authToken`,  instead of `username` and `apiKey`. A call to SoftLayer_Customer::getObject would look like this in XML.

```xml
<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<methodCall>
  <methodName>getObject</methodName>
  <params>
    <param>
      <value>
        <struct>
          <member>
            <name>headers</name>
            <value>
              <struct>
                <member>
                  <name>authenticate</name>
                  <value>
                    <struct>
                      <member>
                        <name>userId</name>
                        <value>
                          <int>$USERID</int>
                        </value>
                      </member>
                      <member>
                        <name>complexType</name>
                        <value>
                          <string>PortalLoginToken</string>
                        </value>
                      </member>
                      <member>
                        <name>authToken</name>
                        <value>
                          <string>$IMS_TOKEN</string>
                        </value>
                      </member>
                    </struct>
                  </value>
                </member>
                <member>
                  <name>SoftLayer_User_CustomerInitParameters</name>
                  <value>
                    <struct>
                      <member>
                        <name>id</name>
                        <value>
                          <int>$USERID</int>
                        </value>
                      </member>
                    </struct>
                  </value>
                </member>
                <member>
                  <name>SoftLayer_ObjectMask</name>
                  <value>
                    <struct>
                      <member>
                        <name>mask</name>
                        <value>
                          <string>
                            mask[username;apiAuthenticationKeys]
                        </string>
                        </value>
                      </member>
                    </struct>
                  </value>
                </member>
              </struct>
            </value>
          </member>
        </struct>
      </value>
    </param>
  </params>
</methodCall>
```