# Gstreamer python binding tutorial

## Docker
- base on ubuntu 22.04 python base docker

```
docker build -f Dockerfile.python_base -t ubuntu22.python .
```

```bash
 gst-launch-1.0  videotestsrc \
    ! video/x-raw,width=640,height=480 \
    ! autovideosink

```

```
docker run -it --rm \
    --name gst \
    --hostname gst \
    -u=$(id -u $USER):$(id -g $USER) \
    -e DISPLAY=$DISPLAY \
    -v $(pwd):/workspace \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    vsc-gst-demos-6a03c872d7e1bdfff97b7b4b546a744626192180e19c0a116727bb14aa0005c2:latest \
    /bin/bash
```

# Reference
[velovix/sunhacks_2020_gstreamer_talk](https://gist.github.com/velovix/8cbb9bb7fe86a08fb5aa7909b2950259)