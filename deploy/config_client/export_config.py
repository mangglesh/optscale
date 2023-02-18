
from client import Client as EtcdClient
import json

etcd_cl = EtcdClient(host="localhost", port=2379)

print(json.dumps(etcd_cl.read_branch("/")))