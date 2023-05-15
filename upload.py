import subprocess
import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import DeepLake

from dotenv import load_dotenv

load_dotenv()

def clone_repo(repo_url, location=""):
    """
    Clone a git repository into a specified location.

    :param repo_url: The URL of the repository to clone.
    :param location: The location to clone the repository into. Default is the current directory.
    """
    subprocess.run(["git", "clone", repo_url, location])

def prepare_data(root_dir):
    """
    Prepare data from a root directory
    """
    docs = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith('.py') or file.endswith(".md"):
                try: 
                    loader = TextLoader(os.path.join(dirpath, file), encoding='utf-8')
                    docs.extend(loader.load_and_split())
                except Exception as e: 
                    pass
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(docs)
    print(f"{len(texts)}")
    return texts

def push_data_to_deeplake(texts, dataset_path):
    """
    Push data to deeplake
    """
    embeddings = OpenAIEmbeddings()

    db = DeepLake.from_documents(texts, embeddings, dataset_path=dataset_path)
    return db



# example usage
if __name__ == "__main__":
    clone_repo("https://github.com/getyourguide/DDataFlow.git", "./repos/DDataFlow")
    texts = prepare_data("./repos/DDataFlow")
    db = push_data_to_deeplake(texts, "hub://theodoremeynard/ddataflow")
