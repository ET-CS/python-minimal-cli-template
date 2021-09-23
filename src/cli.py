from argparse import ArgumentParser


def main():
    parser = ArgumentParser(prog='My App')
    parser.add_argument('name', help="The user's name.")
    args = parser.parse_args()
    print("Hello, %s!" % args.name)
