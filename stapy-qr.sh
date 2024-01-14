#!/usr/bin/env bash
set -euo pipefail

NUMBER=$1

python -m myqr \
  "https://bit.ly/stapy${NUMBER}slido" \
  "stapy${NUMBER}slido.png" \
  --color ea5b76

python -m myqr \
  "https://bit.ly/stapy${NUMBER}form" \
  "stapy${NUMBER}form.png" \
  --color fed552

python -m myqr \
  "https://bit.ly/stapy${NUMBER}zoom" \
  "stapy${NUMBER}zoom.png" \
  --color 6495cf
