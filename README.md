
# Project Scope Document

**Project Title:** **EmRec**:Speech Emotion Recognition Using Machine Learning. 

**Prepared by:** Nasim Ghazanfari Nasrabadi, Nicole Bidwell, Waleed Mahmood


## 🔍 Project Overview

This project focuses on developing a machine learning model that can detect and classify human emotions from spoken English audio. By analyzing vocal features such as tone, pitch, energy, and rhythm, the model aims to predict the emotional state of a speaker with high accuracy.

The core of this project is a supervised learning pipeline trained on labeled emotional speech data. The system extracts acoustic features from .wav files and classifies them into distinct emotional categories.

## 🌟 Objectives

Build a system that can recognize emotions in human speech.

Train and evaluate the model using the RAVDESS dataset.

Extract meaningful audio features using signal processing techniques.

Demonstrate the model’s potential real-world applications in health, AI, and communication.

## 📦 Dataset: RAVDESS

Name: Ryerson Audio-Visual Database of Emotional Speech and Song

Language: English

Size: ~1,440 audio clips (spoken utterances)

Speakers: 24 actors (balanced male and female)

Emotions: Neutral, Calm, Happy, Sad, Angry, Fearful, Disgust, Surprised

Format: High-quality .wav files

Label Source: Emotion label is encoded in the filename

## 🗞️ Data Description

Each audio file name follows a structured naming convention:

modality-vocal_channel-emotion-intensity-statement-repetition-actor.wav

The project extracts metadata from filenames to create a structured dataset, including:

Emotion label (target variable)

Actor ID

Intensity (normal or strong)

Gender (derived from actor ID)

## 🔧 Features Extracted

Features are extracted from audio files using the librosa Python library, including:

MFCCs (Mel-Frequency Cepstral Coefficients) – core feature for speech analysis

Chroma Features – pitch class representation

Spectral Features – centroid, bandwidth, rolloff, contrast

Zero Crossing Rate (ZCR) – measures signal noisiness

RMS Energy – signal loudness

Tonnetz – tonal centroid features

## 🧠 Modeling Approach

Preprocessing: Audio features are extracted and normalized.

Label Encoding: Emotion classes are converted into numerical labels.

Modeling Algorithms:

Classical ML: Random Forest, SVM

Deep Learning: CNNs on spectrograms

Evaluation:

Accuracy

Precision, Recall, F1-score

Confusion Matrix

## 🧪 Evaluation

Performance is evaluated using:

Train/Test Split (80/20 or cross-validation)

Classification Report (for precision, recall, F1-score)

Confusion Matrix (to analyze misclassifications)

## 🌍 Real-World Applications

Mental Health Monitoring: Detect emotional distress from voice

Customer Support: Route frustrated callers to specialized agents

In-Car Systems: Alert drivers when stress or fatigue is detected

Education: Gauge student engagement during remote learning

Voice Assistants: Make AI responses more human and empathetic

## 📈 Project Deliverables

Clean and labeled dataset with extracted features

Trained emotion classification model

Evaluation metrics and visualizations

Project report/documentation

Real-time emotion prediction demo tool
