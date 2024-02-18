
```markdown
# Project Setup

This project includes the necessary steps to set up and run the application.

## Instructions

### 1. Update the apt Package Index
To update the apt package index, run the following command:
```bash
  sudo apt update
```
2. Install the Docker App
To install the Docker application, follow these steps:

```bash
# Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Set up the stable repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update the apt package index
sudo apt update

# Install Docker
sudo apt install docker-ce docker-ce-cli containerd.io
```
 3. Run doc.py
After installing Docker, you can run the `doc.py` script by executing the following command:
```bash
python doc.py
```
 4. Run `/static/ npm run dev`
To start the development server for the static files, navigate to the `/static/` directory and run the following command:
```bash
npm run dev
```
5. Run priv.py


https://qrco.de/beo9n
