# minikube

minikube start   --container-runtime=docker  --v=10 --alsologtostderr --cpus 2 --memory 8192

minikube start
minikube dashboard

# Argo
kubectl create ns argo &&
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/stable/manifests/install.yaml &&
kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=argo:default --namespace=argo

kubectl -n argo port-forward deployment/argo-server 2746:2746 &&
 &&
*****

# minio

helm install --namespace=argo argo-artifacts stable/minio --set service.type=LoadBalancer --set fullnameOverride=argo-artifacts

kubectl port-forward service/argo-artifacts -n argo 9000:9000

### Patch 
kubectl -n argo patch configmap/workflow-controller-configmap --patch "$(cat ./minio-modified-minio.yaml)"



# argo-events
kubectl create ns argo-events &&

kubectl apply -f  https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/install.yaml

kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/eventbus/native.yaml

demo@demo:~$ kubectl apply -f  https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/install.yaml


kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=argo-events:default --namespace=argo-events



# Install with a validating admission controller
kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/install-validating-webhook.yaml

kubectl -n argo-events apply -f https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/eventbus/native.yaml



# Argo Samples
https://github.com/argoproj/argo-workflows/blob/master/examples/README.md
https://github.com/argoproj/argo-workflows/tree/master/examples

argo submit --watch -n argo https://raw.githubusercontent.com/argoproj/argo-workflows/master/examples/steps.yaml

# Argo Events Samples

git clone https://github.com/vfarcic/argo-events-demo.git

kubectl -n argo-events apply -f https://raw.githubusercontent.com/vfarcic/argo-events-demo/master/event-source.yaml
kubectl -n argo-events apply -f https://raw.githubusercontent.com/vfarcic/argo-events-demo/master/sensor.yaml



kubectl -n argo-events apply -f 01event-source-test-01.yaml
kubectl -n argo-events apply -f 01event-sensor-test-01.yaml


kubectl -n argo-events port-forward service/webhook-eventsource-svc 12000:12000
kubectl -n argo-events get eventsource

curl -X POST -H "Content-Type: application/json"   -d '{"message":"this is my first webhook"}'  http://localhost:12000/devops-toolkit

https://www.youtube.com/watch?v=sUPkGChvD54

# Argo Events Workflow

kubectl -n argo-events apply -f https://raw.githubusercontent.com/



#
#



# Setup

## Install Minikube

### Linux
Nota: Este documento muestra cómo instalar Minikube en Linux usando un ejecutable autocontenido. Para métodos alternativos de instalación en Linux, ver Otros métodos de Instalación en el repositorio GitHub oficial de Minikube.
Puedes instalar Minikube en Linux descargando un ejecutable autocontenido:

curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube
Para tener disponible en la consola el comando minikube, puedes añadir el comando al $PATH o moverlo por ejemplo a /usr/local/bin:

sudo cp minikube /usr/local/bin && rm minikube



 <!-- Actual text -->

You can find me on [![Twitter][1.2]][1], or on [![LinkedIn][2.2]][2]
<!-- Icons -->

[1.2]: https://github.com/geoinca/miniok/blob/main/img/tw.png 

[2.2]: https://github.com/geoinca/miniok/blob/main/img/lk.png  

<!-- Links to your social media accounts -->

[1]: https://twitter.com/geo.inca_
[2]: https://www.linkedin.com/in/geovanny.inca/