import textwrap
from confluent_kafka import Producer

import json
import random
from datetime import datetime
import time

# 定义一个函数来生成随机订单数据（数据类型为Python字典）
def generate_order():

    countries = [
        "USA",
        "Canada",
        "UK",
        "Germany",
        "France",
        "Australia",
        "Japan",
        "Ireland",
    ]
    
    order = {
        "order_id": random.randint(1000, 9999),
        "customer_id": random.randint(1, 10),
        "total_price": round(random.uniform(20.0, 1000.0), 2),
        "customer_country": random.choice(countries),
        "merchant_country": random.choice(countries),
        "order_date": datetime.now().isoformat(),
    }

    return order



def main():
    config = {
        "bootstrap.servers": "node1:9092",
    }

    producer = Producer(config)

    topic = "orders"

    # 定义一个回调函数来处理消息传递结果（成功或失败）
    def delivery_callback(err, msg):
        if err:
            print("ERROR: Message failed delivery: {}".format(err))
        else:
            print(
                # 使用textwrap.dedent来格式化多行字符串，去除多余的缩进
                  textwrap.dedent(
                f"""
                    Produced event to topic {msg.topic()}:
                    key = {msg.key().decode('utf-8')}
                    value = {msg.value().decode('utf-8')}
                """)
            )

    while True:
        order = generate_order()
        print(f"Sending order: {order}")

        producer.produce(
            topic,
            key = str(order["customer_id"]),# key用作分区
            value = json.dumps(order),# 将Python字典转换为JSON字符串（序列化）
            callback = delivery_callback
        )
        producer.poll(0)

        time.sleep(1)



if __name__ == "__main__":
    main()