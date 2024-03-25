import cmd
import shlex
import readline
import threading
import sys
import socket

def msg_sendreciever(client, socket):
    while response := socket.recv(1024).rstrip().decode():
        print(f"\n{response}\n{client.prompt}{readline.get_line_buffer()}", end="", flush=True)

class cmd_client(cmd.Cmd):

    prompt = ">> "

    def __init__(self, socket, complete_socket):
        self.socket = socket
        self.complete_socket = complete_socket
        return super().__init__()

    def do_EOF(self, args):
        return 1

    def emptyline(self):
        pass

    def do_who(self, args):
        self.socket.sendall('who\n'.encode())
    
    def do_cows(self, args):
        self.socket.sendall('cows\n'.encode())
        
    def do_login(self, args):
        self.socket.sendall(f'login {args}\n'.encode())
        
    def complete_login(self, text, line, begidx, endidx):
        words = (line[:endidx] + '.').split()
        self.complete_socket.sendall('cows\n'.encode())
        DICT = shlex.split(self.complete_socket.recv(1024).decode())[2:]

        return [c for c in DICT if c.startswith(text)]

    def do_say(self, args):
        rcver, message = shlex.split(args)
        self.socket.sendall(f'say {rcver} "{message}"\n'.encode())
        
    def complete_say(self, text, line, begidx, endidx):
        words = (line[:endidx] + '.').split()
        self.complete_socket.sendall('who\n'.encode())
        DICT = shlex.split(self.complete_socket.recv(1024).decode())[:-3]

        return [c for c in DICT if c.startswith(text)]

    def do_yield(self, args):
        self.socket.sendall(f'yield {args}\n'.encode())
        
    def do_quit(self, args):
        self.socket.sendall('quit\n'.encode())
        

host = "localhost" if len(sys.argv) < 2 else sys.argv[1]
port = 1337 if len(sys.argv) < 3 else int(sys.argv[2])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as complete_s:
        s.connect((host, port))
        complete_s.connect((host, port))
        cli = cmd_client(s, complete_s)
        request = threading.Thread(target = msg_sendreciever, args = (cli, cli.socket))
        request.start()
        cli.cmdloop()