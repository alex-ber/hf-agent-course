FROM python:3.12-slim

#https://stackoverflow.com/a/72551258
ENV PIP_ROOT_USER_ACTION=ignore
# This hack is widely applied to avoid python printing issues in docker containers.
# See: https://github.com/Docker-Hub-frolvlad/docker-alpine-python3/pull/13
# http://bugs.python.org/issue19846
# > At the moment, setting "LANG=C" on a Linux system *fundamentally breaks Python 3*, and that's not OK.
ENV PYTHONUNBUFFERED=1
ENV LANG=C.UTF-8
##https://stackoverflow.com/questions/59732335/is-there-any-disadvantage-in-using-pythondontwritebytecode-in-docker/60797635#60797635
ENV PYTHONDONTWRITEBYTECODE=1


#one can checkout from GIT if desired
COPY . /opt/project/hf-agents-course
WORKDIR /opt/project/hf-agents-course


RUN set -ex && \
     #latest pip,setuptools,wheel \
     #reason for setuptools==65.6.3 \
     #https://stackoverflow.com/questions/76043689/pkg-resources-is-deprecated-as-an-api#comment136784284_76044568 \
     python -m pip install --no-cache-dir --upgrade pip==23.1.2 setuptools==65.6.3  \
             #python -m piptools compile --no-strip-extras requirements.in \
         pip-tools==7.3.0 wheel==0.36.1 && \
     python -m pip install --no-cache-dir -r requirements.txt

#CMD ["/bin/sh"]
#https://docs.docker.com/reference/build-checks/json-args-recommended/
#CMD tail -f /dev/null
CMD ["tail", "-f", "/dev/null"]
#SHELL tail -f /dev/null


#delete all  containers
#docker rm -f $(docker ps -a -q)

#This command will only show the dangling images
#(images that are not tagged or referenced by any container)
#docker images -f "dangling=true"
#delete all dangling images
#docker image prune -f
#delete all unused images
#docker image prune -a -f

#delete all images
#docker rmi -f $(docker images -q)

#deleta all build cache
#docker builder prune --all
#verify builder cache deleted
#docker builder du


#https://gallery.ecr.aws/lambda/python/
#docker system prune --all
#docker rm -f hf-agent-course


#docker rmi -f hf-agent-course-i
#docker rm -f hf-agent-course
#docker build --no-cache --progress=plain . -t hf-agent-course-i
#docker exec -it $(docker ps -q -n=1) bash

#wsl --shutdown
#wsl --list --running

#sudo docker stats | sudo tee -a docker_stats.log
#sudo watch -n 15 "docker stats --no-stream | sudo tee -a docker_stats.log"
