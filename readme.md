NOTE: Utilizing workstation with the following specs: 3 NVIDIA RTX A6000
Tutorial Followed: https://medium.com/@mbrazel/open-source-self-hosted-rag-llm-server-with-chromadb-docker-ollama-7e6c6913da7a

NOTE: utilizing python 3.10 virtual environment.

1. Deployed WSL2 on machine and initiated CUDA installation on WSL2
2. Initiated Docker Deployment from work computer
  2a. $ sudo snap install docker
  2b. $ curl https://ollama.ai/install.sh | sh
      $ ollama serve &
      $ ollama pull <model_name>
      $ ollama run <model_name>

  2b. $ sudo docker run -p 8000:8000 chromadb/chroma 
    - Used to download chromadb/chroma container to host your data...
    - NOTE: need to look into kubernetes in maintaining and viewing my Docker containers...

  2c. Ran **python .\chroma_client.py** to create inital vector database of all the documents in "data" directory.
    - Will take sometime to load, be patient...

3. See Python Tips and Tricks for specific Docker application setup with app.py
  3a. app.py is the web-application function used to interact with our local LLM, but a web-app can just be hosted via LAN using gradio instead...
  3b. it's also not a use case for the project I'm going for, have an interactive based terminal seems more useful. 

4. The next steps are as follows:
  4a. Update chromadb + Docker to reflect new data
  4b. Validate response time and accuracy with rag_query.py and the larger database content, if slow response attempt to increase performance via more GPU (Work Laptop), additional preprocessing steps, or less data
  4c. Once response time and accuracy are suitable, implement gradio server for users to interact with model within LAN
  4d. Further brainstorming regarding how to incorproate with the DDS-Mv1e OR in a separate instance...

**Generating Modfile for Ollama Optimization**
- Ollama Modfile Setup Basics: https://www.gpu-mart.com/blog/custom-llm-models-with-ollama-modelfile
- More Ollama Basics: https://github.com/ollama/ollama/blob/main/docs/modelfile.md
- System Prompts and Modelfile Location: https://github.com/ollama-webui/ollama-modelfiles?tab=readme-ov-file




