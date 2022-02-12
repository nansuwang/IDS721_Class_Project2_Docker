# IDS721_Class_Project2: Kubernetes based Continuous Delivery
[![CI with Github Actions](https://github.com/nansuwang/IDS721_Class_Project2_Docker/actions/workflows/main.yml/badge.svg)](https://github.com/nansuwang/IDS721_Class_Project2_Docker/actions/workflows/main.yml)

## Introduction
It is a demo project for assignment in IDS721 course.
A Kubernetes based Continuous Delivery application is built.

It is a Python script for select the kth largest element in a list.

The application is based on the fast selection algorithm.

The application is realized using FastAPI.

It is containerized using Docker! Docker image could be easily built by running
```shell
docker build -t .
```

## Workflow
1. An AWS Cloud9 environment supported by EC2 instance is built for this assignment
2. The quick selection algorithm is implemented
3. A FastAPI is built for providing the micro-service
4. A Docker Image is built holding all the dependencies
5. The Amazon Elastic Container Registry (Amazon ECR) is used for storing the image
6. The service is a Kubernetes based service containing Continuous Delivery
7. CI/CD workflow is built in this assignment
