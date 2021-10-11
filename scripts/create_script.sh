#!/bin/bash
# https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-create-package-with-dependency

rm -rf temp my-deployment-package.zip && mkdir temp
pip install --target ./temp boto3 python-dotenv

cd temp && zip -r ../my-deployment-package.zip .
cd ../bot && zip -g ../my-deployment-package.zip *.py .env