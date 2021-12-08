set workdir=%~dp0
cd %workdir%
SET PYTHONPATH=.
python server/main.py
