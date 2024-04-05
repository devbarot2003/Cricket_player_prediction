import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import pickle


def load_data():
    with open('data.pkl', 'rb') as f:
        data = pickle.load(f)  # Replace 'your_data.csv' with the actual filename/path of your dataset
    return data

# Load your trained model
def load_model():
    with open('your_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Function to predict batting and bowling points
def predict_points(model, data):
    # Assuming 'data' is a dictionary containing user inputs
    X = pd.DataFrame(data, index=[0])

    # Make predictions
    predictions = model.predict(X)
    return predictions

# Main function to run the Streamlit app
def main():
    # Load your dataset
    data = load_data()


    # Load your trained model
    model = load_model()

    # Title and description for the app
    st.title("Cricket Points Prediction")
    st.write("Enter the details below to predict batting and bowling points:")

    # Get user inputs
    runs = st.number_input("Runs:")
    boundaries = st.number_input("Boundaries:")
    sixes = st.number_input("Sixes:")
    fifties = st.number_input("Fifties:")
    hundreds = st.number_input("Hundreds:")
    ducks = st.number_input("Ducks:")
    wickets = st.number_input("Wickets:")
    _4w_haul = st.number_input("4 Wicket Hauls:")
    _5w_haul = st.number_input("5 Wicket Hauls:")
    maidens = st.number_input("Maidens:")

    # Get list of unique player names from the dataset
    player_names = data['Player_Name'].unique()
    

    # Select player name from dropdown menu
    player_name = st.selectbox("Select Player Name:", player_names)
    label_encoder = LabelEncoder()
    encoded = label_encoder.fit_transform([player_name])

    
    # Predict points when the user clicks the 'Predict' button
    if st.button("Predict"):
        # Prepare input data for prediction
        data = {
            'Runs': runs,
            'Boundaries': boundaries,
            'Six': sixes,
            'Fifty': fifties,
            'Hundred': hundreds,
            'Duck': ducks,
            'Wickets': wickets,
            '4W_Haul': _4w_haul,
            '5W_Haul': _5w_haul,
            'Maidens': maidens,
            'Player_Name_encoded': encoded
        }
        # Predict batting and bowling points
        predictions = predict_points(model, data)
        batting_points, bowling_points = predictions[0]

        # Display the predicted points
        st.write("Predicted Batting Points:", round(batting_points))
        st.write("Predicted Bowling Points:", round(bowling_points))

if __name__ == "__main__":
    main()
