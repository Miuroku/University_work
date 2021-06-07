source venv/bin/activate &&
python library/setup.py bdist_wheel &&
python utility/setup.py clean --all install clean --all