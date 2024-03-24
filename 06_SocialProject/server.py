import asyncio
import cowsay
import shlex

users = dict()

async def handler(reader, writer):
    client = writer.get_extra_info("peername")
    print(f'New Client on {client}')
    my_id = None
    my_queue = asyncio.Queue()
    my_cmd = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(my_queue.get())

    while not reader.at_eof():
        done, pending = await asyncio.wait([my_cmd, receive], return_when=asyncio.FIRST_COMPLETED)

        for request in done:
            if request is my_cmd:
                my_cmd = asyncio.create_task(reader.readline())
                print(f'{client}: {request.result()}')
                args = shlex.split(request.result().decode()) #
                print(args)
                match args:
                    case ['who']:
                        response = "\n".join(users.keys()) + "\n\n" if users.keys() else "No one "
                        response += "is online now"
                        writer.write(f'{response}\n'.encode())
                    
                    case ['cows']:
                        response = ' '.join(sorted(set(cowsay.list_cows()) - set(users.keys())))
                        response = "available accounts:\n\n" + response
                        writer.write(f'{response}\n'.encode())
                    
                    case ['login', cow_name]:
                        if cow_name in users.keys():
                            writer.write('LoginError: Exists user with this id\n'.encode())
                            break
                        my_id = cow_name
                        users[my_id] = my_queue
                        print(f"{client} logs in as {my_id}\n")
                        client = my_id
                    
                    case ['say', rcv_name, msg]:
                        if not my_id:
                            writer.write('NoAccessError: You are non-authorized client, please log in\n'.encode())
                            break
                        if rcv_name not in users.keys():
                            writer.write(f'NoUserError: There is no user with name \"{rcv_name}\"\n'.encode())
                            break

                        await users[rcv_name].put(f'{cowsay.cowsay(msg, cow=my_id)}')                    
                    
                    case ['yield', msg]:
                        if not my_id:
                            writer.write('NoAccessError: You are non-authorized client, please log in\n'.encode())
                            break
                        
                        for user in users.values():
                            if user is not my_queue:
                                await user.put(f'{cowsay.cowsay(msg, cow=my_id)}')                    
                    
                    case ['quit']:
                        if not my_id:
                            writer.write('NoAccessError: You are non-authorized client, please log in\n'.encode())
                            break

                        client = writer.get_extra_info("peername")
                        print(f"{client} logs out from {my_id}\n")
                        del users[my_id]
                        my_id = None
                    
                    case _:
                        continue
                    

            if request is receive:
                receive = asyncio.create_task(my_queue.get())
                writer.write(f"{request.result()}\n".encode())
                await writer.drain()
    my_cmd.cancel()
    receive.cancel()
    if my_id:
        del users[my_id]
    writer.close()
    await writer.wait_closed()
    print(f'{client} left')

async def main():
    print('Start working')
    server = await asyncio.start_server(handler, '0.0.0.0', 1337)
    print('activate server')
    async with server:
        print('Server Forever')
        await server.serve_forever()

asyncio.run(main())