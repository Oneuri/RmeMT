from win32com.client import Dispatch


def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)


if __name__ == '__main__':
    speak("hmm")
    speak("Hey Urjit.")
    speak("How are you?")
    speak("Here is the speech for you")
    speak("Please listen carefully!")
    with open('yes.txt') as f:
        for text in f.readlines():
            speak(text)
            print(text)
    '''
    url = "http://textfiles.com/adventure/aencounter.txt"
    file = urllib.request.urlopen(url)

    for line in file:
    	decoded_line = line.decode("utf-8")
        speak(decoded_line)
	print(decoded_line)
    '''
