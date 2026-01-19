# UpdateInterventionsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.update_interventions_model import UpdateInterventionsModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateInterventionsModel from a JSON string
update_interventions_model_instance = UpdateInterventionsModel.from_json(json)
# print the JSON string representation of the object
print(UpdateInterventionsModel.to_json())

# convert the object into a dict
update_interventions_model_dict = update_interventions_model_instance.to_dict()
# create an instance of UpdateInterventionsModel from a dict
update_interventions_model_from_dict = UpdateInterventionsModel.from_dict(update_interventions_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


