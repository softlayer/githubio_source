# Contributing to SLDN


## Procedural

1. Fork the [githubio_source](https://github.com/softlayer/githubio_source) repository
2. Make your changes. All of the pages on sldn.softlayer.com are from the `/content` directory. The only exception is the `/content/reference` directory, which is automatically generated, and shouldn't be edited manually.
3. Create a pull request into the master branch
4. Your request will be reviewed according to the requirements rules below.
5. Once your request is merged in, an automated build will regenerate the HTML and be merged into the official SLDN repo.


## Requirements

A good example should meet the following criteria

1. Have multiple API call examples
2. If `id`s are required, have an example of how to get the `id`s appropriate for use with the API call you are making an example for
3. Example should do something useful with the output, such as displaying a table of useful information, or printing a "Success" message if the API just returns a boolean value
4. Use an `objectMask` if the function accepts one
5. Use an `objectFilter` if the function accepts one
6. Use a `resultLimit` if the fuction returns an array
7. If the function takes in parameters, explain how to get valid values for them.
8. Language specific examples should use the official SoftLayer library
9. doc blocks should have the language specifified
`````
like this
```python
def some_function():
    pass
```
`````
10. Have some "plain english" explanations for what API calls do, even if its obvious from the function name.