#!/bin/bash
set -eo pipefail

open -a "Google Chrome" http://localhost:8080/tree & gcloud compute --project "fast-ai-220304" ssh --zone "us-west1-b" jupyter@"fastai-instance" -- -L 8080:localhost:8080
