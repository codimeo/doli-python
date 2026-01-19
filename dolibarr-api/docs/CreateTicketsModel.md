# CreateTicketsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_tickets_model import CreateTicketsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTicketsModel from a JSON string
create_tickets_model_instance = CreateTicketsModel.from_json(json)
# print the JSON string representation of the object
print(CreateTicketsModel.to_json())

# convert the object into a dict
create_tickets_model_dict = create_tickets_model_instance.to_dict()
# create an instance of CreateTicketsModel from a dict
create_tickets_model_from_dict = CreateTicketsModel.from_dict(create_tickets_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


