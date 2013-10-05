from os import chdir, execlp, fork, waitpid, path, makedirs

from os.path import dirname
from os.path import join

from datetime import datetime

from zipfile import ZipFile


def mfold(input):
    """
    Executes mfold in order to generate appropriate files
    """
    current_datetime = datetime.now().strftime('%H:%M:%S-%d-%m-%y')

    mfold_dirname = "mfold_files"
    tmp_dirname = join(dirname(__file__), mfold_dirname, current_datetime)

    if not path.exists(tmp_dirname):
        makedirs(tmp_dirname)
    chdir(tmp_dirname)

    with open(current_datetime, "w") as f:
        f.write(input)

    pid = fork()
    if pid == 0:
        execlp("mfold", "mfold", "SEQ=%s" % current_datetime)
    waitpid(pid, 0)

    zipname = "%s.zip" % current_datetime

    with ZipFile(zipname, 'w') as mfold_zip:
        mfold_zip.write("%s_1.pdf" % current_datetime)
        mfold_zip.write("%s_1.ss" % current_datetime)

    return join(tmp_dirname, zipname)
