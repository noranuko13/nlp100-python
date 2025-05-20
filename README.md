# nlp100-python


## Commands

```shell
# Build Docker image
docker compose build --no-cache

# Start container
docker compose run --rm runner

# Syntax
flake8 . && mypy .

# Test
pytest

# Stop container
docker compose down
```


## License

- [言語処理100本ノック 2015](http://www.cl.ecei.tohoku.ac.jp/nlp100/)  
   Copyright (c) 2012-2015 [Naoaki Okazaki](http://www.chokkan.org/), [Inui-Okazaki Laboratory](http://www.cl.ecei.tohoku.ac.jp/).

- The source code of this project is licensed under [the MIT License](LICENSE).
