---
title: "CPU and Memory usage in Virtual servers"
description: "How the portal page retrieves the memory and cpu usage"
date: "2020-03-30"
classes: 
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Metric_Tracking_Object"
tags:
    - "metric"
    - "virtualguest"
---


```php
<?php
require_once(dirname(__FILE__) . '/SoftLayer/SoapClient.class.php');

class VirtualServers
{
    public $client_virtual;
    public $metric_trackingId;
    public $client_metric;

    function __construct($client_virtual,$client_metric)
    {
        $this->client_virtual = $client_virtual;
        $this->client_metric = $client_metric;
    }

    function _calculate_averages($records)
    {
        $total = array();
        $total_counter = array();
        foreach ($records as $item) {
            if (!isset($total[$item->type])) {
                $total[$item->type] = $item->counter;
                $total_counter[$item->type] = 1;
            } else {
                $item_counter_total = $total[$item->type] + $item->counter;
                $total[$item->type] = $item_counter_total;
                $total_counter[$item->type] = $total_counter[$item->type] + 1;
            }
        }

        $average = array();
        foreach ($total as $key => $value) {
            $usage_counter = $value / $total_counter[$key];
            $average[$key] = $usage_counter;
        }
        return $average;
    }

    function get_cpu_usage($start_date, $end_date)
    {
        $guest = $this->client_virtual->getObject();

        $valid_types = array();
        for ($i = 0; $i < $guest->startCpus; $i++) {
            $valid_type = (object)array("keyName" => "CPU" . strval($i),
                "name" => "cpu" . strval($i), "summaryType" => "max");
            $valid_types[] = $valid_type;
        }

        $cpu_record = $this->client_metric->getSummaryData($start_date, $end_date, $valid_types, 3600);
        return $cpu_record;
    }

    function get_memory_usage($start_date, $end_date)
    {
        //build the SoftLayer_Container_Metric_Data_Type array
        $valid_types = [(object)array("keyName" => "MEMORY_USAGE", "summaryType" => "max", "unit" => "GB")];

        $memory_record = $this->client_metric->getSummaryData($start_date, $end_date, $valid_types, 3600);
        return $memory_record;
    }
    
    function memory_graph($start_date, $end_date, $file_path)
    {
        $memory = $this->client_virtual->getMemoryMetricImageByDate(date('Y-m-d H:i:s', strtotime($start_date)),
        date('Y-m-d H:i:s', strtotime($end_date)));
        
        $memory_image = $memory->graphImage;
        $data = base64_decode(preg_replace('#^data:image/\w+;base64,#i', '',
        base64_encode($memory_image)));
        file_put_contents($file_path, $data);
    }
        
    function cpu_graph($start_date, $end_date, $file_path, $cpuType)
    {
        $usage_cpu = $this->client_metric->getGraph(date('Y-m-d H:i:s', strtotime($start_date)),
        date('Y-m-d H:i:s', strtotime($end_date)),$cpuType );
        
        $cpu_image = $usage_cpu->graphImage;
        $data = base64_decode(preg_replace('#^data:image/\w+;base64,#i', '',
        base64_encode($cpu_image)));
        file_put_contents($file_path, $data);
    }
}

/**
 * Set your SoftLayer API username and key.
 */
$apiUsername = 'set me';
$apiKey = 'set me';

$guestId = 55984279;
$start_date = "2020-03-04T00:00:00";
$end_date = "2020-04-09T23:59:59";
// change the path data for the path you want.
$file_path_memory = 'C:\\myfileMemory.png';
$file_path_cpu = 'C:\\myfileCpu.png';

$client_virtual = \SoftLayer\SoapClient::getClient('SoftLayer_Virtual_Guest', $guestId, $apiUsername, $apiKey);
$metric_trackingId = $client_virtual->getMetricTrackingObjectId();
$client_metric = \SoftLayer\SoapClient::getClient('SoftLayer_Metric_Tracking_Object', $metric_trackingId, $apiUsername, $apiKey);
$objectMask = new \SoftLayer\Common\ObjectMask();
$objectMask->id;
$objectMask->startCpus;
$client_virtual->setObjectMask($objectMask);

$virtual_server = new VirtualServers($client_virtual, $client_metric);
$cpu_records = $virtual_server->get_cpu_usage($start_date, $end_date);
$cpu_averages = $virtual_server->_calculate_averages($cpu_records);
$memory_records = $virtual_server->get_memory_usage($start_date, $end_date);
$memory_averages = $virtual_server->_calculate_averages($memory_records);

// print records and cpu usage
echo ("CPU USAGE RECORDS:\n");
foreach ($cpu_records as $record){
    print_r($record);
}

// print("\nCPU AVERAGES:")
echo ("\nCPU AVERAGES:\n");
foreach ($cpu_averages as $key => $value){
    print_r($key . ": " . strval($value)."\n");
}

// cpu graph
$cpuType = array();
foreach ($cpu_averages as $key => $value){
    $cpuType[] = $key;
}

$virtual_server->cpu_graph($start_date, $end_date, $file_path_cpu, $cpuType);

// print records and memory usage
echo ("\nMEMORY USAGE RECORDS:\n");
foreach ($memory_records as $record){
    print_r($record);
}

// # there is only 1 memory and its value must be divided by 2^30 to convert it to GB
print_r("\nMEMORY AVERAGE: " . strval($memory_averages['memory_usage']/(2**30)) . " GB");


// memory graph
$virtual_server->memory_graph($start_date, $end_date, $file_path_memory);

```
