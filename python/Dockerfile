FROM --platform=linux/amd64 python:3.8-slim
COPY python/requirements.txt ./requirements.txt
ENV PYTHONPATH /usr/src/app/

RUN apt-get update && apt-get install -y libsodium-dev gcc\
    && pip install --use-deprecated=legacy-resolver --no-cache-dir -r requirements.txt \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /usr/src/app/

COPY deploy/config_client ./config_client
COPY rest-api/rest_api_client ./rest_api_client
COPY rest-api/optscale_exceptions ./optscale_exceptions
COPY rest-api/cloud_adapter ./cloud_adapter
COPY herald/herald_client ./herald_client
COPY insider/insider_client ./insider_client
COPY metroculus/metroculus_client ./metroculus_client
COPY auth/auth_client ./auth_client
COPY rest-api/optscale_types ./optscale_types
COPY katara/katara_client ./katara_client
