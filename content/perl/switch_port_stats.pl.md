---
title: "switch_port_stats.pl"
description: "switch_port_stats.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Hardware_Server"
    - "SoftLayer_Container_Network_Port_Statistic"
    - "SoftLayer_NetworkComponent"
    - "SoftLayer_Account"
    - "SoftLayer_Network_Component"
tags:
    - "vlans"
---


```perl
# Retrieve a list of switch port statistics for a server's network interfaces.
# 
# This script makes a single call to the getPortStatistics() method in the
# SoftLayer_Network_Component API service
# for each of a server's network components to query port statistics for that
# interface from SoftLayer's switches. Port statistics are modeled by the
# SoftLayer__Container_Network_Port_Statistic data type
# See below for more details.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_NetworkComponent/getPortStatistics
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Network_Port_Statistic
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
 
use lib 'softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use JSON;
use Data::Dumper;
use strict;
 
# Your SoftLayer API username and key.
my $api_username = 'set me';
my $api_key = 'set me';
 
# Your server's id. Call the getHardware() method in the SoftLayer_Account API
# service (http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware)
# to get a list of your account's hardware records.
my $server_id = 87165;
 
# Declaring a new API service object for the SoftLayer_Hardware_Server API
# service.
my $client = SoftLayer::API::SOAP->new('SoftLayer_Hardware_Server', $server_id, $api_username, $api_key);
 
# Switchport statistics are measured off the server's network components. Use
# an object mask to network component records along with our server record.
$client->setObjectMask({
    'networkComponents' => {},
});
 
# Making the call to retrieve our hardware record. Once we have that we can query
# the server's network components.
my $server = $client->getObject();
 
# If there was an error returned from the SoftLayer API then die out with the
# error message.
if ($server->fault) {
    die "Unable to retrieve server record. " . $server->faultstring;
}
 
# Separating our network components for easier processing later.
$server = $server->result;
my $network_components = $server->{networkComponents};
 
# Printing out a simple report header.
print "\nSwitchport statistics for " . $server->{fullyQualifiedDomainName} . "\n\n";
 
# Looping through our server's network components. For each NIC make a call to the
# SoftLayer_Network_Component API service method getPortStatics() to get a list
# of switchport statistics retrieved from the switch on the other side of your
# NIC. Print a simple report per NIC.
for my $i (0 .. $#{$network_components}) {
    my $component = $network_components->[$i];
 
    # Skiping the management network component.
    if ($component->{name} eq 'mgmt') {
        next;
    }
 
    # It's all right to redeclare your API object.
    $client = SoftLayer::API::SOAP->new('SoftLayer_Network_Component', $component->{id}, $api_username, $api_key);
 
    # Retrieve switchport statistics for the NIC.
    my $stats = $client->getPortStatistics();
 
    # Make sure we didn't run into an error.
    if ($stats->fault) {
        die "Unable to retrieve switchport statics for " . $component->{name} . $component->{port} . ". " . $stats->faultstring;
    }
 
    # Make boolean up/down responses easier to read.
    $stats = $stats->result;
    $stats->{administrativeStatus} = ($stats->{administrativeStatus} eq '1') ? 'Up' : 'Down';
    $stats->{operationalStatus} = ($stats->{operationalStatus} eq '1') ? 'Up' : 'Down';
 
    # Print our port's statistics report.
    print <<EOT;
Statistics for $component->{name}$component->{port} ($component->{primaryIpAddress})
Administrative status:        $stats->{administrativeStatus}
Operational status:           $stats->{operationalStatus}
MTU:                          $stats->{maximumTransmissionUnit}
Inbound octets (from server): $stats->{inOctets}
Outbound octets (to server):  $stats->{outOctets}
Inbound unicast packets:      $stats->{inUnicastPackets}
Outbound unicast packets:     $stats->{outUnicastPackets}
Inbound discarded packets:    $stats->{inDiscardPackets}
Outbound discarded packets:   $stats->{outDiscardPackets}
Inbound error packets:        $stats->{inErrorPackets}
Outbound error packets:       $stats->{outErrorPackets}

EOT
}

```
