# Axel Task Project Assignment
Service is deployed live on heruko on following [link](https://axeltestservice.herokuapp.com/)
![](https://img.shields.io/badge/Deploy-Heruko-informational?style=flat&logo=heroku&logoColor=white&color=2bbc8a)
![](https://img.shields.io/badge/Framework-Flask-informational?style=flat&logo=flask&logoColor=white&color=2bbc8a)
## How to run
1. Clone repository
```bash
git clone git@github.com:ahmadabdullah247/axel_task.git
cd 'axel_task'
```
2. (Optional) For ease of reproducibility I like to keep my project libraries seperate. Feel free to omit this if you like. 
```bash
python -m virtualenv .venv
source .venv/bin/activate
```
3. This will install all the libraries you need to run the server.
```bash
pip install -r requirements.txt
```
4. You can run the server by using any one of the following commands
```bash
flask run
python app.py
```
5. To run test 
```bash
python test_app.py
```
