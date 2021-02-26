#!/usr/bin/python3
from. import base_model
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
