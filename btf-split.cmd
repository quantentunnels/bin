@echo off

::setlocal ENABLEEXTENSIONS
set infile=%~f1
set infolder=%~dp1
set bfpath=%USERPROFILE%\bftools
set outfileroot=%infolder%%~n1

if not exist %infile% (
echo Input file is not valid.
exit /b 1 )
 
:: # Parameters
:: number of images per substack (20 fps &2 min = 2400 frames)
set delta=2400
set nSubstacks=15
set start=15

echo Writing output to %outfileroot%_sub*.BTF
for /l %%i in (%start%,1,%nSubstacks%) do ( call :createSubstack "%%i" )
echo Done!

exit /b

:createSubstack
set outfile=%outfileroot%_sub%~1.BTF
set /a startTime=(%~1-1)*%delta%+1
set /a endTime=%~1*%delta%+1
echo Extracting frame %startTime%-%endTime%...
call %bfpath%\bfconvert.bat -range %startTime% %endTime%  %infile% %outfile%