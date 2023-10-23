# freedompay-client.model.pay_pal_init_request.PayPalInitRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Commit** | bool,  | BoolClass,  |  | [optional] 
**Disabled** | bool,  | BoolClass,  |  | [optional] 
**DisableFunding** | str,  | str,  |  | [optional] 
**Intent** | str,  | str,  |  | [optional] must be one of ["Unknown", "AUTHORIZE", "CAPTURE", ] 
**InvoiceNumber** | str,  | str,  |  | [optional] 
**PaymentMethodPayeePreferred** | str,  | str,  |  | [optional] must be one of ["Unknown", "UNRESTRICTED", "IMMEDIATE_PAYMENT_REQUIRED", ] 
**ShippingPreference** | str,  | str,  |  | [optional] must be one of ["Unknown", "GET_FROM_FILE", "NO_SHIPPING", ] 
**TotalPrice** | str,  | str,  |  | [optional] 
**CountryCode** | str,  | str,  |  | [optional] 
**CurrencyCode** | str,  | str,  |  | [optional] 
**Debug** | bool,  | BoolClass,  |  | [optional] 
**Locale** | str,  | str,  |  | [optional] 
**CultureCode** | str,  | str,  |  | [optional] 
**EsKey** | str,  | str,  |  | [optional] 
**Legal** | [**LegalControl**](LegalControl.md) | [**LegalControl**](LegalControl.md) |  | [optional] 
**StoreId** | str,  | str,  |  | [optional] 
**Styles** | str,  | str,  |  | [optional] 
**TerminalId** | str,  | str,  |  | [optional] 
**ValidationMessageType** | str,  | str,  |  | [optional] must be one of ["Unknown", "None", "Feedback", "Tooltip", ] 
**ReferenceId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

