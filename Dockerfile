FROM node:20.12.2

# Install python
RUN apt-get update && \
    apt-get install -y python3-pip python3.11 python3.11-dev && \
    apt-get clean cache && \
    mkdir -p /home/node/app

WORKDIR /home/node/app

COPY ./script_dependencies.py /home/node/app/script_dependencies.py

CMD ["python3", "script_dependencies.py"]
