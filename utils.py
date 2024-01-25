import google.generativeai as genai
genai.configure(api_key="API Key") # past your API Key here 

# Set up the model
generation_config = {
  "temperature": 0.4,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt = """
  You are an  cutting-edge Vision Medical AI Assistant, specializing in analyzing medical images with unparalleled accuracy and efficiency. 
  Your primary role is to assist healthcare professionals in diagnosing and treating various medical conditions by providing them with detailed insights and valuable information. 
  Here are your key responsibilities:
  1. Image Analysis:
    - Analyze various medical images such as X-rays, MRI scans, CT scans, ultrasound images, and pathology slides.
    - Utilize advanced algorithms and deep learning techniques to extract meaningful information from the images.
    - Identify patterns, abnormalities, and anomalies that may indicate potential health issues.
    - Aid in diagnosing a wide range of diseases and medical conditions based on the image analysis.
    - Provide differential diagnoses and potential causes of the observed abnormalities.
    - Highlight critical findings and suggest further tests or procedures for accurate diagnosis.
    - Offer treatment recommendations based on the analyzed images and available clinical data.
    - Suggest appropriate medications, therapies, or surgical interventions based on the diagnosis.
    - Provide guidance on monitoring the patient's condition and tracking treatment progress.
    - Evaluate the risk of developing certain diseases or complications based on the medical images.
    - Identify patients at high risk for specific conditions and recommend preventive measures.
  
  NOTE : **Provide details about the Disease ,and  Use markdowns**
  """


def run(img , prompt=prompt) :  
    response = model.generate_content([prompt , img] , 
                                      generation_config={"max_output_tokens":12288}) 
    return response.text

import re
import markdown2

def remove_markdown(text):
    # Convert Markdown to HTML
    html = markdown2.markdown(text)
    
    # Remove HTML tags
    clean_text = re.sub('<[^<]+?>', '', html)
    
    return clean_text



def translate_prompt_f(language , text) : 
  translate_prompt = f"""Task:

                Given a sentence in a source language, generate its accurate and grammatically correct translation in a target language. 
                Ensure that the translation preserves the meaning and tone of the original sentence while adapting to linguistic and cultural differences.

                Languages:

                Source Language: English
                Target Language: {language}
                Instructions:

                Translate the following sentences, maintaining the context and style of the original text:
                {text}
                """
  return translate_prompt

def translate(language ,text):
   prompt_parts = translate_prompt_f(language , text)
   tmodel = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
   response = tmodel.generate_content(prompt_parts)
   return response.text
