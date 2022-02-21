---
title: "GetGraphData.php"
description: "GetGraphData.php"
date: "2017-11-23"
classes: 
    - "SoftLayer_Monitoring_Agent"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Container_Metric_Data_Type"
tags:
    - "monitoring"
---


```php
<?php
/**
 * Example to get the graph data from a monitoring agent
 * The script gets the CPU usage in a determinate date range
 * 
 * Important manual pages:
 * http://sldn.softlayer.com/reference/services/Softlayer_Monitoring_Agent
 * http://sldn.softlayer.com/reference/services/SoftLayer_Monitoring_Agent/getGraphData
 * 
 * License <http://sldn.softlayer.com/article/License>
 * Author SoftLayer Technologies, Inc. <sldn@softlayer.com>
 * 
 */
require_once ('Softlayer/SoapClient.class.php');

# Your SoftLayer API username and key.
$apiUsername = 'set me';
$apiKey = 'set me';

# Creating an skeleton SoftLayer_Container_Metric_Data_Type object which represent
# the metric data that we will get. 
$metricDataTypes = array();
$metricDataType = new stdClass();
$metricDataType->summaryType = "average";
$metricDataType->keyName = "CDM_CPU_USAGE";
$metricDataType->name = "cdm_cpu_usage_U3lzdGVt";
$metricDataTypes[] = $metricDataType;


# The start date for the graph data
$starDate = "2014-09-29T01:48:08.474Z";
# The end date for the graph data
$endDate = "2014-09-29T01:53:08.474Z";
# The agent ID from where we want to get the graph data
# to get the monitor agents in your virtual guest
# call the SoftLayer_Virtual_Guest::getMonitoringAgents method
$agentId = 1448912;

$monitorAgentService = Softlayer_SoapClient::getClient('SoftLayer_Monitoring_Agent', null, $apiUsername, $apiKey);

# Setting the init Parameter
$monitorAgentService->setInitParameter($agentId);


try {
    $result = $monitorAgentService->getGraphData($metricDataTypes, $starDate, $endDate);
    print_r($result);
} catch (Exception $e) {
    echo 'Unable to get the graph data: ' . $e->getMessage();
}

?>

```
