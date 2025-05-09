import numpy as np
import pandas as pd
from joblib import load
from sklearn.metrics import mean_squared_error

test_data = pd.read_csv("strat_testset.csv")

model = load("buildingcostpredictor.joblib")
mypipeline = load("data_pipeline.joblib")

# X_test = test_data.drop("Price", axis=1)
# Y_test = test_data["Price"].copy()
# X_test_prepared = mypipeline.transform(X_test)

# # Predict using the loaded model
# finalpredictions = model.predict(X_test_prepared)
# finalmse = mean_squared_error(Y_test, finalpredictions)
# finalrmse = np.sqrt(finalmse)
# print("Test RMSE:", finalrmse)
# print(finalpredictions,list(Y_test))

input_features = np.array([[
    3,         # number of bedrooms
    2,         # number of bathrooms
    1800,      # living area
    5000,      # lot area
    1,         # number of floors
    0,         # waterfront present
    2,         # number of views
    3,         # condition of the house
    7,         # grade of the house
    1200,      # Area of the house (excluding basement)
    600,       # Area of the basement
    1995,      # Built Year
    2010,      # Renovation Year
    98103,     # Postal Code
    47.659,    # Latitude
    -122.342,  # Longitude
    1800,      # living_area_renov
    5000,      # lot_area_renov
    3,         # Number of schools nearby
    30         # Distance from the airport
]
])

print(model.predict(input_features))