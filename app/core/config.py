import os


class Config:
    def __init__(self):
        self.POSTGRES_CONNECTION_STRING = os.environ['POSTGRES_CONNECTION_STRING']
        self.CHROMA_CONNECTION_STRING = os.environ['CHROMA_CONNECTION_STRING']
        self.MONGODB_CONNECTION_STRING = os.environ['MONGODB_CONNECTION_STRING']


CONFIG = Config()
