# The most safe way to connect internet of cracked switch

* First you need one route installed the OpenWrt operating system

* Second run flask server witch plain.py

* Third connect to route's temrinal and execute the command below

```bash
iptables -t filter -I FORWARD -m mac --mac-source 70:47:F8:03:52:AC -j REJECT
iptables -t nat -I PREROUTING -m mac --mac-source 70:47:F8:03:52:AC -p tcp --dport 80 -j DNAT --to-destination IP:PORT
```

before excute command,you need replace the mac address with your switch mac address,and IP:PORT is replaced with your flask server IP:PORT


```bash

# if you don't wanna run a flask server, the efficiency way is copying the command below and excuting in OpenWrt terminal.

iptables -t filter -I FORWARD -m mac --mac-source 70:48:F7:02:53:D8 -j REJECT

iptables -t nat -I PREROUTING -m mac --mac-source 70:48:F7:02:53:D8 -p tcp --dport 80 -j DNAT --to-destination 101.37.172.130:8091

iptables -t filter -I FORWARD -m mac --mac-source 70:48:F7:02:53:D8 -d 101.37.172.130 -j ACCEPT

```


# Chinese Version

* 第一你需要一台OpenWrt路由器

* 用plain.py 启动flask服务器

* 执行以下命令

```bash
iptables -t filter -I FORWARD -m mac --mac-source 70:47:F8:03:52:AC -j REJECT
iptables -t nat -I PREROUTING -m mac --mac-source 70:47:F8:03:52:AC -p tcp --dport 80 -j DNAT --to-destination IP:PORT
```
执行前，把mac地址替换成你的switch的mac地址，IP:PORT替换成你的flask服务器的IP跟PORT




