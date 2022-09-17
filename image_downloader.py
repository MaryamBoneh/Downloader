import argparse
from simple_image_download import simple_image_download as simp


parser = argparse.ArgumentParser()
parser.add_argument('--imgs_name', help='Separate the photo names with commas')
parser.add_argument('--count', help='The number of photos you want to download from each topic', default=100)
args = parser.parse_args()

response = simp.simple_image_download

keywords = args.imgs_name.split(',')

for kw in keywords:
    response().download(kw, int(args.count))
