from mpi4py import MPI, rc

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print("rc.thread_level", rc.thread_level)

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
elif rank == 1:
    data = comm.recv(source=0, tag=11)