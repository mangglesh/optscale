#!/bin/bash
set -e


bash deploy/packages/deploy.sh deploy/config_client $1
bash deploy/packages/deploy.sh rest-api/rest_api_client $1
bash deploy/packages/deploy.sh rest-api/optscale_exceptions $1
bash deploy/packages/deploy.sh rest-api/cloud_adapter $1
bash deploy/packages/deploy.sh herald/herald_client $1
bash deploy/packages/deploy.sh insider/insider_client $1
bash deploy/packages/deploy.sh metroculus/metroculus_client $1
bash deploy/packages/deploy.sh auth/auth_client $1
bash deploy/packages/deploy.sh rest-api/optscale_types $1
bash deploy/packages/deploy.sh katara/katara_client $1
