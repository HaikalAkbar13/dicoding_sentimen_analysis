# Dicoding Machine Learning Development First Project (Sentiment Analysis)

### Name : Muh Haikal Akbar  
### DicodingUser : muh_haikal_akbar  
### Email : haikalakbar10k@gmail.com  
---
Hi, my name is [Your Name]. This is my submission for the Machine Learning Development First Project (**Sentiment Analysis**).

## Context  
*Artificial Intelligence (AI)* has seen significant advancements and adoption across various sectors including finance, manufacturing, healthcare, education, and more. Its rapid integration into the economy has sparked widespread discussions and debates about its overall impact on job markets, business efficiency, productivity, and even societal structures.

Some see AI as a powerful force for economic growth, increased automation, and improved decision-making. Others are concerned about potential job losses, increased inequality, and ethical dilemmas. Social media platforms, especially Twitter, have become key venues where people share their opinions, insights, and concerns about AI's role in the economy.

This project aims to analyze public sentiment on Twitter regarding the economic impact of AI and categorize the reactions into three main sentiment classes: **Positive**, **Neutral**, and **Negative**.

## Objective  
The objective of this project is to build a machine learning model capable of identifying sentiment patterns in Twitter posts related to the *economic implications of AI*. The model will classify each tweet into one of the following categories:

- **Positive**: Expresses optimism or support for AI's role in economic growth.  
- **Neutral**: Shares information or commentary without strong sentiment.  
- **Negative**: Expresses concern, criticism, or pessimism about AI’s economic effects.

By performing this classification, we aim to better understand how the public perceives the economic consequences of AI adoption.

## Model and Approach Used  
In this project, a supervised learning approach was implemented to develop a sentiment classification model. The main steps in the workflow included:

1. **Data Preprocessing**  
   Tweets were cleaned by converting text to lowercase, removing URLs, mentions, hashtags, punctuations, and stopwords. Tokenization and lemmatization were applied to normalize the content.

2. **Text Vectorization**  
   Techniques such as TF-IDF or pretrained word embeddings (e.g., Word2Vec, GloVe, or BERT embeddings) were used to convert the text into numerical features suitable for training.

3. **Model Selection and Training**  
   Various models such as LSTM, CNN, and transformer-based architectures like BERT or RoBERTa were tested. The best-performing model on validation data was selected for final deployment.

4. **Evaluation Metrics**  
   The model was evaluated using accuracy, precision, recall, and F1-score. Stratified K-fold cross-validation was used to ensure robust evaluation.

5. **Prediction and Deployment**  
   The final trained model was used to predict the sentiment of unseen tweets, classifying them into **Positive**, **Neutral**, or **Negative** categories.

## Technical Goals  
- Build an end-to-end sentiment analysis system using real-world Twitter data related to AI and the economy.  
- Apply effective preprocessing techniques tailored for social media text.  
- Explore and compare performance of various NLP models and embeddings.  
- Use appropriate evaluation metrics to assess model accuracy and reliability.
