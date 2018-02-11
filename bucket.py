import argparse
import sys

from slackbucket.config import MetaConfig
from slackbucket.bucket import Bucket


def main(args):
    cfgs = MetaConfig(path=args.config)
    slack = cfgs.cfgs['cs-cofc'].slack
    b = Bucket(slack, cfgs.cfgs['cs-cofc'])
    try:
        b.start()
    except KeyboardInterrupt:
        b.stop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='bucket')
    parser.add_argument('-c', '--config', default='/usr/src/app/config.yaml', help='Config.yaml location')
    args = parser.parse_args()
    main(args)
