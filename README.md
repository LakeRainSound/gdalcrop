# gdalcrop
gdalwarpを利用して，tif画像をシェープファイルで切り抜くことができる．

## Install
```
$ git clone https://github.com/LakeRainSound/gdalcrop.git
$ cd LakeRainSound/gdalcrop
$ docker build -t gdalcrop .
```
## Usage
次のようにディレクトリを構成する．`shapefile`というディレクトリに実際の`.shp`拡張子を持つファイルを入れる．`image`に`.tif`拡張子を持つファイルを入れる（ただし`image`という名前である必要はない）．
```
target_dir --- shapefile -- .shp files
            |_ image -- .tif files
```

```bash
$ cd target_dir
$ docker run -it --rm  -v `pwd`:/app gdalcrop <image directory> <shapefile name> <-o output_dir>
```
実行後に
```
target_dir --- shapefile  -- .shp files
            |_ image      -- .tif files
            |_ output_dir -- shapefile name -- cropped .tif files
```
のようにファイルが生成される．