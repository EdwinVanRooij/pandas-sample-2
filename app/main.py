#!/usr/bin/env python

__author__ = "Edwin van Rooij"

import pandas as pd
import json


def main(event, context):
    """Main application flow."""
    # event = event.get('input').get('body')
    # event = json.loads(event.get('input').get('body'))
    #
    # # Show all params for debugging
    # print("MyEvent: ", event)
    # print("MyContext: ", context)
    #
    # # Save titles to show later on
    # strings_title = event.get("seriesStringsTitle")
    # numbers_title = event.get("seriesNumbersTitle")
    #
    # # Turn lists into Series for DataFrames later on
    # string_series = pd.Series(event.get("seriesStrings"))
    # number_series = pd.Series(event.get("seriesNumbers"))
    #
    # # Create DataFrames to enable data manipulation
    # strings_dataframe = pd.DataFrame([string_series])
    # numbers_dataframe = pd.DataFrame([number_series])
    #
    # # Manipulate data
    # # ...
    #
    # # Visualize strings data
    # print("\n\n" + strings_title)
    # print(strings_dataframe.head())
    #
    # # Visualize numbers data
    # print("\n\n" + numbers_title)
    # print(numbers_dataframe.head())
    #
    # # Return the DataFrames in JSON format
    # string_json = json.dumps({
    #     strings_title: strings_dataframe.to_json(),
    #     numbers_title: numbers_dataframe.to_json()
    # })

    # Must be in this format for Amazon API gateway
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps({'input': 'something more',
    #                         'busy': "something",
    #                         'guest_email': "something"})
    # }
    return {
        'statusCode': 200,
        'body': json.dumps({'input': event,
                            'busy': 'busyy',
                            'guest_email': 'emaill'})
    }


if __name__ == "__main__":
    # event = {
    #     "seriesStringsTitle": "A Series Of Strings",
    #     "seriesNumbersTitle": "A Series Of Numbers",
    #     "seriesStrings": ["value1", "value2", "value3", "value4"],
    #     "seriesNumbers": [1, 2, 3, 4, 5]
    # }
    event = {
        "input": {
            "resource": "/myPandasFunction",
            "path": "/myPandasFunction",
            "httpMethod": "POST",
            "body": "{\n        \"seriesStringsTitle\": \"A Series Of Strings\",\n        \"seriesNumbersTitle\": \"A Series Of Numbers\",\n        \"seriesStrings\": [\"value1\", \"value2\", \"value3\", \"value4\"],\n        \"seriesNumbers\": [1, 2, 3, 4, 5]\n    }",
            "isBase64Encoded": False
        },
        "busy": "something",
        "guest_email": "something"
    }
    print(main(event, None))
