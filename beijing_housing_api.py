import connexion

# Instantiate our Flask app object
app = connexion.FlaskApp(__name__, port=8080, specification_dir='swagger/')
application = app.app

# Load our pre-trained model
# clf = joblib.load('./model/iris_classifier.joblib')

# Implement a simple health check function (GET)
def health():
    # Test to make sure our service is actually healthy
    try:
        1 + 1
    except:
        return {"Message": "Service is unhealthy"}, 500

    return {"Message": "Service is OK"}

def predict_location(min_total_price, max_total_price, min_square, max_square, district, tradeMonth, tradeYear, num_of_bedroom, num_of_bathroom, subway, elevator):
    # Accept the feature values provided as part of our POST
    # Use these as input to clf.predict()
    # prediction = clf.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    #
    # # Map the predicted value to an actual class
    # if prediction[0] == 0:
    #     predicted_class = "Iris-Setosa"
    # elif prediction[0] == 1:
    #     predicted_class = "Iris-Versicolour"
    # else:
    #     predicted_class = "Iris-Virginica"

    # Return the prediction as a json
    return {"prediction" : "test is ok"}

app.add_api("beijing_housing_api.yaml")

# Start the app
if __name__ == "__main__":
    app.run()