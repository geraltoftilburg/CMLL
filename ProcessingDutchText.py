import os
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

nltk.download('punkt')
nltk.download('stopwords')

dutch_stop_words = set(stopwords.words('dutch'))
dutch_stemmer = SnowballStemmer("dutch")

#Clean lines of text 
def clean_text(text):
    #Remoev speaker information 
    text = re.sub(r'\*\w+:', '', text).strip()
    #Remove annotations enclosed in <> or [], these seem to be unspoken words or gibberish
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'<.*?>', '', text)
    #Remove special characters
    text = re.sub(r'[+*:@%_]', '', text)
    #Remove anything else that is not letters
    text = re.sub(r"[^a-z' ]", '', text, flags=re.I)
    return text.strip()

#Function to tokenize, remove common stop words, and do stemming
def process_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token not in dutch_stop_words and token.isalpha()]
    tokens = [dutch_stemmer.stem(token) for token in tokens]
    return tokens

#Function to read files
def read_cha_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.readlines()
    return content

#Function to extract lines aka narratives from the file
def extract_and_process_narratives(content):
    narratives = [line for line in content if line.startswith('*CHI:')]
    cleaned_narratives = [clean_text(narrative) for narrative in narratives]
    processed_narratives = [process_text(narrative) for narrative in cleaned_narratives]
    return processed_narratives

#Function to process directories and files
def process_directory(input_dir, output_dir):
    #Walk through the input directory
    for root, dirs, files in os.walk(input_dir):
        #Process each directory
        for dirname in dirs:
            #Create a corresponding directory in the output structure with '_processed' appended
            output_subdir = os.path.join(root.replace(input_dir, output_dir), dirname + '_processed')
            os.makedirs(output_subdir, exist_ok=True)
        
        #Process each file
        for file in files:
            if file.endswith('.cha'):
                #Construct full file paths
                input_file_path = os.path.join(root, file)
                #Create new filename with '_processed' appended before the extension
                new_filename = os.path.splitext(file)[0] + '_processed' + os.path.splitext(file)[1]
                output_file_path = os.path.join(root.replace(input_dir, output_dir) + '_processed', new_filename)
                
                #Process the .cha file
                content = read_cha_file(input_file_path)
                processed_narratives = extract_and_process_narratives(content)
                
                #Write the processed content to the new file with '_processed' in the filename
                with open(output_file_path, 'w', encoding='utf-8') as f_out:
                    for narrative in processed_narratives:
                        f_out.write(' '.join(narrative) + '\n')


def main():
    #Set the input and output directories (CHANGE TO WHEREVER YOUR FILES ARE)
    input_dir = "C:/Users/dogaa/Desktop/DutchTurkish-AarssenBos"
    output_dir = "C:/Users/dogaa/Desktop/Processed DutchTurkish-AarssenBos"

    #Make sure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    #Start processing the directory
    process_directory(input_dir, output_dir)

if __name__ == "__main__":
    main()


