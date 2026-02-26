import streamlit as st
import numpy as np
import pickle

# Load trained files
model = pickle.load(open("hybrid_ids_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
label_encoder = pickle.load(open("label_encoder.pkl", "rb"))

st.title("🔐 Network Intrusion Detection System")
st.write("Enter network traffic parameters to detect intrusion.")

st.subheader("Enter Network Features")

# Example 10 features (CHANGE according to your dataset feature count)
feature1 = st.number_input("Feature 1 (duration)", value=0.0)
feature2 = st.number_input("Feature 2 (protocol_type)", value=0.0)
feature3 = st.number_input("Feature 3 (service)", value=0.0)
feature4 = st.number_input("Feature 4 (flag)", value=0.0)
feature5 = st.number_input("Feature 5 (src_bytes)", value=0.0)
feature6 = st.number_input("Feature 6 (dst_bytes)", value=0.0)
feature7 = st.number_input("Feature 7", value=0.0)
feature8 = st.number_input("Feature 8", value=0.0)
feature9 = st.number_input("Feature 9", value=0.0)
feature10 = st.number_input("Feature 10", value=0.0)

# Put all features into array
features = np.array([[feature1, feature2, feature3, feature4, feature5,
                      feature6, feature7, feature8, feature9, feature10]])

if st.button("🚀 Detect Intrusion"):

    try:
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)
        result = label_encoder.inverse_transform(prediction)

        if result[0] == "Attack":
            st.error("⚠️ Intrusion Detected!")
        else:
            st.success("✅ Normal Traffic Detected")

    except Exception as e:
        st.error(f"Error: {e}")