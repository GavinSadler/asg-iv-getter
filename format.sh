
src="./src"

echo "=== Running autoflake ==="

python -m autoflake -i -r -v $src

echo "=== Running isort ==="

python -m isort $src

echo "=== Running black ==="

python -m black $src