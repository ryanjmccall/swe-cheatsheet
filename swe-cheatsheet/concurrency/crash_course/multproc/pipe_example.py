from multiprocessing import Pipe, Process


def child(conn):
    for i in range(10):
        conn.send(f'{i}')
    conn.close()


def main():
    parent_conn, child_conn = Pipe()
    p = Process(target=child, args=(child_conn,))
    p.start()
    for _ in range(10):
        print(parent_conn.recv())
    parent_conn.close()
    p.join()

if __name__ == "__main__":
    main()

