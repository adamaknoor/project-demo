FROM baseImage
FROM jenkins/jenkins:lts
USER root
RUN apt-get update && apt-get install -y sudo
RUN apt-get update && apt-get install -y curl git
USER jenkins
