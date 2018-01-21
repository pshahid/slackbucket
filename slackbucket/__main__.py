import argparse

from core import MetaConfig, Bucket

def main(args):
    cfgs = MetaConfig()
    b = Bucket(cfgs.cfgs['cs-cofc'])
    try:
        b.start()
    except KeyboardInterrupt:
        b.stop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='bucket')
    args = parser.parse_args()
    main(args)
