FROM python:3.11

RUN apt update
RUN apt install -y gcc cmake wget

RUN pip install --upgrade pip

WORKDIR /work

CMD ["/bin/bash"]
