#!/usr/bin/python3
"""Uloz.to quick multiple sessions downloader."""

import argparse
import sys
import signal

from ulozto_downloader import downloader, captcha

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Download file from Uloz.to using multiple parallel downloads.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('url', metavar='URL', type=str, help="URL from Uloz.to (tip: enter in 'quotes' because the URL contains ! sign)")
    parser.add_argument('--parts', metavar='N', type=int, default=10, help='Number of parts that will be downloaded in parallel')
    parser.add_argument('--output', metavar='DIRECTORY', type=str, default="./", help='Target directory')

    args = parser.parse_args()

    d = downloader.Downloader(captcha.tkinter_user_prompt)

    # Register sigint handler
    def sigint_handler(sig, frame):
        d.terminate()
        print('Program terminated.')
        sys.exit(1)
    signal.signal(signal.SIGINT, sigint_handler)

    d.download(args.url, args.parts, args.output)
