---
title: "SoftLayer_Auxiliary_Press_Release"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Auxiliary"
classes:
    - "SoftLayer_Auxiliary_Press_Release"
---

# SoftLayer_Auxiliary_Press_Release
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Auxiliary_Press_Release' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release' >Datatype</a></li>
    </ul>
</div>

## Description 



### associatedMethods

*  [SoftLayer_Auxiliary_Press_Prelease::getObject](/reference/services/SoftLayer_Auxiliary_Press_Prelease/getObject )



### seeAlso

* [SoftLayer_Auxiliary_Press_Release_Content](/reference/services/SoftLayer_Auxiliary_Press_Release_Content )


* [SoftLayer_Auxiliary_Press_Release_About_Press_Release](/reference/services/SoftLayer_Auxiliary_Press_Release_About_Press_Release )


* [SoftLayer_Auxiliary_Press_Release_Contact_Press_Release](/reference/services/SoftLayer_Auxiliary_Press_Release_Contact_Press_Release )


* [SoftLayer_Auxiliary_Press_Release_Media_Partner_Press_Release](/reference/services/SoftLayer_Auxiliary_Press_Release_Media_Partner_Press_Release )




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
            <div class='views-field-body'>A press release's internal identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#publishDate" name=publishDate>publishDate</a>
            </span>
            <div class='views-field-body'>The data a press release was published. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#releaseLocation" name=releaseLocation>releaseLocation</a>
            </span>
            <div class='views-field-body'>A press release's location. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#subTitle" name=subTitle>subTitle</a>
            </span>
            <div class='views-field-body'>A press release's sub-title. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#title" name=title>title</a>
            </span>
            <div class='views-field-body'>A press release's title. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#websiteHighlightFlag" name=websiteHighlightFlag>websiteHighlightFlag</a>
            </span>
            <div class='views-field-body'>Whether or not a press release is highlighted on the SoftLayer Website. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>boolean</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#about" name=about>about</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_About_Press_Release'>SoftLayer_Auxiliary_Press_Release_About_Press_Release[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#contacts" name=contacts>contacts</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Contact_Press_Release'>SoftLayer_Auxiliary_Press_Release_Contact_Press_Release[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#mediaPartners" name=mediaPartners>mediaPartners</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Media_Partner_Press_Release'>SoftLayer_Auxiliary_Press_Release_Media_Partner_Press_Release[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#pressReleaseContent" name=pressReleaseContent>pressReleaseContent</a>
            </span>
            <div class='views-field-body'> </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Auxiliary_Press_Release_Content'>SoftLayer_Auxiliary_Press_Release_Content </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#aboutCount" name=aboutCount>aboutCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#contactCount" name=contactCount>contactCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#mediaPartnerCount" name=mediaPartnerCount>mediaPartnerCount</a>
            </span>
            <div class='views-field-body'>A count of  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


