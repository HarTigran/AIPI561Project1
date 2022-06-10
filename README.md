# AIPI561Project1
CLI Prediction Tool

[![Project 1 AIPI 561](https://github.com/robbjr21/AIPI561Project1/actions/workflows/main.yml/badge.svg)](https://github.com/robbjr21/AIPI561Project1/actions/workflows/main.yml)

Link to model: https://huggingface.co/distilbert-base-cased-distilled-squad?context=My+name+is+Sarah+and+I+live+in+London&question=Where+do+I+live%3F

This algorithm is pre-trained to answer questions based on a supplied context.

# Steps to Configure
1) Create a virtual environment.

```
cd Image-Embeddings-CLI-Tool/
virtualenv venv
```

2) Activate the virtual environment.

```
source venv/bin/activate
```

3) Then run: **(recommended)**

```
make all
```

- or install the requirements using pip.

```
pip install -r requirements.txt
```

## Usage

To use the pre-trained algorithm. Provide the question and the context in the following manner:

```
python3 q_and_a.py "What is biggest?, A meter is bigger than a centimeter. A centimeter is bigger than a millimeter. A millimeter is bigger than a micron.”
```
