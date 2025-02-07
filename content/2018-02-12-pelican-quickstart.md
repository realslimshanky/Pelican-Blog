Title: What Pelican quickstart actually do and how it does that?
Date: 2018-02-12
Modified: 2018-02-13
Category: Python
Tags: Python, Pelican, Quickstart, Tutorial
Slug: what-pelican-quickstart-actually-do-and-how-it-does-that
Authors: Shashank Kumar
Summary: In this blog, I'll go through the process after running the command `pelican-quickstart` without any arguments inside a [virtual environment](https://docs.python.org/3/tutorial/venv.html) to see what goes down in the background. Later in the blog, I'll figure out how everything works.
Cover: images/DDEOIFYV0AAB3Wx.jpeg

I chose to use [Pelican](https://github.com/getpelican/pelican) to build my personal blog out of my love for Python. It took me two days to go through the tutorials given by Official Pelican [documentation](https://docs.getpelican.com/en/stable) and setup [Shanky's Brainchild](https://blog.shanky.xyz) with the help of the [Flex](https://github.com/alexandrevicenzi/flex) theme created by [Alexandre Vicenzi](https://alexandrevicenzi.com). Pelican contributors have made sure you have a quick and easy beginning in order to get down to business asap and evolve as per your needs. For this very purpose, we use `pelican-quickstart`.

In this blog, I'll go through the process after running the command `pelican-quickstart` without any arguments inside a [virtual environment](https://docs.python.org/3/tutorial/venv.html) to see what goes down in the background. Later in the blog, I'll figure out how everything works. You can also move directly to **Demystifying pelican-quickstart**.

#### Prerequisites and Warm-Up

Before we start, make sure to have a virtual environment setup, use either venv or pipenv. Install the protagonist package [`pelican`](https://pypi.python.org/pypi/pelican). Optionally, if one is familiar with [Markdown](https://daringfireball.net/projects/markdown) like me and want to create website/blog using it, install [`Markdown`](https://pypi.python.org/pypi/Markdown) package.

* * *

#### Running `pelican-quickstart`

After setting up the virtual environment and activated it, creating a new folder for our website say `justanotherblog`, running `pelican-quickstart` from inside the folder, a few questions will be asked by Pelican. As a result of answering all of the successfully, following directory structure can be seen which is in turn created by `pelican-quickstart`.

    justanotherblog/
                    content/
                    output/
                    develop_server.sh
                    fabfile.py
                    Makefile
                    pelicanconf.py
                    publishconf.py


Let's look into the question that were asked and how they affect our blog.

###### Where do you want to create your new web site? [.]

Here, it is asked about the location of the website. The default value is `.` or the location from where the `pelican-quickstart` has been called and is denoted by `[.]`. If one does not want to change the location can simply enter without inputting anything. You can also specify a location like `/home/username/justanotherblog`.

**Resultant** - Location specified here will be the parent location for all the Pelican files.

###### What will be the title of this web site?

When this question is asked, title of the website should be provided. Failure in doing so or just hitting enter here would immediately prompt `You must enter something` and the question will be asked again.

**Resultant** - Title specified here will be store inside `pelicanconf.py` as `SITENAME = 'Just Another Blog'`.

###### Who will be the author of this web site? 

When this question is asked, author name should be provided. And just like before, failure in doing so or just hitting enter here would immediately prompt `You must enter something` and the question will be asked again.

**Resultant** - Name specified here will be saved inside `pelicanconf.py` as `AUTHOR = 'Shashank Kumar'`

###### What will be the default language of this web site? [en]

Whichever language you would like to use to write the content of your blog should be stated here. Language should be in form of 2 letters code and failure in doing so will prompt `You must enter a 2 letters long string` with the question asked again. You can look up 2 letter code for languages in this [ISO 639.1](https://www.loc.gov/standards/iso639-2/php/code_list.php) guide. Default language is English - en as denoted by `[en]`.

**Resultant** - The choosen language will be stored inside `pelicanconf.py` as `DEFAULT_LANG = 'en'`.

###### Do you want to specify a URL prefix? e.g., http://example.com   (Y/n)

Here, you have to state whether or not you want to use a URL prefix or simply host your blog. The default value is `Y` (y or Yes) or one can also choose `n` (N or No). Failure in doing to will prompt `You must answer 'yes' or 'no'` and the question will be asked again.

**Resultant** - If chosen `Y`, a subsequent question will be asked to state the URL. If chosen `n`, `SITEURL = ''` will be saved inside `pelicanconf.py` which can be changed later.

###### What is your URL prefix? (see above example; no trailing slash)

If the previous question was answered with a `Y`, this question will be asked. Now is the time to state the URL you are planning to host the blog. Although we cannot enter while providing a URL by simply entering (`You must enter something` will be prompted while doing os), there's no failure to this step as the URL is not validated.

**Resultant** - The stated URL will be saved inside `pelicanconf.py` as SITEURL = 'URL stated'.

###### Do you want to enable article pagination? (Y/n)

Pagination is the property of a blog to provide part of items or contents in one page and shift the rest to susequest pages with proper numering in order to allow easy access. Allowing pagination in Pelican will help showcase blogs on the homepage spreading across pages. The default value is `Y` (y or Yes) or one can also choose `n` (N or No) to disable pagination.

**Resultant** - If chosen `Y`, a subsequent question will be asked about the no of articles or blogs per page. If chosen `N`, this will be saved as `DEFAULT_PAGINATION = False` inside `pelicanconf.py`

###### How many articles per page do you want? [10]

If the previous question was answered with a `Y`, this question will be asked. This is where the number of articles or blogs per page is declared. The default number is `10`. There's no failure to this step as number is not validated.

**Resultant** - `DEFAULT_PAGINATION = 10` will be stored inside `pelicanconf.py`.

###### What is your time zone? [Europe/Paris] 

Time zones are important in order to properly state the date and time of creation of blogs and also while generating feeds. The default time zone is set to `Europe/Paris` which can be changed by providing another one. Look into this [wikipedia guide](http://en.wikipedia.org/wiki/List_of_tz_database_time_zones) for the complete list.

**Resultant** - `TIMEZONE = 'Europe/Paris'` will be saved inside `pelicanconf.py`.

###### Do you want to generate a Fabfile/Makefile to automate generation and publishing? (Y/n)

Fabfile.py and Makefile are used to manage development server, publishing website to gh-pages or via ssh and similar feature. The default answer to this is `Y` (y or Yes), after which Pelican will ask few questions to create the proper configuration for Fabfile.py and Makefile. If `n` (N or No) is entered, generation of Fabfile.py and Makefile will be skipped.

**Resultant** - If `Y` is selected, configuration for generating Fabfile.py and Makefile will be asked after the next question.

###### Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n)

Auto-reload and simpleHTTP scripts are very helpful while in development as they facilitate local server management and auto-reload whenever the content of the website is changed. This step is specifically to ask whether `develop_server.sh` file should be created with command line scripts in order to provide auto-reload and simpleHTTP facilities.

**Resultant** - If `Y` is selected, `develop_server.sh` will be created with proper configurations.

> The reason why before asking for Fabfile.py and Makefile configurations, we are asked about `develop_server.sh` is because Makefile can also use `develop_server.sh` to facilitate local server management.

Now, let's look into options that will come up if `Y` is chosen for generating Fabfile/Makefile.

###### Do you want to upload your website using FTP? (y/N)

If files of this website is to be uploaded to the server using FTP connection this option can be useful. The default is `n` (N or No).

**Resultant** - `n` (N or No) will leave placeholders inside Fabfile.py and Makefile to be filled later. If `Y` (y or Yes) is chosen, 3 subsequest questions will be asked related to the FTP configuration.

- What is the hostname of your FTP server? [localhost] 
- What is your username on that server? [anonymous] 
- Where do you want to put your web site on that server? [/]

Each of the above questions have default value which can be changed later from inside the Fabfile.py and Makefile.

###### Do you want to upload your website using SSH? (y/N)

Another option one can use to upload their files is SSH, state whether or not you want to configure SSH here.

**Resultant** - `n` (N or No) will leave placeholders inside Fabfile.py and Makefile to be filled later. If `Y` (y or Yes) is chosen, 4 subsequest questions will be asked related to the SSH configuration.

- What is the hostname of your SSH server? [localhost] 
- What is the port of your SSH server? [22] 
- What is your username on that server? [root] 
- Where do you want to put your web site on that server? [/var/www]

Each of the above questions have default value which can be changed later from inside the Fabfile.py and Makefile.

###### Do you want to upload your website using Dropbox? (y/N)

Another helpful option is using Dropbox to upload the files, this is where you state whether or not you would like to configure it.

**Resultant** - `n` (N or No) will leave placeholders inside Fabfile.py and Makefile to be filled later. If `Y` (y or Yes) is chosen, only 1 subsequest question will be asked related to the Dropbox configuration.

- Where is your Dropbox directory? [~/Dropbox/Public/]

Above questions have default value which can be changed later from inside the Fabfile.py and Makefile.

###### Do you want to upload your website using S3? (y/N)

If you have a Amazon S3 web service configured, state `y` to use the option to provide your configuration details.

**Resultant** - `n` (N or No) will leave placeholders inside Fabfile.py and Makefile to be filled later. If `Y` (y or Yes) is chosen, only 1 subsequest question will be asked related to the S3 configuration.

- What is the name of your S3 bucket? [my_s3_bucket]

Above questions have default value which can be changed later from inside the Fabfile.py and Makefile.

###### Do you want to upload your website using Rackspace Cloud Files? (y/N)

Rackspace Cloud Files users can use the Official API to upload files of the website, by enabling this option the API can be configured.

**Resultant** - `n` (N or No) will leave placeholders inside Fabfile.py and Makefile to be filled later. If `Y` (y or Yes) is chosen, 3 subsequest questions will be asked related to the Rackspace Cloud Files configuration.

- What is your Rackspace Cloud username? [my_rackspace_username]
- What is your Rackspace Cloud API key? [my_rackspace_api_key]
- What is the name of your Cloud Files container? [my_cloudfiles_container]

Each of the above questions have default value which can be changed later from inside the Fabfile.py and Makefile.

###### Do you want to upload your website using GitHub Pages? (y/N)

GitHub Pages are also supported by Fabfile.py and Makefile, entering `y` will about more details for it's configuration.

**Resultant** - `n` (N or No) will leave placeholders inside Fabfile.py and Makefile to be filled later. If `Y` (y or Yes) is chosen, only 1 subsequest question will be asked related to the GitHub Pages configuration.

- Is this your personal page (username.github.io)? (y/N)

Above questions have default value which can be changed later from inside the Fabfile.py and Makefile.

* * *

#### Demystifying `pelican-quickstart`

The entire process ends up in the desired project structure as stated above. Now let's look into the other side of the action Pelican contributors have put a lot of efforts in.

###### Handling Command-line Arguments

`pelican-quickstart` used [argparse](https://docs.python.org/3/howto/argparse.html) to handle command-line arguments which user can provide at the very beginning. By running `pelican-quickstart -h` it's more clear which arguments one can provide.

- `PATH` - Use `-p path/to/folder` to provide the desirable path for website 
- `title` - Use `-t Website-Title` to provide the title
- `author` - Use `-a Author-Name` to provide the name of author
- `lang` - Use `-l en` with 2 letter language code for default language

Once the program is executed, an ArgumentParser object is created which can handle above optional arguments and store it in a `dict` object. The values of this `dict` can be checked further in the program to ask appropriate questions.

###### The Interrogation Process

`pelican-quickstart` has a `dict` named as `CONF` with default configurations which are modified with every question asked to the user.

    CONF = {
        'pelican': 'pelican',
        'pelicanopts': '',
        'basedir': os.curdir,
        'ftp_host': 'localhost',
        'ftp_user': 'anonymous',
        'ftp_target_dir': '/',
        'ssh_host': 'localhost',
        'ssh_port': 22,
        'ssh_user': 'root',
        'ssh_target_dir': '/var/www',
        's3_bucket': 'my_s3_bucket',
        'cloudfiles_username': 'my_rackspace_username',
        'cloudfiles_api_key': 'my_rackspace_api_key',
        'cloudfiles_container': 'my_cloudfiles_container',
        'dropbox_dir': '~/Dropbox/Public/',
        'github_pages_branch': _GITHUB_PAGES_BRANCHES['project'],
        'default_pagination': 10,
        'siteurl': '',
        'lang': _DEFAULT_LANGUAGE,
        'timezone': _DEFAULT_TIMEZONE
    }

There are 3 variables used inside `CONF`.

- `_GITHUB_PAGES_BRANCHES` - It's a `dict` which contains local and remote branch information.

        _GITHUB_PAGES_BRANCHES = {
            'personal': 'master',
            'project': 'gh-pages'
        }

- `_DEFAULT_LANGUAGE` - [locale](https://docs.python.org/3.5/library/locale.html) is used to access the user's default language from their local machine. It's set to `English` by default or in case the local machine doesn't have a default language.

- `_DEFAULT_TIMEZONE` - [tzlocal](https://pypi.python.org/pypi/tzlocal) package is used to figure out the local timezone of user's machine. It's set to `Europe/Paris` by default or in case of failure in fetching local timezone.

###### Cross Version Compatibility

`pelican-quickstart` is a great example of how a Python program can be made compatible with both Python 2 and 3. For this purpose [future](https://docs.python.org/3.5/library/__future__.html), [codecs](https://docs.python.org/3.5/library/codecs.html) and [six](https://pypi.python.org/pypi/six) packages are used.

- `six` is compatible with both Python 2 and 3 and helps in figuring out which of the functions should be used if either of the versions is encountered. Once such instance is when we need to figure out whether to use `raw_input()` or `input()`. A boolean `six.PY3` is used which results `True` if the version is Python 3 and `False` otherwise. Hence the appropriate function can be returned as seen below.

        :::python
        def _input_compat(prompt):
            if six.PY3:
                r = input(prompt)
            else:
                r = raw_input(prompt)
            return r

- `future` is used to bring support of `print()` using `print_function` and provide `UTF-8` support to print function using `unicode_literals`. Or as Python lovers say, bringing future to earlier versions of Python.

- `codecs` is also compatible with both Python 2 and 3 and provides support for file management. Mostly `codecs.open` is used by `pelican-quickstart` to facilitate the compatibility.

        :::python
        with codecs.open(os.path.join(CONF['basedir'], 'pelicanconf.py'), 'w', 'utf-8') as fd:

###### Creating files and folders out of thin air

To finish of, all `pelican-quickstart` has to do is create files and folders considering all the configurations it has taken from the user. To create folders, `os.makedirs` is used from [os](https://docs.python.org/3.5/library/os.html) package is used. Creating folders is rather a simple process as compared to how files are generated using configurations provided.

[Jinja2](http://jinja.pocoo.org/) plays a major role in facilitating the smooth transition of configurations to Python, .sh and Makefile. [Jinja Templates](https://github.com/getpelican/pelican/tree/master/pelican/tools/templates) for `Makefile`, `develop_sever.sh`, `fabfile.py`, `pelicanconf.py`, and `publishconf.py` are already stored within `pelican-quickstart`. Now the task of is to open the template, use `CONF` dict to find out all the important configuration and replace the `value` with the placeholders named with similar `key` as in `CONF`. For example, `pelicanconf.py.jinja2` contains `AUTHOR = {{author}}` where `author` is replaced with the `value` of `author` in `CONF` and a new file `pelicanconf.py` is created after all the replacements.

* * *

These are most of the content I understood by reading the source of [pelican-quickstart](https://github.com/getpelican/pelican/blob/master/pelican/tools/pelican_quickstart.py) and looking into the repository itself. In case you find any error in my blog feel free to comment down below or reach out to me and help out in making this blog a little better. Thank you for your patience.
