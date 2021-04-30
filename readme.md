# Xfce 4 is copyright Olivier Fourdan (fourdan@xfce.org). 
https://es.joecomp.com/how-install-xrdp-server-ubuntu-18
sudo apt-get install docker-ce=5:19.03.15~3-0~ubuntu-bionic docker-ce-cli=5:19.03.15~3-0~ubuntu-bionic containerd.io

# docker
http://www.linuxandubuntu.com/home/how-to-install-docker-on-ubuntu
19.03

sudo apt-get install docker-ce=5:19.03.15~3-0~ubuntu-bionic docker-ce-cli=5:19.03.15~3-0~ubuntu-bionic containerd.io 
Permisos
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04


# minikube
v1.16.0

curl -LO https://storage.googleapis.com/minikube/releases/v1.16.0/minikube-linux-amd64 &&
sudo install minikube-linux-amd64 /usr/local/bin/minikube



 curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
 sudo install minikube-linux-amd64 /usr/local/bin/minikube


https://kubernetes.io/blog/2019/03/28/running-kubernetes-locally-on-linux-with-minikube-now-with-kubernetes-1.14-support/

curl -LO https://storage.googleapis.com/minikube/releases/v1.16.0/minikube-darwin-amd64
minikube start --mount-string /Volumes/hd/TFM/laravel:/mnt/data
```console
/mnt/vda1/data
minikube start --vm-driver kvm2  --v=10 --alsologtostderr --cpus 4 --memory 10240 --mount --mount-string="/home/demo/k8/laravel:/mnt/data" 
minikube version: v1.18.1
minikube start --vm-driver kvm2 --mount --mount-string="/home/demo/k8/laravel:/mnt/data" --cpus 4 --memory 10240 --v=10
 
minikube start --vm-driver kvm2 --vm-driver kvm2  --v=10 --alsologtostderr --cpus 4 --memory 10240 --mount-string /home/demo/k8/laravel:/mnt/data


minikube start  --vm-driver=hyperkit --container-runtime=docker  --v=10 --alsologtostderr --cpus 4 --memory 8192 --mount-string /home/demo/k8/laravel:/mnt/data

minikube start  --vm-driver=hyperkit --container-runtime=docker  --v=10 --alsologtostderr --cpus 4 --memory 8192 --mount-string /home/demo/k8/laravel:/mnt/data

minikube start  --vm-driver=kvm2 --container-runtime=docker  --v=10 --alsologtostderr --cpus 4 --memory 8192 --mount-string /home/demo/k8/laravel:/mnt/data

minikube start   --cpus 2 --memory 8192
minikube start  --memory 8192 --mount   --mount-string /home/demo/k8/laravel:/mnt/data
--vm-driver=hyperkit

curl -LO https://storage.googleapis.com/minikube/releases/latest/docker-machine-driver-hyperkit
curl -LO https://github.com/kubernetes/minikube/releases/download/v1.16.0/docker-machine-driver-hyperkit

https://cloudnative.mx/como-empezar-con-kubernetes-usando-minikube/


wget https://github.com/kubernetes/minikube/releases/download/v1.16.0/minikube-linux-amd64


minikube start
minikube dashboard

```

    ▪ User ID:      docker
    ▪ Group ID:     docker
    ▪ Version:      9p2000.L
    ▪ Message Size: 262144
    ▪ Permissions:  755 (-rwxr-xr-x)
    ▪ Options:      map[]
    ▪ Bind Address: 192.168.39.1:41065
🚀  Userspace file server: ufs starting

# Argo

https://github.com/argoproj/argo-workflows
https://iamstoxe.com/posts/argo-getting-started/
en este caso usaremos la v2.12.11 

Installing the Argo Command Line Interface
```console
# Download the binary
curl -sLO https://github.com/argoproj/argo/releases/download/v2.12.11/argo-linux-amd64.gz

# Unzip
gunzip argo-linux-amd64.gz

# Make binary executable
chmod +x argo-linux-amd64

# Move binary to path
mv ./argo-linux-amd64 /usr/local/bin/argo

# Test installation
argo version
```

```console
kubectl create ns argo 

kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/stable/manifests/install.yaml 

kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/v2.12.11/manifests/install.yaml

kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=argo:default --namespace=argo

kubectl -n argo port-forward deployment/argo-server 2746:2746 &&


```

modify >>     - argo >>         - server >>             - argo-server >>                - edit

```console
spec:
  ports:
    - name: web
      protocol: TCP
      port: 2746
      targetPort: 2746
      nodePort: 31477
  selector:
    app: argo-server
  clusterIP: 10.98.28.218
  clusterIPs:
    - 10.98.28.218
  type: LoadBalancer
  sessionAffinity: None
  externalTrafficPolicy: Cluster
```
*****

# minio
```console
helm install --namespace=argo argo-artifacts stable/minio --set service.type=LoadBalancer --set fullnameOverride=argo-artifacts

kubectl port-forward service/argo-artifacts -n argo 9000:9000
```
cd minioartifacts
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


kubectl -n argo-events port-forward service/webhook-eventsource-svc 12000:12000

kubectl -n argo-events get eventsource

curl -X POST -H "Content-Type: application/json"   -d '{"message":"this is my first webhook"}'  http://localhost:15000/devops-toolkit

curl -X POST -H "Content-Type: application/json"   -d '{"message":"this is my first webhook"}'  http://localhost:12000/example4

curl -d '{"channel":"tfm","message":"test message"}' -H "Content-Type: application/json" -X POST http://localhost:12000/example2

