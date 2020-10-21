---
title: "Bandwidth"
description: "Working with bandwidth data, including graphs."
date: "2017-11-23"
classes: 
    - "SoftLayer_Container_Bandwidth_GraphOutputs"
    - "SoftLayer_Metric_Tracking_Object"
tags:
    - "bandwidth"
---

## Bandwidth Graph

```perl
# Retrieve a bandwidth graph for a single server.
#
# Retrieving a bandwidth graph for a single server for an arbitrary start and
# end date, specifying graph size and other graphing options. We can do this
# with two calls to the SoftLayer API.
#
# Counter data such as bandwidth counters and CCI resource use are stored in
# a server's metric tracking object. Our first call retrieves that server's
# tracking object record. The second call is to the tracking object service
# which will generate a PNG image of our bandwidth graph.
#
# Important manual pages.
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
# http://sldn.softlayer.com/reference/services/SoftLayer_Metric_Tracking_Object/getBandwidthGraph
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Container_Bandwidth_GraphOutputs
# License <http://sldn.softlayer.com/article/License>
# Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# The id number of the server whose graph you wish to retrieve. Call the
# getHardware() method in the SoftLayer_Account API service to retrieve a list
# of the servers on your account.
my $server_id  = 153851;
# The date at which you wish to start graphing bandwidth.
my $start_date = '2010-10-1';
# The date at which you wish to end graphing bandwidth.
my $end_date = '2014-8-11';
# Whether to get a graph for 'public' or 'private' bandwidth usage.
my $graph_type = 'public';
# The height of the text in the bandwidth graph in pixels.
my $font_size = 8;
# The width of the graph to retrieve in pixels.
my $graph_width = 827;
my $graph_height = 273;
my $hide_time_zone = True;

# Creating a SoftLayer API client object
my $metric_tracking_object = SoftLayer::API::SOAP->new('SoftLayer_Metric_Tracking_Object', undef, $username, $key);
my $hardware_server = SoftLayer::API::SOAP->new('SoftLayer_Hardware_Server', undef, $username, $key);

$hardware_server->setInitParameter($server_id);
my $result = $hardware_server->getMetricTrackingObject();
if ($result->fault) {
  die 'Unable to retrieve hte metric tracking object: ' . $result->faultstring;
}
my $tracking_object = $result->result;

# getBandwidthGraph() returns a SoftLayer_Container_Bandwidth_GraphOutputs
# object. The contents of the bandwidth image is in $image->graphImage.
# From here you can write it to the file system, display it to a web
# browser, or run other functions on it.
$metric_tracking_object->setInitParameter($tracking_object->{id});
$result = $metric_tracking_object->getBandwidthGraph($start_date, $end_date, $graph_type, $font_size, $graph_width, $graph_height, $hide_time_zone);
if ($result->fault) {
  die 'Unable to retrieve bandwidth image. ' . $result->faultstring;
}
my $image = $result->result;
print ("Image retrieved!");

```


## Bandwidth Usage



```perl
# Retrieve a bandwidth usage for a list of  servers.
#
# The scripts returns the bandwidth usage from an arbitrary
# list of servers, the script makes a simple call to the
# Softlayer_Hardware_Server::getObject method using a object mask
# in order to get the bandwidth information.
#
# Important manual pages:
# http://sldn.softlayer.com/reference/services/SoftLayer_Hardware_Server/getObject
# http://sldn.softlayer.com/reference/datatype/SoftLayer_Hardware_Server/
#
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib '/path/to/client/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# The list of server that wish to see the bandwidth usage
my @server_ids = ( 153851, 166391 );

# Creating a SoftLayer API client object
my $hardware_server = SoftLayer::API::SOAP->new('SoftLayer_Hardware_Server', undef, $username, $key);

# Adding an object mask to retrieve our hardware' related items such as its
# host name and currentBillableBandwidthUsage. Object masks
# can retrieve any information related to your object. See
# http://sldn.softlayer.com/reference/datatypes/SoftLayer_Hardware_Server
# for a list of the relational properties you can retrieve along with hardware.
my $object_mask = 'mask[hostname,currentBillableBandwidthUsage]';
$hardware_server->setObjectMask($object_mask);

my $total = 0.0;
for my $server_id (@server_ids) {
    $hardware_server->setInitParameter($server_id);
    my $result = $hardware_server->getObject();
    if ($result->fault) {
        die 'Unable to get bandwidth data. ' . $result->faultstring;
    }
    my $bandwidth_data = $result->result;
    print ($bandwidth_data->{'hostname'} . ": " . $bandwidth_data->{'currentBillableBandwidthUsage'} . "GB" , "\n");
    $total = $total + $bandwidth_data->{'currentBillableBandwidthUsage'};
}

print ("Total :" . $total , "\n");

```
