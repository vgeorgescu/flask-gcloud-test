#!/bin/bash

set -e

# expecting the install directly in the home directory
GCLOUD=${HOME}/google-cloud-sdk/bin/gcloud

if ${GCLOUD} version 2>&1 >> /dev/null; then
    echo "Cloud SDK is already installed"
else
    SDK_URL=https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-228.0.0-linux-x86_64.tar.gz
    INSTALL_DIR=${HOME}

    cd ${INSTALL_DIR}
    wget ${SDK_URL} -O cloud-sdk.tar.gz
    tar -xzvf cloud-sdk.tar.gz
fi

echo $GCLOUD_SERVICE_KEY | ${GCLOUD} auth activate-service-account --key-file=-
${GCLOUD} config set project ${GOOGLE_PROJECT_ID}
${GCLOUD} config set compute/zone ${GOOGLE_COMPUTE_ZONE}