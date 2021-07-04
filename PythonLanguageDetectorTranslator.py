# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO DETECT THE LANGUAGE OF USER-INPUT TEXT AND ALSO TRANSLATE USER-ENTERED TEXT TO
# ANY LANGUAGE SELECTED FROM THE LIST USING googletrans LIBRARY.
#
# Googletrans is a free and unlimited python library that implemented Google Translate API.
# It uses the Google Translate Ajax API to detect langauges and translate text.
#
# The module can be installed using the command - pip install googletrans

# Importing necessary packages
import tkinter as tk
from tkinter import *
import googletrans
from googletrans import Translator

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    languagesListLabel = Label(root, text="SELECT A LANGUAGE FROM THE LIST", bg="darkslategrey")
    languagesListLabel.grid(row=0, column=3, padx=5, pady=5)

    root.languagesListBox = Listbox(root, width=30, height=15, bg='snow3')
    root.languagesListBox.grid(row=1, column=3, rowspan=6, columnspan=3, padx=5, pady=2)

    # Displaying the languages in the ListBox
    for c in languagesList:
        root.languagesListBox.insert(END, (c + '-' + languagesList[c]))
    # Binding onLanguagSelect() event to the ListBox Widget
    root.languagesListBox.bind('<<ListboxSelect>>', onLanguageSelect)

    inputTextLabel = Label(root, text="TEXT TO DETECT : ", bg="darkslategrey")
    inputTextLabel.grid(row=0, column=0, padx=10, pady=5)
    inputTextEntry = Entry(root, width=20, bg='snow3', textvariable=textToDetect)
    inputTextEntry.grid(row=0, column=1, padx=10, pady=5)

    findButton = Button(root, text="DETECT & TRANSLATE", command=detecttranslateLanguage)
    findButton.grid(row=1, column=1, padx=5, pady=5, columnspan=2)

    detectedLanguageLabel = Label(root, text="DETECTED LANGUAGE : ", bg="darkslategrey")
    detectedLanguageLabel.grid(row=2, column=0, padx=10, pady=5)
    root.detectedLanguage = Label(root, width=20, bg='snow3')
    root.detectedLanguage.grid(row=2, column=1, padx=10, pady=5)

    translatedLabel = Label(root, text="TRANSLATED TEXT : ", bg="darkslategrey")
    translatedLabel.grid(row=3, column=0, padx=10, pady=5)
    root.translated = Label(root, width=20, bg='snow3')
    root.translated.grid(row=3, column=1, padx=10, pady=5)

    i_tranlateTextLabel = Label(root, text="TEXT TO TRANSLATE : ", bg="darkslategrey")
    i_tranlateTextLabel.grid(row=4, column=0, padx=10, pady=5)
    root.i_tranlateTextEntry = Entry(root, width=20, bg='snow3', textvariable=textToTranlate)
    root.i_tranlateTextEntry.grid(row=4, column=1, padx=10, pady=5)

    languageLabel = Label(root, text="SELECTED LANGUAGE : ", bg="darkslategrey")
    languageLabel.grid(row=5, column=0, padx=10, pady=5)
    root.languageEntry = Label(root, width=20, bg='snow3')
    root.languageEntry.grid(row=5, column=1, padx=10, pady=5)

    translateButton = Button(root, text="TRANSLATE TEXT", command=translateText)
    translateButton.grid(row=6, column=1, padx=5, pady=5, columnspan=2)

    translatedTextLabel = Label(root, text="TRANSLATED TEXT : ", bg="darkslategrey")
    translatedTextLabel.grid(row=7, column=0, padx=10, pady=5)
    root.translatedText = Label(root, width=20, bg='snow3')
    root.translatedText.grid(row=7, column=1, padx=10, pady=5)

# Defining onLanguageSelect() function for ListBox selection detection
def onLanguageSelect(evt):
    language = root.languagesListBox.get(root.languagesListBox.curselection())
    root.languageEntry.config(text=language)

# Defining detecttranslateLanguage() function to detect the language of the entered text
def detecttranslateLanguage():
    # Storing the input text to detect language
    inpuTextToDetect = textToDetect.get()
    # Detecting the language  of the entered text using the detect() method which returns the
    # detected language in the form of shorthand notation
    detectedLanguage = tranlator.detect(inpuTextToDetect)
    detectedLanguage = detectedLanguage.lang
    # Using the returned shorthand notation fetching the language from the languagesList and
    # displaying it tkinter window
    detectedLanguage = languagesList[detectedLanguage]
    root.detectedLanguage.config(text=detectedLanguage)
    # Translating the entered text to the ENGLISH language using the translate() which
    # takes input text and shorthand notation of the language as arguments.
    # Language to which text to be translated is stored in the dest attribute
    translatedText = tranlator.translate(inpuTextToDetect, dest='en')
    # Showing the translated text in the tkinter window
    root.translated.config(text=translatedText.text)

# Defining translateText() function to tranlated the entered text to selected language
def translateText():
    # Storing the user-input text to be translated in inputTexToTranslated variable
    inputTextToTranslate = textToTranlate.get()
    # Storing the selected language from the ListBox in language variable
    language = root.languageEntry['text']
    # Splitting the language on '-' and fetching the first item from the resulting list
    # which corresponds to the SHORTHAND NOTATION OF THE LANGUAGE and storing it
    shorthand_notation = language.split('-')[0]
    # Translating the entered text to the selected language using the translate() which
    # takes input text and shorthand notation of the language as arguments.
    # Language to which text to be translated is stored in the dest attribute
    translatedText = tranlator.translate(inputTextToTranslate, dest=shorthand_notation)
    # Showing the translated text in the tkinter window
    root.translatedText.config(text=translatedText.text)

# Creating object of tk class
root = tk.Tk()
# Setting the title, background color, windowsize & disabling the resizing property
root.title("PythonLanguageDetectorTranslator")
root.config(background="darkslategrey")
root.geometry("690x350")
root.resizable(False, False)

# Creating the tkinter variables
textToDetect = StringVar()
textToTranlate = StringVar()
# Fetching the languages supported by googletrans using LANGUAGES which returns dictionary
# of supported languages and storing it the languagesList variable
languagesList = googletrans.LANGUAGES

# Creating an object of the Translator class
tranlator = Translator()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
