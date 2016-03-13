@echo off

cd ..
echo "Cloning Repos..."
git clone https://github.com/innatewonder/onyx.git
git clone https://github.com/innatewonder/mythril.git
git clone https://github.com/innatewonder/opal.git

echo "Linking Directories..."
cd mythril\include
mklink /D networking ..\..\onyx\include\networking
mklink /D audio ..\..\opal\include\audio
cd ..\src
mklink /D networking ..\..\onyx\src\networking
mklink /D audio ..\..\opal\src\audio

cd ..\..\opal\include
mklink /D networking ..\..\onyx\include\networking
mklink /D core ..\..\mythril\include\core
cd ..\src
mklink /D networking ..\..\onyx\src\networking
mklink /D core ..\..\mythril\src\core

cd ../../onyx/include
mklink /D core ..\..\mythril\include\core
cd ../src
mklink /D core ..\..\mythril\src\core

@echo on