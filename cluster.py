import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn.cluster import KMeans

def generate_elbow_plot(train_scaled, validate_scaled, test_scaled, cluster_features):
    X_train = train_scaled[cluster_features]
    X_validate = validate_scaled[cluster_features]
    X_test = test_scaled[cluster_features]

    with plt.style.context('seaborn-whitegrid'):
        plt.figure(figsize=(9, 6))
        pd.Series({k: KMeans(k).fit(X_train).inertia_ for k in range(2, 12)}).plot(marker='x')
        plt.xticks(range(2, 12))
        plt.xlabel('k')
        plt.ylabel('inertia')
        plt.title('Change in inertia as k increases')
        
    return X_train, X_validate, X_test
        
def fit_clusters(train, validate, test, X_train, X_validate, X_test, cluster_num, cluster_name, x_plot, y_plot, compare_hue):
    kmeans = KMeans(n_clusters=cluster_num, random_state=1414)
    kmeans.fit(X_train)

    train[cluster_name] = kmeans.predict(X_train)
    train[cluster_name] = "cluster_" + train[cluster_name].astype(str)
    validate[cluster_name] = kmeans.predict(X_validate)
    validate[cluster_name] = "cluster_" + validate[cluster_name].astype(str)
    test[cluster_name] = kmeans.predict(X_test)
    test[cluster_name] = "cluster_" + test[cluster_name].astype(str)

    sns.scatterplot(x=x_plot, y=y_plot, hue=cluster_name, data=train)
    plt.title("Color coded by clusters")
    plt.show()
    sns.scatterplot(x=x_plot, y=y_plot, hue=compare_hue, data=train)
    plt.title(f"Color coded by {compare_hue}")
    plt.show()
    
def rename_clusters(name_dict, df, column_name):
    df = df.copy()
    
    keys = list(name_dict.keys())
    
    for key in keys:
        df[column_name] = df[column_name].str.replace(key, name_dict[key])
        
    return df