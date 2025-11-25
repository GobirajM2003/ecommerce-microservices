# 🚀 End-to-End DevOps E-Commerce Project

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white)

## 📖 Project Overview
This project demonstrates a full **DevOps Lifecycle**. It is a Microservices Application (Frontend + Backend) that I took from local development all the way to a self-healing Kubernetes cluster with monitoring.

## 🏗️ Architecture
* **Backend:** Python Flask API (Product Inventory).
* **Frontend:** HTML/JavaScript with Nginx (Store Interface).
* **Database:** JSON-based mock data.

## 🛠️ Technologies & Skills Implemented

| Area | Technology | What I Did |
| :--- | :--- | :--- |
| **Containerization** | Docker | Wrote Dockerfiles to optimize images for production. |
| **Orchestration** | Docker Compose | Linked microservices for local development. |
| **CI/CD** | GitHub Actions | Automated the testing and build pipeline on every push. |
| **Cloud** | Render | Deployed the application to the public internet. |
| **IaC** | Terraform | Provisioned Nginx infrastructure using code (not manual clicks). |
| **Kubernetes** | Minikube | Deployed to a cluster with **3 replicas** and **Self-Healing** enabled. |
| **Monitoring** | Prometheus/Grafana | Set up real-time CPU & Memory dashboards using Helm. |

---

## 💻 How to Run This Project

### 1. Run Locally (Docker Compose)
The easiest way to see the app running:
```bash
    docker-compose up --build

    Frontend: http://localhost:80

    Backend: http://localhost:5000/products

#### 2. Run in Kubernetes (Minikube)

To see the self-healing cluster in action:
    Bash

    minikube start
    eval $(minikube docker-env)
    kubectl apply -f k8s/backend.yaml
    kubectl apply -f k8s/frontend.yaml

3. Monitoring (Grafana)

To view the system metrics:
    Bash

    helm install monitoring prometheus-community/kube-prometheus-stack
    kubectl port-forward service/monitoring-grafana 3000:80

    Access Grafana at http://localhost:3000