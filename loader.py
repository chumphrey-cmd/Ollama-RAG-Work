import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter


def load_and_split_documents(directory_path="data"):
    """
    Loads all PDF documents from a directory and splits them into chunks.

    Args:
        directory_path (str): The path to the directory containing the PDF files.
    Returns:
        list: A list of document objects, each representing a chunk of text.
    """

    loader = DirectoryLoader(directory_path, glob="**/*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    all_docs = text_splitter.split_documents(documents)
    return all_docs
