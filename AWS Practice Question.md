
# Cloud Concepts (26 Questions)

1. Which of the following is NOT a pillar of the AWS Well-Architected Framework?  
    A. Security  
    B. Reliability  
    C. Encryption  
    D. Cost Optimization
2. The AWS Cloud provides elasticity. What does elasticity mean?  
    A. Scaling resources manually  
    B. Automatically adjusting capacity to demand*  
    C. Unlimited data storage  
    D. Static resource allocation
3. Which of these is an example of Infrastructure as a Service (IaaS)?  
    A. AWS Lambda  
    B. Amazon EC2  
    C. Amazon S3
    D. AWS CloudFormation
4. Which deployment model includes services provided over the public internet and shared across organizations?  
    A. Private Cloud  
    B. On-Premises  
    C. Public Cloud
    D. Edge Cloud
5. What does the AWS Responsibility Model state about patching the guest operating system on EC2?  
    A. It’s the customer’s responsibility  
    B. It’s AWS’s responsibility  
    C. It’s shared equally  
    D. It’s not required
6. Regions in AWS are:  
    A. Physically isolated data centers  
    B. Collections of availability zones
    C. Single data centers  
    D. Edge locations
7. Which AWS service helps you estimate cost savings when committing to a term?  
    A. AWS Budgets
    B. AWS Cost Explorer  
    C. AWS Pricing Calculator  
    D. AWS Savings Plans
8. What attribute of the cloud shifts capital expense (CapEx) to operational expense (OpEx)?  
    A. Elasticity  
    B. On-demand pricing
    C. Global infrastructure  
    D. High availability
9. Which statement best describes the AWS Cloud?  
    A. A physical hardware platform  
    B. On-premises data center  
    C. A collection of remote servers accessed via the internet
    D. A private network
10. AWS edge locations are used by which service?  
    A. Amazon RDS  
    B. Amazon CloudFront  
    C. AWS IAM
    D. AWS Config
11. One benefit of the cloud is pay-as-you-go pricing. Which scenario illustrates this?  
    A. Paying a large upfront fee  
    B. Paying hourly only for instances you run
    C. Pre-purchasing compute capacity  
    D. Reserving resources for a year
12. Which service helps you evaluate your architecture against best practices?  
    A. AWS Trusted Advisor  
    B. AWS CloudTrail  
    C. AWS Config
    D. AWS IAM
13. Which is NOT part of the shared responsibility model?  
    A. Security of the cloud  
    B. Security in the cloud  
    C. Customer data  
    D. Physical data center security
14. To meet a global audience with low latency, you should deploy to:  
    A. One Region  
    B. Multiple Availability Zones in one Region
    C. Multiple Regions  
    D. A single edge location
15. What does “loT” stand for?  
    A. Layers of Technology  
    B. Internet of Things
    C. Instances on T-class  
    D. Infrastructure on Demand
16. Which AWS service provides a virtual private network?  
    A. AWS VPN  
    B. AWS IAM  
    C. AWS WAF  
    D. Amazon Route 53
17. What is an advantage of cloud elasticity?  
    A. Predictable monthly costs  
    B. Ability to scale back automatically at low usage  
    C. Manual hardware provisioning  
    D. Unlimited compute at no charge
18. Which model allows you to provision resources in your own data center but use AWS APIs?  
    A. Hybrid Cloud  
    B. Private Cloud  
    C. Public Cloud  
    D. Community Cloud
19. What AWS service gives you insights into API activity across your account?  
    A. AWS CloudTrail  
    B. AWS CloudWatch  
    C. AWS Config  
    D. AWS Inspector
20. Which feature lets you allocate capacity across multiple AZs?  
    A. Elastic Load Balancing  
    B. AWS Shield  
    C. AWS WAF  
    D. AWS Directory Service
21. Which AWS service can run containers without provisioning servers?  
    A. Amazon ECS  
    B. Amazon EKS  
    C. AWS Fargate  
    D. AWS Glue
22. What do availability zones provide?  
    A. Single fault domain  
    B. Multiple internet paths  
    C. Isolated locations within a region for high availability  
    D. Edge caching
23. Which benefit category includes elasticity, global reach, and on-demand resources?  
    A. Operational resilience  
    B. Financial benefits  
    C. Technical benefits  
    D. Performance benefits
24. What is an edge location used for?  
    A. Data storage  
    B. Lambda function execution  
    C. CloudFront content delivery  
    D. VPC peering
25. Which AWS service can help you estimate monthly costs?  
    A. AWS Cost Explorer  
    B. AWS CloudWatch  
    C. AWS Health Dashboard  
    D. AWS CloudFormation
26. Which of these best describes “pay-for-what-you-use”?  
    A. Reserved Instances  
    B. Pay-as-you-go  
    C. On-premises  
    D. Dedicated Hosts

