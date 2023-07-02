FROM huggingface/transformers-pytorch-gpu:4.29.2

COPY install_models.py /usr/scripts/embeddings/
WORKDIR /usr/scripts/embeddings/
RUN python3 install_models.py
COPY . /usr/scripts/embeddings/

ENV TRANSFORMERS_OFFLINE=1
EXPOSE 8080
CMD [ "python3", "embeddings_server.py" ]
