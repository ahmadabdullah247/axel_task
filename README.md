# Axel Task Project Assignment

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