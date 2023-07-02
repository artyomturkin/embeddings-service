from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neox-20b")
# Run first tokenization for consistent api latency
tokenizer("initialize", return_tensors="pt").input_ids

from aiohttp import web

routes = web.RouteTableDef()

@routes.post('/v1/embeddings')
async def mpt(request):
  b = await request.json()
  
  ids = tokenizer(b["input"], return_tensors="pt").input_ids
  output = ids[0].cpu().detach().numpy().tolist()

  return web.json_response({
    'object': 'list',
    'model': 'EleutherAI/gpt-neox-20b',
    'usage': {
        "prompt_tokens": len(output),
        "total_tokens": len(output)
    },
    'data': [{
        'object': 'embedding',
        'embedding': output,
        'index': 0
    }]
  })

import os
port = os.getenv('EMBEDDINGS_SERVER_PORT', 8080)

app = web.Application()
app.add_routes(routes)
web.run_app(app, port=port)
