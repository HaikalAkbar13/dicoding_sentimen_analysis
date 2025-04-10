# Dicoding Machine Learning Development First Project (Sentiment Analysis)

### Name : Muh Haikal Akbar  
### DicodingUser : muh_haikal_akbar  
### Email : haikalakbar10k@gmail.com  
---
Hi, my name is Haikal. This is my submission for the Machine Learning Development First Project (**Sentiment Analysis**).

## Context  
*USA Tariffs* (also known as *Trump Tariffs*) refer to a series of import tariffs introduced by U.S. President Donald Trump as part of his administration’s protectionist trade strategy. These tariffs mainly targeted imports from China, the European Union, Canada, and Mexico, with the intention of protecting American industries, encouraging domestic manufacturing, and reducing trade deficits.

The implementation of these tariffs sparked intense global reactions and widespread discourse, particularly on social media platforms like Twitter. Supporters believed that these tariffs would protect local jobs, boost the U.S. economy, and ensure fairer trade deals. On the other hand, critics argued that the tariffs led to increased prices for consumers, disrupted supply chains, and triggered retaliatory measures from other countries.

The global economic impact was significant — the tariffs strained U.S.-China trade relations, slowed down global trade, and introduced uncertainty into international markets. Sectors such as agriculture, automotive, and technology were notably affected, with some businesses relocating supply chains or facing reduced export opportunities.

This project aims to analyze public sentiment on Twitter regarding these tariffs and categorize the reactions into three main sentiment classes: **Agree**, **Neutral**, and **Disagree**.

## Objective  
The objective of this project is to build a machine learning model capable of identifying sentiment patterns in Twitter posts related to the *USA Tariffs* topic. The model will classify each tweet into one of the following categories:

- **Agree**: Expresses support for the tariff policy.  
- **Neutral**: Does not convey a clear opinion or takes an informational stance.  
- **Disagree**: Expresses opposition or disapproval of the tariff policy.

By performing this classification, we aim to better understand the overall public perception of the tariffs as expressed on social media.

## Model and Approach Used  
In this project, a supervised learning approach was implemented to develop a sentiment classification model. The main steps in the workflow included:

1. **Data Preprocessing**  
   Tweets were cleaned by converting text to lowercase, removing URLs, mentions, hashtags, punctuations, and stopwords. Tokenization and lemmatization were also applied to standardize the text.

2. **Text Vectorization**  
   Techniques such as TF-IDF or word embeddings (e.g., Word2Vec or GloVe) were used to convert the textual data into numerical representations suitable for training machine learning models.

3. **Model Selection and Training**  
   Multiple Deep Learning algorithms such as CNN, RoBERTa, and BERT were evaluated. The model with the best validation performance was selected as final Model.

4. **Evaluation Metrics**  
   Model performance was assessed using metrics including accuracy, precision, recall, and F1-score. K-fold cross-validation was also used to validate the model’s generalizability.

5. **Prediction and Deployment**  
   The trained model was used to classify new or unseen tweets into one of the three sentiment categories: **Agree**, **Neutral**, or **Disagree**.

## Technical Goals  
- Build an end-to-end sentiment analysis using real-world Twitter data.  
- Apply data preprocessing techniques suitable for social media text.  
- Experiment with different machine learning algorithms and text vectorization techniques.  
- Evaluate model performance using appropriate classification metrics.
