# minikube

```console
minikube start   --container-runtime=docker  --v=10 --alsologtostderr --cpus 2 --memory 8192
minikube start   --cpus 2 --memory 8192
minikube start --vm-driver=hyperkit --memory 8192 --mount \
               --mount-string /home/demo/k8/DockerPHPTutorial/src:/data

minikube start
minikube dashboard

```

# Argo
```console
kubectl create ns argo 

kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/stable/manifests/install.yaml 

kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=argo:default --namespace=argo

kubectl -n argo port-forward deployment/argo-server 2746:2746 &&
```
*****

# minio
```console
helm install --namespace=argo argo-artifacts stable/minio --set service.type=LoadBalancer --set fullnameOverride=argo-artifacts

kubectl port-forward service/argo-artifacts -n argo 9000:9000
```
### Patch 
```console
kubectl -n argo patch configmap/workflow-controller-configmap --patch "$(cat ./minio-modified-minio.yaml)"
```


# argo-events
```console
kubectl create ns argo-events &&

kubectl apply -f  https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/install.yaml

kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/eventbus/native.yaml


kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=argo-events:default --namespace=argo-events

kubectl create clusterrolebinding geoinca-cluster-admin-binding --clusterrole=cluster-admin --user=geoinca@gmail.com

```
secret 
```console
kubectl create secret generic argo-artifacts --from-literal=accesskey="AKIAIOSFODNN7EXAMPLE" --from-literal=secretkey="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"  -n argo-events
```


# Install with a validating admission controller
```console
kubectl apply -f https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/install-validating-webhook.yaml

```




# Argo Samples
```console
https://github.com/argoproj/argo-workflows/blob/master/examples/README.md

https://github.com/argoproj/argo-workflows/tree/master/examples

argo submit --watch -n argo https://raw.githubusercontent.com/argoproj/argo-workflows/master/examples/steps.yaml

```


# Argo Events Samples
```console

git clone https://github.com/vfarcic/argo-events-demo.git

kubectl -n argo-events apply -f https://raw.githubusercontent.com/vfarcic/argo-events-demo/master/event-source.yaml

kubectl -n argo-events apply -f https://raw.githubusercontent.com/vfarcic/argo-events-demo/master/sensor.yaml



kubectl -n argo-events apply -f 01event-source-test-01.yaml

kubectl -n argo-events apply -f 01event-sensor-test-01.yaml

kubectl  -n argo-events  get services

kubectl -n argo-events port-forward service/slack-eventsource-svc 12000:12000

kubectl -n argo-events port-forward service/webhook-eventsource-svc 16000:16000

kubectl -n argo-events get eventsource

curl -X POST -H "Content-Type: application/json"   -d '{"message":"this is my first webhook"}'  http://localhost:15000/devops-toolkit

curl -X POST -H "Content-Type: application/json"   -d '{"message":"this is my first webhook"}'  http://localhost:16000/example

```






https://www.youtube.com/watch?v=sUPkGChvD54

# Argo Events Workflow

https://argoproj.github.io/argo-events/setup/minio/

event-sources
```console
kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/event-sources/minio.yaml


```
sensor
```console
kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/sensors/minio.yaml

```
test argo
```console
argo submit --watch -n argo  https://raw.githubusercontent.com/geoinca/miniok/main/argo/tfm-world10.yaml
```
## Webhook

### sample 1

event-sources
```console
https://raw.githubusercontent.com/geoinca/miniok/main/argoevents/webhook/a00a-event-source.yaml
```
sensor

```console
https://raw.githubusercontent.com/geoinca/miniok/main/argoevents/webhook/a00b-event-sensor.yaml
```

### sample 2

event-sources
```console
https://raw.githubusercontent.com/geoinca/miniok/main/argoevents/webhook/a001a-event-source.yaml
```
sensor

```console
https://raw.githubusercontent.com/geoinca/miniok/main/argoevents/webhook/a001b-event-sensor.yaml
```
## Minio

event-sources
```console
kubectl -n argo-events apply -f https://raw.githubusercontent.com/geoinca/miniok/main/argoevents/minio/001a-event-source-minio.yaml
```
sensor

```console
kubectl -n argo-events apply -f https://raw.githubusercontent.com/geoinca/miniok/main/argoevents/minio/001b-event-sensor-minio.yaml
```

### sample 2

event-sources
```console

kubectl -n argo-events apply -f https://raw.githubusercontent.com/geoinca/miniok/main/argoevents/minio/030a-event-source-minio.yaml
```
sensor

```console
kubectl -n argo-events apply -f https://raw.githubusercontent.com/geoinca/miniok/main/argoevents/minio/030b-event-sensor-minio.yaml
```


# Setup
## Requirements
* Installed Kubernetes 1.9 or later
* Installed [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* Have a [kubeconfig](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) file (default location is `~/.kube/config`).

## Install Minikube

### Linux
Nota: Este documento muestra cómo instalar Minikube en Linux usando un ejecutable autocontenido. Para métodos alternativos de instalación en Linux, ver Otros métodos de Instalación en el repositorio GitHub oficial de Minikube.
Puedes instalar Minikube en Linux descargando un ejecutable autocontenido:
```console
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64  && chmod +x minikube
```
Para tener disponible en la consola el comando minikube, puedes añadir el comando al $PATH o moverlo por ejemplo a /usr/local/bin:
```console
sudo cp minikube /usr/local/bin && rm minikube
```



## 1. Download Argo

Download the latest Argo CD version from https://github.com/argoproj/argo/releases/latest.

argo cliente  
```console
curl -sSL -o /usr/local/bin/argo         https://github.com/argoproj/argo/releases/download/v2.3.0/argo-linux-amd64
```


```console
kubectl delete all --all -n argo-events
kubectl delete namespace argo-events
```
## Use Secrets

https://kubernetes.io/es/docs/concepts/configuration/secret/
https://github.com/argoproj/argo-workflows/blob/master/examples/secrets.yaml

```console
kubectl apply -f slack-secret.yaml -n argo
```
kubectl apply -f /home/demo/k8/miniok/.bas/sp/wp/tfm-ngp-pvc.yaml -n test

kubectl  port-forward service/nginx-service 8888:80 -n test
 <!-- Actual text -->

## Git

https://git-scm.com/docs/git-merge
https://www.solucionex.com/blog/git-merge-o-git-rebase


You can find me on [![Twitter][1.2]][1], or on [![LinkedIn][2.2]][2]
<!-- Icons -->

[1.2]: https://github.com/geoinca/miniok/blob/main/img/tw.png 

[2.2]: https://github.com/geoinca/miniok/blob/main/img/lk.png  

<!-- Links to your social media accounts -->

[1]: https://twitter.com/geo.inca_
[2]: https://www.linkedin.com/in/geovanny.inca/