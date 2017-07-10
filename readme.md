# FBC Plano Awanas Site

## Viewing the data model
The data model is stored in the project directory as a DOT file, which can be
rendered by a number of tools, including [GraphViz](http://www.graphviz.org).
To view the graph without installing any additional tools, copy the contents of
`datamodel.dot` and use
[GraphvizOnline](https://dreampuf.github.io/GraphvizOnline/) (preferred) or
[WebGraphViz](http://webgraphviz.com) to convert to a visual graph.

## How to use

### Important
Instructions below take some measure of familiarity with bash and git
for granted. Even on Windows, I'm assuming that you're running this either in
[Cygwin](http://www.cygwin.com) or in
[Bash on Ubuntu on Windows](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)
(if you're on Windows 10). File paths will use the \*nix spec (forward slashes
for directories, ex: `/c/Users/youruser`, not `C:\Users\youruser`), and some of
the commands specified will need extra work to make functional in Windows.

You have been warned.

### Requirements
This project is developed using Django on Python 3.5.2. You will need:

1. Python 3.5.2
2. venv for Python 3.5.2
3. pip for Python 3.5.2 (inside the venv)

So long as you have Python3.5+, you should be fine.

You will also need `git`. Once you have it installed, make sure your username
and email are properly configured. These commands will do it:

```
git config --global user.email "<your email address"
git config --global user.name "<your name>"
# You'll probably also want to set this, while you're in there
git config --global push.default simple
```

If you don't want to put your actual email in there, and you have a GitHub
account (required if you plan to make changes and push them back to the
repository), you can use `<account>@users.noreply.github.com` as your email
address instead.

### Getting started
1. Open your bash prompt
2. Follow the steps below
    ```
    # Navigate to wherever you want to put the project, example:
    cd /c/Users/$youruser/Desktop/

    # Clone the repo
    git clone -b develop https://github.com/fbcp-awanas/website.git awanas

    # Navigate into the directory
    cd awanas

    # Make the virtual environment
    python3 -m venv .
    ## If the above fails with an error like this:
    ## Error: Command '['/home/user/awanas/awanas/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1
    ## Run this instead
    # python3 -m venv . --without-pip

    # Activate the virtual environment
    . bin/activate

    # Install pip (if you had to use the --without-pip flag above)
    # curl https://bootstrap.pypa.io/get-pip.py | python

    # Upgrade pip
    pip install -U pip

    # Install the requirements for the project
    pip install -r requirements.txt

    # Set up the database and superuser
    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py createsuperuser
    ```

You now have a copy of the project locally on your disk.

### Running the development server
1. Open your bash prompt and navigate to the project directory
2. Make sure to activate the virtual environment via `. bin/activate` - you
should see the project name in parentheses to the left of your prompt to
indicate that the project is active.
3. Run `./manage.py runserver`
    **Note:** You may want to run `./manage.py makemigrations` first, to 
    make sure that no changes to the model have been perpetrated since you 
    last updated the db. If any new migrations exist, run `./manage.py migrate` 
    to apply them, then run `./manage.py runserver`
4. Open a web browser to `http://127.0.0.1:8000/admin` to log into the admin
interface using your superuser credentials
    **Note:** If you don't know your superuser credentials, run `./manage.py createsuperuser` to make a new one.

### Importing dummy data
1. In the active virtual environment, run:
    ```
    ./manage.py shell <dummydata.py
    ```

### Starting over
It may be necessary to start from scratch (for example, to test new procedures with dummy data). If so:

1. Delete the `db.sqlite3` file
2. Re-set up the database and superuser
    ```
    ./manage.py makemigrations
    ./manage.py migrate
    ./manage.py createsuperuser
    ```

### Making changes
If you make changes to the files in the project directory, you should make sure
to commit them and push them back to github. Skip to **Detailed git examples**
in the Appendix for more detail, but here's the simplified workflow:

```
# Check your current status
git status

# Stage all changes/additions/deletions
git add -A
# OR stage individual files
git add <file1> <file2> ...

# Commit changes
git commit -m "<commit message>"

# Push to GitHub
git push
```

# Appendix
## References
* [Git reference guide](https://git-scm.com/docs)

## Detailed git examples
Use `git status` to see what files have changed. Example:

```
(website) 16:49 ~/website (develop)$ git status
On branch develop
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)
        modified:   .gitignore
        modified:   www/models.py
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        datamodel.dot
        datamodel.txt
        readme.md
        requirements.txt
no changes added to commit (use "git add" and/or "git commit -a")
```

This shows that I both added and changed files, and that they are not ready to
be committed (they must be 'staged' first).

**Note:** You should only ever push changes to the `develop` branch (identified
in the `git status` output on the first line). Do not commit or push any
changes against `master` - that should be considered the current "working"
branch, so all changes should be vetted in develop first.

To stage files, use `git add`. In this case, I want to stage everything, so I
can run `git add -A`

```
(website) 16:49 ~/website (develop)$ git add -A
(website) 16:51 ~/website (develop)$ git status
On branch develop
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
        modified:   .gitignore
        new file:   datamodel.dot
        new file:   datamodel.txt
        new file:   readme.md
        new file:   requirements.txt
        modified:   www/models.py
```

Now, I need to commit the files. Use `git commit -m "<message>"` for that,
replacing `<message>` with a brief message describing what you did in this
commit.

After committing, push the changes back to github via `git push`. If you get an
error that there is no upstream tracking branch, try `git push origin develop`
(or whatever branch you're working on, in place of `develop`)