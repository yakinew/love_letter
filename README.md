# love_letter
Generate a love letter to my wife using Gemini, and send it with my gmail account to my wife email.

## Gemini

### Generate Gemini API key

To generate a Gemini API key, go to https://ai.google.dev/gemini-api/docs/api-key to see some explainations about it, how to create a key, how to verify it and how to use it.

Finaliy, you need to set an environment variable with this key. Use a `.env` file for that.
```
GEMINI_API_KEY='<your-gemini-api-key>'
```

### Gemini Model
If you use a specific language model, you can set it in the `.env` file as well. For example:
```
GEMINI_MODEL='gemini-1.5-flash'
```


## GMail

### Gamil API key
To generate a Gamil API key, go to https://myaccount.google.com/apppasswords and create an "app password". The password should be a string of 4 groups of 4 letters each. Save the password in the `.env` file wiht no spaces.

```
MY_EMAIL_KEY='aabbccddeeffgghh'
```

### Email Addresses and Name

Set you email address and your wife email address as well.

```
MY_NAME='<your-name>'
MY_EMAIL='<your-account>@gmail.com'
WIFE_NAME='<your-wife-name>'
MY_WIFE_EMAIL='<your-wife-account>@gmail.com'
```


## Run the application

To run the love letter generator, you can use the `dockerize.sh`. This script build the docker image and run it with the enviroment variables from the `.env` file.
