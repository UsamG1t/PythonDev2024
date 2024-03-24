import cmd
import shlex
import readline
import threading
import sys
import socket

def msg_sendreciever(client, socket, message):
    socket.sendall(message.encode())
    responce = socket.recv(1024).rstrip().decode()
    print(f"\n{responce}\n{client.prompt}{readline.get_line_buffer()}", end="", flush=True)

class cmd_client(cmd.Cmd):

    prompt = ">> "

    def __init__(self, socket):
        self.socket = socket
        return super().__init__()

    def do_EOF(self, args):
        return 1

    def emptyline(self):
        pass

    def do_who(self, args):
        request = threading.Thread(target = msg_sendreciever, args = (self, self.socket, "who\n"))
        request.start()
    
    def do_cows(self, args):
        request = threading.Thread(target = msg_sendreciever, args = (self, self.socket, "cows\n"))
        request.start()
        # self.socket.sendall('cows\n'.encode())
        # print(self.socket.recv(1024).decode())
    
    def do_login(self, args):
        request = threading.Thread(target = msg_sendreciever, args = (self, self.socket, f"login {args}\n"))
        request.start()    
        # self.socket.sendall(f'login {args}\n'.encode())
        # print(self.socket.recv(1024).decode())
    
    def complete_login(self, text, line, begidx, endidx):
        words = (line[:endidx] + '.').split()
        self.socket.sendall('cows\n'.encode())
        DICT = shlex.split(self.socket.recv(1024).decode())[2:]

        return [c for c in DICT if c.startswith(text)]

    def do_say(self, args):
        rcver, message = shlex.split(args)
        request = threading.Thread(target = msg_sendreciever, args = (self, self.socket, f"say {rcver} '{message}'\n"))
        request.start()    
        # self.socket.sendall(f'say {rcver} "{message}"\n'.encode())
        # print(self.socket.recv(1024).decode())
    
    def complete_say(self, text, line, begidx, endidx):
        words = (line[:endidx] + '.').split()
        self.socket.sendall('who\n'.encode())
        DICT = shlex.split(self.socket.recv(1024).decode())[2:]

        return [c for c in DICT if c.startswith(text)]

    def do_yield(self, args):
        request = threading.Thread(target = msg_sendreciever, args = (self, self.socket, f"yield {args}\n"))
        request.start()    
        # self.socket.sendall(f'yield {args}\n'.encode())
        # print(self.socket.recv(1024).decode())
    
    def do_quit(self, args):
        request = threading.Thread(target = msg_sendreciever, args = (self, self.socket, f"quit\n"))
        request.start()    
        # self.socket.sendall('quit\n'.encode())
        # print(self.socket.recv(1024).decode())
    

host = "localhost" if len(sys.argv) < 2 else sys.argv[1]
port = 1337 if len(sys.argv) < 3 else int(sys.argv[2])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    cli = cmd_client(s)
    cli.cmdloop()