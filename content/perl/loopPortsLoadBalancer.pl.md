---
title: "loopPortsLoadBalancer.pl"
description: "loopPortsLoadBalancer.pl"
date: "2018-04-25"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress"
tags:
    - "loadbalancers"
---


```perl
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
# Generate an API key at the SoftLayer Customer Portal:
# https://manage.softlayer.com/Administrative/apiKeychain
my $username = 'SL207819';
my $key = 'apikey_goes_here';

# Getting the load blancers in the account
#my $softLayerAccount = SoftLayer::API::SOAP->new('SoftLayer_Account', undef, $username, $key);
#my $result = $softLayerAccount->getAdcLoadBalancers();
#print Dumper($result->result);

# The load balancer ID 
my $loadBalancerID = 33184;

my $softLayerLoadBalancer = SoftLayer::API::SOAP->new('SoftLayer_Network_Application_Delivery_Controller_LoadBalancer_VirtualIpAddress', $loadBalancerID, $username, $key);
# setting an object mask to get more data from the load balancer such as virtualServer, serviceGroups, etc.
my $objectMask = "mask[virtualServers[serviceGroups[services]]]";
$softLayerLoadBalancer->setObjectMask($objectMask);
# getting the load balancer
my $result = $softLayerLoadBalancer->getObject();
my $loadbalancerObject = $result->result;
# storing the virtual servers in a variable
my $virtualServers = $loadbalancerObject->{virtualServers};
# loop the virtual servers in the load balancer
for my $j (0 .. $#{$virtualServers}) {
    my $virtualServer = $virtualServers->[$j];
    my $serviceGroups = $virtualServer->{serviceGroups};
    print ("virtualServerID : " . $virtualServer->{id} . "\n");
    print ("name : " . $virtualServer->{name} . "\n");
    print ("port : " . $virtualServer->{port} . "\n");
    # loop the service groups in the virtual servers
    for my $i (0 .. $#{$serviceGroups}) {
        my $serviceGroup = $serviceGroups->[$i];
        my $services = $serviceGroup->{services};
        print ("    serviceGroupID : " . $serviceGroup->{id} . "\n");
        print ("    name : " . $serviceGroup->{name} . "\n");
        print ("    routingMethodId : " . $serviceGroup->{routingMethodId} . "\n");
        print ("    routingTypeId : " . $serviceGroup->{routingTypeId} . "\n");
        print ("    timeout : " . $serviceGroup->{timeout} . "\n");
        # loop the services in the service group
        for my $h (0 .. $#{$services}) {
            my $service = $services->[$h];
            print ("        serviceID : " . $service->{id} . "\n");
            print ("        name : " . $service->{name} . "\n");
            print ("        notes : " . $service->{notes} . "\n");
            print ("        port : " . $service->{port} . "\n");
            print ("        status : " . $service->{status} . "\n");
            print ("        ipAddressId : " . $service->{ipAddressId} . "\n");
            print ("        enabled : " . $service->{enabled} . "\n");
        }
    }
    print ("\n");
    print ("\n");
}

#print Dumper($virtualServers);




```
