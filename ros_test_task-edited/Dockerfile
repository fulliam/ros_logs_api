FROM ros:noetic

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    python3-rosdep \
    python3-rosinstall \
    python3-vcstools \
    && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-c"]
RUN apt-get update \
    && apt-get install --assume-yes --no-install-recommends --quiet \
        software-properties-common \
    && apt-get install --assume-yes --no-install-recommends --quiet \
    python3 \
    python3-pip \
    python3-venv \
    && apt-get clean all

WORKDIR /app
COPY . /app

RUN pip3 install -r ./src/requirements.txt
RUN python3 -m venv venv
RUN source venv/bin/activate
RUN chmod +x ./src/runme.sh ./src/logger/logger_node.py ./src/listener/listener_node.py

EXPOSE 8001

CMD ["bash", "-c", "./src/runme.sh"]