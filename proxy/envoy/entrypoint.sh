#!/bin/sh

sed -e "s/\${SERVICE_NAME}/${SERVICE_NAME}/" \
    -e "s/\${SERVICE_PORT}/${SERVICE_PORT}/" \
    -e "s/\${OPA_HOST}/${OPA_HOST}/" \
    -e "s/\${OPA_PORT}/${OPA_PORT}/" \
    /config/envoy.yaml > /etc/envoy.yaml

/usr/local/bin/envoy -c /etc/envoy.yaml -l ${LOG_LEVEL:-info}
