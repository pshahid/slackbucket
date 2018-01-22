import argparse

from config import MetaConfig
from bucket import Bucket


def main(args):
    cfgs = MetaConfig()
    slack = cfgs.cfgs['cs-cofc'].slack
    b = Bucket(slack, cfgs.cfgs['cs-cofc'])
    try:
        b.start()
    except KeyboardInterrupt:
        b.stop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='bucket')
    args = parser.parse_args()
    main(args)
