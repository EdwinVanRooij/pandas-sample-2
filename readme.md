# Installation & usage instructions

## Development

Install pandas locally

`sudo python3 -m pip install --upgrade pandas`

Create a python3 virtualenv locally*

`virtualenv -p python3 .`

Activate virtualenv

`source bin/activate`

or (based upon which shell you're using)

`source bin/activate.fish`

`pip3 install pandas`

> \* installing the virtualenv tool is different per operating system, google how to do this for yours

## Deployment

Create package (run from `app/`)

`zip -g PandasSample.zip main.py`

Add libraries (run from `lib/python3.6/site-packages`\*\*)

`zip -r9 ../../../app/PandasSample.zip .`

> \*\* this directory may be different for various operating systems, see [here](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html#deployment-pkg-for-virtualenv)



__Below is deprecated.__
_This is the final command to create a zip in one line, when running Linux with the Fish shell interpreter, from `app/`._
`zip -g PandasSample.zip main.py; and zip -r9 PandasSample.zip ../lib/python3.6/site-packages/`


## Notes

There are 4 different testing scenario's to accomplish the use case @ Peter's mail:

- 1. Testing the lambda locally using a locally-defined test event (in the python script).
This is the first stage. Everything should work here before moving on.
We're verifying if the base functionality of the script works here.

- 2. Testing the lambda directly from the web interface using a there-defined test event.
This is the second step. Upload the local environment to aws lambda, check if it works there.
It's required to replicate the test event locally into a json test event on the web interface here.


- 3. Testing the lambda via the web interface using an API gateway.
This adds another conversion layer to the test event. This means that the initial test event is not as you define it. When you add a way to connect to the lambda using the HTTP protocol, so by using the AWS API gateway, this gateway transforms the event you sent in the http post body. It adds a lot of meta data to it, like this:
```
            "resource": "/myPandasFunction",
            "path": "/myPandasFunction",
            "httpMethod": "POST",
            "body": "{\n        \"seriesStringsTitle\": \"A Series Of Strings\",\n        \"seriesNumbersTitle\": \"A Series Of Numbers\",\n        \"seriesStrings\": [\"value1\", \"value2\", \"value3\", \"value4\"],\n        \"seriesNumbers\": [1, 2, 3, 4, 5]\n    }",
            "isBase64Encoded": False
    }
```
Where `body` in `input` is the only thing you've passed it (through the http post request body).
It's necessary to change the python script after adding an api gateway, because the `event` param now contains all of the extra meta data, instead of just the previous `event`.
(It's also necessary to change the test event when directly testing the lambda using the lambda test web interface, because the script will now expect the meta data.)

- 4. Testing the lambda via CURL using an API gateway.
For some reason there's a difference between testing the api gateway through curl (or any other http client) and the amazon api gateway testing interface.
