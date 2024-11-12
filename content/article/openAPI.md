---
title: "Open API Definitions for SLDN"
description: "Introducing OpenAPI spec sheet for SLDN api"
date: "2024-11-12"
tags:
    - "article"
    - "sldn"
---

# [Open API](https://swagger.io/specification/)

We now have tenative support for an Open API spec. You can download it from [SLDN](/openapi/sl_openapi.json)

Due to the way SLDN is designed, the spec sheet is fairly lengthy and a bit complicated, but perhaps it will be useful.


# Generation

If you are interested in how the file is generated, check out [bin/generateOpenAPI.py](https://github.com/softlayer/githubio_source/tree/master/bin/generateOpenAPI.py)

[OpenAPI CLI](https://openapi-generator.tech/docs/installation) Can be used to generate HTML or whatever else from this document.
```
$> mkdir generated
$> wget https://sldn.softlayer.com/static/openapi/sl_openapi.json
$> java -jar openapi-generator-cli.jar  generate -g html -i sl_openapi.json -o generated/ --skip-operation-example
```

You will need the `--skip-operation-example` option otherwise openapi-generator-cli will run out of memory building SLDN objects.