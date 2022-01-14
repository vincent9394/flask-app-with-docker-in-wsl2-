https://www.digitalocean.com/community/tutorials/how-to-develop-a-docker-application-on-windows-using-wsl-visual-studio-code-and-docker-desktop

## Run the program with docker
1. python3 -m venv myapp
2. source bin/activate
3. docker build -t myapp .
4. docker run -p 8080:8080 myapp

## If you want to stop the program, 
docker stop <container id>


## If you are using jupyter notebook run the python only
install the follow package
```
pip install flask gunicorn
```

