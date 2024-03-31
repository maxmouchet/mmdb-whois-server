import maxminddb
import logging

SEPARATOR = b"\r\n"


class Handler:
    def __init__(self, database, footer):
        self.reader = maxminddb.open_database(database)
        self.footer = footer

    async def handle(self, reader, writer):
        buffer = b""
        while True:
            if data := await reader.read(4096):
                buffer += data
                if SEPARATOR in data:
                    buffer = buffer.split(SEPARATOR)[0]
                    break

        query = buffer.decode()
        remote = writer.get_extra_info("peername")
        logging.info("Request from %s:%s -- %s", remote[0], remote[1], query)

        info = self.reader.get(query)
        w = max(len(k) for k in info) + 2

        for k, v in info.items():
            k = k.replace("_", "-") + ":"
            writer.write(f"{k:{w}} {v}".encode() + SEPARATOR)

        if self.footer:
            writer.write(SEPARATOR + self.footer.encode() + SEPARATOR)

        await writer.drain()

        writer.close()
        await writer.wait_closed()
