@echo off
for %%f in (*.mp4) do (
    echo Processing %%f
    ffmpeg -i "%%f" -c:v libx264 -profile:v baseline -c:a aac -strict -2 "../outputs/converted/%%~nf.mp4"
    if exist "../outputs/converted/%%~nf.mp4" (
        del "%%f"
    )
)
echo Done!