%%file threewaypipe.py


import os, sys, signal

MESSAGE_TUPLE = ("I love HMMY", "(most of) the women are ugly", "but the food", "is even worse")

def child(read, write):
    os.close(write)
    #print("~"*40)
    for message in MESSAGE_TUPLE:
        message = os.read(read, len(message))
        print(f"I am process {os.getpid()} and I read \"{message.decode()}\"")
        os.kill(os.getpid(), signal.SIGSTOP)
    exit(0)

def main():
    p = os.pipe()
    reader = 12
    os.dup2(p[0], reader)
    if not p:
        print("Problem during the pipe oppening (nordstream moment), quitting...")
        os.close(p)
        os._exit(1)
    
    child_1 = os.fork()
    if child_1 == -1:
        print("Forking error, quitting.")
        os.close(p)
        os.exit(1)
    elif child_1 == 0:
        child(p[0], p[1])
    else:
        child_2 = os.fork()
        if child_2 == -1:
            print("Forking error, quitting.")
            os.close(p)
            os.exit(1)
        elif child_2 == 0:
            child(reader, p[1])
        else:
            for message in MESSAGE_TUPLE:
                print(f"I am parent {os.getpid()} and I write \"{message}\"")
                os.write(p[1], message.encode())
                os.write(p[1], message.encode())
                while True:
                    info_1 = os.waitpid(child_1, os.WSTOPPED)
                    info_2 = os.waitpid(child_2, os.WSTOPPED)
                    child_1_stopped = os.WIFSTOPPED(info_1[1])
                    child_2_stopped = os.WIFSTOPPED(info_2[1])
                    if child_1_stopped and child_2_stopped:
                        os.kill(child_1, signal.SIGCONT)
                        os.kill(child_2, signal.SIGCONT)
                        break
            os.close(p[1])
            os.wait()


if __name__ == '__main__':
    main()