# 0x13. Firewall
---
## Introduction

An overview of the concepts related to Firewall and ufw (Uncomplicated Firewall) along with instructions for completing the tasks associated with the Firewall project.

## Concepts

### Web stack debugging

In the context of this project, understanding web stack debugging is crucial. It involves identifying and resolving issues within the web stack, which comprises various layers such as the web server, application server, database server, etc.

## Background Context

Firewall serves as a barrier between a trusted internal network and untrusted external networks, controlling incoming and outgoing network traffic based on predetermined security rules.

## Resources

Read or watch:
- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_(computing))

## Explanation

Firewall acts as a filter for network traffic, allowing or blocking specific protocols, ports, or IP addresses based on predefined rules. ufw is a user-friendly command-line tool for configuring firewall rules on Ubuntu systems.

In the provided scenario, we are required to configure the ufw firewall on the web-01 server to block all incoming traffic except for certain TCP ports (22, 443, 80).

## Tasks

### 0. Block all incoming traffic but

#### Requirements:
- Configuration should be applied to web-01
- Configure ufw to block all incoming traffic except for TCP ports 22 (SSH), 443 (HTTPS SSL), and 80 (HTTP)

#### Steps:
1. Install ufw if not already installed: `sudo apt-get install ufw`
2. Block all incoming traffic: `sudo ufw default deny incoming`
3. Allow incoming traffic on TCP ports 22, 443, and 80:

 ```bash
    sudo ufw allow 22/tcp
    sudo ufw allow 443/tcp
    sudo ufw allow 80/tcp
```
4. Enable ufw: `sudo ufw enable`
5. Verify the status of ufw: `sudo ufw status`


## Warning

Be cautious while configuring firewall rules. Improperly configured rules can lead to unintended consequences such as loss of connectivity to the server.

## Conclusion

Understanding Firewall concepts and how to configure them using tools like ufw is essential for securing network infrastructure. By following the provided instructions, users can effectively control incoming and outgoing traffic based on their specific requirements.

