# Overview
mealchk-cli provides an experimental CLI for detecting potential artificial or processed ingredients, and can be used to help aid following a paleo, whole30, or clean-eating lifestyle.

Please note that due to the way manufacturers label food, in some cases some ingredients may not always be detected.

This tool should not be used alone, but rather to supplement other checks.

## Installation & Setup

### Providers
#### Local (Pytesseract)
##### MacOS

```brew install tesseract```

# Executing

```pip3 install -r requirements.txt```

```python main.py mealchk-cli```

#### Google Cloud (gcloud)
##### Configure API key
Ensure that a valid API key is set via the GOOGLE_APPLICATION_CREDENTIALS environment variable.

e.g. export GOOGLE_APPLICATION_CREDENTIALS="/home/you/project-000-fff.json"

# Technical documentation

mealchk-api is written in Python.

# Image recognition providers
Multiple methods of image recognition are available to use, currently the following are supported:

* local (default, via pytesseract)
* AWS Rekognition (TODO)
* Google Cloud (google-cloud-vision)

The provider can currently be set by setting the PROVIDER const within main.py (future releases will allow provider to be set via command line arguments)

# Example usage:

```python3 main.py img/sample/ingredients1.jpg```
```python3 main.py img/sample/ingredients2.jpg```
```python3 main.py img/sample/ingredients3.jpg```

# Credit

Developed by Ricky Hewitt <ricky@rickyhewitt.dev>

# License
Licensed under GNU GPL v3.
