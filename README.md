# Automating-With-Python
## _Demonstating Automation By Python

[![UnsolicitedSite]](https://unsolicitedsite.co.in)

[![Article]](https://travis-ci.org/joemccann/dillinger)

This is a repo containing some very simple automation programs made in python by me. They could help you with your daily work or you could just try them for fun.
The instructions on how to use any of these programs is mentioned in this README file.



## Article Page Cleaner

- Looks for the URL in your clipboard or the URL you pasted
- Uses BeautifulSoup V4 to parse your provided HTML file
- Makes a new HTML file by the name 'cleaned.HTML' (Included in the folder)
- Opens the recently created HTML using the WebBrowser Library provided by Python

### Installation
Installation is easy. You need some requirements before working with 'cleaner.py'. To install the requirements, just run the 'requirements.txt' file provided in the folder.

Open a command line IN the folder where you have downloaded the provided folder in the repository and type this command in the command line.

``` 
pip install -r requirements.txt
```

Once the requirements are installed. You can easily use the program. Open a command line IN the folder where you've downloaded the provided folder in the git repository. 

#### There are 2 ways you can use this program:
- Copy the URL containing the article you want to clean. 
- OR
- Just type the URL after the file name while executing the program.

    #### First method
    Find a website containing the article you want to clean. Select the URL and copy it. DONE.
    Now go to the command line which is opened in the same folder which contains the 'cleaner.py' and run this command.
    ```
    python3 cleaner.py
    ```
     The cleaned version of the article you want to read must open.

    #### Second Method
    Just type in the URL of the article you want ot clean with the name of the python file like this:
    ```
    python3 cleaner.py https://www.TheArticleIWantCleaned.com
    ```
> Note: `Make sure you enter or copy the correct  URL address with a 'https://'. Otherwise, an error would be displayed. Just re-run the program with the correct URL again, on occasions of an error.`
