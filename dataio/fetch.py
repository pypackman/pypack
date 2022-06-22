"""
fetch and install a package.
"""

import wget, toml, sys
from dataio.confio import LoadConf

def GetSourcesList(url: str) -> dict:
    print(url + "/packages.toml")
    print(wget.download(url + "packages.toml"))
    
    pass

def FetchAndInstall(name: str) -> bool:
    config = LoadConf()
    print("loading configuration...")
    srclist = GetSourcesList(config['sources']['list'])
    print("reading package list...")
    sys.path.append('/tmp')
    try:
        installer = wget.download(config['sources']['list'] + srclist[name]['path'] + "/install.py")
        print("downloading installer.py...")
    except:
        print("This package is not a valid package!")
        return False
    with open('/tmp/installer.py', 'wb') as installerFile:
        installerFile.write(installer.content)
        try:
            import installer
        except ImportError:
            print('failed to read installer.py! halting on fatal error.')
            print('please report it to the devs.')
    return True