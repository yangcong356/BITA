__all__ = ['common', 'configs', 'datastes', 'models', 'processors', 'tasks', 'runners', 'project']

import os
import sys
from omegaconf import OmegaConf
from BITA.common.registry import Registry

root_dir = os.path.dirname(os.path.abspath(__file__))
default_cfg = OmegaConf.load(os.path.join(root_dir, "configs/default.yaml"))

Registry.register_path("library_root", root_dir)
repo_root = os.path.join(root_dir, "..")
Registry.register_path("repo_root", repo_root)
cache_root = os.path.join(repo_root, default_cfg.env.cache_root)
Registry.register_path("cache_root", cache_root)

Registry.register("MAX_INT", sys.maxsize)
Registry.register("SPLIT_NAMES", ["train", "val", "test"])
