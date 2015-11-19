# file-upload-server

- zlib压缩后文件上传, 用于网络相对较慢的环境

- logs是一个空目录, 记录运行时的日志

- 安装配置(根据需要替换成自己的配置)

    ```
    cd /data/web
    git clone https://github.com/wasw100/file-upload-server.git
    sudo chown -R ubuntu:ubuntu file-upload-server
    ```

- 创建virtualenv环境, 并安装依赖package

- 配置supervisor, 将upservirosr/file-upload-server.conf到supervisor的配置文件位置
