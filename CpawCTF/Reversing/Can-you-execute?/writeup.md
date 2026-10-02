# 問題url

https://ctf.cpaw.site/questions.php?qnum=7

# writeup

Dockerfileを作成
```dockerfile
FROM ubuntu:24.04

WORKDIR /work

CMD ["/bin/bash"]

```

イメージを作る
```bash
docker build --platform linux/amd64 -t ctf-linux .
```

仮想環境の中に入る

```bash
docker run --rm -it \
  --platform linux/amd64 \
  -v "$PWD":/work \
  -w /work \
  ctf-linux
```

ファイルを実行できるようにする
```bash
chmod +x exec_me
```

ファイルを実行する
```bash
./exec_me
```
