#!/bin/bash

mkdir -p rollback

sf sgd source delta \
  --from HEAD \
  --to HEAD~1 \
  --output-dir rollback
