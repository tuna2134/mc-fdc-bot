from grpc import stream_stream_rpc_method_handler
from yaml import safe_load

from typing import TypedDict, List


class DiscordType(TypedDict):
    token: str
    prefix: str

class DataType(TypedDict):
    discord: DiscordType

with open("config.yml", "r") as fp:
    DATA: DataType = safe_load(fp)

DATA["version"] = "0.0.1"