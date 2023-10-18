## Steps to build the app
### 1. Preparation:
Ensure you have Azure CLI installed. If not, install it.
Install Azure Functions Core Tools. It's needed to create and deploy the Azure Functions:

```npm install -g azure-functions-core-tools@3 --unsafe-perm true```

Login to your Azure account:

```az login```

### 2. Flask App for Azure Functions:
Create a new directory for your Azure Function and navigate to it:

```mkdir AZ-Function-App```

Now, initialize a Python-based Azure Functions project in this dir:


```func init --worker-runtime python```

Then, create a new function:

```func new --template "HTTP trigger" --name HiBob ```

Update the code in HiBob/__init__.py with.

For simplicity, in the HiBob/function.json file (related to the Azure Function you've created), make sure that the authLevel is set to anonymous. Setting authLevel to anonymous means no API key is required to access the function.

### 3. Deploy the Function App to Azure:

Create a resource group in Azure:

```az group create --name hris_temp_rg --location canadacentral```

Create a storage account required by the Function App:

```az storage account create --name sotrage182658 --location canadacentral --resource-group hris_temp_rg --sku Standard_LRS```

Create the Function App:

```az functionapp create --resource-group hris_temp_rg --consumption-plan-location canadacentral --runtime python --runtime-version 3.8 --functions-version 3 --name hris --storage-account sotrage182658 --os-type Linux```

Deploy the Function App:

From within AZ-Function-App directory, zip the deployment in pwsh terminal:

```Compress-Archive -Path * -DestinationPath deploy.zip```

and finally, publish your function app:

```az webapp deployment source config-zip --resource-group hris_temp_rg --name hris --src deploy.zip```


### 4. Access the Function App:
After deploying, your function will be accessible via:


https://hris.azurewebsites.net/api/Hibob


## Business Requirements

### 1. Data Source

https://hris.azurewebsites.net/api/Hibob


### 2. Transformation Rules

for each row of the data create a "CERTIFICATE" and "ADDRESS" record. Add a "HEADER" on the top with the static values, and a "TRAILER" with the count of the records (if three rows are available from the REST API, trailer count would be 3 x 2 = 6).

```
HEADER|99999|quwiqi|
CERTIFICATE|<name>|<age>||||
ADDRESS|<city>|<country>|
TRAILER|<count the rows; i.e. 2>
```

### 3. create a text file

Dumpt above data into a text file and name it poc.txt.

### 4. SFTP

TBD