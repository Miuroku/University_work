import Queue as myQueue

def main():
    qw = myQueue.Queue()

    qw.push(3)
    qw.push(6)
    qw.push(0)
    qw.push(1)

    print(qw.get_min())

main()