import tiktoken
import sys

def count_tokens_from_file(file_path, model_name):
    try:
        encoding = tiktoken.encoding_for_model(model_name)

        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        tokens = encoding.encode(text)
        return len(tokens)

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python count_tokens.py <model> <File Path> ")
        sys.exit(1)

    model_name = sys.argv[1]
    file_path = sys.argv[2]

    token_count = count_tokens_from_file(file_path, model_name)

    if token_count is not None:
        print(f"File '{file_path}' Number of tokens (model: {model_name}): {token_count}")
