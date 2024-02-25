import argparse
from cowsay import cowsay, list_cows, Option

parser = argparse.ArgumentParser(
                    description = "cowsay-alike program",
                    epilog = """
                    If u're tired, go to bed, dudes.
                    Try to understand this program later
                    """)

parser.add_argument('message', metavar = 'text', type = str, nargs = '?',
                    action = 'store',
                    help = 'Message that cow say')
parser.add_argument('-c', '--character', type = str, nargs = '?', action = 'store',
                    default = 'default', help = 'The name of the cow')
parser.add_argument('-e', '--eyes', type = str, nargs = '?', action = 'store',
                    default = Option.eyes, help = 'cows eye-string')
parser.add_argument('-l', action = 'store_true', 
                    help = 'show list of characters')
parser.add_argument('-f', '--file', type = argparse.FileType('W'), nargs = '?',
                    help = 'custom cow file')
parser.add_argument('-T', '--tongue', type = str, nargs = '?', action = 'store',
                    default = Option.tongue, help = 'cows tongue-string')
parser.add_argument('-W', '--width', type = int, nargs = '?',  default = 40,
                    help = 'cows eye-string')

args = parser.parse_args()

if args.l:
    print(sorted(list_cows()))
else:
    print( cowsay(args.message, cow = args.character, eyes = args.eyes, 
                                tongue = args.tongue, width = args.width))