import argparse

parser = argparse.ArgumentParser(
                    description = "cowsay-alike program",
                    epilog = "If u're tired, go to bed, dudes. Try to understand this program later")

parser.add_argument('message', metavar = 'text', type = str, nargs = '?',
                    action = 'store',
                    help = 'Message that cow say')
parser.add_argument('-e', type = str, nargs = '?', action = 'store',
                    help = 'cows eye-string')
parser.add_argument('-f', type = argparse.FileType('W'), nargs = '?',
                    help = 'custom cow file')
parser.add_argument('-T', type = str, nargs = '?', action = 'store',
                    help = 'cows tongue-string')
parser.add_argument('-W', type = int, nargs = '?',
                    help = 'cows eye-string')

args = parser.parse_args()
print(args.message, args.W, args.T, args.e, args.f)

