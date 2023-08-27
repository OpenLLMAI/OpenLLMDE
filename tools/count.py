import json
from transformers import AutoTokenizer

with open("/path/to/your/json", 'r') as f:
    data = json.load(f)

tokenizer = AutoTokenizer.from_pretrained("/path/to/your/tokenizer/")

count = 0

for chat in data:
    conversations = chat["conversations"]
    for conv in conversations:
        value = conv["value"]
        tokenize = tokenizer.tokenize(value)
        count += len(value)

print(count)
