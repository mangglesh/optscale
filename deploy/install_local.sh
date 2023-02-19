#!/bin/bash
set -e


bash deploy/packages/deploy.sh deploy/config_client
bash deploy/packages/deploy.sh rest-api/rest_api_client
bash deploy/packages/deploy.sh rest-api/optscale_exceptions
bash deploy/packages/deploy.sh rest-api/cloud_adapter
bash deploy/packages/deploy.sh herald/herald_client
bash deploy/packages/deploy.sh insider/insider_client
bash deploy/packages/deploy.sh metroculus/metroculus_client
bash deploy/packages/deploy.sh auth/auth_client
bash deploy/packages/deploy.sh rest-api/optscale_types
bash deploy/packages/deploy.sh katara/katara_client
