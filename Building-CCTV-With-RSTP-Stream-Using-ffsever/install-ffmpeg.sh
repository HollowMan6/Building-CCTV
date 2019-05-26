#!/bin/bash 
echo "安装ffmpeg3.4.6, 请确保所有deb文件位于当前shell打开的目录下的ffmpeg3.4.6文件夹下"
echo "Install ffmpeg 3.4.6. Make sure that all DEB files are in the ffmpeg 3.4.6 folder under the directory currently opened by the shell"
dpkg -i ./ffmpeg3.4.6/*.deb
echo "现在可以尝试运行ffmpeg, 如果提示找不到ffmpeg命令请再次运行一遍该脚本即可"
echo "Now you can try running ffmpeg. If you are prompted not to find the ffmpeg command, please run the script again."