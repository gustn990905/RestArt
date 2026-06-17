import os
import logging
import random
from typing import List
from fastapi import FastAPI, HTTPException
import uvicorn
import pymysql
import requests
import cv2
import numpy as np
from io import BytesIO
from PIL import Image
from sklearn.cluster import SpectralClustering
from scipy.spatial.distance import cdist
from pydantic import BaseModel, HttpUrl
from skimage.metrics import structural_similarity as ssim

# FastAPI ?좏뵆由ъ??댁뀡 珥덇린??
app = FastAPI()

# 濡쒓퉭 ?ㅼ젙
logging.basicConfig(level=logging.INFO)

# ?곗씠?곕쿋?댁뒪 ?ㅼ젙
db_config = {
    "host": os.getenv("RESTART_DB_HOST", "localhost"),
    "user": os.getenv("RESTART_DB_USER", "restart_user"),
    "password": os.getenv("RESTART_DB_PASSWORD", ""),
    "database": os.getenv("RESTART_DB_NAME", "restart"),
}

def connect_db(config):
    """ ?곗씠?곕쿋?댁뒪 ?곌껐 ?⑥닔 """
    try:
        connection = pymysql.connect(host=config['host'],
                                     user=config['user'],
                                     password=config['password'],
                                     database=config['database'],
                                     cursorclass=pymysql.cursors.DictCursor)
        logging.info("Database connection successful")
        return connection
    except Exception as e:
        logging.error(f"Database connection failed: {e}")
        return None

# ?곗씠?곕쿋?댁뒪 ?곌껐
db_connection = connect_db(db_config)

def get_image_url_list(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT url FROM images")
            result = cursor.fetchall()
            return [row['url'] for row in result]
    except Exception as e:
        logging.error(f"Failed to fetch image URLs: {e}")
        return []

# image_url_list 媛?몄삤湲?
image_url_list = get_image_url_list(db_connection)
