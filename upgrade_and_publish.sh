v=$(poetry version patch -s) && git add pyproject.toml && git commit -m v$v && git tag v$v && git push --tags && poetry publish --build
