# TicketsCreateNewMessageModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.tickets_create_new_message_model import TicketsCreateNewMessageModel

# TODO update the JSON string below
json = "{}"
# create an instance of TicketsCreateNewMessageModel from a JSON string
tickets_create_new_message_model_instance = TicketsCreateNewMessageModel.from_json(json)
# print the JSON string representation of the object
print(TicketsCreateNewMessageModel.to_json())

# convert the object into a dict
tickets_create_new_message_model_dict = tickets_create_new_message_model_instance.to_dict()
# create an instance of TicketsCreateNewMessageModel from a dict
tickets_create_new_message_model_from_dict = TicketsCreateNewMessageModel.from_dict(tickets_create_new_message_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


