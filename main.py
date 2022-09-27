import os
import pathlib
import os
from pathlib import Path

def getfiles(input_folder, extensions):
    files = [
        str(filepath) 
        for filepath in  pathlib.Path(input_folder).glob('**/*') 
        if os.path.isfile(filepath) and 
        os.path.splitext(os.path.basename(str(filepath)))[-1] in extensions
    ]
    return files


def renamefiles(fs,mapping):
    replaced = 0
    for of in fs:
        base = os.path.basename(of)
        parent = Path(of).parent
        for k, v in mapping.items():
            base = base.replace(k,v)
        nf = os.path.join(parent, base)
        if of != nf:
            print(f"{os.path.basename(of)} --> {os.path.basename(nf)}")
            os.rename(of, nf)
            replaced += 1
        else:
            print(f"{os.path.basename(of)}, no changes to make")

    print(f'{len(fs)} files found')
    print(f'{replaced} files replaced')


inputfolder = '/home/zeljana/Desktop/sample/data'


files = getfiles(
    inputfolder,
    ['.txt']
    #['.xml', '.pdf', .'json', '.txt']
)


renamefiles(files,{
    'data':'nole'
})