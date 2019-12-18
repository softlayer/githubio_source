---
title: "SoftLayer_Network_CdnMarketplace_Metrics"
description: "This Service class will describe in detail each Simple Object Access Protocol (SOAP) API call used in the Content Delive... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_CdnMarketplace_Metrics"
---
# SoftLayer_Network_CdnMarketplace_Metrics
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_CdnMarketplace_Metrics' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_CdnMarketplace_Metrics' >Datatype</a></li>
    </ul>
</div>

## Description
This Service class will describe in detail each Simple Object Access Protocol (SOAP) API call used in the Content Delivery Network (CDN) metrics. These APIs will allow callers to collect metrics for the CDN service. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [getCustomerInvoicingMetrics](/reference/services/SoftLayer_Network_CdnMarketplace_Metrics/getCustomerInvoicingMetrics)
Get the static & dynamic bandwidth and mapping hits of predetermined statistics for direct display (no graph) for a customer's account over a given period of time. Frequency can be 'day', 'aggregate'. If the value 'day' is specified for Frequency, return data will be ordered based on startDate to endDate, and if the value 'aggregate' is specified for Frequency, aggregated data from startDate to endDate will be returned. There is a delay within 3 days(including today) for fetching the metrics data. 

#### [getCustomerUsageMetrics](/reference/services/SoftLayer_Network_CdnMarketplace_Metrics/getCustomerUsageMetrics)
Get the total number of predetermined statistics for direct display (no graph) for a customer's account over a given period of time 

#### [getMappingBandwidthByRegionMetrics](/reference/services/SoftLayer_Network_CdnMarketplace_Metrics/getMappingBandwidthByRegionMetrics)
Get the total number of predetermined statistics for direct display (no graph) for a customer's account over a given period of time 

#### [getMappingBandwidthMetrics](/reference/services/SoftLayer_Network_CdnMarketplace_Metrics/getMappingBandwidthMetrics)
Get the amount of edge hits for an individual mapping. 

#### [getMappingHitsByTypeMetrics](/reference/services/SoftLayer_Network_CdnMarketplace_Metrics/getMappingHitsByTypeMetrics)
Get the total number of hits at a certain frequency over a given range of time. Frequency can be day, week, and month where each interval is one plot point for a graph. Return Data must be ordered based on startDate, endDate and frequency 

#### [getMappingHitsMetrics](/reference/services/SoftLayer_Network_CdnMarketplace_Metrics/getMappingHitsMetrics)
Get the total number of hits at a certain frequency over a given range of time per domain mapping. Frequency can be day, week, and month where each interval is one plot point for a graph. Return Data will be ordered based on startDate, endDate and frequency. 

#### [getMappingUsageMetrics](/reference/services/SoftLayer_Network_CdnMarketplace_Metrics/getMappingUsageMetrics)
Get the total number of predetermined statistics for direct display for the given mapping 

</div>

