FROM python:3.9-slim

COPY entrypoint.sh /entrypoint.sh
COPY ../agent.py /agent.py
COPY ../detect_language.py
COPY ../dt_diff_lib.py /dt_diff_lib.py
COPY ../workflow_requirements.txt /workflow_requirements.txt

ENTRYPOINT ["/entrypoint.sh"]