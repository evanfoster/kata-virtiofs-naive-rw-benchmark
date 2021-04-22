Before running your tests, ensure your KUBECONFIG is defined (if not using `~/.kube/config`) and your context is set.

To run the tests, simply run `make`, or `make run`. If you want to specify a namespace other than `default`, run `NAMESPACE=foo make`

After running your test, you'll need to `make clean`. This isn't handled automatically because doing so would nuke the pod logs.

The image is built and pushed using `make build`. They go to my Docker Hub namespace by default, but this can be overridden with the `IMAGE_NAME` environment variable.

This test depends on the following:
* Docker/containerd nodes as a control
* CRI-O nodes with Kata
  * The nodes should be labeled and tainted with `node.kubernetes.io/kata-containers=true`
  * Kata should be configured to use `virtio-fs`
  * Two `runtimeClassName`s must exist:
    * `kata-qemu`, for Kata
    * `runc`, for standard runc
