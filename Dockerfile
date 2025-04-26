FROM python:3.9-slim

COPY entrypoint.sh /entrypoint.sh
COPY agent.py /github/workspace/agent.py
COPY detect_language.py /github/workspace/detect_language.py
COPY dt_diff_lib.py /github/workspace/dt_diff_lib.py
COPY workflow_requirements.txt /github/workspace/workflow_requirements.txt

ENTRYPOINT ["/entrypoint.sh"]