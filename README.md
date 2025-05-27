# Noise Margin Detector

A powerful tool for predicting and analyzing noise margins in electronic circuits using machine learning. This application helps engineers and hobbyists quickly assess the noise characteristics of their circuit designs without extensive simulation.

## 🚀 Features

- **Noise Level Prediction**: Predicts noise levels (Low/Medium/High) based on circuit parameters
- **Interactive Interface**: User-friendly web interface built with Streamlit
- **Circuit Parameter Customization**:
  - Adjustable VDD (Supply Voltage)
  - Configurable Threshold Voltage (Vth)
  - Temperature settings
  - Load Capacitance adjustment
  - Custom component management
- **Noise Reduction Tips**: Provides actionable recommendations based on predicted noise levels
- **Machine Learning Model**: Powered by XGBoost for accurate noise margin classification

## 📊 Model Performance

The XGBoost model has been trained on a synthetic dataset with the following metrics:
- Accuracy: ~95%
- Precision: 94-96% (varies by class)
- Recall: 93-96% (varies by class)
- F1-Score: 93-96% (varies by class)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SplinterSword/Noise_Margin_Detector.git
   cd Noise_Margin_Detector
   ```

2. **Set up a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using Pipenv:
   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```

## 🚀 Usage

1. **Run the Streamlit application**
   ```bash
   streamlit run newapp.py
   ```

2. **Access the web interface**
   Open your browser and navigate to `http://localhost:8501`

3. **Configure circuit parameters**
   - Use the sidebar to adjust:
     - VDD (Supply Voltage)
     - Threshold Voltage (Vth)
     - Temperature
     - Load Capacitance
     - Add/configure circuit components

4. **Get noise prediction**
   - Click the "Check Noise" button to get the predicted noise level
   - View detailed noise reduction recommendations

## 📂 Project Structure

```
Noise_Margin_Detector/
├── DataGeneration.ipynb    # Jupyter notebook for generating synthetic dataset
├── Minor.ipynb            # Model training and evaluation notebook
├── Pipfile                # Pipenv dependencies
├── README.md              # This file
├── best_xgb_model.joblib  # Pre-trained XGBoost model
├── newapp.py              # Main Streamlit application
├── noise_margin_dataset.csv  # Sample dataset
└── requirements.txt       # Python dependencies
```

## 🤖 Model Details

The noise margin prediction is powered by an XGBoost classifier trained on synthetic data. The model takes the following inputs:

- **VDD (Volts)**: Supply voltage (1.0V - 3.3V)
- **Vth (Volts)**: Threshold voltage (0.4V - 1.2V)
- **Temperature (°C)**: Operating temperature (25°C - 125°C)
- **Load Capacitance (pF)**: Load capacitance (1pF - 1000pF)

The model outputs one of three noise level classifications:
- **Low**: Minimal noise, circuit is stable
- **Medium**: Moderate noise, consider optimizations
- **High**: Significant noise, design improvements recommended

## 📝 Noise Reduction Tips

Based on the predicted noise level, the application provides specific recommendations:

### For Medium Noise Levels:
- Use shielded cables to minimize electrostatic noise
- Implement twisted pair cables to eliminate normal mode noise
- Isolate signals to prevent ground loops
- Use differential measurements for better signal integrity

### For High Noise Levels:
- Ensure proper grounding of all components
- Strategically route wires to segregate high and low voltage lines
- Implement anti-aliasing filters
- Consider application-specific noise control measures

## 📈 Future Improvements

- [ ] Add support for more circuit components
- [ ] Implement real-time noise simulation
- [ ] Add visualization of noise margins
- [ ] Support for importing SPICE netlists
- [ ] Add more detailed component models
- [ ] Implement user authentication for saving designs

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📧 Contact

Project Link: [https://github.com/SplinterSword/Noise_Margin_Detector](https://github.com/SplinterSword/Noise_Margin_Detector)
