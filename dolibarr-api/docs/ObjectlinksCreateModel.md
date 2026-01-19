# ObjectlinksCreateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data, see Example above for required parameters. Currently unused is relationtype. notrigger is default 0, which means to trigger, else set notrigger: 1 | [optional] 

## Example

```python
from dolibarr_api.models.objectlinks_create_model import ObjectlinksCreateModel

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectlinksCreateModel from a JSON string
objectlinks_create_model_instance = ObjectlinksCreateModel.from_json(json)
# print the JSON string representation of the object
print(ObjectlinksCreateModel.to_json())

# convert the object into a dict
objectlinks_create_model_dict = objectlinks_create_model_instance.to_dict()
# create an instance of ObjectlinksCreateModel from a dict
objectlinks_create_model_from_dict = ObjectlinksCreateModel.from_dict(objectlinks_create_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


