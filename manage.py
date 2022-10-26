from app import app
from app.models import *

if __name__ == "__main__":
    from app.urls import *
    app.run(debug=True)
