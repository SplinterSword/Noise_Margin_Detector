import streamlit as st
import joblib
import numpy as np

# Load the pre-trained XGBoost model
model_path = 'best_xgb_model.joblib'
noise_model = joblib.load(model_path)

def predict_noise(vdd, vth, load_capacitance, temperature):
    input_features = np.array([[vdd, vth, load_capacitance, temperature]])
    noise_prediction = noise_model.predict(input_features)[0]
    
    noise_levels = {
        0: 'Low',
        1: 'Medium', 
        2: 'High'
    }
    
    return noise_levels[noise_prediction]

def noise_reduction_tips(noise_level):
    if noise_level == 'Low':
        return "Your circuit appears to have low noise levels. Good design!"
    
    tips = {
        'Medium': [
            "Shield Your Cables: Use shielded cables to minimize electrostatic noise.",
            "Use Twisted Pair Cables: Helps eliminate normal mode noise.",
            "Isolate Signals: Prevent ground loops by isolating noisy devices.",
            "Use Differential Measurements: Reduces common mode noise and improves signal integrity."
        ],
        'High': [
            "Ground Wires Properly: Establish a ground plane for stable reference potential.",
            "Route Wires Strategically: Segregate high and low voltage lines to avoid interference.",
            "Use Anti-Aliasing Filters: Minimize aliasing and filter high-frequency noise.",
            "Consider Application-Specific Noise Control: Consult vendors and follow component instructions."
        ]
    }
    
    return tips.get(noise_level, [])

def get_component_units():
    return {
        'Resistor': ['Ω', 'kΩ', 'MΩ'],
        'Capacitor': ['pF', 'nF', 'μF'],
        'Voltage Source': ['V', 'mV'],
        'Current Source': ['A', 'mA', 'μA']
    }

def main():
    st.title("Circuit Noise Predictor")
    
    # Sidebar for circuit parameters
    st.sidebar.header("Circuit Parameters")
    vdd = st.sidebar.number_input("VDD (Volts)", min_value=0.1, max_value=10.0, value=3.3, step=0.1)
    vth = st.sidebar.number_input("Threshold Voltage (Vth)", min_value=0.1, max_value=5.0, value=0.7, step=0.1)
    temperature = st.sidebar.number_input("Temperature (°C)", min_value=-50, max_value=200, value=25)
    load_capacitance = st.sidebar.number_input("Load Capacitance (pF)", min_value=1, max_value=1000, value=10)
    
    # Components section
    st.sidebar.header("Circuit Components")
    num_components = st.sidebar.number_input("Number of Components", min_value=0, max_value=10, value=0)
    
    components = []
    component_units = get_component_units()
    
    for i in range(num_components):
        col1, col2, col3 = st.sidebar.columns(3)
        with col1:
            component_type = st.selectbox(f"Component {i+1} Type", 
                list(component_units.keys()), 
                key=f'type_{i}')
        with col2:
            component_value = st.number_input(f"Value", min_value=0.0, key=f'value_{i}')
        with col3:
            component_unit = st.selectbox(f"Unit", 
                component_units[component_type], 
                key=f'unit_{i}')
        
        components.append({
            'type': component_type,
            'value': component_value,
            'unit': component_unit
        })
    
    # Predict Noise Button
    if st.sidebar.button("Check Noise"):
        try:
            noise_level = predict_noise(vdd, vth, load_capacitance, temperature)
            st.header(f"Noise Level: {noise_level}")
            
            # Display noise reduction tips
            tips = noise_reduction_tips(noise_level)
            
            if noise_level in ['Medium', 'High']:
                st.subheader("Noise Reduction Tips")
                for tip in tips:
                    st.markdown(f"- {tip}")
            
            # Circuit Details Visualization
            st.subheader("Circuit Details")
            details = {
                "VDD": f"{vdd} V",
                "Threshold Voltage": f"{vth} V",
                "Temperature": f"{temperature} °C",
                "Load Capacitance": f"{load_capacitance} pF"
            }
            
            for key, value in details.items():
                st.text(f"{key}: {value}")
            
            # Components Visualization
            if components:
                st.subheader("Circuit Components")
                for comp in components:
                    st.text(f"{comp['type']}: {comp['value']} {comp['unit']}")
        
        except Exception as e:
            st.error(f"Error predicting noise: {e}")

if __name__ == "__main__":
    main()
