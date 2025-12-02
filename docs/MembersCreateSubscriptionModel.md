# MembersCreateSubscriptionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Start date | 
**end_date** | **str** | End date | 
**amount** | **float** | Amount (may be 0) | 
**label** | **str** | Label | [optional] 

## Example

```python
from dolibarr_api.models.members_create_subscription_model import MembersCreateSubscriptionModel

# TODO update the JSON string below
json = "{}"
# create an instance of MembersCreateSubscriptionModel from a JSON string
members_create_subscription_model_instance = MembersCreateSubscriptionModel.from_json(json)
# print the JSON string representation of the object
print(MembersCreateSubscriptionModel.to_json())

# convert the object into a dict
members_create_subscription_model_dict = members_create_subscription_model_instance.to_dict()
# create an instance of MembersCreateSubscriptionModel from a dict
members_create_subscription_model_from_dict = MembersCreateSubscriptionModel.from_dict(members_create_subscription_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


