#!/bin/sh

script_path="$1"
cluster_name="$2"

python3 "${script_path}" "${cluster_name}" &
python3 "${script_path}" "${cluster_name}" &
python3 "${script_path}" "${cluster_name}" &