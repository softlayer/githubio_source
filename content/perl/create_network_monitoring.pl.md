---
title: "create_network_monitoring.pl"
description: "create_network_monitoring.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Network_Monitor_Version"
tags:
    - "monitoring"
---


```
# Create network monitoring
# 
# The script creates a monitoring network with Service ping
# in a determinate IP address
# 
# Important manual pages
# http://sldn.softlayer.com/reference/services/SoftLayer_Network_Monitor_Version1_Query_Host
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Network_Monitor_Version1_Query_Host
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# The Id of the server you wish to mointor
my $server_id = 7377448;
 
# Id of the query type which can be found with SoftLayer_Network_Monitor_Version1_Query_Host_Stratum/getAllQueryTypes.
# This exmaple uses SERVICE PING: Test ping to address, will not fail on slow server response because high latency or
# high server load
my $query_type_id = 1;
 
# IP address on the previsously defined server to monitor
my $ip_address = '10.120.63.196';

# Creating a SoftLayer API client object
my $user_customer_notificiation = SoftLayer::API::SOAP->new('SoftLayer_Network_Monitor_Version1_Query_Host', undef, $username, $key);

# Defining the SoftLayer_Network_Monitor_Version1_Query_Host templateObject.
# the template object will create a monitoring network for a virtual guest
# to create the  the monitoring network in a hardware change "guestId" by "hardwareId"
my $new_monitor = bless({
    'guestId' => $server_id,
    'queryTypeId' => $query_type_id,
    'ipAddress'=> $ip_address
},'slapi:SoftLayer_Network_Monitor_Version1_Query_Host');

my $result = $user_customer_notificiation->createObject($new_monitor);
if ($result->fault) {
    die 'Unable to create network monitoring. ' . $result->faultstring;
}
print Dumper($result->result);

```
