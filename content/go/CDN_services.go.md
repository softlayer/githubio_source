---
title: "CDN_services.go"
description: "CDN_services.go"
date: "2020-10-07"
classes: 
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping"
    - "SoftLayer_Network_CdnMarketplace_Configuration_Mapping_Path"
    - "SoftLayer_Container_Network_CdnMarketplace_Configuration_Input"
tags:
    - "cdn"
---

### ListVendors 
```
package main
import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
)
func main() {
	// SoftLayer API username and key
	username := "set-me"
	apikey := "set-me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	service := services.GetNetworkCdnMarketplaceVendorService(sess)

	receipt, err := service.ListVendors()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
		return
	}
	fmt.Println(string(jsonFormat1))
}
```

### VerifyCdnAccountExists

```
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set - me"
	apikey := "set - me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	service := services.GetNetworkCdnMarketplaceAccountService(sess)

	vendor:=sl.String("akamai")

	receipt, err := service.VerifyCdnAccountExists(vendor)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
		return
	}
	fmt.Println(string(jsonFormat1))
}
```

### CreateDomainMapping

```
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set - me"
	apikey := "set - me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	service := services.GetNetworkCdnMarketplaceConfigurationMappingService(sess)

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

	receipt, err := service.CreateDomainMapping(&templateCdn)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
		return
	}
	fmt.Println(string(jsonFormat1))
}
```
Note: In case that the CDN account not exist, this method creates a CDN account internally after you confirm the creation, this creation can wait for some time

reference : https://cloud.ibm.com/docs/CDN?topic=CDN-faqs&locale=en#how-is-my-ibm-cloud-content-delivery-network-service-account-created 
            https://cloud.ibm.com/docs/CDN?topic=CDN-cdn-api-reference#create-domain-mapping
### DeleteDomainMapping

```
package main


import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set - me"
	apikey := "set - me"

	// Create SoftLayer API session
 	sess := session.New(username, apikey)

	service := services.GetNetworkCdnMarketplaceConfigurationMappingService(sess)
    // Input the unique Id 
	uniqueId := sl.String("123456789")

	receipt, err := service.DeleteDomainMapping(uniqueId)

	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
		return
	}
	fmt.Println(string(jsonFormat1))
}
```

### VerifyDomainMapping

```
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "sl307608-dcabero"
	apikey := "8f639dfb380af0667ee4949cdf2dbc9eb8e20b2d777e92aba7312f24a9524988"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	service := services.GetNetworkCdnMarketplaceConfigurationMappingService(sess)
	uniqueId := sl.Int(723231201263657)

	receipt, err := service.VerifyDomainMapping(uniqueId)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
		return
	}
	fmt.Println(string(jsonFormat1))
}
```

### StartDomainMapping

```
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set - me"
	apikey := "set - me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	service := services.GetNetworkCdnMarketplaceConfigurationMappingService(sess)

	uniqueId := sl.String("723231201263657")

	receipt, err := service.StartDomainMapping(uniqueId)

	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
		return
	}
	fmt.Println(string(jsonFormat1))
}
```

### StopDomainMapping

```
package main


import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set - me"
	apikey := "set- me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	service := services.GetNetworkCdnMarketplaceConfigurationMappingService(sess)
    // Input the uniqueId
	uniqueId := sl.String("123456789")

	receipt, err := service.StopDomainMapping(uniqueId)

	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
		return
	}
	fmt.Println(string(jsonFormat1))
}
```

### ListDomainMappings

```
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
)

func main() {
	// SoftLayer API username and key
	username := "set - me"
	apikey := "set - me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	service := services.GetNetworkCdnMarketplaceConfigurationMappingService(sess)

	receipt, err := service.ListDomainMappings()
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
		return
	}
	fmt.Println(string(jsonFormat1))
}
```

### ListDomainMappingByUniqueId

```
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set - me"
	apikey := "set - me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	service := services.GetNetworkCdnMarketplaceConfigurationMappingService(sess)
    // Input the uniqueId
	uniqueId := sl.String("123456789")

	receipt, err := service.ListDomainMappingByUniqueId(uniqueId)

	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
		return
	}
	fmt.Println(string(jsonFormat1))
}
```

### CreateOriginPath

```
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/datatypes"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set - me"
	apikey := "set - me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	service := services.GetNetworkCdnMarketplaceConfigurationMappingPathService(sess)

	templateCdn:= datatypes.Container_Network_CdnMarketplace_Configuration_Input{
		Header: sl.String("www.techsupport.com"),
		Cname: sl.String("cdnakaogtechSpport.cdn.appdomain.cloud"),
		Domain: sl.String("www.testGotest.com"),
		Path: sl.String("/example2"),
		Protocol: sl.String("HTTPS"),
		Origin: sl.String("10.10.15.2"),
		OriginType: sl.String("HOST_SERVER"),
		VendorName: sl.String("akamai"),
		HttpsPort: sl.Int(80),
		UniqueId: sl.String("123456789"),
	}

	receipt, err := service.CreateOriginPath(&templateCdn)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
		return
	}
	fmt.Println(string(jsonFormat1))
}
```

### ListOriginPath

```
package main

import (
	"encoding/json"
	"fmt"
	"github.com/softlayer/softlayer-go/services"
	"github.com/softlayer/softlayer-go/session"
	"github.com/softlayer/softlayer-go/sl"
)

func main() {
	// SoftLayer API username and key
	username := "set - me"
	apikey := "set - me"

	// Create SoftLayer API session
	sess := session.New(username, apikey)

	service := services.GetNetworkCdnMarketplaceConfigurationMappingPathService(sess)
    // Input the unique Id 
	uid:= sl.String("123456789")

	receipt, err := service.ListOriginPath(uid)
	if err != nil {
		fmt.Printf("\n Unable to place order:\n - %s\n", err)
		return
	}

	// Following helps to print the result in json format.
	jsonFormat1, jsonErr1 := json.MarshalIndent(receipt, "", "     ")
	if jsonErr1 != nil {
		fmt.Println(jsonErr1)
		return
	}
	fmt.Println(string(jsonFormat1))
}
```