import numpy as np
import pandas as pd
from joblib import load
import sys
import json
#from sklearn.metrics import mean_squared_error

test_data = pd.read_csv("strat_testset.csv")
feature_names = load("feature_names.joblib")

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

def predict_price(input_data):
    formatted_input_data = np.array([[ 
    input_data["bedrooms"],
    input_data["bathrooms"],
    input_data["living_area"],
    input_data["lot_area"],
    input_data["floors"],
    input_data["waterfront"],
    input_data["views"],
    input_data["condition"],
    input_data["grade"],
    input_data["area_excluding_basement"],
    input_data["basement_area"],
    input_data["built_year"],
    input_data["renovation_year"],
    input_data["postal_code"],
    input_data["latitude"],
    input_data["longitude"],
    input_data["living_area_renov"],
    input_data["lot_area_renov"],
    input_data["nearby_schools"],
    input_data["distance_airport"],
    ]])
    # print(formatted_input_data, file=sys.stderr)
    # print(feature_names, file=sys.stderr)

    # input_df = pd.DataFrame(formatted_input_data)
    
    #rint(f"Received input: {input_data}", file=sys.stderr)
    #print(f"Received input: {input_df}", file=sys.stderr)
    #input_prepared = mypipeline.transform(formatted_input_data)
    #print(f"Received input: {input_prepared}", file=sys.stderr)
    

    # try:
    #     prediction = model.predict(formatted_input_data)
    # except Exception as e:
    #     print(f"Prediction error: {e}", file=sys.stderr)
    #     raise
    prediction = model.predict(formatted_input_data)
    return prediction[0]


if __name__ == "__main__":
    # Get the input data from stdin (which is passed by the Node.js backend)
    input_data = json.loads(sys.stdin.read())
    prediction = predict_price(input_data)
    # Output the prediction as a JSON string
    print(json.dumps({"predicted_price": float(prediction)}))