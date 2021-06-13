#!/bin/bash

# Build, run and verify apache Docker image and container.

echo -e "\n\n- Building Docker apache image.\n"
docker build -t apache_image .

echo -e "\n- Run apache Docker Container.\n"
docker run -t -d -p 8081:8081 --name apache_run apache_image

echo -e "\n- Verify apache Docker Container is running.\n"
docker ps


