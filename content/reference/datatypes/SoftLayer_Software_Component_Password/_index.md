---
title: "SoftLayer_Software_Component_Password"
description: "This SoftLayer_Software_Component_Password data type contains a password for a specific software component instance."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_Password"
---

# SoftLayer_Software_Component_Password
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Software_Component_Password' >Datatype</a></li>
    </ul>
</div>

## Description 
This SoftLayer_Software_Component_Password data type contains a password for a specific software component instance. 



### seeAlso

* [SoftLayer_Software_Component](/reference/datatypes/SoftLayer_Software_Component )


* [SoftLayer_Software_Password_History](/reference/datatypes/SoftLayer_Software_Password_History )




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
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The date this username/password pair was created. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>An id number for this specific username/password pair. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The date of the last modification to this username/password pair. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#notes" name=notes>notes</a></span>
            <div class='views-field-body'>A note string stored for this username/password pair. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#password" name=password>password</a></span>
            <div class='views-field-body'>The password part of the username/password pair. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#port" name=port>port</a></span>
            <div class='views-field-body'>The application access port for the Software Component. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#softwareId" name=softwareId>softwareId</a></span>
            <div class='views-field-body'>An id number for the software component this username/password pair is valid for. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#username" name=username>username</a></span>
            <div class='views-field-body'>The username part of the username/password pair. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#software" name=software>software</a></span>
            <div class='views-field-body'>The SoftLayer_Software_Component instance that this username/password pair is valid for. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sshKeys" name=sshKeys>sshKeys</a></span>
            <div class='views-field-body'>SSH keys to be installed on the server during provisioning or an OS reload. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Security_Ssh_Key'>SoftLayer_Security_Ssh_Key[] </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#sshKeyCount" name=sshKeyCount>sshKeyCount</a></span>
            <div class='views-field-body'>A count of sSH keys to be installed on the server during provisioning or an OS reload. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


