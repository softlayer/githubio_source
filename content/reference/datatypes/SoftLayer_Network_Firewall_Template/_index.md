---
title: "SoftLayer_Network_Firewall_Template"
description: "The SoftLayer_Network_Firewall_Template type contains general information for a SoftLayer network firewall template. 

F... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Template"
---

# SoftLayer_Network_Firewall_Template
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Firewall_Template' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Firewall_Template' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_Firewall_Template type contains general information for a SoftLayer network firewall template. 

Firewall templates are recommend rule sets for use with SoftLayer Hardware Firewall (Dedicated).  These optimized templates are designed to balance security restriction with application availability.  The templates given may be altered to provide custom network security, or may be used as-is for basic security. At least one rule set MUST be applied for the firewall to block traffic. Use the [[SoftLayer Network Component Firewall]] service to view current rules. Use the [[SoftLayer Network Firewall Update Request]] service to submit a firewall update request. 

### External Links


* [Firewall at Wikipedia](http://en.wikipedia.org/wiki/Firewall_(networking))






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
[id]: #id
#### [id]
A Firewall template's internal identifier.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
The name of the firewall rules template.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[rules]: #rules
#### [rules]
The rule set that belongs to this firewall rules template.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Firewall_Template_Rule'>SoftLayer_Network_Firewall_Template_Rule[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[ruleCount]: #rulecount
#### [ruleCount]
A count of the rule set that belongs to this firewall rules template.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


