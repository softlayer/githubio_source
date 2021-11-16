---
title: "Golang Example Framework"
description: "Explains how to setup a simple CLI framework to copy/paste examples into and easily get going."
date: "2021-09-29"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Hardware"
    - "SoftLayer_Hardware_Server"
tags:
    - "examples"
    - "cli"
---


The framework for new golang examples will be a simple CLI application that you can copy / paste in commands individually as needed to hopefully help better understand how to work with the data returned from the SoftLayer API in a practicle manner.

To do all this, we first need to setup a basic framework project to add these commands into. We will be using the [Cobra](https://github.com/spf13/cobra) CLI framework for golang, letting us create an individual command for each example as we go along.

First, our project will be under `github.com/softlayer/softlayer-go/examples`.
And will have the following basic directory structure.

* `github.com/softlayer/softlayer-go/examples`
    * `main.go`
    * `cmd/`
        * `root.go`


### main.go
The main.go file is very simple.

```go
package main

import (
    // "github.com/spf13/cobra"
    "github.com/softlayer/softlayer-go/examples/cmd"
)

func main() {
  cmd.Execute()
}
```

### cmd/root.go
root.go is the "main" section of our new cli program, and is very basic.

```go
package cmd

import (
    "github.com/spf13/cobra"
)

var (
    rootCmd = &cobra.Command{
        Use:   "sl",
        Short: "An example CLI application for working with IBM Classic Infrastructure",
        Long: `A collection of example commands that can be easily used to better understand how
the SoftLayer API works in golang. Authentication is set with the SL_USERNAME and SL_API_KEY env variables, or the
~/.softlayer config file.`,
    }
)

// Execute executes the root command.
func Execute() error {
    return rootCmd.Execute()
}

// Use this to setup anything for the whole command suite if needed.
func init() {}
```

### cmd/server_list.go

server_list.go is our actual command that we will run
```go
package cmd

import (
    "fmt"

    "github.com/spf13/cobra"

    "github.com/softlayer/softlayer-go/services"
    "github.com/softlayer/softlayer-go/session"
)

func init() {
    rootCmd.AddCommand(listServerCmd)
}

var listServerCmd = &cobra.Command{
    Use:   "server-list",
    Short: "Lists all servers on the account",
    Long:  `Lists all servers on the account`,
    RunE: func(cmd *cobra.Command, args []string)  error{
        return listServerCommand(cmd, args)
    },
}

func listServerCommand(cmd *cobra.Command, args []string) error {
    resultLimit := 5
    resultOffset := 0
    objectMask := "mask[id,hostname,domain,primaryIpAddress,primaryBackendIpAddress]"
    // When using a result Limit to break up your API request, its important to include an orderBy objectFilter
    // to enforce an order on the query, as the database might not always return results in the same order between
    // queries otherwise
    objectFilter := `{"hardware":{"id":{"operation":"orderBy","options":[{"name":"sort","value":["ASC"]}]}}}`
    // Sets up the session with authentication headers.
    sess := session.New()
    // uncomment to output API calls as they are made.
    // sess.Debug = true

    // creates a reference to the service object (SoftLayer_Account)
    service := services.GetAccountService(sess)

    // Sets the mask, filter, result limit, and then makes the API call SoftLayer_Account::getHardware()
    servers, err := service.Mask(objectMask).Filter(objectFilter).
        Offset(resultOffset).Limit(resultLimit).GetHardware()
    if err != nil {
        return err
    }
    fmt.Printf("Id, Hostname, Domain, IP Address\n")
    for {
        for _, s := range servers {
            ipAddress := "-"
            if *s.PrimaryIpAddress != "" {
                ipAddress = *s.PrimaryIpAddress
            }
            fmt.Printf("%v, %v, %v, %v\n", *s.Id, *s.Hostname, *s.Domain, ipAddress)
        }
        // If we get less than the number of results we asked for, we are at the end of our server list
        if len(servers) < resultLimit {
            break
        }
        // Increment the offset to get next set of results
        resultOffset = resultOffset + resultLimit
        servers, err = service.Mask(objectMask).Filter(objectFilter).
            Offset(resultOffset).Limit(resultLimit).GetHardware()
        if err != nil {
            return err
        }
    }

    return nil
}
```


## Putting Everything Together

with all those files in place (or just copied from the [softlayer-go](https://github.com/softlayer/softlayer-go) github) you should be able to compile and run this example CLI program.

```bash
cd $GOPATH/src/github.com/softlayer/softlayer-go/examples
go build
./examples server-list
Id, Hostname, Domain, IP Address
111111, host17.vmware, test.ibm.com, 160.40.20.110
222222, host16.vmware, test.ibm.com, 160.40.20.110

```

Now for any of the newer examples that return a cobra.Command object, you should just be able to copy/paste that into a file in the  `github.com/softlayer/softlayer-go/examples/cmd` directory, compile this example and use it.