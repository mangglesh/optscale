#!/bin/bash
set -e

# copy setup files
cp ./deploy/packages/setup.py $1/
cd $1
python setup.py sdist

# deploy files
if [[ $2 == "deploy" ]]
then
    for FILE in ./dist/*
    do
        echo "Uploading File > $FILE";
        twine upload --repository codeartifact $FILE
    done
fi

# remove generated files
rm ./setup.py
rm -rf ./build
rm -rf ./dist
rm -rf ./*.egg-info