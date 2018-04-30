---
title: "Getting started with the Cloud Foundry and Bluemix Command Line Utilities"
description: "In order to fully utilize the power of your Bluemix account it is recommended to install the [Cloud Foundry](https://www"
date: "2016-06-14"
author: "rtiffany"
tags:
    - "blog"
---

In order to fully utilize the power of your Bluemix account it is recommended to install the [Cloud Foundry](https://www.cloudfoundry.org/) and [Bluemix](https://new-console.ng.bluemix.net) command line clients. This guide will walk you through that process as well as some of the basic command line options.

## Installing Cloud Foundry Command Line Client
Please see our [Knowledgelayer Guide](http://knowledgelayer.softlayer.com/articles/bluemix-and-cloud-foundry-command-line-utilities) on how to install the Cloud Foundry CLI.

Once installed you will use the `cf` command when interacting with Cloud Foundry applications and your Bluemix account. 

### Basic cf commands

**cf api**
Set the API endpoint. The `cf api` command allows you to set the region that you will be interacting with from the command line.  

    $ cf api https://api.{DomainName}

**cf login**
The `cf login` command logs you in to the specific account, API endpoint, space and organization that you specify. If you simply invoke `cf login` you will be prompted to fill out the information, otherwise you can use the following command to log in to the specific Org and Space where your apps and services reside.

    $ cf login [-a API_ENDPOINT] [-u USERNAME] [-p PASSWORD] [-o ORG] [-s SPACE]

**cf marketplace**
Lists all of the services that are available in the marketplace. The services listed by this command are also shown in the [Bluemix Catalog](https://new-console.ng.bluemix.net/catalog/).

**cf push**
The push command is used to deploy a new application to Bluemix, or update an existing application if you have made local changes to the configuration. The push command uses the applications [manifest.yml](https://new-console.ng.bluemix.net/docs/manageapps/depapps.html#appmanifest) file to determine how the application is deployed if no command line options are specified.

    $ cf push APP_NAME

    # Specify the applications configuration when pushing the app
    $ cf push APP_NAME [-b BUILDPACK_NAME] [-d DOMAIN] [-f MANIFEST_PATH] [-i NUM_INSTANCES] [-k DISK] [-m MEMORY]

**cf scale**
Displays or changes the instance number, disk space limit, and memory limit for an application.

    $ cf scale APP_NAME [-i NUM_INSTANCES] [-k DISK] [-m MEMORY]

**cf set-env**
Sets an environment variable for an application. These can also be [specified](https://docs.cloudfoundry.org/devguide/deploy-apps/manifest.html#env-block) in the applications manifest.yml file.

    $ cf set-env APP_NAME

**cf help**
Displays help information for all cf commands, or for a specific cf command if the command_name parameter is used.

    $ cf help (will display all options)  
    $ cf help command_name (will display the help section of a specific command)

### Interacting with Bluemix containers using cf
You can use the Cloud Foundry command line to interact with [IBM Containers](https://new-console.ng.bluemix.net/docs/containers/container_index.html#container_index) by installing the `ic` container plugin using the following [guide](https://new-console.ng.bluemix.net/docs/containers/container_cli_cfic.html). Once installed you can use the command `cf ic` to interact with your IBM containers instead of the `docker` command.

**cf ic [COMMAND]**

    # For examaple, to build a container from a Dockerfile and push it to Bluemix you would use `cf ic build` in place of `docker build`
    $ cf ic build -t NAME_OF_CONTAINER . 

See [here](https://new-console.ng.bluemix.net/docs/containers/container_cli_reference_native-docker.html#container_cli_reference_native-docker) for the full rundown on supported docker commands when using the `ic` plugin. 

### Installing the Bluemix Command Line client
Please see our [Knowledgelayer Guide](http://knowledgelayer.softlayer.com/articles/bluemix-and-cloud-foundry-command-line-utilities) on how to install the Bluemix CLI.

## Basic bluemix commands
Except for the OpenStack CLI tool that is used for Virtual Servers management, the Cloud Foundry cf command line tool is a prerequisite for all other Bluemix CLI tools. The Bluemix CLI provides an extended experience to manage your Bluemix environment above and beyond the management of Cloud Foundry applications. The CLI can be invoked using the command `bluemix` or `bx`.

**bx api**
As with `cf`, the `bx api` command allows you to set the region that you will be interacting with from the command line.

    $ bx api https://api.{DomainName}

**bx login**
The `bx login` command logs you in to the specific account, API endpoint, space and organization that you specify. If you simply invoke `bx login` you will be prompted to fill out the information, otherwise you can use the following command to log in to the specific Org and Space where your apps and services reside.

    $ bx login [-a API_ENDPOINT] [-u USERNAME] [-p PASSWORD] [-o ORG] [-s SPACE]

**bx list**
List all Cloud Foundry applications, services, containers, and virtual servers in the targeted organization and space.

**bx iam**
Allows for the creation and management of organizations, spaces and users on a Bluemix Account.

    $ bx iam

To create a new organization for example, issue the command `bx iam org-create NEW_ORG_NAME`

    $ bx iam org-create MyNewBluemixTestingOrg
    Creating org MyNewBluemixTestingOrg as ryan@tinylab.info...
    OK

    TIP: Use 'bx target -o MyNewBluemixTestingOrg' to target new org

**bx service**
List, create, update, delete, and bind Bluemix Services. You can also use the command `bx offerings` to list all of the available service offerings in the marketplace.

    # Create a new Auto-Scale service using the free tier.
    $ bx service create Auto-Scaling free MyNewAutoScaleService

    # Bind our new Auto-Scaling service to an existing application.
    $ bx service bind MyGreatApp MyNewAutoScaleService

**bx cf**
Run the Cloud Foundry CLI with Bluemix context. This is used when a Bluemix CLI sub-command is needed to replicate a `cf` sub-command that is not natively built in to the `bx` command.

## More information
[Bluemix cf Quick Reference Card](ftp://public.dhe.ibm.com/cloud/bluemix/cli_reference_card.pdf)  