curl -X POST -H 'Authorization: Bearer xoxb-xxx-xxx-xxx' \
-H 'Content-type: application/json' \
--data '{"channel":"tfm","text":"I hope the tour went well, Mr. Wonka.","attachments": [{"text":"Who wins the lifetime supply of chocolate?","fallback":"You could be telling the computer exactly what it can do with a lifetime supply of chocolate.","color":"#3AA3E3","attachment_type":"default","callback_id":"select_simple_1234","actions":[{"name":"winners_list","text":"Who should win?","type":"select","data_source":"users"}]}]}' \
https://slack.com/api/chat.postMessage

curl -X POST -H 'Authorization: Bearer xoxb-xox-xox-xox' \
-H 'Content-type: application/json' \
--data '{"channel":"tfm","text":"test linix"}' \
https://slack.com/api/chat.postMessage

```
## Deploy Laravel 
```console
git clone https://github.com/geoinca/DockerPHPTutorial.git

demo@u18a-2:~/k8/DockerPHPTutorial/kuberdev$ ls -al
total 40
drwxr-xr-x 2 demo demo 4096 Mar 31 19:14 .
drwxr-xr-x 5 demo demo 4096 Mar 31 19:14 ..
-rw-r--r-- 1 demo demo  180 Mar 31 19:14 dbserver-svc.yaml
-rw-r--r-- 1 demo demo  194 Mar 31 19:14 dbserver-vc.yaml
-rw-r--r-- 1 demo demo  960 Mar 31 19:14 dbserver.yaml
-rw-r--r-- 1 demo demo  697 Mar 31 19:14 phpmyadmin-deploy.yaml
-rw-r--r-- 1 demo demo  179 Mar 31 19:14 phpmyadmin-service.yaml
-rw-r--r-- 1 demo demo  118 Mar 31 19:14 tfmsecretwords.yaml
-rw-r--r-- 1 demo demo  184 Mar 31 19:14 webserver-svc.yaml
-rw-r--r-- 1 demo demo  555 Mar 31 19:14 webserver.yaml
demo@u18a-2:~/k8/DockerPHPTutorial/kuberdev$ kubectl apply -n argo -f dbserver-svc.yaml
service/mysql8-service created
demo@u18a-2:~/k8/DockerPHPTutorial/kuberdev$ kubectl apply -n argo -f dbserver-vc.yaml
persistentvolumeclaim/mysql-pv-claim created
demo@u18a-2:~/k8/DockerPHPTutorial/kuberdev$ kubectl apply -n argo -f  dbserver.yaml
deployment.apps/mysql configured
demo@u18a-2:~/k8/DockerPHPTutorial/kuberdev$ kubectl apply -n argo -f tfmsecretwords.yaml
secret/mysql-secrets created
demo@u18a-2:~/k8/DockerPHPTutorial/kuberdev$ kubectl apply -n argo -f phpmyadmin-deploy.yaml
deployment.apps/phpmyadmin-deployment created
demo@u18a-2:~/k8/DockerPHPTutorial/kuberdev$ kubectl apply -n argo -f phpmyadmin-service.yaml
service/phpmyadmin-service created
demo@u18a-2:~/k8/DockerPHPTutorial/kuberdev$ kubectl apply -n argo -f webserver-svc.yaml
service/web-service created
demo@u18a-2:~/k8/DockerPHPTutorial/kuberdev$ kubectl apply -n argo -f webserver.yaml
deployment.apps/webserver created
demo@u18a-2:~/k8/DockerPHPTutorial/kuberdev$

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

### TFM sample
```console

demo@u18a-2:~/k8/argo-events-demo$ kubectl apply -n argo-events -f https://raw.githubusercontent.com/geoinca/argo-events-demo/master/s1_00_event-sources.yaml
eventsource.argoproj.io/webhook created
demo@u18a-2:~/k8/argo-events-demo$ kubectl apply -n argo-events -f  https://raw.githubusercontent.com/geoinca/argo-events-demo/master/s1_04_sensor.yaml
sensor.argoproj.io/webhook4 created
demo@u18a-2:~/k8/argo-events-demo$

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


#Git
git clone  https://github.com/geoinca/laravel.git

pwd
minikube start  --memory 8192 --mount   --mount-string /home/demo/k8/laravel:/data

git clone https://github.com/geoinca/DockerPHPTutorial.git

git clone https://github.com/geoinca/miniok.git

https://github.com/geoinca/argo-events-demo.git



www
composer update 
docker run --rm -v $(pwd):/app composer install

php artisan route:list

## build Docker Image

docker run --rm  geoincaks/pythonimg:0.2.1 /bin/bash 
docker build -t  geoincaks/ubuntutest:0.1.3 .
IMAGE 00
```console
docker build -t geoincaks/pythonimg:0.2.1 -f Dockerfile00CountObj .
docker push geoincaks/pythonimg:0.2.1
```

IMAGE 01
```console
docker build -t geoincaks/pythonfacealignment:0.2.0 -f Dockerfile01FaceAlignment .
docker push geoincaks/pythonfacealignment:0.2.0
```
IMAGE 02
```console
docker build -t geoincaks/pythonwarpimg:0.2.0 -f Dockerfile02WarpImg .
docker push geoincaks/pythonwarpimg:0.2.0
```

IMAGE 04
```console
docker build -t geoincaks/pythonpanorama:0.1.2 -f Dockerfile04Panorama .
docker push geoincaks/pythonpanorama:0.1.2
```
You can find me on [![Twitter][1.2]][1], or on [![LinkedIn][2.2]][2]
<!-- Icons -->

[1.2]: https://github.com/geoinca/miniok/blob/main/img/tw.png 

[2.2]: https://github.com/geoinca/miniok/blob/main/img/lk.png  

<!-- Links to your social media accounts -->

[1]: https://twitter.com/geo.inca_
[2]: https://www.linkedin.com/in/geovanny.inca/