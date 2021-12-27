from pydantic import BaseModel
from typing import List
import yaml
from pathlib import Path
import os

app_path = "." / Path(__file__).parent.parent.absolute()

with (app_path / "config.yaml").open() as f:
    _default_config = yaml.safe_load(f)
_config = _default_config.copy()

with open(os.getenv("DISCORD_TOKEN"), "rb") as f:
    _config["discord_token"] = f.readline()


class _Config(BaseModel):
    discord_token: str
    min_post_char_length: int
    accepted_languages: List[str]
    message: str


Config: _Config = _Config.validate(_config)
