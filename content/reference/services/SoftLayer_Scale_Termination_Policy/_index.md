---
title: "SoftLayer_Scale_Termination_Policy"
description: "A policy for automatic removal of members from a group. This policy determines which members are chosen first for remova... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Scale"
classes:
    - "SoftLayer_Scale_Termination_Policy"
---
# SoftLayer_Scale_Termination_Policy
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Scale_Termination_Policy' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Scale_Termination_Policy' >Datatype</a></li>
    </ul>
</div>

## Description
A policy for automatic removal of members from a group. This policy determines which members are chosen first for removal. The values can be: 


* OLDEST - The oldest member is the next one removed.
* NEWEST - The newest member is the next one removed.
* CLOSEST_TO_NEXT_CHARGE - The member closest to the next charge is removed. This is helpful for billing because it
will let you remove the member you have gotten the most out of. Note, this is usually closest to the next billing hour. 





        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Termination_Policy/getAllObjects'> getAllObjects</a> </span>
            <div class='views-field-body'>Get a list of all termination policies</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Scale_Termination_Policy/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Scale_Termination_Policy record.</div>
        </div>
        </div>
</div>

