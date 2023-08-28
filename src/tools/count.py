import argparse
import json
from transformers import AutoTokenizer
import tiktoken


def count_tokenizer(json_path, model_name):
    with open(json_path, 'r') as f:
        data = json.load(f)

    encoding = tiktoken.encoding_for_model(model_name)
    count = 0

    for chat in data:
        conversations = chat["conversations"]
        for conv in conversations:
            value = conv["value"]
            num_tokens = len(encoding.encode(value))
            count += num_tokens

    return count

def count_tokenizer_local(json_path, tokenizer_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)

    count = 0

    for chat in data:
        conversations = chat["conversations"]
        for conv in conversations:
            value = conv["value"]
            tokenize = tokenizer.tokenize(value)
            count += len(value)

    print(count)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Count the number of tokens in a JSON file using a tokenizer.')
    parser.add_argument('json_path', type=str, help='Path to the JSON file.')
    parser.add_argument('tokenizer_path', type=str, help='Path to the tokenizer directory or tiktoken name.')
    parser.add_argument('--use-tiktoken', action='store_true', help='Use tiktoken to count tokens.')
    args = parser.parse_args()

    if args.use_tiktoken:
        count_tokenizer(args.json_path, args.tokenizer_path)
    else:
        count_tokenizer(args.json_path, args.tokenizer_path)

