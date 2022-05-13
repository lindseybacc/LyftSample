'''
    @author Lindsey B
    @file name LyftSample.py
    @date May 12, 2022
    @note This program will accept a POST request containing 
    1 argument in URL and return a new string printing 
    every 3rd letter of the original string.
'''
import requests
import json
from flask import Flask

'''  ----------------------------------------------------------------
    @function getThird
    This function will take a string and create a new string 
    that contains every 3rd character of original string.
    @param sentence         - this parameter passes a string to edit
    @return                 - this function will return a new string
------------------------------------------------------------------ '''
def getThird(sentence):
    
    list(sentence)          # turning string into list
    newSentence = ''        # string to hold new edited string

    # using index letter to get each 3rd character
    for letter in range(2, len(sentence), 3):
        newSentence = newSentence + sentence[letter]

    return newSentence


'''  ----------------------------------------------------------------
    @function Main excecutions
------------------------------------------------------------------ '''
def main():
    # initializing local web app
    app = Flask(__name__)

    @app.route("/")
    @app.route("/home")
    def home(): # instructions to navigate to /test route
        return "Go to /test, follow usage: 'test/<string_to_cut>'"
    
    # route with post parameter instruction
    @app.route("/test/<string:string_to_cut>")
    def test(string_to_cut):

        # local URL to test 
        url = 'http://127.0.0.1:8000'
        # dictionary with key and value taken from parameter
        sample_arg = {
            "string_to_cut" : str(string_to_cut)
            } 
        # url & data to edit   
        response = requests.get(url, data=sample_arg)
    
        # calling function to make a new string with every 3rd letter
        new_string = getThird(sample_arg["string_to_cut"])
        
        # python dictionary to create an object (later used by JSON)
        string_dict = {
            "return_string": new_string
        }
        
        # returning edited string as JSON object
        jsonReturn = json.dumps(string_dict)

        # printing json object
        print(jsonReturn)

        return jsonReturn

    # local site to test parameters
    if __name__ == '__main__':
        app.run(debug=True, port=8000)

# running program
main()
