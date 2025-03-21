![](https://img.shields.io/github/commit-activity/t/subhamay-bhattacharyya/1111-api-gateway-py-sam)&nbsp;![](https://img.shields.io/github/last-commit/subhamay-bhattacharyya/1111-api-gateway-py-sam)&nbsp;![](https://img.shields.io/github/release-date/subhamay-bhattacharyya/1111-api-gateway-py-sam)&nbsp;![](https://img.shields.io/github/repo-size/subhamay-bhattacharyya/1111-api-gateway-py-sam)&nbsp;![](https://img.shields.io/github/directory-file-count/subhamay-bhattacharyya/1111-api-gateway-py-sam)&nbsp;![](https://img.shields.io/github/actions/workflow/status/subhamay-bhattacharyya/1111-api-gateway-py-sam/deploy-stack.yaml)&nbsp;![](https://img.shields.io/github/issues/subhamay-bhattacharyya/1111-api-gateway-py-sam)&nbsp;![](https://img.shields.io/github/languages/top/subhamay-bhattacharyya/1111-api-gateway-py-sam)&nbsp;![](https://img.shields.io/github/commit-activity/m/subhamay-bhattacharyya/1111-api-gateway-py-sam)&nbsp;![](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/bsubhamay/90bae5bd5b45f9eb760a124aa3886c99/raw/1111-api-gateway-py-sam.json?)


---

## Table of Contents

- [About the Project](#about-the-project)
- [Architecture](#architecture)
  - [AWS Services Used](#aws-services-used)
  - [Overview](#overview)
  - [Architecture Components](#architecture-components)
    - [AWS Cloud Environment](#1-aws-cloud-environment)
    - [Virtual Private Cloud (VPC)](#2-virtual-private-cloud-vpc)
    - [Private Subnets](#3-private-subnets)
    - [Route Tables](#4-route-tables)
    - [AWS Lambda Functions](#5-aws-lambda-functions)
    - [API Gateway](#6-api-gateway)
    - [Interface Endpoints](#7-interface-endpoints)
    - [AWS Public Services](#8-aws-public-services)
    - [Users](#9-users)
    - [AWS Power Tools for Lambda](#10-aws-power-tools-for-lambda)
  - [Key Design Considerations](#key-design-considerations)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
  - [Clone the Repository](#1-clone-the-repository)
  - [Install Dependencies](#2-install-dependencies)
  - [Build the SAM Application](#3-build-the-sam-application)
  - [Deploy to AWS](#4-deploy-to-aws)
  - [Test the API Endpoint](#5-test-the-api-endpoint)
  - [Cleanup](#cleanup)
- [Contributing](#contributing)
  - [Code of Conduct](#code-of-conduct)
- [License](#license)
- [Contact](#contact)

---

# Create a API Gateway Rest API endpoint with Lambda proxy integration using AWS SAM as IaaC and Python as Lambda runtime.

This project demonstrates how to deploy an API Gateway endpoint integrated with an AWS Lambda function using Python. AWS Serverless Application Model (SAM) is used as the Infrastructure as Code (IaC) tool to define and manage the deployment.

This project has been inspired by AWS API Gateway tutorial - [Create a REST API with a Lambda proxy integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-as-simple-proxy-for-lambda.html)

## 🏗 Architecture

Below is the architecture of the application:

- **Amazon API Gateway**: Handles HTTP requests and routes them to Lambda.
- **AWS Lambda (Python)**: Processes requests and returns responses.
- **AWS SAM**: Deploys and manages the infrastructure as code.

![AWS Architecture](architecture-diagram/architecture-diagram.jpg) <!-- Replace with the actual path to the diagram -->

### AWS Services Used

## Overview
This architecture illustrates a **serverless API deployment** using **AWS API Gateway, AWS Lambda, and a VPC with private subnets**.

## Architecture Components

### 1. AWS Cloud Environment
- The entire setup is hosted within an **AWS Cloud** region.

### 2. Virtual Private Cloud (VPC)
- A **VPC (Virtual Private Cloud)** is created to host private resources.
- **Network Access Control Lists (NACLs)** are configured for security.

### 3. Private Subnets
- Two **private subnets** are deployed in separate **Availability Zones (A and B)**.
- Each subnet hosts an **AWS Lambda function**, ensuring redundancy and high availability.

### 4. Route Tables
- The architecture uses private **route tables** with IP ranges:
  - `172.16.0.0`
  - `172.16.1.0`
  - `172.16.2.0`
- These subnets **do not** have direct internet access.

### 5. AWS Lambda Functions
- **Lambda functions are deployed inside private subnets.**
- They handle backend logic and process API requests.

### 6. API Gateway
- **Amazon API Gateway** is the public-facing endpoint for receiving HTTP requests.
- Routes incoming traffic to the appropriate AWS Lambda function.

### 7. Interface Endpoints
- **AWS Interface Endpoints** are used for private communication between AWS services.
- Allow Lambda functions to interact with AWS Public Services **without requiring an Internet Gateway or NAT Gateway**.

### 8. AWS Public Services
- Represents AWS-managed services that API Gateway or Lambda functions might access, such as:
  - Amazon S3
  - DynamoDB
  - Other AWS APIs

### 9. Users
- **End-users send HTTP requests to API Gateway**, which invokes the backend Lambda functions securely.

### 10. AWS Power Tools for Lambda

**AWS Powertools for AWS Lambda** is a suite of utilities that helps developers build serverless applications faster while following best practices. It provides features like structured logging, tracing, metrics, and various utilities to enhance AWS Lambda functions. AWS Powertools is available for **Python, Java, .NET, and TypeScript**.


## Key Design Considerations
- **Security:** Lambda functions reside in private subnets for restricted access.
- **Scalability:** API Gateway and Lambda automatically scale based on traffic.
- **Reliability:** Multi-AZ deployment ensures fault tolerance.
- **Cost Optimization:** Uses AWS Serverless services to reduce infrastructure costs.

## Conclusion
This architecture is ideal for **secure, scalable, and cost-efficient serverless API deployments** using AWS Lambda within a VPC.

---

## 🛠 Prerequisites

Before setting up the project, ensure you have:
- An AWS account

Ensure you have the following installed:
- **AWS CLI** ([Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html))
- **AWS SAM CLI** ([Installation Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html))
- **Python 3.x** ([Download](https://www.python.org/downloads/))
- **Docker** (For local testing, optional but recommended)
---

## 🚀 Installation & Setup

Follow these steps to set up the project locally:

### 1. Clone the Repository
```sh
git clone https://github.com/your-repo/aws-api-gateway-sam.git
cd aws-api-gateway-sam
```

### 2. Install Dependencies
```sh
pip install -r src/requirements.txt
```

### 3. Build the SAM Application
```sh
sam build
```

### 4. Deploy to AWS
```sh
sam deploy --guided
```
Follow the prompts to provide the necessary configuration, such as stack name and AWS region.

### 5. Test the API Endpoint
Once deployed, retrieve the API Gateway URL from the output and test it using:
```sh
curl https://your-api-id.execute-api.your-region.amazonaws.com/Prod/
```

## Cleanup
To delete the deployed resources:
```sh
sam delete
```
```mermaid
mindmap
  root )AWS Cloud(
    VPC
      Network ACL
         Allow and Deny rules
      Subnets
        Route Table
        Private Subnet
      Security Group
        Security Group Rule
      VPC Endpoints
    Lambda
    API Gateway
      Rest API Lambda Proxy Integration
```
---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this project better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

##### Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Subhamay Bhattacharyya
[![Linkedin](https://i.sstatic.net/gVE0j.png) LinkedIn](https://www.linkedin.com/in/subhamay-bhattacharyya/)
[![GitHub](https://i.sstatic.net/tskMh.png) GitHub](https://github.com/subhamay-bhattacharyya)
[![Email Badge](https://img.shields.io/badge/Gmail-Contact_Me-green?style=flat-square&logo=gmail&logoColor=FFFFFF&labelColor=3A3B3C&color=62F1CD)](mailto:subhamay.aws@gmail.com)
Project Link: [https://github.com/subhamay-bhattacharyya/1111-api-gateway-py-sam](https://github.com/subhamay-bhattacharyya/1111-api-gateway-py-sam)