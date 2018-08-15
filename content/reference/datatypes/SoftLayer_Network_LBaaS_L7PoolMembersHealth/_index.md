---
title: "SoftLayer_Network_LBaaS_L7PoolMembersHealth"
description: "SoftLayer_Network_LBaaS_L7PoolMembersHealth provides statistics of members belonging to a particular L7 pool."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7PoolMembersHealth"
---

# SoftLayer_Network_LBaaS_L7PoolMembersHealth
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7PoolMembersHealth' >Datatype</a></li>
    </ul>
</div>

## Description 
SoftLayer_Network_LBaaS_L7PoolMembersHealth provides statistics of members belonging to a particular L7 pool. 





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
                <a href="#l7PoolUuid" name=l7PoolUuid>l7PoolUuid</a>
            </span>
            <div class='views-field-body'>Instance uuid of the L7 pool </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#membersHealth" name=membersHealth>membersHealth</a>
            </span>
            <div class='views-field-body'>Members statistics of the L7 pool </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_LBaaS_MemberHealth'>SoftLayer_Network_LBaaS_MemberHealth[] </a></p>
            </div>
        </div>
            </div>
    </div>


