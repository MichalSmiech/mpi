from mpi4py import MPI, rc
import threading

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print("rc.thread_level", rc.thread_level)

print("rc.threads", rc.threads)

def send():
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
    print(rank, 'sent')

def receive():
    data = comm.recv(source=MPI.ANY_SOURCE, tag=11)
    print(rank, data)

if rank == 0:
    threading.Thread(target=send, args=()).start()
elif rank == 1:
    threading.Thread(target=receive, args=()).start()