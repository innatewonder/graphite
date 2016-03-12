@echo off

cd ..
echo "Cloning Repos..."
git clone https://github.com/innatewonder/onyx.git
git clone https://github.com/innatewonder/mythril.git

echo "Linking Directories..."
cd mythril\include
mklink /D networking ..\..\onyx\include\networking
cd ..\src
mklink /D networking ..\..\onyx\src\networking
cd ..\..\

@echo on