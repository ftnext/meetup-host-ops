#!/usr/bin/env bash
set -euo pipefail

# Usage: ./shorten_and_qr.sh http://example.com/awesome awesome_page

LONG_URL=$1
CUSTOM_SLUG=$2
QR_CODE_PATH="${CUSTOM_SLUG}.png"

set -x
python bitly.py "${LONG_URL}" "${CUSTOM_SLUG}"
python qr_bitly.py create "${CUSTOM_SLUG}" "${QR_CODE_PATH}"
