# UpdateTicketsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Data | [optional] 

## Example

```python
from dolibarr_api.models.update_tickets_model import UpdateTicketsModel

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTicketsModel from a JSON string
update_tickets_model_instance = UpdateTicketsModel.from_json(json)
# print the JSON string representation of the object
print(UpdateTicketsModel.to_json())

# convert the object into a dict
update_tickets_model_dict = update_tickets_model_instance.to_dict()
# create an instance of UpdateTicketsModel from a dict
update_tickets_model_from_dict = UpdateTicketsModel.from_dict(update_tickets_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


