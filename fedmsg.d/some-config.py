import socket
hostname = socket.gethostname()

config = dict(
    endpoints={
        "fedimg.%s" % hostname: [
            "tcp://127.0.0.1:6009",
            "tcp://127.0.0.1:6008",
            "tcp://127.0.0.1:6007",
            "tcp://127.0.0.1:6006",
        ],
    },
}
