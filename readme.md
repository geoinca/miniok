minikube

minikube start   --container-runtime=docker  --v=10 --alsologtostderr --cpus 2 --memory 8192

# Minio

## Requirements
* Installed Kubernetes 1.9 or later
* Installed [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
* Have a [kubeconfig](https://kubernetes.io/docs/tasks/access-application-cluster/configure-access-multiple-clusters/) file (default location is `~/.kube/config`).

## 1. Download Argo

Download the latest Argo CD version from https://github.com/argoproj/argo/releases/latest.

argo cliente  
```
curl -sSL -o /usr/local/bin/argo         https://github.com/argoproj/argo/releases/download/v2.3.0/argo-linux-amd64
curl -sLO https://github.com/argoproj/argo/releases/download/v2.11.8/argo-linux-amd64.gz
```
# Unzip
```
gunzip argo-linux-amd64.gz
```
# Make binary executable
```
chmod +x argo-linux-amd64
```

```
# Configure the service
kubectl create ns argo &&
kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/stable/manifests/install.yaml


# Create role bindings to give argo admin
kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=argo:default --namespace=argo



kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/stable/manifests/install.yaml &&
kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=default:default
kubectl create ns minio &&
helm install --namespace=minio argo-artifacts stable/minio --set service.type=LoadBalancer --set fullnameOverride=minio-service

# otra opción
kubectl create secret generic argo-artifacts --from-literal=accesskey="AKIAIOSFODNN7EXAMPLE" --from-literal=secretkey="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" 

kubectl apply -n minio -f minio-argo-artifact.install.yml

kubectl -n argo patch configmap/workflow-controller-configmap --patch "$(cat ./minio-modified-minio.yaml)"
 
# Now run the below script
# Add the official Helm stable charts
$ helm repo add stable https://kubernetes-charts.storage.googleapis.com/


# Create a file named secrets.minio.yaml and paste the following as it’s contents
```
apiVersion: v1
kind: Secret
metadata:
  name: my-minio-cred
type: Opaque
data:
  accessKey: REVNT01JTklPQVJHT0VYQU1QTEU= # DEMOMINIOARGOEXAMPLE
  secretKey: REVNTy9NSU5JTy9BUkdPL0tFWVNFQ1RSRUNUL0VYQU1QTEU= #DEMO/MINIO/ARGO/KEYSECTRECT/EXAMPLE

mc config host add minio http://minio-service.minio:9000 REVNT01JTklPQVJHT0VYQU1QTEU REVNTy9NSU5JTy9BUkdPL0tFWVNFQ1RSRUNUL0VYQU1QTEU


sed "s/{{MINIO}}/${minikubeUrl}/g" ./minio-default.yaml > ./minio-modified.yaml
```
# Apply the minio secrets to k8s
```
$ kubectl apply -f ./secrets.minio.yaml -n argo
```


# Update helms package list
$ helm repo update

# Install minio, in namespace argo, with the name argo-artifacts and a service.type of LoadBalancer
$ helm install --namespace=argo argo-artifacts stable/minio --set service.type=LoadBalancer --set fullnameOverride=argo-artifacts



minio-default.yaml
```
data:
  artifactRepository: |
    s3:
      bucket: my-bucket
      #keyFormat: prefix/in/bucket     #optional
      endpoint: {{MINIO}}              #AWS => s3.amazonaws.com; GCS => storage.googleapis.com
      insecure: true                   #omit for S3/GCS. Needed when minio runs without TLS
      accessKeySecret:                 #omit if accessing via AWS IAM
        name: my-minio-cred
        key: accessKey
      secretKeySecret:                 #omit if accessing via AWS IAM
        name: my-minio-cred
        key: secretKey
      useSDKCreds: false                #tells argo to use AWS SDK's default provider chain, enable for things like IRSA support


```

# Apply the default artifact repository to argo

# Get the service url
$ minikubeUrl=$(minikube service -n argo argo-artifacts --url)

# replace the http://
$ minikubeUrl=$(echo $minikubeUrl | sed 's/http:\/\///g' -)

# Replace with actual minio url and make a new file ./minio-modified.yaml
$ sed "s/{{MINIO}}/${minikubeUrl}/g" ./minio-default.yaml > ./minio-modified.yaml

e
192.168.39.25:30808

# Apply to k8s in the argo namespace
$ kubectl -n argo patch configmap/workflow-controller-configmap --patch "$(cat ./minio-modified.yaml)"

# Remove modified yaml
$ rm -f ./argo/minio-modified.yaml



mc config host add miniox http://argo-artifacts.argo.svc.cluster.local:9000 AKIAIOSFODNN7EXAMPLE wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

argo submit -n default --watch https://raw.githubusercontent.com/argoproj/argo/master/examples/artifact-passing.yaml
argo submit -n argo --watch https://raw.githubusercontent.com/argoproj/argo/master/examples/hello-world.yaml
argo submit         --watch https://raw.githubusercontent.com/argoproj/argo/master/examples/hello-world.yaml