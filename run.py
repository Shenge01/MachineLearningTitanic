# fentry point to start our flask application

from .model_api.app import create_app

application = create_app()

if __name__ == '__main__':
	application.run()
