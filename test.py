from googletrans import Translator

def batch_translate(texts):
    translator = Translator()
    return [translator.translate(text, src='auto', dest='en').text for text in texts]

text = "நீங்கள் எந்த வகையான தமிழ் உரை வேண்டும் என்பதை கூறுங்கள். எடுத்துக்காட்டாக, கவிதை, கட்டுரை, கதையாடல், அல்லது ஒரு குறிப்பிட்ட தலைப்புக்கான விவரணையா"
# Wrap the single string in a list
trans = batch_translate([text])
print(trans[0])  # Access the first (and only) translated text
