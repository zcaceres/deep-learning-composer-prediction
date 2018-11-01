#! /bin/bash

# For directory
gcloud compute scp --recurse ./data fastai-instance:~/data

# For single file
# gcloud compute scp ./wk1/img/spectro-conversion.gif fastai-instance:~
