#!/bin/bash

export PKG_DIR="python/lib/python3.8/site-packages/"

mkdir temp && cd temp
rm -rf ${PKG_DIR} && mkdir -p ${PKG_DIR}

docker run --rm -v $(pwd):/temp -w /temp lambci/lambda:build-python3.8 \
    pip3 install -t ${PKG_DIR} pynacl

zip -r pynacl_layer.zip *