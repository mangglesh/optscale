REGISTRY=$1


build_n_push(){
NAME=$1
DOCKERFILE_PATH=$2
CONTEXT_PATH=$3
IMAGE_REGISTRY=$REGISTRY"/"$NAME":latest"
echo "docker build -f $DOCKERFILE_PATH -t $IMAGE_REGISTRY $CONTEXT_PATH"
docker build -f $DOCKERFILE_PATH -t $IMAGE_REGISTRY $CONTEXT_PATH

echo "docker push $IMAGE_REGISTRY -q"
docker push $IMAGE_REGISTRY
}
build_n_push "optscale-rest-api-server" "rest-api/Dockerfile" "rest-api/"

build_n_push "optscale-auth" "auth/Dockerfile" "auth/"

build_n_push "optscale-bumi_scheduler" "bumi_scheduler/Dockerfile" "bumi_scheduler/"

build_n_push "optscale-diworker" "diworker/Dockerfile" "diworker/"

build_n_push "optscale-herald_server_engine" "herald/Dockerfile" "herald/"

build_n_push "optscale-herald_server_api" "herald/Dockerfile" "herald/"

build_n_push "optscale-katara_service_scheduler" "katara/Dockerfile_service" "katara/"

build_n_push "optscale-katara_service_api" "katara/Dockerfile_service" "katara/"

build_n_push "optscale-katara_worker" "katara/Dockerfile_worker" "katara/"

build_n_push "optscale-resource_discovery_scheduler" "deploy/docker_images/resource_discovery/Dockerfile" "deploy/docker_images/resource_discovery/"

build_n_push "optscale-resource_discovery_worker" "deploy/docker_images/resource_discovery/Dockerfile_worker" "deploy/docker_images/resource_discovery/"

build_n_push "optscale-metroculus_api" "metroculus/metroculus_api/Dockerfile" "metroculus/"

build_n_push "optscale-metroculus_scheduler" "metroculus/metroculus_scheduler/Dockerfile" "metroculus/"

build_n_push "optscale-metroculus_worker" "metroculus/metroculus_worker/Dockerfile" "metroculus/"

build_n_push "optscale-insider_api" "insider/insider_api/Dockerfile" "insider/"

build_n_push "optscale-insider_scheduler" "insider/insider_scheduler/Dockerfile" "insider/"

build_n_push "optscale-insider_worker" "insider/insider_worker/Dockerfile" "insider/"

build_n_push "optscale-trapper_scheduler" "trapper/trapper_scheduler/Dockerfile" "trapper/"

build_n_push "optscale-trapper_worker" "trapper/trapper_worker/Dockerfile" "trapper/"