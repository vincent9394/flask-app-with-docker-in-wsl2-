# %%
import os
from flask import Flask,redirect
# %%
app = Flask(__name__)

@app.route('/')
def hello():
    # Attempt to read REDIRECT_TO from the environment. If nothing is set
    # perform a 301 redirect to DigitalOcean's website
    return redirect(os.environ.get("REDIRECT_TO", "https://digitalocean.com/community/tutorials"), code=301)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# %%
