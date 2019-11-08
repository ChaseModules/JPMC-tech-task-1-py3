# Chase Module 0

## How to use

* `chmod 755 start.sh`
  * allow the start script permissions.
* `./start.sh`
  * if detects if 8080 is being used, if so, run the client, if not run the server and the client.
  * So dont change the server port.

## pre-setup

* install yapf (vscode will prompt you globally)
  * if vscode doesn't prompt you. Go to your global python directory  (which python3.7 or whatever version you have.)
  * `<pythonhomedirectory>/python -m pip install yapf --user`
    * then in your vscode user settings, in the yapf arguments
    * ["--style", "{based_on_style: chromium, indent_width: 2}"]
    * there's a gui that helps you do it too.
  
## EASY setup

* install pyenv
* pyenv install
  * `brew install pyenv`
  * initializer script
    `echo 'eval "$(pyenv init -)"' >> ~/.bash_profile`
* set global defaults
  * pyenv global '3.6.2'
* pyenv local `<versionno>`
  * this will install that version in your home directory
  * the place you local will use stuff from there.
  * highly unrecommended. you dont wanna install wholly unnecessary stuff

## Currrent setup

* above instruction but wihtout using pyenv local
* brew install pyenv-virtualenv
* `brew install pyenv-virtualenv`
* `echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile`
* `pyenv virtualenv <python-version> <name>`
  * creates a virtualenv around your app
    * so pip install will only install packages in that virtualenv.
* pyenv activate `<name>`
  * or use tab completions to select your env.
  * a prompt called `<name>` should be next to your stuff.
  * I call mine 3.6.2chase
* virtualenv will now be called fakeenv because tldr.

## Steps

### Step 1 activate your fakeenv

* pyenv activate 3.6.2chase
* pip install python-dateutil
  * pip freeze > requirements.txt
    * if you ever decide to delete your fakeenv
      * install a new fakeenv
        * pip install -r requirements.txt (-r denotes install packages in order);

### Step 2

* python server3.py &
  * why the & ?
    * it's annoying that a single terminal is needed to keep a server up.
    * close your terminal and the server will shutdown
    * You'll want the server for debugging later though if you do flask apps
* python client3.py > test.txt
  * sees all the ratios.
  * `grep -c Quoted text.txt`
    * there's 1000 instancces of quoted but 500 actual api requests.
* API Requests
  * `curl 'http://localhost:8080/query?id=1'`
  * or fire up postman, api route is /query
