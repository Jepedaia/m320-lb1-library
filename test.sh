#!/bin/bash
VENV_PYTEST="/home/jepedaia/PycharmProjects/M320/m320-ix25-m320-lu09-a01-school-ia25b-grimaj/.venv/bin/pytest"
VENV_PYLINT="/home/jepedaia/PycharmProjects/M320/m320-ix25-m320-lu09-a01-school-ia25b-grimaj/.venv/bin/pylint"

echo "=========================================="
echo " Running Unit Tests (pytest)..."
echo "=========================================="
if [ -f "$VENV_PYTEST" ]; then
    $VENV_PYTEST -v "$@"
else
    pytest -v "$@"
fi

echo ""
echo "=========================================="
echo " Running Pylint Check..."
echo "=========================================="
if [ -f "$VENV_PYLINT" ]; then
    $VENV_PYLINT --rcfile .github/autograding/pylintrc exceptions.py book.py loan.py library_card.py member.py library.py
else
    pylint --rcfile .github/autograding/pylintrc exceptions.py book.py loan.py library_card.py member.py library.py
fi
