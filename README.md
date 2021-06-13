# NETACAD-DEVASC SKILLS-BASED EXAM
# April-May 2021

--------

## Task 1 -- GitHub Skills Test

### Preparation:
- Access to DEVASC-VM and a GitHub account.

### Implementation, major steps:
- Create, initialize, stage and commit a local repository.
- Create a repository on GitHub.
- Push the local content to GitHub.

### Troubleshooting:
- Nothing to troubleshoot.

### Verification:
- Screenshot indicating success can be found in the folder ./Task-1

--------

## Task-2 -- Ansible Skills Test

### Preparation:
- Access to DEVASC-VM and CSR1000v-VM

### Implementation, major steps:
- Create an ansible.cfg and hosts file in the folder ./Task-2, and add necessary configurations,
see the ansible.cfg and hosts file.
- Create the ansible playbook file ios_status.yaml, configure it for these 4 tasks:
- show version
- show interfaces
- clear counters g1
- show ip route (an extra one I added)
- show version and show interfaces
- the first 4 of them of them with a task to send output to different files
- Run the ansible playbook file: ansible-playbook ios_status.yaml

### Troubleshooting:
- No problems, except a minor syntax error in the clear conunter task,
solved after consulting the ansible documentation.

### Verification:
- Screenshot indicating success can be found in the folder ./Task-2
- Config files and ios_status.yaml playbook file can be found in the folder ./Task-2
- Generated output files can be found in the folder ./Task-2/output

--------

## Task-3 -- Docker

### Preparation:
- Access to DEVASC-VM
- Looked at Chapter 6 and googled the internet:
 - https://medium.com/@vi1996ash/steps-to-build-apache-web-server-docker-image-1a2f21504a8e
 - https://www.tutorialspoint.com/docker/building_web_server_docker_file.htm

### Implementation, major steps:
- Created the Dockerfile:
```
 FROM ubuntu
 RUN apt-get update
 RUN apt-get install -y tzdata (added after TSHOOT)
 ENV TZ=Europe/ETC (added after TSHOOT)
 RUN ln -s /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone (added after TSHOOT)
 RUN apt-get install -y apache2
 RUN apt-get install -y apache2-utils
 RUN apt-get clean
 RUN sed -i 's/Listen 80/Listen 8081/g' /etc/apache2/ports.conf
 RUN sed -i 's/<VirtualHost *:80>/<VirtualHost *:8081>/g' /etc/apache2/sites-enabled/000-default.conf
 COPY index.html /var/www/html/
 EXPOSE 8081
 CMD ["apache2ctl", "-D", "FOREGROUND"]
```
- Created the index.html file
- Created the apache_docker.sh bash script


### Troubleshooting:
- Error:
 - After creating the Dockerfile timezone error and tzdata config problem
- Fix:
 - Consulted the internet:
   - https://stackoverflow.com/questions/44331836/apt-get-install-tzdata-noninteractive
   - https://www.thegeekstuff.com/2010/09/change-timezone-in-linux/
- Error: 
  - Line 10 dont seem to change 000-default.conf
- Fix:
  - Line 9 ports.conf override this

### Verification:
- Dockerfile, shell script and index.html are located in the folder ./Task-3
- Screenshots indicating success are located in the folder ./Task-3
- The file docker.txt generated from running the apache_docker.sh script are located in the folder ./Task-3

--------

## Task-4 -- Jenkins

### Preparation:
- DEVASC-VM and github
- Consulted Chapter 6

### Implementation, major steps:
- Started / running the Jenkins Container
- Configured a job in Jenkins
- Build
- Looked at Console Output and tested access to localhost:8081

### Troubleshooting:
- No errors

### Verification:
- Different screenshots are located in ./Task-4

--------

## Task-5 -- REST API & RESTCONF

### Preparation:
- DEVASC-VM and CSR1000v-VM
- Looked at Chapter 8 Lab

### Implementation, major steps:
- Wrote a sample python script for the OPTIONS curl command, and fixed some minor errors
- Copied the sample to the other curl commands, and made the necessary changes
- Tested
- Added a prettier output/ response 

### Troubleshooting:
- Errors:
  - Some few syntax errors
  - Wanted a pretty output/ response
- Fix:
  - Fixed the syntax errors
  - Had an idea for a pretty output/ response, and found some help on https://www.kite.com/python/answers/how-to-iterate-through-a-json-string-in-python
  
### Verification:
- Screenshot, response.txt and the task_5.py script are located in ./Task-5

--------

## Task-6 -- Webex Teams API

### Preparation:
- DEVASC-VM
- Looked at Chapter 8 Lab
- Consulted https://realpython.com/working-with-files-in-python/#listing-all-files-in-a-directory and https://developer.webex.com/docs/api/basics for examples on file handling and upload to webex.

### Implementation, major steps:
- Retrieved a token from https://developer.webex.com/
- Collected some of the individual python scripts from the Chapter 8 Webex Lab, and put them together in a single script  
- Added support for file upload
- Most of the testing was done one step at a time, so I did't have to delete the webex teams room every time

### Troubleshooting:
- Errors:
  - All of the errors were minor syntax errors
- Fix:
  - Fixed the syntax errors
  
### Verification:

- Screenshots, and the task_6.py script are located in ./Task-6
- The uploaded screenshots are located in ./Task-6/screenshots

----------------

## Task-7 -- BASH

### Preparation:
- DEVASC-VM
- Info and code snippets from classes with Yvan Rooseleer

### Implementation, major steps:
- Downloaded the files to the correct folders
- Changed the code snippets so they did the right job

### Troubleshooting:
- Errors:
  - The was an error with the IOS_VERSION, turned out to be a carriage return (cr) at the end of each line in the running-config file, causing problems comparing with REQUIRED_IOS
  - HOSTNAME is having the same error, but that is insignifcant
- Fix:
  - Found a way to strip the cr with sed https://stackoverflow.com/questions/15520339/how-to-remove-carriage-return-from-a-variable-in-shell-script
  
### Verification:
- The file check_ios.rep are located in ./Task-7
- Screenshot, and the check_ios.sh script are located in ./Task-7

----------------







dd647b1d0b0d4ff08419b1c3915efbd0
