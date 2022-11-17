## venv
虚拟
![](images/2022-11-17-18-03-11.png)

## 安装


![](images/2022-11-17-19-14-29.png)

```sh
sudo apt install python3-venv
```

## 创建虚拟环境

```sh
python3 -m venv test_env
```

## 启用虚拟环境

![](images/2022-11-17-19-16-48.png)

```sh
.\test_env\bin\activate.bat
```

使用pip安装需要的包：
```sh
pip install tensorflow
```

## 退出虚拟环境
```sh
deactivate
```