---
title: "Password Auth"
description: "Authenticate to the API with a username + password instead of an API key. Might be useful if you want to GET the api key without logging in to the portal"
date: "2015-11-15"
classes:
    - "SoftLayer_Account"
tags:
    - "authentication"
---

```ruby
require 'softlayer_api' # Requires softlayer_api >= 3.2

# Create a client
client = SoftLayer::Client.with_password(
    username: 'change me', password: 'change me')

# Test our client
puts client['Account'].object_mask('mask[id, apiAuthenticationKeys]').
    getCurrentUser
```
