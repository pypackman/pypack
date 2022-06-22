"""
Config IO (for loading the TOML.)
"""
import toml, os

def LoadConf() -> dict:
    with open(f'{os.path.dirname(os.path.abspath(__file__))}/../config.toml') as t: return toml.loads(t.read())