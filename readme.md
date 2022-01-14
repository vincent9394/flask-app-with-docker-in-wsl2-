https://www.digitalocean.com/community/tutorials/how-to-develop-a-docker-application-on-windows-using-wsl-visual-studio-code-and-docker-desktop

## Run the program with docker
3. docker build -t myapp .
4. docker run -p 8080:8080 myapp

## If you want to stop the program, 
docker stop <container id>

## If you are running the python local, you need to set up the environment
1. python3 -m venv myapp
2. source myapp/bin/activate
3. pip install -r requirements.txt 

## Run the python file
```
python app.py
```


## If you are using jupyter notebook run the python only
install the follow package
```
pip install flask gunicorn
```

