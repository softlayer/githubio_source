---
title: "SoftLayer_Container_Graph"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Graph"
---

# SoftLayer_Container_Graph
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Graph' >Datatype</a></li>
    </ul>
</div>

## Description 






<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
-----
[baseUnit]: #baseunit
#### [baseUnit]
base units associated with the graph.  
<span class="type-label">Type: </span>**string**

-----
[endDatetime]: #enddatetime
#### [endDatetime]
Graph range end datetime.  
<span class="type-label">Type: </span>**string**

-----
[height]: #height
#### [height]
The height of the graph image.  
<span class="type-label">Type: </span>**integer**

-----
[image]: #image
#### [image]
The graph image.  
<span class="type-label">Type: </span>**binary data**

-----
[interval]: #interval
#### [interval]
The graph interval in seconds.  
<span class="type-label">Type: </span>**integer**

-----
[metrics]: #metrics
#### [metrics]
Metric types associated with the graph.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Metric_Data_Type'>SoftLayer_Container_Metric_Data_Type[] </a>**

-----
[normalizeFlag]: #normalizeflag
#### [normalizeFlag]
Indicator to control whether the graph data is normalized.  
<span class="type-label">Type: </span>**binary data**

-----
[options]: #options
#### [options]
The options used to control the graph appearance.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Graph_Option'>SoftLayer_Container_Graph_Option[] </a>**

-----
[plots]: #plots
#### [plots]
A collection of graph plots.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Container_Graph_Plot'>SoftLayer_Container_Graph_Plot[] </a>**

-----
[returnImage]: #returnimage
#### [returnImage]
option to not return the image.  
<span class="type-label">Type: </span>**boolean**

-----
[startDatetime]: #startdatetime
#### [startDatetime]
Graph range start datetime.  
<span class="type-label">Type: </span>**string**

-----
[template]: #template
#### [template]
The name of the template to use; may be null.  
<span class="type-label">Type: </span>**string**

-----
[title]: #title
#### [title]
The title of the graph image.  
<span class="type-label">Type: </span>**string**

-----
[width]: #width
#### [width]
The width of the graph image.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

</div>


