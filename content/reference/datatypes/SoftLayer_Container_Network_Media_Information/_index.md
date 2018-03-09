---
title: "SoftLayer_Container_Network_Media_Information"
description: "This container class holds information on a media file such as file name, codec, frame rate and so on"
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_Media_Information"
---

# SoftLayer_Container_Network_Media_Information
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_Media_Information' >Datatype</a></li>
    </ul>
</div>

## Description 
This container class holds information on a media file such as file name, codec, frame rate and so on 


### associatedMethods

*  [SoftLayer_Network_Media_Transcode_Account::getFileDetail](/reference/services/SoftLayer_Network_Media_Transcode_Account/getFileDetail )



### seeAlso

* [SoftLayer_Network_Media_Transcode_Account](/reference/services/SoftLayer_Network_Media_Transcode_Account )




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
                <a href="#audioBitRate" name=audioBitRate>audioBitRate</a>
            </span>
            <div class='views-field-body'>The audio bit rate </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#audioChannelMode" name=audioChannelMode>audioChannelMode</a>
            </span>
            <div class='views-field-body'>The audio channel mode </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#audioChannels" name=audioChannels>audioChannels</a>
            </span>
            <div class='views-field-body'>The number of audio channels </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#audioCodec" name=audioCodec>audioCodec</a>
            </span>
            <div class='views-field-body'>The audio codec name </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#audioSampleRate" name=audioSampleRate>audioSampleRate</a>
            </span>
            <div class='views-field-body'>The audio sample rate </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#duration" name=duration>duration</a>
            </span>
            <div class='views-field-body'>The duration of a media </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#errorMessage" name=errorMessage>errorMessage</a>
            </span>
            <div class='views-field-body'>The error message if any. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#file" name=file>file</a>
            </span>
            <div class='views-field-body'>The name of a media file </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#fileFormat" name=fileFormat>fileFormat</a>
            </span>
            <div class='views-field-body'>The file format </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#fileSize" name=fileSize>fileSize</a>
            </span>
            <div class='views-field-body'>The size of a media file in byte </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsigned long</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#frameRate" name=frameRate>frameRate</a>
            </span>
            <div class='views-field-body'>The frame rate </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sizeX" name=sizeX>sizeX</a>
            </span>
            <div class='views-field-body'>The width of a media in pixel </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#sizeY" name=sizeY>sizeY</a>
            </span>
            <div class='views-field-body'>The height of a media in pixel </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#totalFrames" name=totalFrames>totalFrames</a>
            </span>
            <div class='views-field-body'>The total of frames </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsigned long</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#videoAspectX" name=videoAspectX>videoAspectX</a>
            </span>
            <div class='views-field-body'>The width in a video's width to height aspect ratio </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>float</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#videoAspectY" name=videoAspectY>videoAspectY</a>
            </span>
            <div class='views-field-body'>The height in a video's width to height aspect ratio </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#videoCodec" name=videoCodec>videoCodec</a>
            </span>
            <div class='views-field-body'>The video codec name </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
    </div>


