# Food recipe recognition
    The goal of this project is to get nutrional information from a single picture of a dishe.
We usualy forget 1/3 of everything we're eating. If we want to log our food, for a better health, for a sporting event, or for a specific diet, the task can be very tidious, we need to scale everything, scan the bar code to have the nutrition information or putting it by hand. The idea here is to make the task easier and getting all information simply by taking one picture.

- Document here the project: foodE
- Description: Project Description
- Data Source:
- Type of analysis:

Please document the project the better you can.

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for foodE in github.com/{group}. If your project is not set please add it:

Create a new project on github.com/{group}/foodE
Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "foodE"
git remote add origin git@github.com:{group}/foodE.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
foodE-run
```

# Install

Go to `https://github.com/{group}/foodE` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/foodE.git
cd foodE
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
foodE-run
```
