# BankaccountsAddLinkModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url_id** | **int** | ID to set in the URL | 
**url** | **str** | URL of the link | 
**label** | **str** | Label | 
**type** | **str** | Type of link (&#39;payment&#39;, &#39;company&#39;, &#39;member&#39;, ...) | 

## Example

```python
from dolibarr_api.models.bankaccounts_add_link_model import BankaccountsAddLinkModel

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountsAddLinkModel from a JSON string
bankaccounts_add_link_model_instance = BankaccountsAddLinkModel.from_json(json)
# print the JSON string representation of the object
print(BankaccountsAddLinkModel.to_json())

# convert the object into a dict
bankaccounts_add_link_model_dict = bankaccounts_add_link_model_instance.to_dict()
# create an instance of BankaccountsAddLinkModel from a dict
bankaccounts_add_link_model_from_dict = BankaccountsAddLinkModel.from_dict(bankaccounts_add_link_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


