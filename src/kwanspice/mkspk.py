"""
Make an SPK file

Created: 1/18/25
"""
import subprocess
from os import unlink
from os.path import exists
from tempfile import mkstemp, NamedTemporaryFile
from typing import Iterable

import numpy as np




def mkspk(*,oufn:str,
            data:list[np.ndarray|list],
            comment:str=None,
            fmt:list[str]|str='f',
            delete_temp:bool=True,
            append:bool=False,
            **kwargs):
    """
    Make an SPK file from a dataset.

    :param cmds: Commands to write to mkspk header

    This is a thin wrapper around the `mkspk`
    Spice utility, so go look there for details.
    """

    def stringify(val)->str:
        """
        Stringify a value for printout in a mkspk command file
        :param val:
        :return:
        """
        if type(val) == str:
            result = f"'{val}'"
        elif isinstance(cmd_val, Iterable):
            result = '('
            for item in cmd_val:
                result+=stringify(item)+' '
            result+=')'
        else:
            result=f'{val}'
        return result
    if not 'data_delimiter' in kwargs:
        kwargs['data_delimiter']=','
    kwargs['lines_per_record']=1 # This depends only on how we write the data -- its not up to the user.
    with NamedTemporaryFile(mode="wt",suffix=".mkspk") as ouf_mkspk, NamedTemporaryFile(mode="wt",suffix=".data") as ouf_data:
        oufn_mkspk=ouf_mkspk.name
        oufn_data=ouf_data.name
        # Write the mkspk command file
        if comment is not None:
            print(comment,file=ouf_mkspk)
        print(r"\begindata",file=ouf_mkspk)
        for cmd_name,cmd_val in kwargs.items():
            print(f"{cmd_name.upper()} = {stringify(cmd_val)}",file=ouf_mkspk)
        ouf_mkspk.flush()
        # Write the data file
        if not type(fmt) is list:
            fmt=[fmt]*len(data[0])
        for record in data:
            line=f"{record[0]:{fmt[0]}}"
            for item,f in zip(record[1:],fmt[1:]):
                line=f"{line}{kwargs['data_delimiter']}{item:{f}}"
            print(line,file=ouf_data)
        ouf_data.flush()
        # Run mkspk
        if not append:
            if exists(oufn):
                unlink(oufn)
        args=["mkspk"]
        if append:
            args+=["-append"]
        args+=["-setup", oufn_mkspk, "-input", oufn_data, "-output", oufn]
        subprocess.check_call(args)





def main():
    pass


if __name__ == "__main__":
    main()
