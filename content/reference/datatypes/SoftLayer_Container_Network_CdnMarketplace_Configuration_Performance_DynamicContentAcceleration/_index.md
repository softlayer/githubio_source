---
title: "SoftLayer_Container_Network_CdnMarketplace_Configuration_Performance_DynamicContentAcceleration"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_CdnMarketplace_Configuration_Performance_DynamicContentAcceleration"
---

# SoftLayer_Container_Network_CdnMarketplace_Configuration_Performance_DynamicContentAcceleration
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_CdnMarketplace_Configuration_Performance_DynamicContentAcceleration' >Datatype</a></li>
    </ul>
</div>

## Description 






<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[detectionPath]: #detectionpath
#### [detectionPath]
The detectionPath is used by CDN edge servers to find the best optimized route from edge to the origin server. The Akamai edge servers fetch the test object from the origin to know the network condition to your origin server, and then calculate the best optimized route with the network condition. The best path to origin must be known at the time a user’s request arrives at an edge server, since any in-line analysis or probing would defeat the purpose of speeding things up.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[mobileImageCompressionEnabled]: #mobileimagecompressionenabled
#### [mobileImageCompressionEnabled]
Serving compressed images reduces the amount of content required to load a page. This feature helps offset less robust connections, such as those formed with mobile devices. Basically, if your site visitors have slow network speeds, MobileImageCompression technology can automatically increase compression of JPEG images to speed up loading. On the other hand, this feature results in lossy compression or irreversible compression, and may affect the quality of the images on your site. 

JPG supported file extensions: .jpg, .jpeg, .jpe, .jig, .jgig, .jgi The default is enabled.   
<span class="type-label">Type: </span>**boolean**


</div>
<div class="prop-row">

-----
[prefetchEnabled]: #prefetchenabled
#### [prefetchEnabled]
Inspects HTML responses and prefetches embedded objects in HTML files. Prefetching works on any page that includes `<img>`, `<script>`, or `<link>` tags that specify relative paths. It also works when the resource hostname matches the request domain in the HTML file, and it is part of a fully qualified URI. When set to true, edge servers prefetch objects with the following file extensions: 

aif, aiff, au, avi, bin, bmp, cab, carb, cct, cdf, class, css, doc, dcr, dtd, exe, flv, gcf, gff, gif, grv, hdml, hqx, ico, ini, jpeg, jpg, js, mov, mp3, nc, pct, pdf, png, ppc, pws, swa, swf, txt, vbs, w32, wav, wbmp, wml, wmlc, wmls, wmlsc, xsd, and zip. 

The default is enabled.   
<span class="type-label">Type: </span>**boolean**


</div>
</div>
<!-- LOCAL PROPERTY END -->

</div>


