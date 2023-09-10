from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
import wolframalpha
import wikipedia
import datetime
import random
from selenium import webdriver
from time import sleep

client = wolframalpha.Client('<Client ID>')

import pyttsx3

def talkToMe(audio):
    "speaks audio passed as argument"
    print("Adam: " + audio)
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-us')
        print('Master ?: ' + query + '\n')
    except sr.UnknownValueError:
        talkToMe('Sorry Master, I did not get that! Try typing the command in this time!')
        query = str(input('Command: '))
    return query


def insta_cross_refrence_followers_with_following():
    from selenium import webdriver
    from time import sleep

    following_list = []
    followers_list = []
    handle = input()

    driver = webdriver.Chrome('<path to chrome driver on computer>')  # Replace with your Chrome driver path
    username = "<Account Username>"
    password = "<Password>"

    driver.get(f"https://www.instagram.com/{handle}/")
    talkToMe("opening Instagram")
    sleep(2)

    # Logging into the Instagram account
    # (You may need to update this part for Instagram's current login mechanism)
    driver.find_element_by_xpath('<XPath for the login button>').click()
    sleep(4)
    driver.find_element_by_xpath('<XPath for the username input>').send_keys(username)
    sleep(2)
    driver.find_element_by_xpath('<XPath for the password input>').send_keys(password)
    sleep(1)
    talkToMe("Login to my account successful")
    driver.find_element_by_xpath('<XPath for the login button>').click()
    sleep(3)

    # Counting and displaying the number of following
    count_following = driver.find_element_by_xpath('<XPath for following count element>')
    print(count_following.text)
    talkToMe("Following count is " + str(count_following) + " sir")
    driver.find_element_by_xpath("<XPath for the following link>").click()
    sleep(4)

    # Scrolling through the following list to collect data
    scroll_box = driver.find_element_by_xpath("<XPath for following list>")
    last_ht, ht = 0, 1
    for i in range(int(count_following.text) - 1):
        # Add sleep and scroll logic here if needed
        following = driver.find_element_by_xpath(f"<XPath for following item {i + 1}>")
        print(following.text)
        following_list.append(following.text)

    # Closing the following list
    driver.find_element_by_xpath("<XPath to close the following list>").click()
    sleep(1)

    # Counting and displaying the number of followers
    count_followers = driver.find_element_by_xpath('<XPath for followers count element>')
    sleep(2)
    driver.find_element_by_xpath("<XPath for the followers link>").click()
    sleep(2)

    # Scrolling through the followers list to collect data
    scroll_box2 = driver.find_element_by_xpath("<XPath for followers list>")
    for j in range(int(count_followers.text) - 1):
        # Add sleep and scroll logic here if needed
        f = driver.find_element_by_xpath(f"<XPath for followers item {j + 1}>")
        print(f.text)
        followers_list.append(f.text)

    talkToMe("cross-referencing followers to following")
    scum_bags = list(set(following_list) - set(followers_list))

    if scum_bags == []:
        print("everyone you follow follows you back")
        talkToMe("everyone seems to be following you back sir")
    else:
        print("some people")
        talkToMe("found people sir you might want to have a look")

    print(scum_bags)
    print(len(scum_bags))
    talkToMe("check complete Mr./Ms. ?")


def assistant(query):
    "if statements for executing commands"
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        m = "morning"
    elif currentH >= 12 and currentH < 18:
        m = "afternoon"
    else:
        m = "evening"

    if "hello" in query:
        name = ""
        talkToMe("Hello Master ? " + name + " it's always good to see you again on this fine " + m)
    elif "insatgram check" in query:  # Corrected the condition
        talkToMe("Enter handle please sir or friend")
        insta_cross_refrence_followers_with_following()
    elif "open my website" in query:
        talkToMe("opening your website and may I say sir it is a good-looking one")
        webbrowser.open('http://www.jasonkmoses.ga/index.php')
    # Add more commands here...
    else:
        query = query
        talkToMe('Searching...')
        try:
            try:
                res = client.query(query)
                results = next(res.results).text
                talkToMe('WOLFRAM-ALPHA says this about - ')
                talkToMe('I got it sir.')
                talkToMe(results)
            except:
                results = wikipedia.summary(query, sentences=2)
                talkToMe('Got it.')
                talkToMe('WIKIPEDIA says - ')
                talkToMe(results)
        except:
            webbrowser.open('www.google.com')


talkToMe("Checking if it is master ?")
talkToMe('Hello sir')
assistant(myCommand())
