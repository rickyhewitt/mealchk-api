# Overview
mealchk-cli provides an experimental CLI for detecting potential artificial or processed ingredients in food labels.

Please note that due to the way manufacturers label food, in some cases some ingredients may not always be detected.

This tool should not be used alone, but rather to supplement other checks.

# Screenshots

**Example #1 (Original image + mealchk-cli output):**

<img src="https://github.com/user-attachments/assets/17c38445-22d1-48e0-a1ee-236e6f27f338" alt="Example 1" width="720" />

**Example #2 (Original image + mealchk-cli output):**

<img src="https://github.com/user-attachments/assets/c5e48545-e267-490c-b17b-e8de1fdcbb49" alt="Example 2" width="720" />

# Image recognition providers
Multiple methods of image recognition are available to use, currently the following are supported:

* local (default, via pytesseract)
* AWS Rekognition (TODO)
* Google Cloud (google-cloud-vision)

The provider can currently be set by setting the PROVIDER const within main.py (future releases will allow provider to be set via command line arguments). You can also add your own image recognition providers within ```providers/```

# Installation & Setup

## Provider plugins

Configuration is only required for the active provider plugin that is enabled. Feel free to skip, for example, the Google Cloud configuration if you are only using local or AWS.

### Local (Pytesseract)
#### MacOS

```brew install tesseract```

### Google Cloud (gcloud)
#### Configure API key
Ensure that a valid API key is set via the GOOGLE_APPLICATION_CREDENTIALS environment variable.

```export GOOGLE_APPLICATION_CREDENTIALS="/home/you/project-000-fff.json"```

# Executing

```
# Create virtualenv
python3 -m venv ./virtualenv

# Activate virtualenv
source ./virtualenv/bin/activate

# Install requirements via pip
pip3 install -r requirements.txt

# Run program
python main.py mealchk-cli
```

# Example usage:

**Example 1 (single image):**

```python3 main.py img/sample/ingredients1.jpg```

**Example 2 (multiple images):**

```python3 main.py img/sample/ingredients2.jpg img/sample/ingredients3.jpg```

## Sample images

Sample images are provided in img/sample. 

Future versions of mealchk may integrate webcam.

# Credit

Developed by Ricky Hewitt <ricky@rickyhewitt.dev>

# License
Licensed under GNU GPL v3.
