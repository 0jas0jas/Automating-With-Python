# Automating-With-Python
## _Demonstating Automation By Python

[![UnsolicitedSite]](https://unsolicitedsite.co.in)

[![Article]](https://unsolicitedsite.co.in/blogpage/posts/post5/post.html)

This is a repo containing some very simple automation programs made in python by me. They could help you with your daily work or you could just try them for fun.
The instructions on how to use any of these programs is mentioned in this README file.



## Article Page Cleaner

- Looks for the URL in your clipboard or the URL you pasted
- Uses BeautifulSoup V4 to parse your provided HTML file
- Makes a new HTML file by the name 'cleaned.HTML' (Included in the folder)
- Opens the recently created HTML using the Browser Library provided by Python

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

## Simple File Organiser

- checks for files in the working directory
- Sorts them according to either their size or their date modified
- Organises all files in neat folders labelled with their size
- Sorts files according to their date modified in the current working directory

### Installation
Installation is easy. Nothing needs to be installed. I mean the OS library should be there but you already have that, don't you? DON'T YOU!?

#### USAGE
- Keep the `organise.py` file in the directory (folder) containing the files you want to organise.

    #### Running the script
    Open your preferred terminal in the directory you want to organise and type:
    ```
    python3 organise.py
    ```
    
    Choose from the two options to get your files organised.
    
### ACTUAL USAGE
> This was a very simple example of how python can be used to manupulate directories and files. Edit/Add/Remove to the file to make if work FOR YOU. For your needs, add more sizes or add some new type of sort. The program is just a template, the usage is created by you, the user.

## Mee6 XP miner

- imports pyautogui
- chooses a random time in seconds to wait beween 20 and 60 seconds
- types 'hello' automatically
- presses enter
- repeats

### Installation
Installation is easy. You need some requirements before working with 'miner.py'. To install the requirements, just run the 'requirements.txt' file provided in the folder.

Open a command line IN the folder where you have downloaded the provided folder in the repository and type this command in the command line.

``` 
pip install -r requirements.txt
```

Once the requirements are installed. You can easily use the program. Open a command line IN the folder where you've downloaded the provided folder in the git repository. 

#### USAGE

 #### Running the script

 Open your preferred terminal in the directory you want to organise and type:
 ```
 python3 miner.py
 ```
    
 A random time will be chosen and displayed in the terminal. Everytime the timer ends, `hello` will be typed and enter will be pressed.
    
### ACTUAL USAGE
> Leave this open overnight and you'll be rich in XPs. Get to the top of the scoreboard. But but but this is also to demonstrate how you can use python to use your keyboard. I mean why actually type `hello` when you can type 17 lines to type `hello`.

## GMAIL EMAIL SENDER

- asks you to sign in to google
- asks you enter some details about the email
- sends it.

### Installation
Installation is easy. You need some requirements before working with 'mail.py'. To install the requirements, just run the 'requirements.txt' file provided in the folder.

Open a command line IN the folder where you have downloaded the provided folder in the repository and type this command in the command line.

``` 
pip install -r requirements.txt
```

Once the requirements are installed. You will have to log in to your google (gmail)account. Open a command line IN the folder where you've downloaded the provided folder in the git repository and type:

```
python3 quickstart.py
```

### USAGE

### Running the script
Open your preferred terminal in the directory you want to organise and type:
```
python3 mail.py
```
    
Type in the details of the email you're planning to send and send it. It's that simple.
    
### ACTUAL USAGE
> As you can judge from the code, this program is too simple and it is supposed to be simple. It's just a template for whatever you want to do with it. You can automate your emails and send beautiful HTML emails. The documentation of EZGmail explains the power of this module: https://pypi.org/project/EZGmail/


## License

MIT

**Free Software, Hell Yeah!**
