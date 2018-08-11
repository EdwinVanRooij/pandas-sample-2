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

Add libraries (run from `app/`)

`zip -r9 PandasSample.zip ../lib/python3.6/site-packages/` **

> \*\* this directory may be different for various operating systems, see [here](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html#deployment-pkg-for-virtualenv)



_This is the final command to create a zip in one line, when running Linux with the Fish shell interpreter, from `app/`._
`zip -g PandasSample.zip main.py; and zip -r9 PandasSample.zip ../lib/python3.6/site-packages/`
