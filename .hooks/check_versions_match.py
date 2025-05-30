#!/usr/bin/env python3
try:
	import tomllib
except ImportError:  # For Python < 3.11
	import tomli as tomllib

import re
import sys
from pathlib import Path


def get_version_from_init(init_path: str):
	text = Path(init_path).read_text(encoding='utf-8')
	match = re.search(r'^__version__\s*=\s*[\'"]([^\'"]+)[\'"]', text, re.MULTILINE)
	if not match:
		print(f'❌ No __version__ found in {init_path}')
		sys.exit(1)
	return match.group(1)


def get_version_from_pyproject(pyproject_path: str):
	text = Path(pyproject_path).read_text(encoding='utf-8')
	try:
		data = tomllib.loads(text)
		return data['project']['version']
	except Exception:
		print('❌ Could not find [project] version in pyproject.toml')
		sys.exit(1)


def main():
	version_init = get_version_from_init('src/strsplitter/__init__.py')
	version_pyproject = get_version_from_pyproject('pyproject.toml')

	if version_init != version_pyproject:
		print(
			f'❌ Version mismatch: __init__.py = {version_init}, pyproject.toml = {version_pyproject}'
		)
		sys.exit(1)

	print(f'✅ Versions match: {version_init}')
	return 0


if __name__ == '__main__':
	sys.exit(main())
