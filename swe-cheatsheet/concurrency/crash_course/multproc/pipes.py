from multiprocessing import Pipe, Process


def child_func(con):
    for i in range(10):
        con.send(f'hello {i}')
    con.close()


if __name__ == '__main__':
    par_conn, child_conn = Pipe()
    p = Process(target=child_func, args=(child_conn,))
    p.start()
    for _ in range(10):
        print(par_conn.recv())

    par_conn.close()
    p.join()
