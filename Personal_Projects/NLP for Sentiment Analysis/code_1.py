import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Step 1: Load Data
def load_data(data_dir):
    texts = []
    labels = []
    for label in ['pos', 'neg']:
        folder = os.path.join(data_dir, label)
        for filename in os.listdir(folder):
            with open(os.path.join(folder, filename), 'r', encoding='utf-8') as file:
                texts.append(file.read())
                labels.append(label)
    return pd.DataFrame({'text': texts, 'label': labels})

data_dir = 'Users/lekhmac/Downloads/aclImdb/train'  # Change to the path where your dataset is located
df_train = load_data(data_dir)

# Step 2: Preprocess Data
def preprocess_data(df):
    df['text'] = df['text'].str.lower()  # Convert to lowercase
    return df

df_train = preprocess_data(df_train)

# Step 3: Split Data
X_train, X_val, y_train, y_val = train_test_split(df_train['text'], df_train['label'], test_size=0.2, random_state=42)

# Step 4: Vectorize Text Data
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_val_vec = vectorizer.transform(X_val)

# Step 5: Train Naive Bayes Classifier
clf = MultinomialNB()
clf.fit(X_train_vec, y_train)

# Step 6: Make Predictions
y_pred = clf.predict(vectorizer.transform(X_val))

# Step 7: Evaluate Model
accuracy = accuracy_score(y_val, y_pred)
print(f'Accuracy: {accuracy:.2%}')
