# Python-Voice-Assistant-Naina
This is Python Voice assistant with Tkinter GUI, It can take commands for news, online music streaming, take a photo, search wikipedia, open google, youtube.
It has Tkinter GUI and is completely hands free.
It use the following python libraries.
  1. Tkinter            -> Pre-installed.
  2. time               -> For Debugging Purpose (no other use)
  3. pyttsx3            -> For Text to speech (pip install pyttsx3)
  4. speech_recognition -> For audio to Text (pip install SpeechRecognition)
  5. wikipedia          -> For Searching Wikipedia (pip install wikipedia)
  6. webbrowser         -> For Opening Browser (Pre-installed)
  7. urllib             -> For URL Handling Module (Pre-installed)
  8. re                 -> For using Regular expressions for extracting useful links/data from html files
  9. cv2                -> For handling images (pip install opencv-python)
 
 # Instructions to use Naina
 1. Click on 'Invoke Naina' Button to begin on the Window.
 2. Give commands when the status bar at the bottom is 'GREEN' ands reads 'Listening..'
 3. Commands that Naina accepts are:
 # IMPORTANT: Incase of any ambiguity in commands then the command with higher Priority will be considered. Commands are given below in decreasing Priority
        a. 'Who are you' is in the command then it Introduces itself.
        b. 'Wikipedia' is in command then it searches for the remaining input on wikipedia
        c. 'Open Youtube' is in command then it opens Youtube in default Browser.
        d. 'Youtube' OR 'Play' is in command then it plays the first youtube search result after removing 'play' and 'youtube' from the command.
        e. 'Open Google' in Command then it opens Google in default browser.
        f. 'take a picture' or 'take a photo' in command then it takes a photo and displays it new window.
                  ---> To close the new window use 'thank you' or 'close' in your command.
        g. 'news' in command then Naina displays and speaks out the top five news from the www.timesnow.com/
        h. Any other command will give 'Sorry say again' as output.
