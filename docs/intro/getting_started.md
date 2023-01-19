## Getting Started
### Installation
```commandline
pip install crestwebframework
```
After installing crest, you should set up the CLI. The steps can vary
depending on what operating system you are using. This guide is designed for Unix-based operating systems.

### Set Up CLI
Firstly, locate the package.
```commandline
pip show crestwebframework
```
Copy or note down the ```Location``` field and run the following commands:
```commandline
sudo ln -s <Location>/crest/cli.py /usr/local/bin/crest
sudo chmod 755 /usr/local/bin/crest
```
Ensure that the CLI is set up correctly by running the help command.
```commandline
crest --help
```
### Create an App
```commandline
crest create myapp
```
