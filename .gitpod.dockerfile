FROM gitpod/workspace-python:2023-05-08-21-16-55

SHELL ["/bin/bash", "-euo", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | python3 - \
  && echo "export PATH=/home/$(whoami)/.local/bin:$PATH" >> ~/.bashrc
