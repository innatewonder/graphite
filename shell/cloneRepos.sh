#!/bin/bash

cd ..
echo "Cloning Repos..."
git clone https://github.com/innatewonder/onyx.git
git clone https://github.com/innatewonder/mythril.git
git clone https://github.com/innatewonder/opal.git

echo "Linking Directories..."
cd mythril/include
ln -s ../../onyx/include/networking/
ln -s ../../opal/include/audio/
cd ../src
ln -s ../../onyx/src/networking/
ln -s ../../opal/src/audio/

cd ../../opal/include
ln -s ../../onyx/include/networking/
ln -s ../../mythril/include/core
cd ../src
ln -s ../../onyx/src/networking/
ln -s ../../mythril/src/core

cd ../../onyx/include
ln -s ../../mythril/include/core
cd ../src
ln -s ../../mythril/src/core