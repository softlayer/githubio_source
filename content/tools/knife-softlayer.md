---
title: "SoftLayer Knife"
description: "A Chef Knife plugin for launching, bootstrapping, and managing compute instances in the IBM SoftLayer cloud."
date: "2017-07-17"
tags:
    - "tools"
---


# [knife-softlayer](https://github.com/softlayer/knife-softlayer)

## Configuration
Add your SoftLayer username and API key to your `knife.rb` file.

```ruby
log_level                :info
log_location             STDOUT
node_name                'node'
client_key               '/path/to/key.pem'
validation_client_name   'some-validator'
validation_key           '/path/to/validator.pem'
chef_server_url          'https://example.com/organizations/org'
syntax_check_cache_path  '/path/to/syntax_check_cache'
knife[:softlayer_username] = "<SOFTLAYER USERNAME>"
knife[:softlayer_api_key]  = "<SOFTLAYER API KEY>"
```

## Usage

See `knife softlayer --help` for more information.

EXAMPLES:


```bash
# look at some options
user@local> knife softlayer flavor list [--all]
```

```bash
# the minimum number of pieces of flare
user@local> knife softlayer server create --hostname test --domain example.com --flavor tiny
```

```bash
# being sort of specific about things
user@local> knife softlayer server create -H test -D example.com \
--block-storage 0:25,2:100,5:1000 \ # device:GB, device:GB, ...
--network-interface-speed 1000 \
--cores 8 \
--ram 49152 \
--os-code REDHAT_6_64 \
--datacenter ams01 \
--node-name random-node-name \
--assign-global-ip <existingGlobalIpv4Address> \
--run-list 'recipe[apt],recipe[git],recipe[rbenv],recipe[memcached],recipe[redis]'