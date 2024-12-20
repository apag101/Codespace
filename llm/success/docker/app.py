# Medium atricle: https://towardsdatascience.com/how-to-run-a-data-science-project-in-a-docker-container-2ab1a3baa889

import pandas as pd
import numpy as np
df = pd.read_csv('source/heart.csv')
df.head()

df.shape

features = []
for column in df.columns:
    if column != 'output':
        features.append(column)
X = df[features]
Y = df['output']

X.describe()

# from sklearn.preprocessing import MinMaxScaler
# for column in X.columns:
#     feature = np.array(X[column]).reshape(-1,1)
#     scaler = MinMaxScaler()
#     scaler.fit(feature)
#     feature_scaled = scaler.transform(feature)
#     X[column] = feature_scaled.reshape(1,-1)[0]

# import numpy as np
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size=0.20, random_state=42)

# # y_train.value_counts()

# from imblearn.over_sampling import RandomOverSampler
# over_sampler = RandomOverSampler(random_state=42)
# X_bal_over, y_bal_over = over_sampler.fit_resample(X_train, y_train)

# y_bal_over.value_counts()

print("test over")

# from imblearn.under_sampling import RandomUnderSampler
# under_sampler = RandomUnderSampler(random_state=42)
# X_bal_under, y_bal_under = under_sampler.fit_resample(X_train, y_train)

# from sklearn.neighbors import KNeighborsClassifier
# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X_train, y_train)
# y_score = model.predict_proba(X_test)

# import matplotlib.pyplot as plt
# from sklearn.metrics import roc_curve
# from scikitplot.metrics import plot_roc,auc
# from scikitplot.metrics import plot_precision_recall
# fpr0, tpr0, thresholds = roc_curve(y_test, y_score[:, 1])
# # Plot metrics 
# plot_roc(y_test, y_score)
# plt.show()
    
# plot_precision_recall(y_test, y_score)
# plt.show()

# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X_bal_over, y_bal_over)
# y_score = model.predict_proba(X_test)
# fpr0, tpr0, thresholds = roc_curve(y_test, y_score[:, 1])
# # Plot metrics 
# plot_roc(y_test, y_score)
# plt.show()
    
# plot_precision_recall(y_test, y_score)
# plt.show()


# model = KNeighborsClassifier(n_neighbors=3)
# model.fit(X_bal_under, y_bal_under)
# y_score = model.predict_proba(X_test)
# fpr0, tpr0, thresholds = roc_curve(y_test, y_score[:, 1])
# # Plot metrics 
# plot_roc(y_test, y_score)
# plt.show()
    
# plot_precision_recall(y_test, y_score)
# plt.show()

# from sklearn.model_selection import GridSearchCV
# model = KNeighborsClassifier()
# param_grid = {
#    'n_neighbors': np.arange(2,8),
#    'algorithm' : ['auto', 'ball_tree', 'kd_tree', 'brute'],
#     'metric' : ['euclidean','manhattan','chebyshev','minkowski']
# }
# grid = GridSearchCV(model, param_grid = param_grid)
# grid.fit(X_train, y_train)
# best_estimator = grid.best_estimator_

# best_estimator.fit(X_train, y_train)
# y_score = best_estimator.predict_proba(X_test)
# fpr0, tpr0, thresholds = roc_curve(y_test, y_score[:, 1])
# # Plot metrics 
# plot_roc(y_test, y_score)
# plt.show()
    
# plot_precision_recall(y_test, y_score)
# plt.show()

