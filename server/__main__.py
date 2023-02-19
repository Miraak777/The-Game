from .constants import ServerConstants
from .common import get_config
from .routes import app

if __name__ == '__main__':
    config = get_config()
    app.run(host=config[ServerConstants.HOST], port=config[ServerConstants.PORT])
