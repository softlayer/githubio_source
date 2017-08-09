title: "Show user accounts with and without two-factor enabled"
description: "Get a list of users with two-factor authentication enabled/disabled. "
date: "2017-08-09"
classes: 
    - "SoftLayer_Account"
tags:
    - "objectFilter"
    - "objectMask"
---


To get a list of users *with* Two-Factor authentication enabled.

```ruby 

=begin
@author Ryan Tiffany
=end

require 'softlayer_api' 
require 'pp' 

# Connect to SoftLayer
client = SoftLayer::Client.new(:timeout => 120)

mask = 'mask[id,username,firstName,lastName,externalBindingCount,externalBindings]'

theFilter = {
'users' => {
	'externalBindings' => {
		'active' => {
			'operation' => '1'
		}}}
}

getUsers = client['SoftLayer_Account'].getUsers(filter=theFilter, mask=mask)
pp getUsers
```


To get a list of users *without* Two-Factor authentication enabled.

```ruby 
=begin
@author Ryan Tiffany
=end

require 'softlayer_api' 
require 'pp' 

# Connect to SoftLayer
client = SoftLayer::Client.new(:timeout => 120)

mask = 'mask[id,username,firstName,lastName,externalBindingCount,externalBindings]'

theFilter = {
'users' => {
	'externalBindings' => {
		'active' => {
			'operation' => '0'
		}}}
}

getUsers = client['SoftLayer_Account'].getUsers(filter=theFilter, mask=mask)
pp getUsers
```