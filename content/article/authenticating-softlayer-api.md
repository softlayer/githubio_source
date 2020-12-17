---
title: "Authenticating to the SoftLayer API"
description: "Authenticating to the SoftLayer API"
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
---

# IBMid

IBMid is how access is managed across IBM's cloud platform. Basically it is the email and password you use to login to https://cloud.ibm.com . Once IBMid can have access to multiple accounts. For accessing Classic Infrastructure (AKA SoftLayer) services, this IBMid will have a SoftLayer user on each account they have access to. 


## IAM Documentation:
- [IAM API](https://cloud.ibm.com/apidocs/iam-identity-token-api)
- [API Keys for Services](https://cloud.ibm.com/docs/account?topic=account-iamapikeysforservices)
- [User Management](https://cloud.ibm.com/apidocs/user-management#list-users)


# [SoftLayer Username and API key](#softlayer-api) {#softlayer-api .anchor-link}

To authenticate with a SoftLaye username and APIkey, you will first need your accounts username. If you are using IBMid to authenticate, this is usually not your email address. The SoftLayer username will usually be in the form of `<ACCOUNT_ID>_<EMAIL_ADDRESS@email.com>`. 

In the portal, this username will also be your VPN username for this account. You can find this in the cloud console by going to 
> *Manage* -> *Access (IAM)* -> Users -> <select your user> -> VPN section


Next you will need your API key. This is under the "classic infrastructure" dropdown of the [apikeys](https://cloud.ibm.com/iam/apikeys) page. You can only have one classic infrastructure API key per user. Once created, it will not be displayed again, so make sure to write it down.

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

While it's XML-RPC counterpart looks like this:

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


# [cloud.ibm.com API key](#cloud-api) {#cloud-api .anchor-link}

On the [apikeys](https://cloud.ibm.com/iam/apikeys) page, simply create a new "IBM Cloud API key". These are different than the Classic Infrastructure api keys.

>*NOTE* when using a cloud.ibm.com key, your username when authenticating with the SL API will be LITTERALLY 'apikey', not your actual username.

- [Understanding API keys](https://cloud.ibm.com/docs/iam?topic=iam-manapikey#manapikey)
- [Managing user API keys](https://cloud.ibm.com/docs/iam?topic=iam-userapikey#userapikey)

If you have the [ibmcloud cli](https://cloud.ibm.com/docs/cli?topic=cli-getting-started) installed, you can also easily create a new key.

```bash
$> ibmcloud iam api-key-create  TEST-cgallo01 -d "A test api key"
Creating API key TEST-cgallo01 as cgallo@us.ibm.com...
OK
API key TEST-cgallo01 was created

Please preserve the API key! It cannot be retrieved after its created.

Name          TEST-cgallo01
Description   A test api key
Created At    2020-02-07T22:05+0000
API Key       aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA
Locked        false
UUID          ApiKey-1c505b6d-9e81-4b87-b929-f9493c2dea63
```

Once you have the key, you can easily make calls to api.softlayer.com with it as follows. Remember, your username here is litterally `apikey`, not your actual username.

```bash
$> SL_APIKEY=aAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaAaA
$>  curl -g -u apikey:$SL_APIKEY  'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getObject.json?objectMask=mask[id]'
{"id":123456}
```

# [Temporary API Token](#temp-token) {#temp-token .anchor-link}

It is possible to use the IBMid authentication service to make softlayer API calls. See [IAM Token API](https://cloud.ibm.com/apidocs/iam-identity-token-api) for more specific details.

### Get the ACCESS_TOKEN
For most users, you will need your username and password, send that to https://iam.cloud.ibm.com/identity/token, and you will be given a token that can be used to make SoftLayer(IMS) api calls.

```bash
IBMUSER=myemail@email.com
IBMPASS=123qweasdzxc
curl -s -u 'bx:bx' -k -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d "grant_type=password&response_type=cloud_iam,ims_portal&username=$IBMUSER&password=$IBMPASS" https://iam.cloud.ibm.com/identity/token
```

For users with an IBM email, you will need to use the SSO endpoint (the above example will also mention this if you try your username/password)

Tokens are retrieved from https://iam.cloud.ibm.com/identity/passcode
```bash
TOKEN=qwe124cxzv
curl -s -u 'bx:bx' -k -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d "grant_type=urn:ibm:params:oauth:grant-type:passcode&passcode=$TOKEN&response_type=cloud_iam,ims_portal" https://iam.cloud.ibm.com/identity/token
```

The result will be something like this:

```
{"access_token":"[PRIVATE DATA HIDDEN]","refresh_token":"[PRIVATE DATA HIDDEN]","token_type":"Bearer","expires_in":3600,"expiration":1608241172,"refresh_token_expiration":1610829572,"scope":"ibm openid"}
```

The `access_token` here will give you access to the default account you have selected, but if you have more than one account (or want an account from the non-default account), you will need to get a token for that specific account first.  For the below examples, we are going to set this token as the `TOKEN_HEADER` enviornment variable.

```bash
export TOKEN_HEADER="Authorization: Bearer zzzzzzzzzzzzzzzzzzzzzzzzzzaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasssssssssssssssssssssssssssssssdddddddddddddddddddddddddddddddddddddd"
```

### Listing Accounts

You'll need your account GUID, and IMS id to get that call `https://accounts.cloud.ibm.com/v1/accounts `.

Below is the example output, with only the important data included.

```bash
curl -H "$TOKEN_HEADER" https://accounts.cloud.ibm.com/v1/accounts | python -m json.tool

{
"total_results": 1,
"resources": [
  {
    "metadata": {
      "guid": "aaaa1fce09180aa9027ec1ad29c20c",  # GUID
      "url": "/v1/accounts/aaaa1fce09180aa9027ec1ad29c20c",
      "linked_accounts": [
        {
          "origin": "IMS",
          "id": "123456",  # IMS ID
          "url": "/v1/accounts/aaaa1fce09180aa9027ec1ad29c20c/IMS/accounts/123456"
        }
      ]
  },
  "entity": {
      "name": "My Account",
      "state": "ACTIVE",
      "primary_owner": {
          "ibmid": "me@us.ibm.com",
      },
    }
  }
]
}

```

With that GUID, you can refresh your token for a new one.

```bash
REFRESH_TOKEN="zzzzzzzzzzzzzzzzzzzzzzzzzzaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasssssssssssssssssssssssssssssssdddddddddddddddddddddddddddddddddddddd"
IMS_ID="123456"
ACCOUNT_GUID="aaaa1fce09180aa9027ec1ad29c20c"
curl -s -u 'bx:bx' -k -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d "account=$ACCOUNT_GUID&grant_type=refresh_token&ims_account=$IMS_ID&refresh_token=$REFRESH_TOKEN&response_type=cloud_iam" https://iam.cloud.ibm.com/identity/token
```

That will give you a new access_token, you can then use for making SoftLayer API calls.


#### ACCESS_TOKEN

Once you have the access token, simply add set it as the `"Authorization: Bearer"` HTTP header.

```bash
curl -H "Authorization: Bearer zzzzzzzzzzzzzzzzzzzzzzzzzzaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasssssssssssssssssssssssssssssssdddddddddddddddddddddddddddddddddddddd" 'https://api.sotlayer.com/rest/v3.1/SoftLayer_Account/getObject'
```

There will also be a `refresh_token` which will only work to get you a new token.
