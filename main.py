import os
import openai
from api_secrets import  API_KEY

openai.api_key = API_KEY

prompt = "Say this is test"

model = 'text-davinci-003'
response = openai.Completion.create(
    prompt= prompt,
    model= model,
    max_tokens= 1500,
    temperature= 0.8,
    n = 1,
    stop = ['---'],
)
# print(response)
#  "created": 1678810576,
# "id": "cmpl-6u1bs8IUlYdc3UudkvAavvt8pVAty",
# "model": "text-davinci-003",
# "object": "text_completion",
# "usage": {
#  "completion_tokens": 16,
#   "prompt_tokens": 6,
#   "total_tokens": 22
print(response.usage.total_tokens)

for results in response.choices[0].text:
    print(results.text)
