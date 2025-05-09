import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split , StratifiedShuffleSplit ,cross_val_score
import seaborn as sns
from pandas.plotting import scatter_matrix
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


from joblib import dump,load

housing = pd.read_csv("Data.csv")
housing = housing.drop(['id','Date'],axis=1)
housing[['number of bathrooms','number of floors']] = housing[['number of bathrooms','number of floors']].round().astype(int)
# print(housing.info())
# print(housing['condition of the house'].value_counts())
# print(housing['number of views'].value_counts())
# print(housing['Renovation Year'].value_counts())
# print(housing['waterfront present'].value_counts())
# print(housing.describe())

# housing.hist(bins=60,figsize=(20,15))
# plt.show()

train_set,test_set = train_test_split(housing,test_size=0.2,random_state=42)
# print(len(train_set))
# print(len(test_set))

split = StratifiedShuffleSplit(n_splits=1,test_size=0.2,random_state=42)
for train_index,test_index in split.split(housing,housing['waterfront present']):
    strat_trainset = housing.loc[train_index]
    strat_testset = housing.loc[test_index]

# print(strat_trainset['waterfront present'].value_counts())
# print(strat_testset['waterfront present'].value_counts())
housing = strat_trainset.copy()


housing = strat_trainset.drop("Price",axis=1)
housing_label = strat_trainset["Price"].copy()

# Save strat_testset
strat_testset.to_csv("strat_testset.csv", index=False)


# plt.figure(figsize=(20,10))
# sns.heatmap(strat_trainset.corr(),annot=True,cmap="YlGnBu")
# plt.show()

# corr_matrix = housing.corr()
# print(corr_matrix['Price'].sort_values(ascending=False))

# attributes = ['Price','living area','grade of the house','Postal Code']
# scatter_matrix(housing[attributes],figsize=(12,8))

# housing.plot(kind="scatter",x="living area",y="Price",alpha=0.8)

# plt.show()

# for missing data

# median = housing["living area"].mean()

# print(housing['living area'].fillna(median))
# print(housing.shape)

#these below steps in pipeline
# imputer = SimpleImputer(strategy="median")
# imputer.fit(housing)

# print(imputer.statistics_)

# X = imputer.transform(housing)

# housing_tr = pd.DataFrame(X,columns=housing.columns)

# print(housing_tr.describe())

mypipeline = Pipeline([("imputer",SimpleImputer(strategy="median")),("std_scaler",StandardScaler()),])

housing_num_tr = mypipeline.fit_transform(housing)

# print(housing_num_tr.shape)


#models

#model = LinearRegression()
#model = DecisionTreeRegressor()
model = RandomForestRegressor()
model.fit(housing_num_tr,housing_label)

# some_data = housing.iloc[:5]
# some_labels = housing_label.iloc[:5]
# prepared_data = mypipeline.transform(some_data)
# print(model.predict(prepared_data))

# print(some_labels)

# housing_predictions = model.predict(housing_num_tr)
# mse = mean_squared_error(housing_label,housing_predictions)
# rmse = np.sqrt(mse)
# print(mse)

scores = cross_val_score(model,housing_num_tr,housing_label,scoring="neg_mean_squared_error",cv=10)
rmse_scores = np.sqrt(-scores)

# print(rmse_scores)


def print_scores(scores):
    print("Scores : ",scores)
    print("Mean : ",scores.mean())
    print("Standared Deviation : ",scores.std())

print_scores(rmse_scores)

#saving model
dump(model,"buildingcostpredictor.joblib")
dump(mypipeline, "data_pipeline.joblib")

#testing

# X_test = strat_testset.drop("Price",axis=1)
# Y_test = strat_testset["Price"].copy()
# X_test_prepared = mypipeline.transform(X_test)
# finalpredictions = model.predict(X_test_prepared)
# finalmse = mean_squared_error(Y_test,finalpredictions)
# finalrmse = np.sqrt(finalmse)

# print(finalrmse)