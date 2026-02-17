# NLP_ticketing

NLP-based ticket classification and priority detection system using Python and scikit-learn

# Ticket Classification & Priority Detection

## 📖 Overview

This project is a simple machine learning–based ticketing system that analyzes
incoming support messages, predicts their category, and assigns a priority level.
It is designed to demonstrate practical NLP techniques applied to real-world
customer support workflows.

## ⚙️ Features

- Text preprocessing and normalization
- Sentence embedding using SentenceTransformers
- Ticket category prediction with Logistic Regression
- Rule-based priority detection for urgent issues
- Modular and extensible code structure

## 🧠 How it works

1. Ticket text is cleaned and normalized
2. Sentences are converted into embeddings using a pre-trained transformer model
3. A logistic regression classifier predicts the ticket category
4. Priority is determined using keyword-based rules

## 🔨Tech stack

- Python
- SentenceTransformers
- scikit-learn
- Regular Expressions (re)
- Git & GitHub

## 🚀 Usage

# Train the classifier

clf = train_classifier(texts, labels)

# Predict ticket category

predict_category("Payment failed during checkout", clf)

# Predict priority

predict_priority("System crash detected")
