FROM python:3.8

WORKDIR /app

RUN apt-get update && apt-get install -y tzdata \
    libgdal-dev

# GDALをpipでインストール
RUN pip install --upgrade pip
RUN pip install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"

# スクリプトを移す
COPY . ./

# 自作ツールをインストール
RUN pip install .
