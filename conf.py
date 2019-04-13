# -*- coding: utf-8 -*-
import multiprocessing
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

bind = "0.0.0.0:8000"
worker_class = "sync"
workers = 2
threads = 16
errorlog = os.path.join(base_dir, "g_error.log")
accesslog = os.path.join(base_dir, "g_access.log")
pro_name = "blog_project"
