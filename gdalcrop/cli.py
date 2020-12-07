from argparse import ArgumentParser
from pathlib import Path


def command_parser():
    parser = ArgumentParser()
    parser.add_argument('tif_dir',
                        type=str)

    parser.add_argument('shapefile_name',
                        type=str)

    parser.add_argument('-o',
                        '--out',
                        required=True,
                        type=str,
                        help='path to output file')

    args = parser.parse_args()

    return args.tif_dir, args.shapefile_name, args.out
