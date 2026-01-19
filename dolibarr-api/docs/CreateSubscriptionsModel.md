# CreateSubscriptionsModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_data** | **List[str]** | Request data | [optional] 

## Example

```python
from dolibarr_api.models.create_subscriptions_model import CreateSubscriptionsModel

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSubscriptionsModel from a JSON string
create_subscriptions_model_instance = CreateSubscriptionsModel.from_json(json)
# print the JSON string representation of the object
print(CreateSubscriptionsModel.to_json())

# convert the object into a dict
create_subscriptions_model_dict = create_subscriptions_model_instance.to_dict()
# create an instance of CreateSubscriptionsModel from a dict
create_subscriptions_model_from_dict = CreateSubscriptionsModel.from_dict(create_subscriptions_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


