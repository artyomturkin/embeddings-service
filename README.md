# Embeddings Service

Implements OpenAI embeddings API.

Supported models:
- EleutherAI/gpt-neox-20b

Port can be configured with `EMBEDDINGS_SERVER_PORT` environment variable, default `8080`.

Example usage:
```sh
curl --location 'http://localhost:8080/v1/embeddings' \
--header 'Content-Type: application/json' \
--data '{
    "model": "EleutherAI/gpt-neox-20b",
    "input": "hello world!"
}'
```
