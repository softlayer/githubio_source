---
title: "create_account_and_api_key.rb"
description: "create_account_and_api_key.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
    - "SoftLayer_Brand"
    - "SoftLayer_User_CustomerInitParameters"
tags:
    - "brands"
---


```
# Creates new account and create API key for that account
#
# The script creates a new account using the createCustomerAccount() method,
# then the script will create the API key for that account, in order to achieve
# that goal it is necessary to make soap request because in oder to create
# the API key we need to call the method addApiAuthenticationKey() using the
# the credentials of the new account as we do not have that information we are
# calling the method using impersonation.
# For perform the impersonation we need the userId and the token for the authentication.
# For more details please see below.
#
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/addApiAuthenticationKey
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getApiAuthenticationKeys
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getOwnedBrands
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account/
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Brand/
# http://sldn.softlayer.com/reference/services/SoftLayer_Brand
# http://sldn.softlayer.com/reference/services/SoftLayer_Brand/createCustomerAccount
# http://sldn.softlayer.com/reference/services/SoftLayer_Brand/getUsers
# http://sldn.softlayer.com/reference/services/SoftLayer_Brand/getToken
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc.<sldn@softlayer.com>
require 'softlayer_api'
require 'pp'

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'
ENDPOINT = 'set me'

# Declaring the API client to use the SoftLayer_Virtual_Guest API service
client = SoftLayer::Client.new(
  username: USERNAME,
  api_key: API_KEY,
  endpoint_url: ENDPOINT
)

brand_service = client.service_named('SoftLayer_Brand')
account_service = client.service_named('SoftLayer_Account')

begin
  # Getting the brand for our account
  # the account could belong to several brands
  # you need to select one brand for the new account.
  brands = account_service.getOwnedBrands

  # Creating an SoftLayer_Account object which contains the data
  # of our new account.
  account_template = {
    'address1' => '8200 Warden Ave',
    'city' => 'Markham',
    'companyName' => 'IBM Bluemix Dedicated',
    'email' => 'email@softlayer.com',
    'firstName' => 'FirstName',
    'lastName' => 'Surename',
    'officePhone' => 'number',
    'postalCode' => 'L6G 1C7',
    'state' => 'TX',
    'brandId' => brands[0]['id'],
    'country' => 'CA'
  }

  # Creating the new account
  new_account = brand_service.createCustomerAccount(account_template)

  # Looking for the master user for the new account
  new_master_user = nil
  users = brand_service.object_with_id(brands[0]['id']).getUsers
  users.each do |user|
    if user['accountId'] == new_account['id']
      new_master_user = user
      break
    end
  end

  # Getting the token
  token = brand_service.object_with_id(brands[0]['id']).getToken(new_master_user['id'])

  print token # This is the token you need to send to the SOAP request
  print '  '
  print new_master_user['id'] # This is the userId you need to send to the SOAP request

rescue StandardError => exception
  puts "Unable to create the new account : #{exception}"
end

# Here call the soap methods

=begin
This is a soap example to create the API key to the account.
It will create the API key for the master account of the new account.
In case the master account already has an API key the request will return an error.
Please replace the values $TOKEN and $USERID

<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://api.service.softlayer.com/soap/v3/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <SOAP-ENV:Header>
    <ns1:clientLegacySession>
      <userId>$USERID</userId>
      <authToken>$TOKEN</authToken>
    </ns1:clientLegacySession>
    <ns1:SoftLayer_User_CustomerInitParameters>
      <id>$USERID</id>
    </ns1:SoftLayer_User_CustomerInitParameters>
  </SOAP-ENV:Header>
  <SOAP-ENV:Body>
    <ns1:addApiAuthenticationKey/>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

You Also can execute this SOAP request to get the APIKey of the master account
Note: The user should already has the APIKey created

<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://api.service.softlayer.com/soap/v3/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <SOAP-ENV:Header>
    <ns1:clientLegacySession>
      <userId>$USERID</userId>
      <authToken>$TOKEN</authToken>
    </ns1:clientLegacySession>
    <ns1:SoftLayer_User_CustomerInitParameters>
      <id>$USERID</id>
    </ns1:SoftLayer_User_CustomerInitParameters>
  </SOAP-ENV:Header>
  <SOAP-ENV:Body>
    <ns1:getApiAuthenticationKeys/>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

=end

```
