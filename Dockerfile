FROM anibali/pytorch:1.10.0-nocuda
USER root
RUN sudo apt-get update && \
    sudo apt-get upgrade -y && \
    sudo apt-get install -y git && \
    sudo apt-get install -y git-lfs
RUN git lfs install

RUN mkdir /app/app
RUN git clone https://huggingface.co/papluca/xlm-roberta-base-language-detection /app/app/xlm-roberta-base-language-detection

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./app /app/app