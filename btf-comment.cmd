@echo off

set bfpath=%USERPROFILE%\bftools
set infile=%~f1
set outfile=%~dpn1.txt

echo # Bioformats core info > %outfile%
call showinf -nopix -nometa %infile% >> %outfile%
echo: >> %outfile%
echo # Hamamatsu metadata >> %outfile%
call %bfpath%\tiffcomment.bat %infile% >> %outfile%
::must replace ; with newlines afterwards