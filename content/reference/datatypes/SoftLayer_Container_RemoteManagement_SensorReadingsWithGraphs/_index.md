---
title: "SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs"
description: "The SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs contains the raw data retrieved from a server's remote... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs"
---

# SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Container_RemoteManagement_SensorReadingsWithGraphs contains the raw data retrieved from a server's remote management card.  Along with the raw data, two sets of graphs will be returned.  One set of graphs is used to display, using thermometer graphs, the temperatures (cpu(s) and system) retrieved from the management card.  The other set is used to display speed for each of the server's fans. 





<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[rawData]: #rawdata
#### [rawData]
The raw data returned from the server's remote management card.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_RemoteManagement_SensorReading'>SoftLayer_Container_RemoteManagement_SensorReading[] </a>**


</div>
<div class="prop-row">

-----
[speedGraphs]: #speedgraphs
#### [speedGraphs]
The graph(s) to display the server's fan speeds.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_RemoteManagement_Graphs_SensorSpeed'>SoftLayer_Container_RemoteManagement_Graphs_SensorSpeed[] </a>**


</div>
<div class="prop-row">

-----
[temperatureGraphs]: #temperaturegraphs
#### [temperatureGraphs]
The graph(s) to display the server's cpu(s) and system temperatures.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_RemoteManagement_Graphs_SensorTemperature'>SoftLayer_Container_RemoteManagement_Graphs_SensorTemperature[] </a>**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


