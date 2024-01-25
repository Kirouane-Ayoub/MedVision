# MedVision

## Overview
Welcome to the Cutting-edge Vision Medical AI Assistant project! Our system utilizes the 'Gemini Vision' model from Google, bringing advanced capabilities to the analysis of medical images. While we acknowledge the complexities of healthcare, our AI assistant aims to provide enhanced support to healthcare professionals with its innovative features.

## Features

1. **Image Analysis:**
   - Analyze X-rays, MRI scans, CT scans, ultrasound images, and pathology slides using advanced algorithms and deep learning techniques.

2. **Disease Detection:**
   - Aid in diagnosing diseases by providing differential diagnoses and suggesting further tests based on thorough image analysis.

3. **Treatment Recommendation:**
   - Offer treatment recommendations, including medications, therapies, and surgical interventions, aligned with the diagnosis.

4. **Risk Assessment:**
   - Evaluate the risk of developing diseases or complications based on medical images, identifying high-risk patients and recommending preventive measures.

## Additional Features

- **Audio Output and Voice Options:**
   - Enjoy an audio output feature with both male and female voice options for a personalized user experience.

- **Language Selection:**
   - Choose from multiple languages (Arabic, English, French) to cater to diverse user preferences.


## Technologies Used

1. **Gemini Vision Model:**
   - We have incorporated the cutting-edge 'Gemini Vision' model from Google for advanced medical image analysis. Learn more about the model [here](https://blog.google/technology/ai/gemini-api-developers-cloud/).

2. **Text-to-Speech (TTS) Integration:**
   - The text-to-speech functionality is powered by the 'elevenlabs' API. To explore the capabilities of this API, visit [elevenlabs](https://elevenlabs.io/).

3. **User Interface Development:**
   - Our user interface is crafted using Streamlit, a powerful framework for creating interactive and intuitive applications. Explore Streamlit's features [here](https://streamlit.io/).


## Usage : 

```
pip install -r requirements.txt
```

Before launching the application, ensure to set your **Google Gemini Vision API key** in the **'utils.py'** file and your **Elevenlabs API key** in the **'text2speech.py'** file for seamless integration and optimal performance.

```
streamlit run app.py
```

![Screenshot from 2024-01-25 14-15-47](https://github.com/Kirouane-Ayoub/MedVision/assets/99510125/05f73a7d-df28-4549-ba76-ecec47018ea7)



