---
title: "SoftLayer_Virtual_Guest_SupplementalCreateObjectOptions"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest_SupplementalCreateObjectOptions"
---

# SoftLayer_Virtual_Guest_SupplementalCreateObjectOptions
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Virtual_Guest_SupplementalCreateObjectOptions' >Datatype</a></li>
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
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#bootMode" name=bootMode>bootMode</a></span>
            <div class='views-field-body'>The mode used to boot the [[SoftLayer_Virtual_Guest]].  Supported values are 'PV' and 'HVM'.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#flavorKeyName" name=flavorKeyName>flavorKeyName</a></span>
            <div class='views-field-body'>When set the startCpus and maxMemory are defined by the flavor. If the flavor includes local storage blockDevice 0 is also defined by the flavor. When startCpus, maxMemory, or blockDevice 0 are also provided on the template object they are validated against the flavor provided.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#immediateApprovalOnlyFlag" name=immediateApprovalOnlyFlag>immediateApprovalOnlyFlag</a></span>
            <div class='views-field-body'>When explicitly set to true, createObject(s) will fail unless the order is started automatically. This can be used by automated systems to fail an order that might otherwise require manual approval. For multi-guest orders via [[SoftLayer_Virtual_Guest/createObjects|createObjects]], this value must be the exact same for every item.  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>boolean</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#postInstallScriptUri" name=postInstallScriptUri>postInstallScriptUri</a></span>
            <div class='views-field-body'>URI of the script to be downloaded and executed after installation is complete. This can be different for each virtual guest when multiple are sent to [[SoftLayer_Virtual_Guest/createObjects|createObjects]].  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
    </div>


