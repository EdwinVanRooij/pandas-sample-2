#!/usr/bin/env python

__author__ = "Edwin van Rooij"

import pandas as pd
import json


def main(event, context):
    """Main application flow."""
    # Show all params for debugging
    print(event)
    print(context)

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
    return json.dumps({
        strings_title: strings_dataframe.to_json(),
        numbers_title: numbers_dataframe.to_json()
    })


if __name__ == "__main__":
    event = {
        "seriesStringsTitle": "A Series Of Strings",
        "seriesNumbersTitle": "A Series Of Numbers",
        "seriesStrings": ["value1", "value2", "value3", "value4"],
        "seriesNumbers": [1, 2, 3, 4, 5]
    }
    print(main(event, None))
