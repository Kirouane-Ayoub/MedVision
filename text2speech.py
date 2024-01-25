from elevenlabs import set_api_key
set_api_key("API Key")  # past your API Key here
from elevenlabs import voices, generate
voices = voices()
def text2speech(text , voice_id) : 
    voice = voices[1] if voice_id == "Man" else voices[0]
    audio = generate(text=text, voice=voice)
    with open("output.mp3", "wb") as file:
        file.write(audio)
