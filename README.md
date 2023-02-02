# TriviaQuest
A python program that creates questions and answers with references from a book. This program extracts text from a given PDF file and generates 5 questions and answers for each page using OpenAI's text-davinci-003 language model API. The generated questions and answers are saved in a text file called "qanda.txt". The script also includes a clean-up function to format and organize the text file for easier readability.

# Requirements
- OpenAI API key
To generate an OpenAI API key, you will need to sign up for an OpenAI account. Once you have created an account, follow these steps to generate an API key:
1. Create an OpenAI account
2. Go to the API section of the OpenAI Dashboard.
3. Click on your profile and click "View API Keys"
4. "Create Secret Key" button
- PyPDF library (pip install PyPDF2)
- OpenAI python library (pip install openai)
# Usage
-Clone the repository by running ```git clone https://github.com/bdakhel/TriviaQuest.git``` in the terminal.
-Navigate to the directory where the script is saved using ```cd TriviaQuest```
-Run the script by providing the path to the PDF file as the first argument and your OpenAI API key as the second argument. For example: 
```python TriviaQuest.py ~/path/to/pdf key.```
-The generated questions and answers will be saved in a text file called "qanda.txt".
# Note
To avoid breaching the API limit, the script waits 3 seconds between making API requests. This means that for large PDF's it the program will run for approximatly 3 seconds per page. This may cause long run times.



