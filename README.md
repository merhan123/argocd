# Kubernetes Flask and monitoring lab

Flask services, an Nginx frontend, and Kubernetes manifests for experimenting with Traefik, Prometheus, and Grafana. This repository does not include an Argo CD installation or Application resource.

## Layout

- `backend_application/`: Flask `/test` and `/metrics` endpoints on port 8000.
- `frontend_application/`: static UI and Nginx proxy to the backend.
- `simple flask/`: separate Flask example on port 5000.
- `manifests/`: application Deployments, Services, and Traefik Ingress.
- `monitoring/`: Prometheus, Grafana, node exporter, and kube-state-metrics.
- `app2/`: additional static page example.

## Build and run

Install Docker and kubectl and configure access to a Kubernetes cluster. Replace YOUR_REGISTRY with a registry namespace accessible by your cluster.

```sh
docker build -t YOUR_REGISTRY/backend:lab ./backend_application
docker build -t YOUR_REGISTRY/frontend:lab ./frontend_application
docker build -t YOUR_REGISTRY/simple-flask:lab "./simple flask"
docker push YOUR_REGISTRY/backend:lab
docker push YOUR_REGISTRY/frontend:lab
docker push YOUR_REGISTRY/simple-flask:lab
```

Update the image references in the three Deployment manifests. The original author's images do not include your local changes automatically.

```sh
kubectl apply -f manifests/backend-deployment.yaml -f manifests/backend-service.yaml
kubectl apply -f manifests/frontend-deployment.yaml -f manifests/frontend-service.yaml
kubectl apply -f manifests/app-deployment.yaml -f manifests/app-service.yaml
kubectl port-forward service/frontend 8080:80
```

Open http://localhost:8080. The buttons call same-origin `/api/test` and `/api/metrics`; Nginx forwards these to the backend Service. Both frontend and backend must use the default namespace with this configuration.

For ingress, install Traefik and configure DNS or hosts-file entries for `testcom`, `frontendbackend`, and `backendapp`, or change the hostnames in `manifests/ingress.yaml`. Apply that file afterward. The optional strip-prefix middleware is not attached to this ingress; removing `/test` would not match the Flask route.

## Monitoring

```sh
kubectl apply -f monitoring/namespace.yaml
kubectl apply -f monitoring/
kubectl -n monitoring get pods,services
```

Inspect Service ports before port-forwarding Prometheus or Grafana. Configure Grafana's data source to point to the Prometheus Service. Dashboards and durable storage are not provisioned here.

## Limitations

This is a learning lab. Review old image versions, floating tags, Flask's development server, permissive CORS, monitoring RBAC, and the one-second scrape interval before adapting it. Grafana uses the demonstration password `admin`; replace it with a Secret before exposing the service. Add TLS, authentication, health probes, resource limits, and persistent storage appropriate to your environment.

A live Kubernetes deployment and end-to-end monitoring validation have not been performed for this cleanup.
