import argparse
from huggingface_hub import HfApi

def upload_model(model_path, repo_id, token):
    api = HfApi()
    api.upload_file(
        path_or_fileobj=model_path,
        path_in_repo="model.zip",
        repo_id=repo_id,
        token=token,
    )
    print(f"Model uploaded to {repo_id}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path", required=True, help="Path to the model file")
    parser.add_argument("--repo_id", required=True, help="Hugging Face repository ID")
    parser.add_argument("--token", required=True, help="Hugging Face API token")
    args = parser.parse_args()

    upload_model(args.model_path, args.repo_id, args.token)
