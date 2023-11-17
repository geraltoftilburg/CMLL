# Install Packages
Run this code in your terminal to install all requiroed packages:
pip install -r requirements.txt 

# Pre-Processsing transcripts for LSA 

This script processes .cha files containing child language data to prepare for Latent Semantic Analysis (LSA). It specifically extracts narratives spoken by children (marked by *CHI: in the .cha files), cleans, tokenizes, removes stopwords, stems the words, and then outputs the processed text to a new directory structure.

**Prerequisites**
Before running the script, ensure that you have Python installed on your system. 

Additionally, the Natural Language Toolkit (NLTK) library is used for text processing. If you haven't already installed NLTK and its data, the script will attempt to do so.

**Directory Structure**
You will need two directories

A directory containing the original .cha files.
An empty directory where the processed files will be saved.
The script will replicate the original directory hierarchy in the output directory, appending _processed to each directory and file name.

**How to Use**
Clone/Download the Script: Obtain the script files and place them in a directory of your choice.

**Set Up the Directories**

Identify or create a directory that contains your .cha files. This will be your input directory.
Create an empty directory for the output. This will be where the processed files are saved.
Configure the Script:

Open script_name.py (replace with the actual name of your script file).
Locate the main function at the bottom of the script.
Change the input_dir variable to the path of your directory with the .cha files.
Change the output_dir variable to the path of your empty directory for processed files.

**Run the Script**
Execute the script from your command line or Python environment. Ensure that your current working directory in the command line is the same as where your script is located. 

**Output**
The script will create a new hierarchy in the output directory, with each subfolder and file name having _processed appended. Only the narratives spoken by children will be present in these files, prepared for LSA.

**Notes**
Be sure to back up your original .cha files before running the script.
It is recommended to test the script on a small subset of your data to ensure it works as expected.