#!/bin/bash

cd ..
echo "Cloning Repos..."
git clone https://github.com/innatewonder/onyx.git
git clone https://github.com/innatewonder/mythril.git

echo "Linking Directories..."
cd mythril/include
ln -s ../../onyx/include/networking/
cd ../src
ln -s ../../onyx/src/networking/
cd ../../
