#!/bin/bash
namespace="$1"
kubectl -n "$namespace" delete pod $(basename -s .yaml ./*.yaml)
