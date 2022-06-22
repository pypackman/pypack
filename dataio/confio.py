"""
Config IO (for loading the TOML.)
"""
import toml

def LoadConf() -> dict:
    with open('config.toml') as t: return toml.loads(t.read())