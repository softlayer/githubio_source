---
title: "Working with CDN Network.rb"
description: "A few examples on interacting with CDN Network"

date: "2019-07-03"
classes: 
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping"    
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path"    
    - "SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge"    
tags:
    - "cdn"
---

### List CDN network

```ruby
require 'softlayer_api'
require 'awesome_print'

SL_API_USERNAME = 'Set me'
SL_API_KEY = 'Set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

cdnService = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping']

begin
  result = cdnService.listDomainMappings()
  ap result
rescue StandardError => error_reason
  puts "Unable to create the image #{error_reason}"
end
         
```

### list CDN origin path
 
```ruby
require 'softlayer_api'
require 'awesome_print'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY,
                               endpoint_url: ENDPOINT_URL)

cdnService = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path']

# Set with CDN unique id. 
uniqueId = "123456489"

begin
  result = cdnService.listOriginPath(uniqueId)
  ap result
rescue StandardError => error_reason
  puts "Unable to create the image #{error_reason}"
end
```

###  Detail CDN by UniqueId

```ruby
require 'softlayer_api'
require 'awesome_print'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

cdnService = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping']

# Set with CDN unique id. 
uniqueId = '1234567898'

begin
  result = cdnService.listDomainMappingByUniqueId(uniqueId)
  ap result
rescue StandardError => error_reason
  puts "Unable to create the image #{error_reason}"
end
```

### Create CDN Network

```ruby
require 'softlayer_api'
require 'awesome_print'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

cdnService = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping']

body_json = {
    "cname": "test41.cdnedge.bluemix.net",
    "domain": "www.tech23support.com",
    "httpPort": 80,
    "origin": "10.10.10.5",
    "originType": "HOST_SERVER",
    "vendorName": "akamai",
    "header": "www.test2.com",
    "path": "/test",
    "protocol": "HTTP"
}

begin
  result = cdnService.createDomainMapping(body_json)
  ap result
rescue StandardError => error_reason
  puts "Unable to create the image #{error_reason}"
end

```
### Create CDN Origin Path

```ruby
require 'softlayer_api'
require 'awesome_print'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

cdnService = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path']

# Set the  CDN uniqueId. 
body_json = {
    "certificateType": "SHARED_SAN_CERT",
    "httpPort": 80,
    "origin": "10.10.10.25",
    "originType": "HOST_SERVER",
    "vendorName": "akamai",
    "header": "www.test2.com",
    "path": "/test",
    "domain": "www.test23.com",
    "protocol": "HTTP",
    "performanceConfiguration": "General web delivery",
    "uniqueId": "123456789"
}

begin
  result = cdnService.createOriginPath(body_json)
  ap result
rescue StandardError => error_reason
  puts "Unable to create the image #{error_reason}"
end
```

### Delete CDN by uniqueID

```ruby
require 'softlayer_api'
require 'awesome_print'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

cdnService = client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping']

# Set with CDN unique id. 
uniqueId = "12345678912345"

begin
  # Calling the getObject method send the virtual guest id
  result = cdnService.deleteDomainMapping(uniqueId)
  ap result
rescue StandardError => error_reason
  puts "Unable to create the image #{error_reason}"
end
```

### Delete CDN origin path

```ruby
require 'softlayer_api'
require 'awesome_print'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

cdnService= client['SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path']

# Set with CDN unique id. 
uniqueId = '123456789123456'

begin
  # Calling the getObject method send the virtual guest id
  result = cdnService.deleteOriginPath(uniqueId)
  ap result
rescue StandardError => error_reason
  puts "Unable to create the image #{error_reason}"
end
```

### Purge CDN

```ruby
require 'softlayer_api'
require 'awesome_print'

SL_API_USERNAME = 'set me'
SL_API_KEY = 'set me'

client = SoftLayer::Client.new(username: SL_API_USERNAME,
                               api_key: SL_API_KEY)

cdnService= client['SoftLayer_Network_CdnMarketplace_Configuration_Cache_Purge']

# Set with CDN unique id and the path. 
uniqueId = '123456789123456789'
path = "/test"

begin
  result = cdnService.createPurge(uniqueId,path)
  ap result
rescue StandardError => error_reason
  puts "Unable to create the image #{error_reason}"
end
```