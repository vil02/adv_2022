FROM gitpod/workspace-python:2022-02-25-16-52-08

SHELL ["/bin/bash", "-euo", "pipefail", "-c"]
RUN curl -sSL https://install.python-poetry.org | python3 - \
  && echo "export PATH=/home/$(whoami)/.local/bin:$PATH" >> ~/.bashrc
