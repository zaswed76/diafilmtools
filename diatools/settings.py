#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml


default_config_file = os.path.join(os.path.dirname(__file__), "etc/config.yaml")

import yaml

def get_config(path):
    with open(path, 'r') as f:
        return yaml.load(f)



class Settings:
    def __init__(self, config_file=default_config_file):
        self.config_file = config_file

    def config(self):
        return get_config(self.config_file)




