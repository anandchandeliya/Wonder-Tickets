# Wonder-Tickets – Cloud-Native Event Booking Platform

**Wonder-Tickets** is a scalable, cost-effective, cloud-native event booking web app built using the AWS ecosystem. It simulates a real-world solution architecture for hands-on AWS Solutions Architect Associate (SAA) preparation.

---

## Live Demo



---

##  Architecture Overview

- **Frontend**: HTML + CSS + Bootstrap (simple UI)
- **Backend**: Python Flask
- **Database**: Amazon RDS (MySQL)
- **Compute**: Amazon EC2 (App Server with Auto Scaling)
- **Load Balancer**: Application Load Balancer (HTTPS via ACM)
- **Storage**: Amazon S3 (future use: static/media files)
- **IAM Roles & Security Groups**: Least privilege principle followed
- **SSH & WinSCP**: For secure server access and app uploads
- **Version Control**: Git & GitHub
- **Domain & SSL**: Optional Cloudflare + AWS ACM for HTTPS

---

##  Features Implemented

- User can view and book event tickets (UI/UX ready)
- Data stored in AWS RDS with persistent backup
- EC2 App Server launched in private subnet (via Bastion)
- Configured Auto Scaling with health checks via ALB
- HTTPS-enabled using AWS Certificate Manager (ACM)
- SSH & WinSCP secured with custom key pairs
- GitHub integrated with SSH key for seamless versioning

---

## Skills Practiced

- VPC, Subnetting, Internet Gateway, NAT Gateway
- Security Group & NACL Configurations
- Bastion Host Access & WinSCP Deployment
- Amazon EC2 & Launch Templates
- Auto Scaling Groups (ASG)
- Application Load Balancer (ALB)
- SSL Certificates (ACM)
- MySQL RDS Integration in Flask
- Git, GitHub, and SSH Authentication

---

##  Future Enhancements

- ECS + Docker for containerized deployment
- S3 + CloudFront for frontend hosting
- CI/CD with GitHub Actions
- IAM Role refinement for least privilege
- CloudWatch for logging & monitoring

---

## Screenshots

> <img width="1002" height="673" alt="image" src="https://github.com/user-attachments/assets/5892bb11-4723-477e-86d3-0358ed698d6c" />


---

## 📜 License

MIT – feel free to fork and build on top of it!
