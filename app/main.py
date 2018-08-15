#!/usr/bin/env python

__author__ = "Edwin van Rooij"

import pandas as pd
import json


def main(event, context):
    """Main application flow."""
    event = json.loads(event.get('body'))

    # Show all params for debugging
    print("MyEvent: ", event)
    print("MyContext: ", context)

    # Save titles to show later on
    strings_title = event.get("seriesStringsTitle")
    numbers_title = event.get("seriesNumbersTitle")

    # Turn lists into Series for DataFrames later on
    string_series = pd.Series(event.get("seriesStrings"))
    number_series = pd.Series(event.get("seriesNumbers"))

    # Create DataFrames to enable data manipulation
    strings_dataframe = pd.DataFrame([string_series])
    numbers_dataframe = pd.DataFrame([number_series])

    # Manipulate data
    # ...

    # Visualize strings data
    print("\n\n" + strings_title)
    print(strings_dataframe.head())

    # Visualize numbers data
    print("\n\n" + numbers_title)
    print(numbers_dataframe.head())

    # Return the DataFrames in JSON format
    string_json = json.dumps({
        strings_title: strings_dataframe.to_json(),
        numbers_title: numbers_dataframe.to_json()
    })

    # Must be in this format for Amazon API gateway
    return {
        'statusCode': 200,
        'body': string_json
    }


if __name__ == "__main__":

    # Represents the data you'd realistically send from a DimML script
    data = {
        "seriesStringsTitle": "A Series Of Strings",
        "seriesNumbersTitle": "A Series Of Numbers",
        "seriesStrings": ["value1", "value2", "value3", "value4"],
        "seriesNumbers": [1, 2, 3, 4, 5]
    }

    # Represents the data you'd receive on the lambda-function's end.
    # This is what you receive in the 'event' parameter after an HTTP request passed through an API gateway.
    event = {
        "resource": "/myPandasFunction",
        "path": "/myPandasFunction",
        "httpMethod": "POST",
        "headers": None,
        "queryStringParameters": None,
        "pathParameters": None,
        "stageVariables": None,
        "requestContext": {
            "path": "/myPandasFunction",
            "accountId": "857403979373",
            "resourceId": "4bzgzk",
            "stage": "test-invoke-stage",
            "requestId": "7f391dee-a069-11e8-86c2-2f4accb420be",
            "identity": {
                "cognitoIdentityPoolId": None,
                "cognitoIdentityId": None,
                "apiKey": "test-invoke-api-key",
                "cognitoAuthenticationType": None,
                "userArn": "arn:aws:iam::857403979373:root",
                "apiKeyId": "test-invoke-api-key-id",
                "userAgent": "aws-internal/3 aws-sdk-java/1.11.347 Linux/4.9.110-0.1.ac.201.71.329.metal1.x86_64 Java_HotSpot(TM)_64-Bit_Server_VM/25.172-b31 java/1.8.0_172",
                "accountId": "857403979373",
                "caller": "857403979373",
                "sourceIp": "test-invoke-source-ip",
                "accessKey": "ASIA4PIKCOZWXR3MC3U2",
                "cognitoAuthenticationProvider": None,
                "user": "857403979373"
            },
            "resourcePath": "/myPandasFunction",
            "httpMethod": "POST",
            "extendedRequestId": "LqG4RGi9IAMF2hQ=",
            "apiId": "1el503x4sk"
        },
        "body": json.dumps(data),
        "isBase64Encoded": False
    }

    print(main(event, None))
