import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import matplotlib.pyplot as plt

def perform_analysis(method, data):
    df = pd.DataFrame(data)
    X = df.drop('target', axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    if method == 'logistic_regression':
        model = LogisticRegression()
    elif method == 'random_forest':
        model = RandomForestClassifier()
    elif method == 'svm':
        model = SVC()

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return predictions  # Return predictions for display

def generate_report(data):
    df = pd.DataFrame(data)
    report_file = 'app/reports/report.xlsx'
    df.to_excel(report_file)
    plt.figure(figsize=(10, 6))
    df.plot(kind='bar')
    plt.title('Data Analysis Report')
    plt.savefig('app/static/reports/report_plot.png')
    return report_file
