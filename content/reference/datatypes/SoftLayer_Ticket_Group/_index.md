---
title: "SoftLayer_Ticket_Group"
description: "SoftLayer tickets have the ability to be assigned to one of SoftLayer's internal departments. The department that a tick... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Group"
---

# SoftLayer_Ticket_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Group' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer tickets have the ability to be assigned to one of SoftLayer's internal departments. The department that a ticket is assigned to is modeled by the SoftLayer_Ticket_Group data type. Ticket groups help to ensure that the proper department is handling a ticket. Standard support tickets are created from a number of pre-determined subjects. These subjects help determine which group a standard ticket is assigned to. 



### seeAlso

* [SoftLayer_Ticket](/reference/services/SoftLayer_Ticket )


* [SoftLayer_Ticket_Subject](/reference/datatypes/SoftLayer_Ticket_Subject )




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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A ticket group's internal identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>A ticket group's name. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#ticketGroupCategoryId" name=ticketGroupCategoryId>ticketGroupCategoryId</a>
            </span>
            <div class='views-field-body'>The internal identifier for the category that a ticket group belongs to.. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#category" name=category>category</a>
            </span>
            <div class='views-field-body'>The category that a ticket group belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Ticket_Group_Category'>SoftLayer_Ticket_Group_Category </a></p>
            </div>
        </div>
                <h2>Count</h2>
            </div>
</div>


