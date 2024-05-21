# TechTrends Project

TechTrends is an online news sharing platform designed to keep consumers updated with the latest news in the cloud-native ecosystem. Users can access and create new articles, leveraging a seamless and efficient platform built with modern technologies.

## Project Description

The TechTrends application is developed using the Python Flask framework and uses SQLite as its database. It follows best practices for application deployment, containerization, continuous integration, and continuous delivery. The project is structured to be deployed on a Kubernetes cluster using Helm for templating and ArgoCD for continuous delivery.

## Features

- **Health Check Endpoint**: `/healthz` endpoint to verify application health.
- **Metrics Endpoint**: `/metrics` endpoint providing application metrics like the total number of posts and database connections.
- **Logging**: Comprehensive logging of key events such as article retrieval, article creation, and page access.

## Running the Application Locally

1. **Initialize the Database**:
   ```bash
   python init_db.py
2.  **Run the Application**: 
	```bash
	python app.py
	```
	Access the application at `http://127.0.0.1:3111/`.

## Containerization with Docker

1.  **Build the Docker Image**:
    `docker build -t techtrends .` 
    
2.  **Run the Docker Container**:
    `docker run -d -p 7111:3111 techtrends`
    
	Access the application at `http://127.0.0.1:7111/`.

## Kubernetes Deployment

### Deploy a Kubernetes Cluster

Use Vagrant to deploy a Kubernetes cluster with k3s:

1.  **Create a Vagrant Box**:

	`vagrant up`
	
2.  **SSH into the Vagrant Box**:

    `vagrant ssh` 
    
3.  **Deploy k3s**: Follow the [k3s installation guide](https://k3s.io/).
    
4.  **Verify Cluster Nodes**:
    
    `kubectl get nodes` 
    

### Kubernetes Manifests

Apply the following Kubernetes manifests to deploy the TechTrends application:

1.  **Namespace**: `namespace.yaml`
    
2.  **Deployment**:  `deploy.yaml`
    
3.  **Service**: `service.yaml`
    
    `kubectl apply -f namespace.yaml`
    `kubectl apply -f deploy.yaml`
    `kubectl apply -f service.yaml` 
    

## Helm Charts

### Create Helm Chart

1. **Chart.yaml**:
   Define the basic information for the Helm chart, such as `apiVersion`, `name`, and `version`.

2. **Values.yaml**:
   Provide default values for variables such as `namespace`, `service`, and `image`. This file will serve as the default configuration.

3. **Templates**:
   Create parameterized templates for `namespace.yaml`, `deploy.yaml`, and `service.yaml`.

### Environment-specific Values

- **Staging**: Create `values-staging.yaml` with configurations specific to the staging environment, such as `namespace` name, `service` port, and `replicaCount`.

- **Production**: Create `values-prod.yaml` with configurations specific to the production environment, including different `namespace`, `service` port, and `replicaCount`.


    

## Continuous Delivery with ArgoCD

### Install ArgoCD

Follow the [ArgoCD installation guide](https://argo-cd.readthedocs.io/en/stable/getting_started/) to install ArgoCD on your Kubernetes cluster.

### Create ArgoCD Applications

1. **Staging Application**: Create a `helm-techtrends-staging.yaml` manifest file to define the staging application.
2. **Production Application**: Create a `helm-techtrends-prod.yaml` manifest file to define the production application.

### Apply ArgoCD Manifests

To apply the ArgoCD application manifests, use the following commands:

```bash
kubectl apply -f helm-techtrends-staging.yaml
kubectl apply -f helm-techtrends-prod.yaml
```
    

### Synchronize Applications

Use the ArgoCD UI to synchronize the staging and production applications, ensuring all resources are deployed successfully.

Access the ArgoCD UI:

`kubectl port-forward svc/argocd-server -n argocd 8080:443` 

Visit `https://localhost:8080` and login with the credentials obtained from the ArgoCD installation guide.

## Conclusion

TechTrends leverages modern development, containerization, and deployment practices to provide a robust platform for sharing news in the cloud-native ecosystem. The integration of Kubernetes, Helm, and ArgoCD ensures efficient and scalable deployment and management of the application across different environments.

## Resources

- [Python Flask](https://flask.palletsprojects.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Docker](https://www.docker.com/)
- [Kubernetes](https://kubernetes.io/)
- [k3s](https://k3s.io/)
- [Helm](https://helm.sh/)
- [ArgoCD](https://argo-cd.readthedocs.io/)
