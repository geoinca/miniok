### Argo Events - Event-Based Dependency Manager for Kubernetes

(https://youtu.be/sUPkGChvD54)


#### Source: https://gist.github.com/a0a7ff04a7e22409cdfd8b466edb4e48

 
  Argo Events                                    
  Event-Based Dependency Manager for Kubernetes  
  https://youtu.be/sUPkGChvD54                   
 

 
#### Setup  
 

##### It could be any Kubernetes cluster

```console

minikube start

kubectl create namespace argo-events

kubectl apply \
    --filename https://raw.githubusercontent.com/argoproj/argo-events/stable/manifests/install.yaml

kubectl --namespace argo-events apply \
    --filename https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/eventbus/native.yaml

git clone https://github.com/vfarcic/argo-events-demo.git

cd argo-events-demo
```
 
#### Creating event sources  
 
```console
cat event-source.yaml

kubectl --namespace argo-events apply \
    --filename event-source.yaml

kubectl --namespace argo-events \
    get eventsources

kubectl --namespace argo-events \
    get services

kubectl --namespace argo-events \
    get pods
```

#### Replace `[...]` with the name of the `webhook-eventsource-*` Pod

```console
export EVENTSOURCE_POD_NAME=[...]

kubectl --namespace argo-events \
    port-forward $EVENTSOURCE_POD_NAME 12000:12000 &


curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"message":"My first webhook"}' \
    http://localhost:12000/devops-toolkit

 minikube  service list
 kubectl -n argo-events port-forward service/webhook-eventsource-svc 12000:12000   
```
#### Open https://github.com/argoproj/argo-events/blob/master/api/event-source.md#eventsourcespec


#### Creating sensors and triggers  

```console
cat sensor.yaml

kubectl --namespace argo-events apply \
    --filename sensor.yaml

curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"message":"My first webhook"}' \
    http://localhost:12000/devops-toolkit

kubectl --namespace argo-events get pods

kubectl --namespace argo-events logs \
    --selector app=payload

kubectl --namespace argo-events \
    delete pods \
    --selector app=payload
```
#### Open https://github.com/argoproj/argo-events/blob/master/api/sensor.md#sensor

 
#### Destroy

```console
pkill kubectl

minikube delete

```

```console

kubectl apply -n argo-events -f https://github.com/argoproj/argo-workflows/blob/master/examples/dag-targets.yaml
kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/tutorials/03-trigger-sources/sensor-minio.yaml


kubectl apply -n argo-events -f vf_01_sensor.yaml


curl -d '{"message":"ok"}'    -H "Content-Type: application/json" -X POST http://localhost:12000/devops-toolkit
curl -d '{"message":"ok :)"}' -H "Content-Type: application/json" -X POST http://localhost:12000/devops-toolkit
kubectl apply -n argo-events -f sensor-minio.yaml
```
demo@demo:~/k8/argo-events-demo$ kubectl -n argo-events apply -f sensor-minio.yaml
sensor.argoproj.io/webhook configured

curl -d '{"message":"ok"}' -H "Content-Type: application/json" -X POST http://localhost:12000/example


 kubectl apply -n argo-events -f s1_00_event-sources.yaml
eventsource.argoproj.io/webhook configured
 kubectl apply -n argo-events -f s1_01_sensor.yaml
sensor.argoproj.io/webhook configured
```