![](https://miro.medium.com/v2/resize:fit:1400/1*8qLwOw3R7kD9V9fs_NtasA.png)

# Security (29 Questions)

1. In the shared responsibility model, who is responsible for patching guest OS on EC2?  
    A. AWS  
    B. Customer  
    C. AWS with a support plan  
    D. Shared equally
2. Which AWS service allows you to manage user access and encryption keys?  
    A. AWS KMS  
    B. AWS Shield  
    C. AWS WAF  
    D. AWS SSO
3. What does MFA stand for?  
    A. Multi-Factor Authentication  
    B. Managed Firewall Access  
    C. Multi-Frame Authorization  
    D. Managed File Archive
4. Security groups act as which of the following?  
    A. Stateful virtual firewall for EC2 instances  
    B. Stateless packet filter  
    C. Web application firewall  
    D. NAT gateway
5. Where do you configure password policies for IAM users?  
    A. IAM console  
    B. AWS Config  
    C. AWS Organizations  
    D. AWS CloudTrail
6. Which AWS service helps detect unauthorized API calls?  
    A. AWS Inspector  
    B. AWS CloudTrail  
    C. AWS Shield  
    D. AWS GuardDuty
7. What feature helps protect against DDoS attacks?  
    A. AWS IAM  
    B. AWS Shield  
    C. AWS Config  
    D. AWS SNS
8. Which of these is a host-based intrusion detection service?  
    A. AWS WAF  
    B. AWS Inspector  
    C. AWS GuardDuty  
    D. AWS Firewall Manager
9. What does IAM stand for?  
    A. Identity and Access Management  
    B. Internet and Application Management  
    C. Infrastructure and Administration Monitor  
    D. Instance Access Manager
10. Which service can rotate encryption keys automatically?  
    A. AWS KMS  
    B. AWS Secrets Manager  
    C. AWS Certificate Manager  
    D. AWS IAM
11. How do you enforce IAM policies across multiple accounts?  
    A. IAM Groups  
    B. AWS Organizations SCPs  
    C. AWS Config Rules  
    D. AWS CloudTrail
12. Which service provides centralized logging of resource configurations?  
    A. AWS CloudTrail  
    B. AWS Config  
    C. Amazon CloudWatch  
    D. AWS X-Ray
13. Which feature allows you to restrict access by IP address?  
    A. Security groups  
    B. NACLs  
    C. IAM policies  
    D. VPC peering
14. What is the default VPC security group’s inbound rule?  
    A. Allow all traffic  
    B. Deny all traffic  
    C. Allow traffic only from within the group  
    D. Allow traffic from 0.0.0.0/0
15. Which AWS service issues SSL/TLS certificates?  
    A. AWS IAM  
    B. AWS Certificate Manager  
    C. AWS KMS  
    D. AWS CloudHSM
16. What service helps you manage secrets like database credentials?  
    A. AWS Secrets Manager  
    B. AWS Parameter Store  
    C. AWS KMS  
    D. AWS Identity Store
17. Which AWS service offers threat detection across accounts?  
    A. AWS GuardDuty  
    B. AWS Inspector  
    C. AWS Shield  
    D. AWS WAF
18. How can you ensure encryption of data at rest in S3?  
    A. Use bucket policies  
    B. Enable SSE-S3 or SSE-KMS  
    C. Use ACLs  
    D. Use MFA delete
19. Which access control method is recommended for applications running on EC2?  
    A. Hard-coded credentials  
    B. Instance profiles with IAM roles  
    C. Root account credentials  
    D. AWS STS only
20. Which service can help you audit permissions granted to IAM principals?  
    A. IAM Access Analyzer  
    B. IAM Credential Report  
    C. AWS Trusted Advisor  
    D. AWS Config
21. Which AWS service can detect misconfigured security groups?  
    A. AWS Config  
    B. AWS CloudTrail  
    C. Amazon Inspector  
    D. AWS Firewall Manager
22. What type of firewall is AWS WAF?  
    A. Network firewall  
    B. Application firewall  
    C. Host-based firewall  
    D. Virtual firewall
23. How do you enforce multi-factor authentication for all IAM users?  
    A. IAM policy with Condition `aws:MultiFactorAuthPresent`  
    B. Security group rule  
    C. S3 bucket policy  
    D. KMS key policy
24. Which AWS service helps manage user authentication for business applications?  
    A. AWS IAM  
    B. AWS Cognito  
    C. AWS SSO  
    D. AWS STS
25. Which feature allows you to monitor and audit user activity?  
    A. Amazon CloudWatch Logs  
    B. AWS CloudTrail  
    C. AWS X-Ray  
    D. AWS Config
26. What mechanism can automatically deny a request that isn’t from your VPC endpoint?  
    A. VPC ACL  
    B. Resource-based policy with `aws:sourceVpce` condition  
    C. Security group rule  
    D. NACL rule
27. Which AWS service issues temporary, limited-privilege credentials?  
    A. AWS IAM  
    B. AWS STS  
    C. AWS Cognito  
    D. AWS SSO
28. Which compliance program is relevant for healthcare data?  
    A. PCI DSS  
    B. HIPAA  
    C. GDPR  
    D. SOC 2
29. What tool can you use to centrally manage firewall rules across accounts?  
    A. AWS WAF  
    B. AWS Firewall Manager  
    C. AWS Shield  
    D. AWS Config

![](https://miro.medium.com/v2/resize:fit:1320/1*iKcywqYV6ZYEB-M_32z_sw.png)

# Technology Services (31 Questions)

1. Which AWS service is object storage built for the cloud?  
    A. Amazon EBS  
    B. Amazon S3  
    C. Amazon EFS  
    D. Amazon FSx
2. Which service provides block-level storage for EC2?  
    A. Amazon EFS  
    B. Amazon S3  
    C. Amazon EBS  
    D. AWS Storage Gateway
3. What service is best for a managed relational database?  
    A. Amazon Redshift  
    B. Amazon DynamoDB  
    C. Amazon RDS  
    D. Amazon Aurora
4. Which database is serverless and NoSQL?  
    A. Amazon Aurora  
    B. Amazon RDS  
    C. Amazon DynamoDB  
    D. Amazon Redshift
5. Which compute service lets you run code without managing servers?  
    A. Amazon EC2  
    B. AWS Lambda  
    C. Amazon ECS  
    D. AWS Batch
6. What service would you choose for container orchestration?  
    A. Amazon RDS  
    B. Amazon ECS or EKS  
    C. Amazon S3  
    D. AWS Glue
7. Which service provides a managed Hadoop/Spark cluster?  
    A. Amazon EMR  
    B. AWS Glue  
    C. Amazon Athena  
    D. Amazon Redshift
8. What service can analyze data in S3 using SQL?  
    A. Amazon Athena  
    B. Amazon Redshift  
    C. Amazon QuickSight  
    D. Amazon EMR
9. Which service provides real-time event streaming?  
    A. Amazon Kinesis  
    B. Amazon SQS  
    C. Amazon SNS  
    D. AWS Step Functions
10. Which service is used for fully managed message queuing?  
    A. Amazon SNS  
    B. Amazon SQS  
    C. Amazon MQ  
    D. AWS IoT Core
11. What service offers push notifications and SMS?  
    A. Amazon SNS  
    B. Amazon SQS  
    C. AWS Pinpoint  
    D. AWS SES
12. Which content delivery network does AWS offer?  
    A. Amazon CloudFront  
    B. Amazon CloudWatch  
    C. AWS WAF  
    D. AWS Shield
13. What service helps you monitor resource health and logs?  
    A. AWS CloudWatch  
    B. AWS CloudTrail  
    C. AWS Config  
    D. AWS X-Ray
14. Which service can detect anomalous application behavior?  
    A. AWS Inspector  
    B. AWS CloudWatch  
    C. Amazon GuardDuty  
    D. AWS Config
15. Which service would you use for DNS management?  
    A. AWS Route 53  
    B. Amazon CloudFront  
    C. AWS Shield  
    D. AWS WAF
16. What service helps you automate infrastructure provisioning?  
    A. AWS CloudFormation  
    B. AWS OpsWorks  
    C. AWS Systems Manager  
    D. AWS Config
17. Which service can run serverless workflows?  
    A. AWS Step Functions  
    B. AWS Lambda  
    C. Amazon SWF  
    D. Amazon ECS
18. What service is best for petabyte-scale data warehousing?  
    A. Amazon Redshift  
    B. Amazon Athena  
    C. Amazon EMR  
    D. Amazon RDS
19. Which storage service is optimized for infrequently accessed data?  
    A. S3 Standard  
    B. S3 Glacier  
    C. EBS gp2  
    D. EFS Standard
20. Which service provides managed Kubernetes?  
    A. Amazon ECS  
    B. Amazon EKS  
    C. AWS Fargate  
    D. Amazon EMR
21. Which service offers long-term archival with low cost?  
    A. S3 Standard-IA  
    B. S3 Glacier Deep Archive  
    C. EBS Cold HDD  
    D. EFS One Zone
22. What service enables you to run SQL queries against S3 without ETL?  
    A. Amazon Athena  
    B. Amazon Redshift Spectrum  
    C. AWS Glue  
    D. Amazon EMR
23. Which service offers managed email sending?  
    A. AWS SES  
    B. SMTP Gateway  
    C. Amazon Chime  
    D. AWS SNS
24. What service provides geospatial indexing for location-based queries?  
    A. Amazon Location Service  
    B. Amazon CloudFront  
    C. Amazon Route 53  
    D. AWS WAF
25. Which service encrypts data in transit and at rest for applications?  
    A. AWS KMS  
    B. AWS Certificate Manager  
    C. AWS WAF  
    D. AWS Step Functions
26. What service would you choose for real-time data ingestion from IoT devices?  
    A. AWS IoT Core  
    B. Amazon Kinesis  
    C. AWS Greengrass  
    D. Amazon SNS
27. Which service is designed for business intelligence dashboards?  
    A. Amazon QuickSight  
    B. Amazon Athena  
    C. Amazon EMR  
    D. AWS Glue
28. Which compute option gives you full control of the OS?  
    A. AWS Lambda  
    B. Amazon EC2  
    C. AWS Fargate  
    D. AWS Batch
29. What service helps you track user behavior in a web app?  
    A. AWS X-Ray  
    B. Amazon Pinpoint  
    C. Amazon Kinesis Data Streams  
    D. Amazon CloudWatch Metrics
30. Which service provides a graph database?  
    A. Amazon Neptune  
    B. Amazon Aurora  
    C. Amazon DynamoDB  
    D. AWS DocumentDB
31. What service helps you build and train machine learning models?  
    A. Amazon SageMaker  
    B. AWS Lambda  
    C. AWS Glue  
    D. Amazon Comprehend

Answers :

![](https://miro.medium.com/v2/resize:fit:600/1*pQki7xYYj9TuHprFZwPZ4w.png)

# Billing & Pricing (14 Questions)

1. Which pricing model lets you save up to 75% compared to On-Demand?  
    A. Savings Plans  
    B. On-Demand  
    C. Spot Instances  
    D. Dedicated Hosts
2. What tool provides cost and usage reports?  
    A. AWS CloudTrail  
    B. AWS Cost Explorer  
    C. AWS CloudWatch  
    D. AWS Config
3. Which feature lets you receive alerts when usage exceeds a threshold?  
    A. AWS Budgets  
    B. AWS CloudFormation  
    C. AWS Systems Manager  
    D. AWS Shield
4. What does the AWS Free Tier include?  
    A. Unlimited 12 months of EC2 usage  
    B. Limited free usage of specified services for 12 months  
    C. 24 months of free S3 storage  
    D. Free support plan
5. Which billing dashboard shows month-to-date costs?  
    A. AWS CloudTrail  
    B. AWS Billing console  
    C. AWS Health Dashboard  
    D. AWS Config
6. Which report shows daily usage and costs by service?  
    A. Cost and Usage Report  
    B. Trusted Advisor  
    C. CloudWatch Logs  
    D. Billing Dashboard
7. Which pricing option is best for fault-tolerant workloads that can be interrupted?  
    A. On-Demand  
    B. Reserved Instances  
    C. Spot Instances  
    D. Savings Plans
8. What is included in the AWS Free Tier for Lambda?  
    A. 1M free requests and 400,000 GB-seconds compute time per month  
    B. 500K free requests  
    C. Unlimited free compute time  
    D. No free tier
9. Which service helps forecast future AWS costs?  
    A. AWS Cost Explorer  
    B. AWS Budgets  
    C. AWS Price List API  
    D. AWS Marketplace
10. What does a Savings Plan provide?  
    A. Fixed discount on EC2, Lambda, and Fargate usage  
    B. Unlimited free usage  
    C. Reserved capacity  
    D. Enhanced support
11. Which report can you export to S3 for detailed cost analysis?  
    A. Cost and Usage Report  
    B. AWS Config report  
    C. CloudTrail logs  
    D. Trusted Advisor report
12. Which tool helps you visualize cost allocation by tags?  
    A. AWS Cost Explorer  
    B. AWS IAM  
    C. AWS Organizations  
    D. AWS Config
13. Which billing feature allows consolidated billing across accounts?  
    A. AWS Organizations  
    B. AWS Directory Service  
    C. AWS SSO  
    D. AWS IAM
14. Which support plan includes 24x7 access to Cloud Support Engineers?  
    A. Basic  
    B. Developer  
    C. Business  
    D. Enterprise

Good luck! Study these questions, revisit the tips above, and you’ll be ready to ace the AWS Cloud Practitioner exam — just like I did in one month.

**Answers**

![](https://miro.medium.com/v2/resize:fit:600/1*zufRRQd1LDew0FWJm-ly4w.png)

[

Awscloudtraining

](https://medium.com/tag/awscloudtraining?source=post_page-----c91d5b288288---------------------------------------)

[

AWS

](https://medium.com/tag/aws?source=post_page-----c91d5b288288---------------------------------------)

[  
](https://medium.com/tag/aws-certification?source=post_page-----c91d5b288288---------------------------------------)


[[AWS Core]]
