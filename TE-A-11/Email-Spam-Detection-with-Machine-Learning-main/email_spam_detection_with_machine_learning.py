# Importing Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, roc_curve, classification_report
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from wordcloud import WordCloud, STOPWORDS
import warnings

# Ignore Warnings
warnings.filterwarnings('ignore')

"""### Dataset Loading"""

# Corrected Dataset Loading
df = pd.read_csv('C:\Users\vchin\OneDrive\Desktop\Email_Detection_System\data\spam.csv')

"""### Dataset First View"""

# Dataset First Look
print(df.head())

"""### Dataset Rows & Columns count"""

print("Number of rows are: ", df.shape[0])
print("Number of columns are: ", df.shape[1])

"""### Dataset Information"""

df.info()

"""#### Duplicate Values"""

dup = df.duplicated().sum()
print(f'Number of duplicated rows are {dup}')

"""#### Missing Values/Null Values"""

print(df.isnull().sum())

"""### Preprocessing"""

# Renaming columns
df.rename(columns={"v1": "Category", "v2": "Message"}, inplace=True)

# Drop unnecessary columns
df.drop(columns=['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True)

# Create Spam column (binary 1/0)
df['Spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)

# Updated dataset view
print(df.head())

"""### Data Visualization"""

# Pie Chart for Category distribution
spread = df['Category'].value_counts()
plt.rcParams['figure.figsize'] = (5,5)
spread.plot(kind='pie', autopct='%1.2f%%', cmap='Set1')
plt.title('Distribution of Spam vs Ham')
plt.show()

# WordCloud for Spam Messages
df_spam = df[df['Category'] == 'spam'].copy()

comment_words = ''
stopwords = set(STOPWORDS)

for val in df_spam.Message:
    val = str(val)
    tokens = val.split()
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    comment_words += " ".join(tokens) + " "

wordcloud = WordCloud(width=1000, height=500, background_color='white',
                      stopwords=stopwords, min_font_size=10,
                      max_words=1000, colormap='gist_heat_r').generate(comment_words)

plt.figure(figsize=(6,6), facecolor=None)
plt.title('Most Used Words In Spam Messages', fontsize=15, pad=20)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()

"""### Splitting the Data"""

X_train, X_test, y_train, y_test = train_test_split(df['Message'], df['Spam'], test_size=0.25, random_state=42)

"""### Model Evaluation Function"""

def evaluate_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    pred_prob_train = model.predict_proba(X_train)[:,1]
    pred_prob_test = model.predict_proba(X_test)[:,1]
    
    roc_auc_train = roc_auc_score(y_train, y_pred_train)
    roc_auc_test = roc_auc_score(y_test, y_pred_test)
    
    print("\nTrain ROC AUC:", roc_auc_train)
    print("Test ROC AUC:", roc_auc_test)

    fpr_train, tpr_train, _ = roc_curve(y_train, pred_prob_train)
    fpr_test, tpr_test, _ = roc_curve(y_test, pred_prob_test)

    plt.plot([0,1],[0,1],'k--')
    plt.plot(fpr_train, tpr_train, label="Train ROC AUC: {:.2f}".format(roc_auc_train))
    plt.plot(fpr_test, tpr_test, label="Test ROC AUC: {:.2f}".format(roc_auc_test))
    plt.legend()
    plt.title("ROC Curve")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.show()

    cm_train = confusion_matrix(y_train, y_pred_train)
    cm_test = confusion_matrix(y_test, y_pred_test)

    fig, ax = plt.subplots(1, 2, figsize=(11,4))

    sns.heatmap(cm_train, annot=True, cmap="Oranges", fmt='d', ax=ax[0])
    ax[0].set_title('Train Confusion Matrix')

    sns.heatmap(cm_test, annot=True, cmap="Oranges", fmt='d', ax=ax[1])
    ax[1].set_title('Test Confusion Matrix')

    plt.tight_layout()
    plt.show()

    cr_train = classification_report(y_train, y_pred_train, output_dict=True)
    cr_test = classification_report(y_test, y_pred_test, output_dict=True)

    print("\nTrain Classification Report:")
    print(pd.DataFrame(cr_train).T.to_markdown())

    print("\nTest Classification Report:")
    print(pd.DataFrame(cr_test).T.to_markdown())

    precision_train = cr_train['weighted avg']['precision']
    precision_test = cr_test['weighted avg']['precision']

    recall_train = cr_train['weighted avg']['recall']
    recall_test = cr_test['weighted avg']['recall']

    acc_train = accuracy_score(y_train, y_pred_train)
    acc_test = accuracy_score(y_test, y_pred_test)

    F1_train = cr_train['weighted avg']['f1-score']
    F1_test = cr_test['weighted avg']['f1-score']

    model_score = [precision_train, precision_test, recall_train, recall_test, acc_train, acc_test, roc_auc_train, roc_auc_test, F1_train, F1_test]
    return model_score

"""### ML Model: Multinomial Naive Bayes"""

clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

MultinomialNB_score = evaluate_model(clf, X_train, X_test, y_train, y_test)

"""### Spam Detection Function"""

def detect_spam(email_text):
    prediction = clf.predict([email_text])
    return "This is a Spam Email!" if prediction == 1 else "This is a Ham Email!"

"""### Test the Spam Detector"""

sample_email = 'Free Tickets for IPL'
result = detect_spam(sample_email)
print(result)
