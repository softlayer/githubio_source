---
title: "SoftLayer_Software_Description"
description: "This class holds a description for a specific installation of a Software Component. 

SoftLayer_Software_Licenses tie a Software Component (A specific installation on a piece of hardware) to it's description. 

The 'Manufacturer' and 'Name' properties of a SoftLayer_Software_Description are used by the framework to factory specific objects, objects that may have special methods for that specific piece of software, or objects that contain application specific data, such as default ports.  For example, if you create a SoftLayer_Software_Component who's SoftLayer_Software_License points to the SoftLayer_Software_Description for 'Swsoft' 'Plesk', you'll actually get a SoftLayer_Software_Component_Swsoft_Plesk object. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Description"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Software_Description"
---
