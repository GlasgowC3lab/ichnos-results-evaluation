#!/bin/bash

# Great Britain data from 
# 01-02-2026 -> 03-02-2026
# 27-02-2026 -> 29-02-2026
# 28-01-2026 -> 30-01-2026

# Germany data from
# 17-11-2025 -> 24-11-2025
# 22-02-2026 -> 24-02-2026
# 07-02-2026 -> 09-02-2026
# 05-03-2026 -> 07-03-2026

# request format
curl 'https://api.electricitymaps.com/v3/carbon-intensity/latest?zone=DE' -H 'auth-token: SECRET'
