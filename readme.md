echo "# miniok" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/geoinca/miniok.git
git push -u origin main

# minikube

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
kubectl -n argo port-forward deployment/argo-server 2746:2746

helm install --namespace=argo argo-artifacts stable/minio --set service.type=LoadBalancer --set fullnameOverride=argo-artifacts
kubectl port-forward service/argo-artifacts -n argo 9000:9000


kubectl -n argo patch configmap/workflow-controller-configmap --patch "$(cat ./minio-modified-minio.yaml)"


$ brew install helm # mac, helm 3.x
$ helm repo add minio https://helm.min.io/ # official minio Helm charts
$ helm repo update
$ helm install --namespace=argo argo-artifacts minio/minio --set service.type=LoadBalancer --set fullnameOverride=argo-artifacts



kubectl apply -n argo -f https://raw.githubusercontent.com/argoproj/argo/stable/manifests/install.yaml &&
kubectl create rolebinding default-admin --clusterrole=admin --serviceaccount=default:default
kubectl create ns minio &&
helm install                  argo-artifacts stable/minio --set service.type=LoadBalancer --set fullnameOverride=minio-service
helm install --namespace=argo argo-artifacts stable/minio --set service.type=LoadBalancer --set fullnameOverride=argo-artifacts
# otra opción
kubectl create secret generic argo-artifacts --from-literal=accesskey="AKIAIOSFODNN7EXAMPLE" --from-literal=secretkey="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY" 

kubectl apply -n minio -f minio-argo-artifact.install.yml

kubectl -n argo patch configmap/workflow-controller-configmap --patch "$(cat ./minio-modified-minio.yaml)"

$ kubectl edit configmap workflow-controller-configmap -n argo      # assumes argo was installed in the argo namespace
...
data:
  artifactRepository: |
    s3:
      bucket: my-bucket
      keyFormat: prefix/in/bucket     #optional
      endpoint: my-minio-endpoint.default:9000        #AWS => s3.amazonaws.com; GCS => storage.googleapis.com
      insecure: true                  #omit for S3/GCS. Needed when minio runs without TLS
      accessKeySecret:                #omit if accessing via AWS IAM
        name: my-minio-cred
        key: accessKey
      secretKeySecret:                #omit if accessing via AWS IAM
        name: my-minio-cred
        key: secretKey
      useSDKCreds: true               #tells argo to use AWS SDK's default provider chain, enable for things like IRSA support

data:
  config: |
    artifactRepository:
      s3:
        bucket: artifacts
        endpoint: argo-artifacts:9000
        insecure: true
        # accessKeySecret and secretKeySecret are secret selectors.
        # It references the k8s secret named 'argo-artifacts'
        # which was created during the minio helm install. The keys,
        # 'accesskey' and 'secretkey', inside that secret are where the
        # actual minio credentials are stored.
        accessKeySecret:
          name: argo-artifacts
          key: accesskey
        secretKeySecret:
          name: argo-artifacts
          key: secretkey


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

# Forward argo-artifacts (minio) port 9000 to our 9000 in namespace argo
kubectl port-forward service/argo-artifacts -n argo 9000:9000

mc config host add minio http://minio-service.minio:9000 REVNT01JTklPQVJHT0VYQU1QTEU REVNTy9NSU5JTy9BUkdPL0tFWVNFQ1RSRUNUL0VYQU1QTEU

mc config host add argo-artifacts http://argo-artifacts.argo:9000 tfq0M5o1QtNOJcP1nizr HbO5COQOXR6z3P0jgTVCBzWxkXFPXKsMqoItRzL6

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
argo submit -n argo    --watch https://raw.githubusercontent.com/argoproj/argo/master/examples/hello-world.yaml
argo submit            --watch https://raw.githubusercontent.com/argoproj/argo/master/examples/hello-world.yaml

argo submit --watch -n argo  https://raw.githubusercontent.com/argoproj/argo/master/examples/artifact-passing.yaml


argo submit --watch -n argo  k3/hello-world09.yaml


# run Hello 
argo submit         -n argo k3/hello-world01.yaml -p message="goodbye world"
argo submit --watch -n argo k3/hello-world01.yaml -p message="goodbye world"
argo submit         -n argo k3/hello-world01.yaml --parameter-file params.yaml

argo submit --watch misc/workflow-argo.yml -p image=geoincaks/asv-environment:latest -p git_ref=master -p dataset=iris -n argo

{"auths":{"index.docker.io":{"username":"geoincaks","password":" ",          "auth":"Z2VvaW5jYWtzOkQwY2czMDMxMjQ="}}}
{"auths":{"index.docker.io":{"username":"geoincaks","password":" ","auth":"Z2VvaW5jYWtzOiZEMGNnMzAzMTI0Jg=="}}}







#docker ubuntutest
 docker build -t geoincaks/ubuntutest:0.1.1 .
 docker push geoincaks/ubuntutest:0.1.1
 docker run -it  docker/whalesay

#docker pythonimg
 docker build -t geoincaks/pythonimg:0.1.2 . 
 docker push geoincaks/pythonimg:0.1.2
 kubectl apply -n argo -f pythonpod.yaml

docker build -t geoincaks/pythonimg:0.1.5 -f Dockerfile00CountObj  . 
docker push geoincaks/pythonimg:0.1.5

docker build -t geoincaks/pythonfacealignment:0.1.6 -f Dockerfile01FaceAlignment  . 
docker push geoincaks/pythonfacealignment:0.1.6

geoincaks/pythonwarpimg:0.1.1
docker build -t geoincaks/pythonwarpimg:0.1.2 -f Dockerfile02WarpImg  .
docker push geoincaks/pythonwarpimg:0.1.2

###acc
countobj01.py 'tfq0M5o1QtNOJcP1nizr' 'HbO5COQOXR6z3P0jgTVCBzWxkXFPXKsMqoItRzL6'  'http://argo-artifacts:9000' 'infolder'
docker build -t geoincaks/pythonimg:0.1.1a   --build-arg s3AccessKey='tfq0M5o1QtNOJcP1nizr' --build-arg s3SecretAccessKey= 'HbO5COQOXR6z3P0jgTVCBzWxkXFPXKsMqoItRzL6' --build-arg s3EndPointUrl='http://argo-artifacts:9000'  --build-arg s3Bucket='infolder' .
 
 
 docker build -t geoincaks/pythonimg:0.1.1 --build-arg s3AccessKey='tfq0M5o1QtNOJcP1nizr' --build-arg s3SecretAccessKey='HbO5COQOXR6z3P0jgTVCBzWxkXFPXKsMqoItRzL6' --build-arg s3EndPointUrl='http://argo-artifacts:9000'  --build-arg s3Bucket='infolder' .
 
 <!-- Actual text -->

You can find me on [![Twitter][1.2]][1], or on [![LinkedIn][3.2]][3].

<!-- Icons -->

[1.2]: http://i.imgur.com/wWzX9uB.png (twitter icon without padding)
[2.2]: https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/linkedin-3-16.png (LinkedIn icon without padding)

<!-- Links to your social media accounts -->

[1]: https://twitter.com/geo.inca_
[2]: https://www.linkedin.com/in/geovanny.inca/