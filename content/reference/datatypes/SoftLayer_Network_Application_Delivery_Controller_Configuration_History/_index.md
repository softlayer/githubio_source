---
title: "SoftLayer_Network_Application_Delivery_Controller_Configuration_History"
description: "The SoftLayer_Network_Application_Delivery_Controller_Configuration_History data type models a single instance of a conf... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Application_Delivery_Controller_Configuration_History"
---

# SoftLayer_Network_Application_Delivery_Controller_Configuration_History
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Application_Delivery_Controller_Configuration_History' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller_Configuration_History' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_Application_Delivery_Controller_Configuration_History data type models a single instance of a configuration history entry for an application delivery controller. The configuration history entries are used to support creating backups of an application delivery controller's configuration state in order to restore them later if needed. 





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
[createDate]: #createdate
#### [createDate]
The date a configuration history record was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
An configuration history record's unique identifier  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
Editable notes used to describe a configuration history record  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[controller]: #controller
#### [controller]
The application delivery controller that a configuration history record belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Application_Delivery_Controller'>SoftLayer_Network_Application_Delivery_Controller </a>**  



</div>

## Count
</div>


