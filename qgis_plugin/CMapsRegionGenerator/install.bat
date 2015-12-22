SET DEST=%HOMEPATH%\.qgis2\python\plugins\CMapsRegionGenerator
mkdir %DEST%
xcopy /e /y *.py %DEST%
xcopy /e /y *.png %DEST%
xcopy /e /y metadata.txt %DEST%
xcopy /e /y *.ui %DEST%
