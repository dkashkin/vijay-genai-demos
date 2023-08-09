# Generative AI for Medical Search

Demonstrates using Enterprise Search for Q&A on a corpus of PDF documents with citations.  

![Architecture](https://github.com/vijaykyr/genai-demos/blob/main/medical_search/app/images/architecture.png "Architecture")

## Deploy Locally
Set environment variables
```commandline
export GOOGLE_CLOUD_PROJECT=[your-project-id]
export SEARCH_ENGINE_ID=[your-enterprise-search-engine-id]
```
Install dependencies
```commandline
pip install -r requirements.txt
```
Launch
```commandline
streamlit run About.py
```

## Deploy to App Engine

Ensure the default App Engine service account has the following IAM permissions:
- Discovery Engine Editor
- Discovery Engine Service Agent

Set the environment variables in `app.yaml`
```yaml
env_variables:
    SEARCH_ENGINE_ID: your-enterprise-search-engine-id
```

Deploy
```commandline
gcloud app deploy
```
