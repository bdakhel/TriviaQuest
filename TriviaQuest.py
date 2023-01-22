import openai
from pypdf import PdfReader
import re
import time
import sys

# Put text of each page into a dictionary with the key as the page number
def textify(pdfName):
    reader = PdfReader('raheeq.pdf')

    book = dict()
    pageNum = 0
    for i in range(len(reader.pages)):
        pageNum += 1  
        text = reader.pages[i].extract_text()
        text = text.replace('\n',' ')
        # text = text.replace('MSA NIU   ','')
        text = re.sub(r'\[.*?\]','', text)
        book[str(pageNum)] = text[3:]
        
    return book

# Clean up a text file of questions and answers
def clean_up():
    file1 = open('qanda.txt','r')
    lines = file1.readlines()
    file1.close()
    print(lines)

    count = 0
    for i, line in enumerate(lines):
        if lines[i].startswith('Q'):
            count += 1
            lines[i] = 'Question ' + str(count) + '. ' + line[3:].strip() + '\n'
            continue
        elif lines[i].startswith('A'):
            if lines[i].startswith('Answer'):
                lines[i] = 'Answer ' + str(count) + '. ' + line[7:].strip() + '\n\n'
                continue
            lines[i] = 'Answer ' + str(count) + '. ' + line[3:].strip() + '\n\n'
            continue
        elif lines[i].startswith('Page'):
            lines[i] = '\n' + lines[i] + '\n'
            continue
        elif lines[i].startswith('\n'):
            lines[i] = ''
            continue
        lines[i] = ''
    print(count)
    file1 = open('clean.txt', 'w')
    file1.writelines(lines)
    file1.close()

# Collect name of book in pdf
pdfName = sys.argv[1]

# Collect key of openai account
key = sys.argv[2]

# Collect text of pdf
book = textify(pdfName)

openai.api_key = key
openai.Model.list()


with open('qanda.txt', 'w') as f:

    for i in range(len(book)):
        # Create prompt
        prompt = "Make 5 questions and answers from this text" + book[str(i+1)]

        # Check time so that API limit is not breached
        start = time.process_time()
        
        # Ask AI prompt
        response = openai.Completion.create(
            model = 'text-davinci-003',
            prompt = prompt,
            temperature = 0.9,
            max_tokens = 2000
        )

        # Write response in text file with page number
        f.write('Page ' + str(i+1))
        f.write(response['choices'][0]['text'])
        f.write('\n \n')

        # Find time passed
        duration = time.process_time() - start
        # Make sure questions arent asked more than once every 3 seconds
        if duration < 3:
            time.sleep(3.01 - duration)
        print("Page ", str(i+1), " complete!")

# Clean up and organize AI response
clean_up()