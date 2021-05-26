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


## Tech

Dillinger uses a number of open source projects to work properly:

- [AngularJS] - HTML enhanced for web apps!
- [Ace Editor] - awesome web-based text editor
- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- [Twitter Bootstrap] - great UI boilerplate for modern web apps
- [node.js] - evented I/O for the backend
- [Express] - fast node.js network app framework [@tjholowaychuk]
- [Gulp] - the streaming build system
- [Breakdance](https://breakdance.github.io/breakdance/) - HTML
to Markdown converter
- [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
