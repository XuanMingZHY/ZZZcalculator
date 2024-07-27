import yaml

def reader():
    # 读取 YAML 文件
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # 输出读取到的配置内容
    return config