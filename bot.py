import spacy
import speech_recognition as sr

# Load the small English model
nlp = spacy.load("en_core_web_sm")

# Regular expression patterns for matching entities
patterns = {"MONEY": [{"LOWER": {"IN": ["rupees", "rs", "inr"]}}, {"IS_DIGIT": True}],
            "REASON": [{"LOWER": {"IN": ["at", "for", "in"]}}, {"POS": {"NOT_IN": ["DET", "PRON"]}, "OP": "*"}],
            "PRIORITY": [{"LOWER": {"IN": ["important", "urgent", "necessary"]}}]}

# convert the 'MONEY' pattern to use integer indices
patterns["MONEY"] = [{"LOWER": {"IN": ["rupees", "rs", "inr"]}}, {"IS_DIGIT": True}]

# Merge the patterns with the NER pipeline of the small English model
ruler = nlp.add_pipe("entity_ruler")
ruler.add_patterns(patterns)

# Function to transcribe speech to text using SpeechRecognition
def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except Exception as e:
        print("Sorry, could not recognize your speech.")
        return None

# Process each text and extract entities
while True:
    # Ask user to speak or type text input
    user_input = input("Press 'T' to type or 'S' to speak your input: ")
    if user_input.lower() == "t":
        text = input("Please enter your text input: ")
    elif user_input.lower() == "s":
        text = transcribe_speech()
        if text is None:
            continue
    else:
        print("Invalid input. Please try again.")
        continue
    
    doc = nlp(text)
    entities = [(ent.label_, ent.text) for ent in doc.ents if ent is not None]
    
    # Check if all entities are present
    money = next((ent[1] for ent in entities if ent[0] == "MONEY"), None)
    reason = next((ent for label, ent in entities if label == "REASON"), None)
    priority = next((ent for label, ent in entities if label == "PRIORITY"), None)
    
    if money is None:
        money = input("Please enter the amount of money spent: ")
    if reason is None:
        reason = input("Please enter the reason for expenditure: ")
    if priority is None:
        priority = input("Please enter the priority level (urgent, important, necessary): ")
    
    print(f"Spent {money} for {reason}, it was {priority}")
    
    # Ask user if they want to continue
    continue_input = input("Press 'C' to continue or any other key to exit: ")
    if continue_input.lower() != "c":
        break
