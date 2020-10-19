# logfilerenamer
Rename generic log files to match the name of the containing path.

Note: this will fail to work if there is more than one .log file in a folder. Multiple .log files will be renamed to the same folder.log name, and only the last one will be kept.

## Initial:

    basepath/
    + folder1/
    ++ generic.log
    + folder2/   
    ++ generic.log
    ++ folder21/
    +++ generic.log
    ++ folder22/
    +++ generic.log

## Final:

    basepath/
    + folder1/
    ++ folder1.log
    + folder2/   
    ++ folder2.log
    ++ folder21/
    +++ folder21.log
    ++ folder22/
    +++ folder22.log
