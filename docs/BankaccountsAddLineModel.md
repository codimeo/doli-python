# BankaccountsAddLineModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Payment date (timestamp) | 
**type** | **str** | Payment mode (TYP,VIR,PRE,LIQ,VAD,CB,CHQ...) | 
**label** | **str** | Label | 
**amount** | **float** | Amount (may be 0) | 
**category** | **int** | Category | [optional] 
**cheque_number** | **str** | Cheque numero | [optional] 
**cheque_writer** | **str** | Name of cheque writer | [optional] 
**cheque_bank** | **str** | Bank of cheque writer | [optional] 
**accountancycode** | **str** | Accountancy code | [optional] 
**datev** | **str** | Payment date value (timestamp) | [optional] 
**num_releve** | **str** | Bank statement numero | [optional] 

## Example

```python
from dolibarr_api.models.bankaccounts_add_line_model import BankaccountsAddLineModel

# TODO update the JSON string below
json = "{}"
# create an instance of BankaccountsAddLineModel from a JSON string
bankaccounts_add_line_model_instance = BankaccountsAddLineModel.from_json(json)
# print the JSON string representation of the object
print(BankaccountsAddLineModel.to_json())

# convert the object into a dict
bankaccounts_add_line_model_dict = bankaccounts_add_line_model_instance.to_dict()
# create an instance of BankaccountsAddLineModel from a dict
bankaccounts_add_line_model_from_dict = BankaccountsAddLineModel.from_dict(bankaccounts_add_line_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


