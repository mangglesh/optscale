import os

import etcd
import logging
import argparse
import json


LOG = logging.getLogger(__name__)
ETCD_CODE_INTERNAL_ERROR = 300
DEFAULT_ETCD_HOST = '127.0.0.1'
DEFAULT_ETCD_PORT = 2379
FILE_NAME = "etcd_dump.json"


class Client(etcd.Client):
    def read_branch(self, branch):
        """
        Read etcd branch and return content of it as a dict

        branch
            /parent/child1
            /parent/child2/grandchild
            /parent/child3
            /parent2

        will be returned as
            {
                'parent':
                    {
                        'child1': value,
                        'child2': {'grandchild': value}
                        'child3': value,
                    },
                'parent2': value,
            }
        :param branch:
        :return:
        """
        keys = self.read(branch, recursive=True)
        res_dict = {}
        for node in keys.children:
            parts = node.key.replace(branch, '', 1).lstrip('/').split('/')
            dict_node = res_dict
            for part in parts[:-1]:
                if part not in dict_node:
                    dict_node[part] = {}
                dict_node = dict_node[part]
            if node.dir:
                dict_node[parts[-1]] = {}
            else:
                dict_node[parts[-1]] = node.value
        LOG.debug("read %s from branch %s", res_dict, branch)
        return res_dict

    def clean_etcd(self):
        main_branch = self.read("/", recursive=True)
        for i in main_branch.children:
            print(i.key)
            if i.key:
                self.delete(i.key, recursive=True)

    def write_branch(self, branch, structure, overwrite_lists=False):
        """
        Recursive writing

        :param nj: lists will be recreated before writing
        :param branch: etcd key name
        :param structure: dict, list or value
        """
        for key, value in structure.items():
            full_key = os.path.join(branch, key)
            if isinstance(value, dict):
                self.write_branch(branch=full_key, structure=value)
            elif isinstance(value, list):
                if overwrite_lists:
                    try:
                        self.delete(full_key, recursive=True)
                    except etcd.EtcdKeyNotFound:
                        pass
                for val in value:
                    self.write(key=full_key, value=val, append=True)
            else:
                LOG.debug("%s = %s", full_key, value)
                self.write(key=full_key, value=value)

    def update_structure(self, base_key, structure, remove_keys=False,
                         always_update=None):
        if always_update is None:
            always_update = []
        keys = self.read(base_key, recursive=False)
        children = [r.key.split('/')[-1] for r in keys.children]
        added = set(structure.keys()) - set(children)
        if remove_keys:
            removed = set(children) - set(structure.keys())
            for key in removed:
                full_key = os.path.join(base_key, key)
                LOG.info('removing %s key', full_key)
                self.delete(full_key, recursive=True)

        for key, value in structure.items():
            full_key = os.path.join(base_key, key)
            if isinstance(value, dict):
                if key in added or full_key in always_update:
                    LOG.info('writing branch %s', full_key)
                    self.write_branch(full_key, value)
                else:
                    self.update_structure(full_key, value, remove_keys=True,
                                          always_update=always_update)
            elif isinstance(value, list):
                pass
            else:
                if key in added or full_key in always_update:
                    LOG.info('added key %s', full_key)
                    self.write(key=full_key, value=value)


if __name__ == '__main__':
    etcd_host = os.environ.get('HX_ETCD_HOST', DEFAULT_ETCD_HOST)
    etcd_port = os.environ.get('HX_ETCD_PORT', DEFAULT_ETCD_PORT)
    parser = argparse.ArgumentParser()
    parser.add_argument('--etcdhost', type=str, default=etcd_host,
                        help=f"etcd port default is {DEFAULT_ETCD_PORT}")
    parser.add_argument('--etcdport', type=int, default=etcd_port,
                        help=f"etcd host default is {DEFAULT_ETCD_HOST}")
    parser.add_argument('-f', type=str, default=FILE_NAME,
                        help="file to be picked")
    parser.add_argument('operation', type=str, default=FILE_NAME,
                        help="operation to be performed dump or put")
    args = parser.parse_args()
    client_obj = Client(host=args.etcdhost, port=args.etcdport)
    if args.operation == "dump":
        result_data = client_obj.read_branch("/")
        json.dump(result_data, open(args.f, "w"), indent=4)
        print("stcd keys written successfully")
    elif args.operation == "write":
        structure = json.load(open(args.f))
        client_obj.clean_etcd()
        client_obj.write_branch("/", structure, overwrite_lists=True)
        print("etcd updated successfully")
    elif args.operation == "update":
        structure = json.load(open(args.f))
        client_obj.update_structure("/", structure, remove_keys == True)
        print("etcd updated successfully")
    else:
        print("invalid operation")
