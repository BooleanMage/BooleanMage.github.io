@echo off
setlocal enabledelayedexpansion

REM Recursively find all .png and .jpg files under the current directory
for /r %%i in (*.png *.jpg) do (
    REM Extracting filename without extension
    set "filename=%%~ni"
    REM Extracting directory path
    set "dirpath=%%~dpi"
    REM Generating output filename with .webp extension
    set "output_filename=!dirpath!!filename!.webp"
    REM Converting .png or .jpg to .webp using ffmpeg
    ffmpeg -i "%%i" "!output_filename!"
)

endlocal
