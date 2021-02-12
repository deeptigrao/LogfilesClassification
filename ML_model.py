import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestClassifier

print("Reading Dataset...")
df = pd.read_csv('data.csv')

def score_to_numeric(x):
    if x=='allow':
        return 1
    if x=='deny':
        return 0
    if x=='drop':
        return 0
    if x=='reset-both':
        return 0

df['output'] = df['Action'].apply(score_to_numeric)

X = df[['NAT Source Port','NAT Destination Port','Bytes','Packets','Elapsed Time (sec)']]
y = df['output']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20)

print("Training model...")
rfc = RandomForestClassifier(n_estimators=15,random_state=42)
rfc.fit(X_train,y_train)

import pickle
filename = 'model_firewall.pkl'
print("Dumping File...")
pickle.dump(rfc, open(filename, 'wb'))