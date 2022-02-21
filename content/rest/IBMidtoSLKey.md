---
title: "Use IBMid to get SL api key"
description: "For accounts that use IBMid, this script can be used to pull down the SoftLayer API key directly."

date: "2017-03-02"
classes: ["SoftLayer_User_Customer"]
tags:
  - "getobject"
  - "ibmid"
  - "objectmask"
---


```
#!/bin/bash
# Parameters: <IBMid username> <IBMid password> <SL Account number (optional)>
# Requires: curl, jq and xmllint installed
creds=$(curl -s -u 'bx:bx' -k -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' -d "grant_type=password&response_type=cloud_iam,ims_portal&username=${1}&password=${2}&ims_account=${3}" https://iam.ng.bluemix.net/oidc/token)

ims_token=$(echo $creds | jq -r '.ims_token')
ims_user_id=$(echo $creds | jq -r '.ims_user_id')
echo $creds > creds.json

# Get api key over xmlrpc
curl -s -X POST -d "<?xml version=\"1.0\" encoding=\"UTF-8\"?>
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
                          <int>$ims_user_id</int>
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
                          <string>$ims_token</string>
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
                          <int>$ims_user_id</int>
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
                          <string>mask[username;apiAuthenticationKeys.authenticationKey]</string>
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
</methodCall>" https://api.softlayer.com/xmlrpc/v3/SoftLayer_User_Customer > response.xml
export SL_USERNAME=$(cat response.xml | xmllint --xpath '(//params/param/value/struct/member/value/string/text())[1]' -)
export SL_API_KEY=$(cat response.xml | xmllint --xpath '(//params/param/value/struct/member/value/array/data/value/struct/member/value/string/text())[1]' -)

echo "SL_USERNAME: $SL_USERNAME"
echo "SL_API_KEY: $SL_API_KEY"

rm -f creds.json response.xml # comment out to debug
```
