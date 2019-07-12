---
title: "SoftLayer_Network_Storage_Allowed_Host_VirtualGuest"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_Allowed_Host_VirtualGuest"
---

# SoftLayer_Network_Storage_Allowed_Host_VirtualGuest
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Storage_Allowed_Host_VirtualGuest' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_Allowed_Host_VirtualGuest' >Datatype</a></li>
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
            <span class='views-field-title'>
                <a href="#accountId" name=accountId>accountId</a>
            </span>
            <div class='views-field-body'>The account to which this allowed host belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#credentialId" name=credentialId>credentialId</a>
            </span>
            <div class='views-field-body'>The credential this allowed host will use </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>The internal identifier of the igroup </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>The name of allowed host, usually an IQN or other identifier </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resourceTableId" name=resourceTableId>resourceTableId</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resourceTableName" name=resourceTableName>resourceTableName</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Account object which this SoftLayer_Network_Storage_Allowed_Host belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#assignedGroups" name=assignedGroups>assignedGroups</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Network_Storage_Group objects this SoftLayer_Network_Storage_Allowed_Host is present in. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Storage_Group'>SoftLayer_Network_Storage_Group[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#assignedIscsiVolumes" name=assignedIscsiVolumes>assignedIscsiVolumes</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#assignedNfsVolumes" name=assignedNfsVolumes>assignedNfsVolumes</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#assignedReplicationVolumes" name=assignedReplicationVolumes>assignedReplicationVolumes</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Network_Storage primary volumes whose replicas are allowed access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#assignedVolumes" name=assignedVolumes>assignedVolumes</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#credential" name=credential>credential</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Network_Storage_Credential this allowed host uses. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Storage_Credential'>SoftLayer_Network_Storage_Credential </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#resource" name=resource>resource</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Virtual_Guest object which this SoftLayer_Network_Storage_Allowed_Host is referencing. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Virtual_Guest'>SoftLayer_Virtual_Guest </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sourceSubnet" name=sourceSubnet>sourceSubnet</a>
            </span>
            <div class='views-field-body'>Connections to a target with a source IP in this subnet prefix are allowed. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#subnetsInAcl" name=subnetsInAcl>subnetsInAcl</a>
            </span>
            <div class='views-field-body'>The SoftLayer_Network_Subnet records assigned to the ACL for this allowed host. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#assignedGroupCount" name=assignedGroupCount>assignedGroupCount</a>
            </span>
            <div class='views-field-body'>A count of the SoftLayer_Network_Storage_Group objects this SoftLayer_Network_Storage_Allowed_Host is present in. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#assignedIscsiVolumeCount" name=assignedIscsiVolumeCount>assignedIscsiVolumeCount</a>
            </span>
            <div class='views-field-body'>A count of the SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#assignedNfsVolumeCount" name=assignedNfsVolumeCount>assignedNfsVolumeCount</a>
            </span>
            <div class='views-field-body'>A count of the SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#assignedReplicationVolumeCount" name=assignedReplicationVolumeCount>assignedReplicationVolumeCount</a>
            </span>
            <div class='views-field-body'>A count of the SoftLayer_Network_Storage primary volumes whose replicas are allowed access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#assignedVolumeCount" name=assignedVolumeCount>assignedVolumeCount</a>
            </span>
            <div class='views-field-body'>A count of the SoftLayer_Network_Storage volumes to which this SoftLayer_Network_Storage_Allowed_Host is allowed access. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#subnetsInAclCount" name=subnetsInAclCount>subnetsInAclCount</a>
            </span>
            <div class='views-field-body'>A count of the SoftLayer_Network_Subnet records assigned to the ACL for this allowed host. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


