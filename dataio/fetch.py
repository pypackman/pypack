"""
fetch and install a package.
"""

import wget, toml, sys, os
from dataio.confio import LoadConf

def GetSourcesList(url: str) -> dict:
    wget.download(url + "/packages.toml", "/tmp/")
    with open('/tmp/packages.toml') as packageList: RET = toml.loads(packageList.read())
    os.remove('/tmp/packages.toml')
    return RET    

def FetchAndInstall(name: str) -> bool:
    print("loading configuration...")
    config = LoadConf()
    print("reading package list...")
    srclist = GetSourcesList(config['sources']['list'])

    try:
        
        wget.download(config['sources']['list'] + srclist[name]['path'] + "/install.py", "/tmp/")
        print("downloading installer.py...", end="\t")
        print("\n")
        
    except:
        print("This package is not a valid package!")
        return False
    try:
        print("running installer...")
        sys.path.append('/tmp')
        import install as i
        i.install()
        
    except ImportError:
        print('failed to read installer.py! halting on fatal error.')
        print('please report it to the devs.')
    os.remove('/tmp/install.py')
    return True