import json
from transformers import AutoTokenizer

def count_token(data_path, tokenizer_path):
    # support multi format: TODO, like json/jsonl/csv...
    with open(data_path, 'r') as f:
        data = json.load(f)

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

    count = 0
    # support multi format: TODO
    for chat in data:
        conversations = chat["conversations"]
        for conv in conversations:
            value = conv["value"]
            tokenize = tokenizer.tokenize(value)
            count += len(value)

    return count

if __name__=="__main__":
    pass
