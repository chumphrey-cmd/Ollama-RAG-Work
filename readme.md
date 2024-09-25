# Ollama RAG

**NOTE: Utilized personal laptop with 3 NVIDIA RTX A6000 in a Windows Environment**

## Prerequisites

1. **Install Linux on Windows with WSL**  
   Follow the instructions [HERE](https://learn.microsoft.com/en-us/windows/wsl/install)

2. **Install CUDA Tooling for Ubuntu on WSL2**  
   Follow the instructions [HERE](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local)

3. **Verify Drivers Installation**

   ```sh
   nvidia-smi

4. **Set Up Python Virtual Environment**
- Create and activate a **Python 3.10** virtual environment

   ```sh
   python -m venv [name_of_venv]
   ```

   ```sh
   .\[name_of_venv]\Scripts\activate
   ```

   ```sh
   pip install -r requirements.txt
   ```

## Installing and Running Models with Ollama (WINDOWS 🪟)

1. Download Ollama for Windows
- Download Ollama for Windows **[HERE](https://ollama.com/download/windows)**
  
**NOTE:** If your virtual environment is created using Windows, you must ensure that the Ollama models are pulled within a PowerShell environment.

2.  Download the Model of Your Choice
- From PowerShell terminal, download a model from [HERE](https://ollama.com/library)

   ```sh
   ollama run "name_of_your_model"
   ```
3. Verify Downloaded Model
- Verify the model and note its syntax (e.g., mistral:latest)

   ```sh
   ollama list
   ```

4. Determine WSL IP Address
- From WSL terminal, determine your WSL IP address (look under the **eth#** interface)
- IP address listed will be used to host and interact with your `chromadb/chroma` Docker container

   ```sh
   ip a
   ```

## Installing and Running Models with Ollama (Unix 🐧)

1. Download Ollama for WSL
- Open WSL terminal and run the following command:

   ```sh
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. Download the Model of Your Choice
- From WSL terminal, download a model from [HERE](https://ollama.com/library)

   ```sh
   ollama run "name_of_your_model"
   ```

3. Verify Downloaded Model
- Verify the model and note its syntax (e.g., mistral:latest)

   ```sh
   ollama list
   ```

4. Determine WSL IP Address
- From WSL terminal, determine your WSL IP address (look under the **eth#** interface)

   ```sh
   ip a
   ```

## Setting Up Ollama RAG

1. Upload Data
- Open your preferred IDE.
- Create a `data` directory.
- Upload PDFs into the `data` directory.

2. Modify Configuration Files
- Open VSCode and modify **chroma_client.py**:
   - Replace **"YOUR_WSL_IP_GOES_HERE"** with your WSL IP.

- Modify rag_query.py:
   - Replace **"YOUR_WSL_IP_GOES_HERE"** with your WSL IP.
   - Replace **"YOUR_OLLAMA_MODEL_GOES_HERE"** with your downloaded Ollama model.
  
3. Save All Changes

## Running the Project

1. **Load and Split Documents**
   - Load PDF docs from the `data` directory and split each into chunks.
     
      ```sh
      python loader.py
      ```

3. **Initialize Docker Container**
   - Pull and initiate `chromadb/chroma` container from Docker

     ```sh
     sudo docker run -p 8000:8000 chromadb/chroma
     ```

4. **Create Vector Database**
   - Initialize the data directory containing your documents to create a vector database

     ```sh
     python chroma_client.py
     ```
   - **Note:** Each time you modify the documents in the `data` directory, re-run `chroma_client.py`.

5. **Launch Interactive RAG System**

      ```sh
      python rag_query.py
      ```

## References/Inspiration

- [Open Source Self-Hosted RAG LLM Server with ChromaDB Docker Ollama](https://medium.com/@mbrazel/open-source-self-hosted-rag-llm-server-with-chromadb-docker-ollama-7e6c6913da7a)

