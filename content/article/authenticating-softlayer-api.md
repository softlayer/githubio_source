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

A SOAP representation of the `authenticate` header looks like this:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://api.service.softlayer.com/soap/v3.1/">
  <SOAP-ENV:Header>
    <ns1:authenticate>
      <username>USERNAME</username>
      <apiKey>APIKEY</apiKey>
    </ns1:authenticate>
  </SOAP-ENV:Header>
  <SOAP-ENV:Body>
    <ns1:getObject></ns1:getObject>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

### XMLRPC

while it's XML-RPC counterpart looks like this:

```xml
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
```


### REST
With REST, you can simply use the HTTP Basic Authentication
`curl  -vvv -u $SL_USER:$SL_APIKEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getObject'`

## Generating Your SoftLayer API Key
There are two ways to generate an API access key, via the portal or by direct API calls. To generate your own API access key in the customer portal see this article: [Managing classic infrastructure API keys](https://cloud.ibm.com/docs/iam?topic=iam-classic_keys&locale=dk)

To generate an API access key via API calls invoke the [SoftLayer_User_Customer::addApiAuthenticationKey](https://softlayer.github.io/reference/services/SoftLayer_User_Customer/addApiAuthenticationKey) method in the SoftLayer_User_Customer service. To remove a user's API access key execute the [SoftLayer_User_Customer::removeApiAuthenticationKey](https://softlayer.github.io/reference/services/SoftLayer_User_Customer/removeApiAuthenticationKey) method in the same service. Be careful when removing API access keys. Removing these keys will remove that user's ability to use the SoftLayer API.

[Example](/python/manageUsers/)

### cloud.ibm.com API key
>*NOTE* when using a cloud.ibm.com key, your username when authenticating with the SL API will be LITTERALLY 'apikey', not your actual username.

- [Understanding API keys](https://cloud.ibm.com/docs/iam?topic=iam-manapikey#manapikey)
- [Managing user API keys](https://cloud.ibm.com/docs/iam?topic=iam-userapikey#userapikey)

```
✗ ibmcloud iam api-key-create  TEST-cgallo01 -d "A test api key"
Creating API key TEST-cgallo01 as cgallo@us.ibm.com...
OK
API key TEST-cgallo01 was created

Please preserve the API key! It cannot be retrieved after it's created.

Name          TEST-cgallo01
Description   A test api key
Created At    2020-02-07T22:05+0000
API Key       aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA
Locked        false
UUID          ApiKey-1c505b6d-9e81-4b87-b929-f9493c2dea63

✗ SL_USER=apikey
✗ SL_APIKEY=aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA
✗  curl -g -u $SL_USER:$SL_APIKEY  'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getObject.json?objectMask=mask[id]'
{"id":123456}
```

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
curl -s -u 'bx:bx' -k -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d "grant_type=urn:ibm:params:oauth:grant-type:passcode&passcode=$TOKEN&response_type=cloud_iam,ims_portal" https://iam.ng.bluemix.net/oidc/token
```

In the response, will be a data field call `ims_token` which will let you authenticate to the SoftLayer API until the token expires (which should also be in the returned data)


The REST endpoint doesn't support authenticating with tokens, but the MOBILE endpoint works, along with the SOAP/XML endpoints.

```
curl -u USERID:IMS_TOKEN 'https://api.softlayer.com/mobile/v3.1/SoftLayer_Account/getObject'
```

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

## Using the SoftLayer Python Library with IMS_TOKEN

The following is a short example of how to get an IMS_TOKEN, and use it to make API calls with the SoftLayer Python library.


```python
"""
Uses an IBM ID username/password to make SoftLayer API calls. 

Using this method, you MUST use the xmlrpc endpoint in your ~/.softlayer file
`endpoint_url = https://api.softlayer.com/xmlrpc/v3.1/`

To use a rest endpoint, you will ahve to use https://api.softlayer.com/mobile/v3.1/, 
which isn't supported by the softlayer python library
"""
 

from pprint import pprint as pp
import logging
import click
import requests
import json
import SoftLayer
from SoftLayer.auth import TokenAuthentication as TokenAuthentication

class example():
 
    def __init__(self, token, user, password):
        if token is not None:
            ims_token = self.get_ims_token_sso(token)
        else:
            ims_token = self.get_ims_token_password(user, password)
        authObject = TokenAuthentication(ims_token['ims_user_id'], ims_token['ims_token'])
        self.client = SoftLayer.create_client_from_env(auth=authObject)
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger
        # logger = logging.getLogger()
        # logger.addHandler(logging.StreamHandler())
   
    def debug(self):
        """
        Useful for printing out the exact API calls that were used. If using the rest transport, will print cure-able commands.
        """
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))
 

    def get_ims_token_sso(self, token):
        """
        For accounts controlled by SSO, use this method.
        """
        url = 'https://iam.ng.bluemix.net/oidc/token'
        payload = {
            'grant_type': 'urn:ibm:params:oauth:grant-type:passcode', 
            'passcode': token,
            'response_type': 'cloud_iam,ims_portal'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        result = requests.post(url, data=payload, auth=('bx','bx'), headers=headers)

        # This is what your token should look like.
        # Once you use an SSO token to get an IMS_TOKEN, it expires 
        # so I use this as an easy way to save the IMS token response.

        # test_token = {
        #     'access_token': 'REALLY LONG STRING GOES HERE',
        #     'expiration': 1550699632,
        #     'expires_in': 3600,
        #     'ims_token': 'ANOTHER-REALLY-LONG_TOKEN_THING',
        #     'ims_user_id': 244956,
        #     'refresh_token': 'REALLYLONGTOKENGOESHERE',
        #     'scope': 'ibm openid',
        #     'token_type': 'Bearer'
        # }
        # return test_token
        return json.loads(result.text)

    def get_ims_token_password(self, username, password):
        url = 'https://iam.ng.bluemix.net/oidc/token'
        payload = {
            'grant_type': 'password', 
            'username': username,
            'password': password,
            'response_type': 'cloud_iam,ims_portal'
        }
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json'
        }
        result = requests.post(url, data=payload, auth=('bx','bx'), headers=headers)
        pp(result.text)
        return json.load(result.text)

    def main(self):
        account = self.client.call('Account', 'getObject')
        pp(account)

@click.command()
@click.option('--sso', help='SSO token from https://iam-id-1.ng.bluemix.net/identity/passcode')
@click.option('--username', help='IBM Id Username')
@click.option('--password', help='IBM Id Password')
def main(sso=None, username=None, password=None):

    main = example(sso, username, password)
    main.main()
    # Uncomment this to print out the API calls made.
    main.debug()
 
if __name__ == "__main__":
    main()
```