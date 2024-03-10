import cowsay
import cmd
import shlex

class CMDL(cmd.Cmd):
    """Cowsay command line"""

    prompt = ">> "
    complete_commands = ['-c', '--character', '-e', '--eyes', '-T', '--tongue']

    list_eyes = ['QQ', 'OO', '()', '$$', '##', 'XX', '@@', '&&', '**', '<3']
    list_tongue = ['U', 'UU', '$', '$$', 'Y', 'YY', 'W', 'WW']


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

    def complete_cowsay(self, text, line, begidx, endidx):
        """completer of cowsay: complete arguments for keys"""
        words = (line[:endidx] + ".").split()
        DICT = []

        key = None
        for rev_arg in words[::-1]:
            if rev_arg in self.complete_commands:
                key = rev_arg
                break

        print(f">>{words} - {text}<<")

        match key:
            case '-c'|'--character':
                DICT = cowsay.list_cows()
            case '-T'|'--tongue':
                DICT = self.list_tongue
            case '-e'|'--eyes':
                DICT = self.list_eyes
        
        return [c for c in DICT if c.startswith(text)]

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

    def complete_cowthink(self, text, line, begidx, endidx):
        """completer of cowthink: complete arguments for keys"""
        words = (line[:endidx] + ".").split()
        DICT = []
        
        key = None
        for rev_arg in words[::-1]:
            if rev_arg in self.complete_commands:
                key = rev_arg
                break

        match key:
            case '-c'|'--character':
                DICT = cowsay.list_cows()
            case '-T'|'--tongue':
                DICT = self.list_tongue
            case '-e'|'--eyes':
                DICT = self.list_eyes
        
        return [c for c in DICT if c.startswith(text)]


    def do_make_bubble(self, args):
        """make_bubble realization;"""

        print(cowsay.make_bubble(args))


if __name__ == "__main__":
    CMDL().cmdloop()