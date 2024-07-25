#!/bin/sh

find ${PWD} -path "*/migrations/*.py" -not -name "__init__.py" -delete
find ${PWD} -path "*/migrations/*.pyc"  -delete