# CreatePartnershipsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_partnerships_model import CreatePartnershipsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePartnershipsModel from a JSON string
create_partnerships_model_instance = CreatePartnershipsModel.from_json(json)
# print the JSON string representation of the object
print(CreatePartnershipsModel.to_json())

# convert the object into a dict
create_partnerships_model_dict = create_partnerships_model_instance.to_dict()
# create an instance of CreatePartnershipsModel from a dict
create_partnerships_model_from_dict = CreatePartnershipsModel.from_dict(create_partnerships_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


