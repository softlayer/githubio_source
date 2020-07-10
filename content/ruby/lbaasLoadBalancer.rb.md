---
title: "Working with Lbaas loadBalancer"
description: "A few examples on interacting with lbaas loadBalancer"

date: "2020-07-08"

classes: 
    - "SoftLayer_Network_LBaaS_LoadBalancer"    
tags:
    - "LBaaS_LoadBalancer"
---

[Lbaas_LoadBalancer](https://sldn.softlayer.com/reference/services/SoftLayer_Network_LBaaS_LoadBalancer/)

### LBaaS loadBalancer examples

#### Some examples use the most important methods. 

```ruby
require 'softlayer_api'
require 'json'

class LoadBalancer

  def initialize(username, apikey)
    client = SoftLayer::Client.new(username: username,
                                   api_key: apikey,)
    @loadBalancer_service = client['SoftLayer_Network_LBaaS_LoadBalancer']
  end

  def getAllObjects()
    return @loadBalancer_service.getAllObjects()
  end

  def cancelLoadBalancer(loadBalancerId, uuid)
    return @loadBalancer_service.object_with_id(loadBalancerId).cancelLoadBalancer(uuid)
  end

  def enableOrDisableDataaLogs(loadBalancerId, uuid, enable)
    return @loadBalancer_service.object_with_id(loadBalancerId).enableOrDisableDataLogs(uuid, enable)
  end

  def getDatacenter(loadBalancerId)
    return @loadBalancer_service.object_with_id(loadBalancerId).getDatacenter()
  end

  def getHealthMonitors(loadBalancerId)
    return @loadBalancer_service.object_with_id(loadBalancerId).getHealthMonitors()
  end

  def getL7Pools(loadBalancerId)
    return @loadBalancer_service.object_with_id(loadBalancerId).getL7Pools()
  end

  def getListenner(loadBalancerId)
    return @loadBalancer_service.object_with_id(loadBalancerId).getListenners()
  end

  def getLoadBalancer(loadBalancerId, uuid)
    return @loadBalancer_service.object_with_id(loadBalancerId).getLoadBalancer(uuid)
  end

  def getMembers(loadBalancerId)
    return @loadBalancer_service.object_with_id(loadBalancerId).getMembers()
  end
end

SL_API_USERNAME = 'set - me'
SL_API_KEY = 'set - me'
loadblancer = LoadBalancer.new(SL_API_USERNAME,SL_API_KEY)

# set with your uuid
uuid = "8187a40f-8cae-479b-b30f-395352a3c100" 
pp loadblancer.getAllObjects

pp loadblancer.getLoadBalancer(123456,uuid)

pp loadblancer.getMembers(123456)


```