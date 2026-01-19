# BankaccountsTransferModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bankaccount_from_id** | **int** | BankAccount ID to use as the source of the internal wire transfer | 
**bankaccount_to_id** | **int** | BankAccount ID to use as the destination of the internal wire transfer | 
**var_date** | **str** | Date of the internal wire transfer (UNIX timestamp) | 
**description** | **str** | Description of the internal wire transfer | 
**amount** | **float** | Amount to transfer from the source to the destination BankAccount | 
**amount_to** | **float** | Amount to transfer to the destination BankAccount (only when accounts does not share the same currency) | [optional] 
**cheque_number** | **str** | Cheque numero | [optional] 

## Example

```python
from dolibarr_api.models.bankaccounts_transfer_model import BankaccountsTransferModel

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountsTransferModel from a JSON string
bankaccounts_transfer_model_instance = BankaccountsTransferModel.from_json(json)
# print the JSON string representation of the object
print(BankaccountsTransferModel.to_json())

# convert the object into a dict
bankaccounts_transfer_model_dict = bankaccounts_transfer_model_instance.to_dict()
# create an instance of BankaccountsTransferModel from a dict
bankaccounts_transfer_model_from_dict = BankaccountsTransferModel.from_dict(bankaccounts_transfer_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


