---
title: "get_quote_details.rb"
description: "get_quote_details.rb"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "quote"
---


```
#
# Retrieves an account's quote information.
#
# This script retrieves the data presented in the SoftLayer Customer Portal's
# (https://control.softlayer.com/account/quotes) using an API call to SoftLayer_Account::getQuotes method.
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Account
# http://sldn.softlayer.com/reference/services/SoftLayer_Account/getQuotes
# @License: http://sldn.softlayer.com/article/License
# @Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
#

require 'rubygems'
require 'softlayer_api'

# We can set the default client to be our client and that way
# we can avoid supplying it later
SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'
client = SoftLayer::Client.new(username: SL_API_USERNAME, api_key: SL_API_KEY)

# grab a list of all the quotes on the account.
quotes = client['Account'].getQuotes
begin
  if quotes.any?
    # Print the table headers
    print "+------------+---------------------------+------------+---------------------------+---------------------------+---------------------------+\n"
    print "| Quote ID   | Name                      | Status     | Note                      | Create Date               | Expiration Date           |\n"
    print "+------------+---------------------------+------------+-------------------------------------------------------+---------------------------+\n"
    quotes.each do |quote|
      printf('| %-10s ', quote['id'])
      printf('| %-25s ', quote['name'])
      printf('| %-10s ', quote['status'])
      printf('| %-25s ', quote['publicNote'])
      printf('| %-10s ', quote['createDate'])
      printf("| %-25s |\n", quote['expirationDate'])
    end
  end
  print "+------------+---------------------------+------------+-------------------------------------------------------+---------------------------+\n"
rescue => error_reason
  puts error_reason
end

```
