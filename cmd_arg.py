import argparse
import requests

def download_file(url, local_filename):
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename


parser = argparse.ArgumentParser()

parser.add_argument("url", help= "url of the file to download")
parser.add_argument("output", help="by which name u want to save file")

args = parser.parse_args()

print(args.url)
print(args.output)

download_file(args.url, args.output)