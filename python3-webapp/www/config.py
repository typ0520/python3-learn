#!/usr/bin/env python3

import config_default
configs = config_default.configs

def merge(defaults, override):
	res = {}
	for k,v in defaults.items():
		if k in override:
			if isinstance(v, dict):
				res[k] = merge(v, override[k])
			else:
				res[k] = override[k]
		else:
			res[k] = v

	return res

try:
	import config_override
	configs = merge(configs, config_override.configs)
except ImportError:
	pass

class Dict(dict):
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

def toDict(d):
	D = Dict()
	for k,v in d.items():
		D[k] = v
	return D

configs = toDict(configs)

if __name__ == '__main__':
	print(configs)