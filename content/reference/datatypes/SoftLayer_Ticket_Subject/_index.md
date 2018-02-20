---
title: "SoftLayer_Ticket_Subject"
description: "The SoftLayer_Ticket_Subject data type models one of the possible subjects that a standard support ticket may belong to.... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Ticket"
classes:
    - "SoftLayer_Ticket_Subject"
---

# SoftLayer_Ticket_Subject
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Ticket_Subject' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Ticket_Subject' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Ticket_Subject data type models one of the possible subjects that a standard support ticket may belong to. A basic support ticket's title matches it's corresponding subject's name. 
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
            <span class='views-field-title'><a href="#categoryId" name=categoryId>categoryId</a></span>
            <div class='views-field-body'>The subject category id that this ticket subject belongs to. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>A ticket subject's internal identifier. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>A ticket subject's name. This name is used for a standard support ticket's title. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#parentId" name=parentId>parentId</a></span>
            <div class='views-field-body'>Specifies the parent subject id. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#category" name=category>category</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket_Subject_Category'>SoftLayer_Ticket_Subject_Category </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#children" name=children>children</a></span>
            <div class='views-field-body'>A child subject </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket_Subject'>SoftLayer_Ticket_Subject[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#group" name=group>group</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket_Group'>SoftLayer_Ticket_Group </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#parent" name=parent>parent</a></span>
            <div class='views-field-body'>A parent subject </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Ticket_Subject'>SoftLayer_Ticket_Subject </a></p></div>
        </div>
            </div>
</div>


