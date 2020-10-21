---
title: "Managing CDN accounts"
description: "How to interact with the CdnMarketplace services. Order CDN, manage mappings and other related functions"
date: "2020-10-07"
classes: 
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping"
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path"
    - "SoftLayer_Container_Network_CdnMarketplace_Configuration_Input"
tags:
    - "cdn"
    
references:    
    - https://cloud.ibm.com/docs/CDN?topic=CDN-faqs&locale=en#how-is-my-ibm-cloud-content-delivery-network-service-account-created 
    - https://cloud.ibm.com/docs/CDN?topic=CDN-cdn-api-reference#create-domain-mapping
"
    
```
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/filter"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	username := "set- me"
	apikey := "set - me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	templateCdn:= datatypes.Container_Network_CdnMarketplace_Configuration_Input{
		Header: sl.String("www.techsupport.com"),
		Cname: sl.String("cdnakaogtechSpport.cdn.appdomain.cloud"),
		Domain: sl.String("www.testGotest.com"),
		Path: sl.String("/example"),
		Protocol: sl.String("HTTPS"),
		Origin: sl.String("10.10.15.2"),
		OriginType: sl.String("HOST_SERVER"),
		VendorName: sl.String("akamai"),
		HttpsPort: sl.Int(80),
	}

	templateCdnPath:= datatypes.Container_Network_CdnMarketplace_Configuration_Input{
		Header: sl.String("www.techsupport.com"),
		Cname: sl.String("cdnakaogtechSpport.cdn.appdomain.cloud"),
		Domain: sl.String("www.testGotest.com"),
		Path: sl.String("/example2"),
		Protocol: sl.String("HTTPS"),
		Origin: sl.String("10.10.15.2"),
		OriginType: sl.String("HOST_SERVER"),
		VendorName: sl.String("akamai"),
		HttpsPort: sl.Int(80),
		UniqueId: sl.String("172498049151824"),
	}

	serviceCdn := services.GetNetworkCdnMarketplaceConfigurationMappingService(sess)
	servicePathCdn := services.GetNetworkCdnMarketplaceConfigurationMappingPathService(sess)
	serviceProductOrder := services.GetProductOrderService(sess)
	productPackageService := services.GetProductPackageService(sess)

	fmt.Println(createCdnAccount(serviceProductOrder,productPackageService))
	fmt.Println(createDomainMapping(serviceCdn ,&templateCdn))
	fmt.Println(createDomainMappingPath(servicePathCdn,templateCdnPath))
}

func createDomainMappingPath(service services.Network_CdnMarketplace_Configuration_Mapping_Path,
	templatePath datatypes.Container_Network_CdnMarketplace_Configuration_Input) string {
	result, err := service.CreateOriginPath(&templatePath)

	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable to delete:\n - %s\n", err)
	}
	return string(jsonFormat1)
}

func createDomainMapping(service services.Network_CdnMarketplace_Configuration_Mapping,
	template *datatypes.Container_Network_CdnMarketplace_Configuration_Input) string {
	result, err := service.CreateDomainMapping(template)

	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable to delete:\n - %s\n", err)
	}
	return string(jsonFormat1)
}

func deleteDomain(service services.Network_CdnMarketplace_Configuration_Mapping, id string) string {
	result, err := service.DeleteDomainMapping(sl.String(id))

	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable to delete:\n - %s\n", err)
	}
	return string(jsonFormat1)
}

func deleteOriginPath(service services.Network_CdnMarketplace_Configuration_Mapping_Path,
	id string, path string) string {
	result, err := service.DeleteOriginPath(sl.String(id), sl.String(path))

	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable to delete:\n - %s\n", err)
	}
	return string(jsonFormat1)
}

func listDomainMapping(service services.Network_CdnMarketplace_Configuration_Mapping) string {
	result, err := service.ListDomainMappings()
	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable to delete:\n - %s\n", err)
	}
	return string(jsonFormat1)
}

func listDomainMappingByUniqueId(service services.Network_CdnMarketplace_Configuration_Mapping, id string) string {
	result, err := service.ListDomainMappingByUniqueId(sl.String(id))
	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable to delete:\n - %s\n", err)
	}
	return string(jsonFormat1)
}

func listOriginPath(service services.Network_CdnMarketplace_Configuration_Mapping_Path, path string ) string {
	result, err := service.ListOriginPath(sl.String(path))
	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable to delete:\n - %s\n", err)
	}
	return string(jsonFormat1)
}

func listVendor(service services.Network_CdnMarketplace_Vendor) string {
	result, err := service.ListVendors()
	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable to delete:\n - %s\n", err)
	}
	return string(jsonFormat1)
}

func startDomainMapping(service services.Network_CdnMarketplace_Configuration_Mapping, id string) string {
	result, err := service.StartDomainMapping(sl.String(id))
	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable to start:\n - %s\n", err)
	}
	return string(jsonFormat1)
}

func stopDomainMapping(service services.Network_CdnMarketplace_Configuration_Mapping, id string) string {
	result, err := service.StopDomainMapping(sl.String(id))
	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable to stop domain mapping:\n - %s\n", err)
	}
	return string(jsonFormat1)
}

func updateDomainMapping(service services.Network_CdnMarketplace_Configuration_Mapping,
	templateUpdate datatypes.Container_Network_CdnMarketplace_Configuration_Input) string  {
	result, err := service.UpdateDomainMapping(&templateUpdate)
	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable to update mapping:\n - %s\n", err)
	}
	return string(jsonFormat1)
}

func updateDomainMappingPath(service services.Network_CdnMarketplace_Configuration_Mapping_Path,
	templateUpdate datatypes.Container_Network_CdnMarketplace_Configuration_Input) string  {
	result, err := service.UpdateOriginPath(&templateUpdate)
	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable to update:\n - %s\n", err)
	}
	return string(jsonFormat1)
}

func verifyCDNAccount(service services.Network_CdnMarketplace_Configuration_Mapping, id string) string {
	result, err := service.VerifyCname(sl.String(id))
	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable Cname:\n - %s\n", err)
	}
	return string(jsonFormat1)
}
func verifyDomainMapping(service services.Network_CdnMarketplace_Configuration_Mapping, id int) string  {
	result, err := service.VerifyDomainMapping(sl.Int(id))
	jsonFormat1, err := json.MarshalIndent(result, "", "     ")
	if err != nil {
		fmt.Printf("\n Unable the Domain mapping:\n - %s\n", err)
	}
	return string(jsonFormat1)
}
func createCdnAccount(service services.Product_Order, productPackageService services.Product_Package) string{

	filter := filter.Build(filter.Path("keyName").Eq("CONTENT_DELIVERY_NETWORK_SERVICE"))
	cdnPackageKeyName, err := productPackageService.Filter(filter).GetAllObjects()
	if err != nil {
		fmt.Printf("\n Unable to retrieve the cdn key name:\n - %s\n", err)
	}
	cdnPackageId := sl.Int(*cdnPackageKeyName[0].Id)

	cdnItemPrices, err := productPackageService.Id(*cdnPackageId).GetItemPrices()
	if err != nil {
		fmt.Printf("\n Unable to get the cdn prices:\n - %s\n", err)
	}
	itemPriceId := sl.Int(*cdnItemPrices[0].Id)

	prices := []datatypes.Product_Item_Price{
		{Id: sl.Int(*itemPriceId)},
	}
	templateObject := datatypes.Container_Product_Order{

		PackageId: sl.Int(*cdnPackageId),
		Prices:    prices,

	}
	jsonFormat, jsonErr := json.MarshalIndent(templateObject, "", "     ")
	if jsonErr != nil {
		fmt.Println(jsonErr)
	}
	fmt.Println(string(jsonFormat))
	receipt, err := service.PlaceOrder(&templateObject,sl.Bool(false))
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
	}
	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
	}
	return(string(jsonFormat1))
}
```