# kafka-streaming-main
kafka practices


## 1. 进入 Kafka 容器：
```sh
docker exec -it kafka bash
```

## 2. 列出 Kafka Topics

Use the following command to list all topics in the Kafka cluster:

```sh
kafka-topics --list --bootstrap-server localhost:9092
```

---

## 3. 创建一个 Kafka Topic

Create a topic named `orders` with 4 partitions and a replication factor of 1:

```sh
kafka-topics --create \
  --bootstrap-server localhost:9092 \
  --topic orders \
  --replication-factor 1 \
  --partitions 4
```

---

## 4. 确认 Topic 已创建

List topics again to verify the new topic was created:

```sh
kafka-topics --list --bootstrap-server localhost:9092
```

## 如何在vscode新建一个python项目？
1. 打开 VSCode。
2. 点击左侧的“资源管理器”图标（文件夹图标）。
3. 点击“打开文件夹”按钮，选择或创建一个新的文件夹作为你的项目目录。
4. Ctrl+Shift+P，输入python，创建虚拟环境
5. 在终端中安装所需的包，例如 `pip install confluent_kafka`。

