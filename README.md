# Refactored

# Used to be named Climate change vs wildlife migration analyser aka CCVWMA
Disclaimer: We used ChatGPT to get a website that can give us a CSV file to use as a dataset. Link to the chat: https://chatgpt.com/share/67daa732-cddc-8008-aeb0-2ef1f1b9e9a1

Prerequisites:

Streamlit and Python properly installed to your computer

How to install Python: https://wiki.python.org/moin/BeginnersGuide/Download

Download link for Python: https://www.python.org/downloads/

How to install Streamlit: https://docs.streamlit.io/get-started/installation/command-line

[Detailed instructions on how to install Streamlit:

Install python normally first


Since VS Code terminal uses CMD prompt from the OS itself (Assuming Windows), do "pip install streamlit" on CMD prompt- NOT python

How to open CMD prompt: press the search button on Windows, then type in CMD and press open to open command prompt.

Then, as matplotlib and seaborn are dependencies, do pip install matplotlib and pip install seaborn on a separate CMD window.]


Code editor (VS Code highly recommended)
Download VS Code: https://code.visualstudio.com/Download


1. Download refactored.py and species-filter-results.csv under releases

1b. Note: After that, make sure to do cd (Path of folder where you keep both the refactored.py file and the .csv file)> In this case, I will keep it in the Desktop folder for simplicity's sake. 
Hence, I will do cd desktop in this case.
Also make sure to put both files in the same folder.


2. Open refactored.py using VS Code and press Ctrl+Shift+` to open the terminal. Make sure to trust the file (if there is a pop up) so that everything runs smoothly.

2b. Note: When VS Code opens, do NOT press run!

3. Type in "cd Desktop" in the VS Code terminal and press enter.

3b. NOTE: VERY IMPORTANT but complex stuff!!! Please look at 1b before typing in cd Desktop!!! If you want to keep the refactored.py folder in another folder, do cd "YOUR PATH HERE" instead, with your path here being the path to the refactored.py folder. For example, if I want to keep the python folder in a folder named "hackathonproject" on my Desktop, put the refactored.py folder in it, then right click on the hackathon folder and press copy as path if you are on Windows 11. Then, type in cd and paste the path down. In this EXAMPLE given, it will be cd "C:\Users\Aaron\Desktop\hackathonproject\" and MAKE SURE TO DELETE THE QUOTES!!!! However, it is easiest to just leave the file in the Desktop instead as you only need to type cd Desktop. )
   
4. Type in "python -m streamlit run refactored.py" in the same terminal and press enter.
   
   
5. Congratulations! A tab should open on your default browser which will display our Streamlit app to display our project. :)
