@echo off

set scriptpath=%USERPROFILE%\Marius\btf-comment

echo Processing...
for /r %~p1 %%G in (*.BTF) do ( 
echo %%G
call %scriptpath% %%G
)
echo done!