---
title: "reload_os.pl"
description: "reload_os.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
tags:
    - "baremetalservers"
---


```perl
# Reload servers from a list of IPs
#
# This script looks for a server with a determinate IP address and reloads
# the Operative System with another one.
#
# It makes a single call to the reloadOperatingSystem() method in the
# SoftLayer_Hardware_Server API service
#
# Important manual pages:
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/findByIpAddress
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/reloadOperatingSystem
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# The ip addresses you wish to reload
my @ips_to_reload = ('1.1.1.1', '2.2.2.2');

# The new OS you wish to load
my $new_os_to_load = 'CentOS 5.x - Minimal Install (64 bit)';

# Declaring a new API service objects for:
my $hardware_server_service = SoftLayer::API::SOAP->new('SoftLayer_Hardware_Server', undef, $username, $key);

# Adding an object mask to retrieve our prices related to the servers
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# for a list of the relational properties you can retrieve along with hardware.
my $object_mask = "mask[billingItem[package[items[prices]]]]";

# Setting the object mask to our hardwareServerService
$hardware_server_service->setObjectMask($object_mask);

# The list of servers to reload
my %servers_to_reload;

# We are looking for the server with the specified IP addresses
# and the price for the new OS to load
for my $ip_to_reload (@ips_to_reload) {
    my $server = $hardware_server_service->findByIpAddress($ip_to_reload);
    if ($server->fault) {
        die 'Unable to get the server. ' . $server->faultstring;
    }
    $servers_to_reload{$ip_to_reload}{'id'} = $server->result->{'id'};
    $items = $server->result->{'billingItem'}->{"package"}->{"items"};
    for my $i (0 .. $#{$items}) {
        if ($items->[$i]->{'description'} eq $new_os_to_load) {
            $servers_to_reload{$ip_to_reload}{'priceId'} = $items->[$i]->{'prices'}->[0]->{'id'};
            last;
        }
    }
}

# We are calling the reloadOperatingSystem for the desired servers
for my $ip_to_reload (@ips_to_reload) {
    my $config = {
       'itemPrices' => [
           {
               'id' => $servers_to_reload{$ip_to_reload}{'priceId'}
           }
       ]
    };
    $hardware_server_service->setInitParameter($servers_to_reload{$ip_to_reload}{'id'});
    my $reload = $hardware_server_service->reloadOperatingSystem('FORCE', $config);
    print ($reload);
}

```
