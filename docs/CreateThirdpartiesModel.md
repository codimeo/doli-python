# CreateThirdpartiesModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_thirdparties_model import CreateThirdpartiesModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateThirdpartiesModel from a JSON string
create_thirdparties_model_instance = CreateThirdpartiesModel.from_json(json)
# print the JSON string representation of the object
print(CreateThirdpartiesModel.to_json())

# convert the object into a dict
create_thirdparties_model_dict = create_thirdparties_model_instance.to_dict()
# create an instance of CreateThirdpartiesModel from a dict
create_thirdparties_model_from_dict = CreateThirdpartiesModel.from_dict(create_thirdparties_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


