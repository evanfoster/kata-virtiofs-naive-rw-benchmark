.PHONY: build run clean
IMAGE_NAME?="evanfoster/kata-virtiofs-naive-rw-benchmark"
NAMESPACE?="default"

default: run

build:
	docker build -f Dockerfile -t $(IMAGE_NAME):latest .
	docker push $(IMAGE_NAME):latest

run:
	./run.sh $(NAMESPACE)

clean:
	./clean.sh $(NAMESPACE)
