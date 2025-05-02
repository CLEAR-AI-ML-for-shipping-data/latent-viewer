import argparse
import sys

from loguru import logger

from . import viewer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--embeddings", help="Embeddings file", required=True)
    parser.add_argument(
        "-a", "--image-archive", help="Trajectory image archive (hdf5)", required=True
    )
    parser.add_argument(
        "-f",
        "--filecolumn",
        help="Filename column in the embeddings file",
        default="filename",
    )
    parser.add_argument(
        "-d", "--debug", help="Run in debug mode", type=bool, default=False
    )

    args = parser.parse_args()
    viewer.embeddings_file = args.embeddings
    viewer.arrays_file = args.image_archive
    viewer.filecolumn = args.filecolumn
    debug = args.debug

    if debug is False:
        logger.remove()
        logger.add(sys.stderr, level="INFO")
    viewer.app.run(debug=debug)

if __name__ == "__main__":
    main()
