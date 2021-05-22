# cleaner.py - Launches a cleaner version of the article
# That you are trying to read on localHost server.  
from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser, sys, pyperclip, bs4, requests, os
from pathlib import Path
import time

if len(sys.argv) > 1:
# Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
# Get address from clipboard.
    address = pyperclip.paste()

address = requests.get(address)

address.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(address.text, 'html.parser')
elems = noStarchSoup.select('h1, p' )
if os.path.isfile('cleaned.html'):
    os.remove('cleaned.html')

p = Path('cleaned.html')
cleaned = open("cleaned.html", "w", encoding='utf-8')
cleaned.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Cleaned Article</title>
    <link rel="shortcut icon" href="https://cdn2.iconfinder.com/data/icons/inficons-set-6/1000/thumbs-up-512.png" type="image/x-icon">
    <style>
        body::-webkit-scrollbar {
            width: 5px;
        }
        
        body::-webkit-scrollbar-track {
            box-shadow: inset 0 0 6px #0F0F13;
        }
        
        body::-webkit-scrollbar-thumb {
            background-color: white;
            outline: 1px solid white;
        }
        body{
            background-color: #0F0F13;
            color: aliceblue !important;
            margin: 100px 85px 100px 85px;
            font-family: sans-serif;
            display: flex;
            flex-direction: column;
        }
        a{
            pointer-events: none;
            cursor: default;
            text-decoration: none;
            color: aliceblue;
        }
        h1{
            font-size: 100px;
            font-weight: 1000;
            text-align: center;
        }
        img{
            width: 100%;
            align-self: center;
        }
        p{
            font-size: 30px;
            font-weight: 200;
            line-height: 50px;
            text-align: justify;
        }
        h2{
            font-size: 70px;
            font-weight: 1000;
            text-align: center;
        }
        h3{
            font-size: 60px;
            font-weight: 1000;
            text-align: center;
        }
        h4{
            font-size: 50px;
            font-weight: 1000;
            text-align: center;
        }
        h5{
            font-size: 40px;
            font-weight: 1000;
            text-align: center;
        }
        h6{
            font-size: 36px;
            font-weight: 1000;
            text-align: center;
        }
    </style>  
</head>
<body>""")
article = str(elems)
cleaned.write(article)
cleaned.write('</body></html>')
cleaned.close()

filename = 'file:///'+os.getcwd()+'/' + 'cleaned.html'
webbrowser.open(filename)