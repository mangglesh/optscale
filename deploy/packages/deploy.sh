#!/bin/bash
set -e

# copy setup files

TEMP_DIR=/tmp/nudgebee-pip-install

rm -rf $TEMP_DIR || true
mkdir -p $TEMP_DIR
cp -r $1 $TEMP_DIR/
cp ./deploy/packages/setup.py $TEMP_DIR

cd $TEMP_DIR
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

#export TWINE_USERNAME=aws
#export TWINE_PASSWORD=`aws codeartifact get-authorization-token --domain nudgebee --domain-owner 280501305789 --query authorizationToken --output text --profile nudgebee`
#export TWINE_REPOSITORY_URL=`aws codeartifact get-repository-endpoint --domain nudgebee --domain-owner 280501305789 --repository nudgebee-pypi --format pypi --query repositoryEndpoint --output text --region us-east-1 --profile nudgebee`