---
title: "SoftLayer_Network_Media_Transcode_Job"
description: "The SoftLayer_Network_Media_Transcode_Job contains information regarding a transcode job such as input file, output form... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Media_Transcode_Job"
---

# SoftLayer_Network_Media_Transcode_Job
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Job' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Media_Transcode_Job contains information regarding a transcode job such as input file, output format, user id and so on. 





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
            <span class='views-field-title'><a href="#autoDeleteDuration" name=autoDeleteDuration>autoDeleteDuration</a></span>
            <div class='views-field-body'>The auto-deletion duration in seconds.  This value determines how long the input file will be kept on the storage. </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#byteIn" name=byteIn>byteIn</a></span>
            <div class='views-field-body'>The size of an input file in byte </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#createDate" name=createDate>createDate</a></span>
            <div class='views-field-body'>The created date </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#id" name=id>id</a></span>
            <div class='views-field-body'>The internal identifier of a transcode job </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#inputFile" name=inputFile>inputFile</a></span>
            <div class='views-field-body'>The input file name </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#modifyDate" name=modifyDate>modifyDate</a></span>
            <div class='views-field-body'>The last modified date </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>dateTime</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#name" name=name>name</a></span>
            <div class='views-field-body'>The name of a transcode job </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#outputFile" name=outputFile>outputFile</a></span>
            <div class='views-field-body'>The output file name </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#transcodeAccountId" name=transcodeAccountId>transcodeAccountId</a></span>
            <div class='views-field-body'>The internal identifier of SoftLayer account </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#transcodeJobGuid" name=transcodeJobGuid>transcodeJobGuid</a></span>
            <div class='views-field-body'>The unique id of a transcode job </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#transcodePresetGuid" name=transcodePresetGuid>transcodePresetGuid</a></span>
            <div class='views-field-body'>The unique id of a pre-defined output format </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#transcodePresetName" name=transcodePresetName>transcodePresetName</a></span>
            <div class='views-field-body'>The name of a transcode output preset </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#transcodeStatusId" name=transcodeStatusId>transcodeStatusId</a></span>
            <div class='views-field-body'>The internal identifier of a transcode status </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#userId" name=userId>userId</a></span>
            <div class='views-field-body'>The internal identifier of the user who created a transcode job </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>integer</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#watermark" name=watermark>watermark</a></span>
            <div class='views-field-body'>Watermark to apply to job </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Container_Network_Media_Transcode_Job_Watermark'>SoftLayer_Container_Network_Media_Transcode_Job_Watermark </a></p></div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#history" name=history>history</a></span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Job_History'>SoftLayer_Network_Media_Transcode_Job_History[] </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#transcodeAccount" name=transcodeAccount>transcodeAccount</a></span>
            <div class='views-field-body'>The transcode service account </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Account'>SoftLayer_Network_Media_Transcode_Account </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#transcodeStatus" name=transcodeStatus>transcodeStatus</a></span>
            <div class='views-field-body'>The status information of a transcode job </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_Network_Media_Transcode_Job_Status'>SoftLayer_Network_Media_Transcode_Job_Status </a></p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#transcodeStatusName" name=transcodeStatusName>transcodeStatusName</a></span>
            <div class='views-field-body'>The status of a transcode job </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>string</p></div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#user" name=user>user</a></span>
            <div class='views-field-body'>The SoftLayer user that created the transcode job </div>
            <span class="type-label">Type:</span> <div class='type-content'><p><a href='/reference/datatypes/SoftLayer_User_Customer'>SoftLayer_User_Customer </a></p></div>
        </div>
                <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'><a href="#historyCount" name=historyCount>historyCount</a></span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> <div class='type-content'><p>unsignedLong</p></div>
        </div>
            </div>
</div>


