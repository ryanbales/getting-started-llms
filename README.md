# Getting Started wiht LLMs
## Overview
This is an example of using the OpenAI API in a python application. The python application is a web application hosted in streamlit.

## Design
This web application runs in python and uses Flask to serve the web pages. It uses Redis via AWS ElastiCache to store the session data and is deployed to AWS using Elastic Beanstalk.  Currently, all conversation data is static and stored in AWS S3 and retreived on-demand.  In the future, this will be updated to use diffeernt data storage systems.

## Prerequisites
In order to get your local environment set up, you will need to have the following installed:

- Homebrew: [Installing Homebrew](https://docs.brew.sh/Installation)
- Python 3.11.4: I recommend using [pyenv](https://github.com/pyenv/pyenv#getting-pyenv)
- Poetry: [Installing Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)

## Settup up your OpenAI API Key
Once you have your local environment set up, you will need to setup an OpenAI developer accouint and obtain an OpenAI API key. Once you have your API key, you will need to set it as an environment variable. You can do this by editing your `.zshrc` file or by running the following command:

```bash
export OPENAI_ORG_ID="your_organization_id_here"
export OPENAI_API_KEY="your_api_key_here"
```

## Running the app locally
In order to run the app locally, you will need to install the dependencies. You can do this by running the following command:

```bash
poetry install
```

Then, you can run the app locally by running the following command:

```bash
poetry run streamlit run app.py
```

This will start the streamlit application on your local machine. You can access it by going to http://localhost:8501/ in your web browser.
