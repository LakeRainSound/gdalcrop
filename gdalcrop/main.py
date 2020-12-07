from pathlib import Path
import time

from osgeo import gdal


def gdalcrop(shp_file_name: str):
    # オリジナルのデータがあるディレクトリ
    origin_data_dir = Path("/app") / Path("image")
    # .shpファイルの場所を指定する
    path_to_shp_file = Path("/app/shapefile") / Path(shp_file_name+".shp")
    # 実際に処理をしていく
    print('start')
    for path_to_origin in origin_data_dir.iterdir():
        if not (path_to_origin.suffix == '.tif'):
            print(path_to_origin.name, "is not warped.")
            continue
        # 出力先のディレクトリを指定
        outdir = Path("/app/cropped") / Path(shp_file_name)
        # 対応するshpファイルのディレクトリを作成
        outdir.mkdir(exist_ok=True, parents=True)
        # 出力先のファイルを指定
        outfile = outdir / path_to_origin.name

        # gdal.Warpを用いて計算
        gdal.Warp(str(outfile), str(path_to_origin),
                  format="GTiff",
                  cutlineLayer=shp_file_name,
                  cutlineDSName=path_to_shp_file,
                  dstNodata="nan",
                  cropToCutline=True
                  )
        print("warped", outfile)
        time.sleep(0.25)


def main():
    gdalcrop("bari_cher")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
