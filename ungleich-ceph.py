#!/usr/bin/env python3

import argparse


def do_full_disk(args):
    print("full disk mode")


def do_rest_of_disk(args):
    print("rest of disk mode")


MODES = {
    "full-disk": do_full_disk,
    "rest-of-disk": do_rest_of_disk,
}


def check_mode(value):
    if value not in MODES:
        raise argparse.ArgumentTypeError("Invalid mode {}".format(value))
    return value


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store', dest='class', required=False,
                        help=('device class, e.g. hdd or ssd (only used in '
                              'rest-of-disk mode)'))
    parser.add_argument('-F', action='store_true', dest='fullsize',
                        required=False, default=False,
                        help='use fullsize (only used in full-disk mode)')
    parser.add_argument('-m', action='store', dest='mode', required=True,
                        type=check_mode,
                        help=('operate in specified mode: full-disk, '
                              'rest-of-disk'))
    parser.add_argument('-n', action='store_true', dest='dry_run',
                        required=False, default=False,
                        help=('do not execute code, only print what would '
                              'be done'))
    parser.add_argument('-w', action='store', dest='weight', required=False,
                        help=('OSD weight (only used in rest-of-disk mode)'))
    parser.add_argument('device', nargs='+', help='device to create OSD on')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    print(args)
    mode = args.mode
    MODES[mode](args)


if __name__ == "__main__":
    main()
