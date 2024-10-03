# Overview
mealchk-cli provides an experimental CLI for detecting potential artificial or processed ingredients, and can be used to help aid following a paleo, whole30, or clean-eating lifestyle.

Please note that due to the way manufacturers label food, in some cases some ingredients may not always be detected.

This tool should not be used alone, but rather to supplement other checks.

# Dependencies

```tesseract```

## MacOS

```brew install tesseract```

# Executing

pip3 install -r requirements.txt
python main.py# mealchk-cli

# Technical documentation

mealchk-api is written in Python, and utilizes AWS AI/ML services for helping analyze provided data.

Presently this application is intended to be used with Google Cloud.

# License
Licensed under GNU GPL v3.
