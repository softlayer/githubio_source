---
title: "softlayer_service_request.go"
description: "softlayer_service_request.go"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "slapi"
---


```go
package slapi

import (
	"bytes"
	"net/http"
	"log"
	"io/ioutil"
	"fmt"
	"encoding/json"
	"net/url"
	"strings"
)

// This structure is used to build the URL request
type SoftLayerServiceRequest struct {
	Endpoint string
	InitParameter int
	ServiceName string
	Method string
	Mask string
	Filter string
	Limit string
}

/*
UrlRequest function builds the url request with the following structure:

  [end_point]/[service]/[initParameter]/[method]?[objectFilter]&[objectMask]&[resultLimit]

Example:
  https://api.softlayer.com/rest/v3/SoftLayer_Account/getVirtualGuests?objectMask=mask[id]

The result depends of parameters set in the SoftLayerRequest argument.
*/
func UrlRequest(sl SoftLayerServiceRequest) string{

	var request *url.URL

	request, err := url.Parse(strings.TrimSuffix(sl.Endpoint, "/"))
	if err != nil {
		panic("boom")
	}

	if sl.InitParameter != 0 {
		request.Path += fmt.Sprintf("/%s/%d/%s", sl.ServiceName, sl.InitParameter, sl.Method)
	} else {
		request.Path += fmt.Sprintf("/%s/%s", sl.ServiceName, sl.Method)
	}

	paramaters := url.Values{}
	if sl.Filter != "" { paramaters.Add("objectFilter", sl.Filter)}
	if sl.Mask   != "" { paramaters.Add("objectMask", sl.Mask) }
	if sl.Limit  != "" { paramaters.Add("resultLimit", sl.Limit) }

	request.RawQuery = paramaters.Encode()

	return request.String()
}

/*
 RestRequest function makes a REST request to the SoftLayer API according to following parameters:
 	urlRequest -  This can be build by using the UrlRequest function
 	username   -  The username you want to use for authentication
 	apikey     -  The apiKey you want to use for authentication
 	parameters -  Value in JSON format which is used in POST requests, set nil for GET requests
 	method     -  Request method GET/POST

 This will return a JSON string with the response.
*/
func RestRequest(urlRequest string, username string, apikey string, parameters *string, method string) http.Response {

	var bodyJSON bytes.Buffer
	if parameters != nil { bodyJSON = *bytes.NewBuffer([]byte(*parameters)) }
	request,_ := http.NewRequest(method, urlRequest, &bodyJSON)
	request.SetBasicAuth(username, apikey)
	request.Header.Set("X-Custom-Header", "SoftLayer-Api")
	request.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	response, err := client.Do(request)
	if err != nil {
		log.Fatal("Do: ", err)
	}

	return *response
}

/*
PrintJsonFormat prints a *Response object in Json format.
	response - The http.Response object
	indent   - The response will be printed in Json format with indentation if TRUE. It will be
		   printed in a single line if FALSE.
*/
func PrintJsonFormat(response http.Response, indent bool) {
	jsonResponse,_ := ioutil.ReadAll(response.Body)

	if indent == false {
		fmt.Println(string(jsonResponse))
	} else {
		buffer := new(bytes.Buffer)
		json.Indent(buffer, []byte(string(jsonResponse)), "", "  ")
		fmt.Println(buffer)
	}
}

```
