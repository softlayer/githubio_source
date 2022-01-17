---
title: "get_graph_data.pl"
description: "get_graph_data.pl"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Metric_Data_Type"
tags:
    - "monitoring"
---


```perl
# 
# Get the graph data from a monitoring agent
# 
# The script gets the CPU usage in a determinate date range
# for more reference see below.
# 
# Important manual pages.
# http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent
# http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getGraphData
# 
# License: http://sldn.softlayer.com/article/License
# Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
use lib 'C:/softlayerApis/perl/softlayer-api-perl-client-master/';
use SoftLayer::API::SOAP;
use Data::Dumper;

# Your SoftLayer API username and key.
my $username = 'set me';
my $key = 'set me';

# Creating an skeleton SoftLayer_Container_Metric_Data_Type object wich represent
# the methic data that we will get. 
my $metric_data_types = [
    bless({
        "summaryType" => "average",
        "keyName" => "CDM_CPU_USAGE",
        "name" => "cdm_cpu_usage_U3lzdGVt"
    },'slapi:SoftLayer_Container_Metric_Data_Type')
];

# The start date for the graph data
my $start_date = "2014-09-29T01:48:08.474Z";
# The end date for the graph data
my $end_date = "2014-09-29T01:53:08.474Z";
# The agent Id from where we want to get the graph data
# to get the monitor agents in your virtual guest
# call the SoftLayer_Virtual_Guest::getMonitoringAgents method
my $agent_id = 1448912;

# Creating a SoftLayer API client object
my $monitor_agent_service = SoftLayer::API::SOAP->new('SoftLayer_Monitoring_Agent', undef, $username, $key);

# Setting the init Parameter
$monitor_agent_service->setInitParameter($agent_id);

my $result = $monitor_agent_service->getGraphData($metric_data_types, $start_date, $end_date);
if ($result->fault) {
    die 'Unable to get the graph data. ' . $result->faultstring;
}
print Dumper($result->result);

```
