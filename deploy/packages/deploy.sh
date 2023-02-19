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
        twine upload $FILE
    done
fi

# remove generated files
rm ./setup.py
rm -rf ./build
rm -rf ./dist
rm -rf ./*.egg-info

#export TWINE_USERNAME=aws
#export TWINE_PASSWORD=`aws codeartifact get-authorization-token --domain nudgebee --domain-owner 280501305789 --query authorizationToken --output text --profile nudgebee`
#export TWINE_REPOSITORY_URL=`aws codeartifact get-repository-endpoint --domain nudgebee --domain-owner 280501305789 --repository nudgebee-pypi --format pypi --query repositoryEndpoint --output text --region us-east-1 --profile nudgebee`