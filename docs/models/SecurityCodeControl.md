# freedompay-client.model.security_code_control.SecurityCodeControl

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LabelType** | str,  | str,  |  | [optional] must be one of ["Unknown", "Default", "Required", "IfPresent", "Optional", "NotAvailable", "PinDefault", ] 
**MaskType** | str,  | str,  |  | [optional] must be one of ["Default", "None", "Blur", "Keypress", ] 
**PlaceholderType** | str,  | str,  |  | [optional] must be one of ["Unknown", "Blank", "Default", "Cvc", "Cvv", "CvcNumber", "CvvNumber", "Pin", ] 
**ValidationType** | str,  | str,  |  | [optional] must be one of ["Unknown", "NotApplicable", "Optional", "Required", "OptionalExplicit", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

