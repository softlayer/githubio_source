---
title: "SoftLayer_Hardware_Benchmark_Certification"
description: "The SoftLayer_Hardware_Benchmark_Certification data type contains general information relating to a single SoftLayer har... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Hardware"
classes:
    - "SoftLayer_Hardware_Benchmark_Certification"
---

# SoftLayer_Hardware_Benchmark_Certification
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Hardware_Benchmark_Certification' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Hardware_Benchmark_Certification' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Hardware_Benchmark_Certification data type contains general information relating to a single SoftLayer hardware benchmark certification document. 


### associatedMethods

*  [SoftLayer_Hardware_Benchmark_Certification::getObject](/reference/services/SoftLayer_Hardware_Benchmark_Certification/getObject )





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
[accountId]: #accountid
#### [accountId]
The internal identifier of the SoftLayer customer account associated with a benchmark certification result.  
<span class="type-label">Type: </span>**integer**

-----
[createDate]: #createdate
#### [createDate]
The date that a benchmark certification result was generated.  
<span class="type-label">Type: </span>**dateTime**

-----
[hardwareId]: #hardwareid
#### [hardwareId]
A benchmark certification results's associated hardware's internal identification number.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
Information regarding a benchmark certification result's associated SoftLayer customer account.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[hardware]: #hardware
#### [hardware]
Information regarding the piece of hardware on which a benchmark certification test was performed.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Hardware'>SoftLayer_Hardware </a>**


## Count
</div>


