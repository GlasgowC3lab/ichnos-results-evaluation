#!/bin/bash

# setup for nextflow
# sudo apt install zip
curl -s "https://get.sdkman.io" | bash
source "/users/grad/kathleen/.sdkman/bin/sdkman-init.sh"
sdk install java 17.0.6-tem
curl -s https://get.nextflow.io | bash
chmod +x ./nextflow
./nextflow self-update
export PATH="/users/grad/kathleen/:$PATH"
export PATH="/users/grad/kathleen/miniconda3/bin:$PATH"  
sudo sysctl -w kernel.perf_event_paranoid=0

# verify cpupower access
sudo cpupower frequency-info

# turbostress
sudo apt install linux-tools-common
sudo apt install linux-tools-generic
sudo apt install stress-ng
# sudo snap install go --channel=1.15/stable --classic

# docker
curl -fsSL https://get.docker.com -o get-docker.sh
./get-docker.sh
sudo adduser kathleen docker
newgrp docker

# verify setup
export PATH="$HOME:$PATH"  # add nextflow to path (from home dir on server only)
export PATH="$HOME/miniconda3/bin:$PATH"  # add conda to path
source "$HOME/.sdkman/bin/sdkman-init.sh"  # recognise sdk java

# enable perf for user
sudo sysctl -w kernel.perf_event_paranoid=0

# test nextflow works as expected (running as a user)
perf stat -a -e power/energy-cores/,power/energy-pkg/,power/energy-ram/ -o perf-out.txt nextflow run hello -c nf-conda.config
