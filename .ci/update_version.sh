#!/bin/bash

if [ $# -ne 1 ]
  then
    echo "No arguments supplied"
fi

version=${1}

cat > src/mint_upload/__init__.py <<EOF
# -*- coding: utf-8 -*-
__version__ = "${version}"
EOF
