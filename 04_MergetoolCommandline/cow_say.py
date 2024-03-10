import cowsay
import cmd
import shlex

class CMDL(cmd.Cmd):
    """Cowsay command line"""

    prompt = ">> "

    def do_EOF(self, args):
        return 1

    def do_list_cows(self, args):
        print(cowsay.list_cows)

    def do_cowsay(self, args):
        """cowsay realization; optional parameters cow|eyes|tongue"""
        args = shlex.split(args)

        cow = 'default'
        eyes = cowsay.Option.eyes
        tongue = cowsay.Option.tongue

        i = 0
        while i < len(args):
            match args[i]:
                case '-c'|'--character':
                    cow = args[i+1]
                    del args[i+1]
                case '-e'|'--eyes':
                    eyes = args[i+1]
                    del args[i+1]
                case '-T'|'--tongue':
                    tongue = args[i+1]
                    del args[i+1]
                case msg:
                    message = msg
            i += 1

        print(cowsay.cowsay(message, cow=cow, eyes=eyes, tongue=tongue))

    def do_cowthink(self, args):
        """cowthink realization; optional parameters cow|eyes|tongue"""
        args = shlex.split(args)

        cow = 'default'
        eyes = cowsay.Option.eyes
        tongue = cowsay.Option.tongue

        i = 0
        while i < len(args):
            match args[i]:
                case '-c'|'--character':
                    cow = args[i+1]
                    del args[i+1]
                case '-e'|'--eyes':
                    eyes = args[i+1]
                    del args[i+1]
                case '-T'|'--tongue':
                    tongue = args[i+1]
                    del args[i+1]
                case msg:
                    message = msg
            i += 1

        print(cowsay.cowthink(message, cow=cow, eyes=eyes, tongue=tongue))

    def do_make_bubble(self, args):
        """make_bubble realization;"""

        print(cowsay.make_bubble(args))


if __name__ == "__main__":
    CMDL().cmdloop()