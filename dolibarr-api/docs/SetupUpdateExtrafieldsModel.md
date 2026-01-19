# SetupUpdateExtrafieldsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.setup_update_extrafields_model import SetupUpdateExtrafieldsModel

# TODO update the JSON string below
json = "{}"
# create an instance of SetupUpdateExtrafieldsModel from a JSON string
setup_update_extrafields_model_instance = SetupUpdateExtrafieldsModel.from_json(json)
# print the JSON string representation of the object
print(SetupUpdateExtrafieldsModel.to_json())

# convert the object into a dict
setup_update_extrafields_model_dict = setup_update_extrafields_model_instance.to_dict()
# create an instance of SetupUpdateExtrafieldsModel from a dict
setup_update_extrafields_model_from_dict = SetupUpdateExtrafieldsModel.from_dict(setup_update_extrafields_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


