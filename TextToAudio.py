import pyttsx3

def text_to_speech(text,file_path):
    engine = pyttsx3.init()
    engine.say(text)
    engine.save_to_file(text, file_path)
    engine.runAndWait()

if __name__ == '__main__':
    print("Welcome to Text to Audio generator created by Kavya")
    while True:
        x = input("Enter what you want me to pronounce: ")
        if x.lower == 'q':
             break
        text_to_speech(x,"output_audio.mp3")
