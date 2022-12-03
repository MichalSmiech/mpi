from mpi4py import MPI, rc

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print("rc.thread_level", rc.thread_level)

print("rc.threads", rc.threads)

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
    print(rank, 'sent')
elif rank == 1:
    data = comm.recv(source=MPI.ANY_SOURCE, tag=11)
    print(rank, data)