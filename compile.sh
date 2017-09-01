#!/bin/bash

rm -rf dist
rm -rf build
pyi-makespec -F --add-data "resources/*:resources" --additional-hooks-dir=hooks  main.py
pyinstaller main.spec