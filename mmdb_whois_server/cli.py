import argparse
import asyncio
import logging

from mmdb_whois_server.handler import Handler


async def async_main():
    parser = argparse.ArgumentParser()
    parser.add_argument("database")
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", default=43, type=int)
    parser.add_argument("--footer", default="")
    parser.add_argument("--log-level", default="info")
    args = parser.parse_args()

    logging.basicConfig(level=args.log_level.upper())

    handler = Handler(args.database, args.footer)
    server = await asyncio.start_server(handler.handle, args.host, args.port)
    logging.info("Listening on %s:%s", args.host, args.port)

    await server.serve_forever()


def main():
    asyncio.run(async_main())
