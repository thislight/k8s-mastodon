#! /usr/bin/env python

import random
import string
import sys

TEMPLATE = """apiVersion: v1
metadata:
  name: mastodon
spec:
  env:
    - name: SECRET_KEY_BASE
      value: "{key_base}"
    - name: OTP_SECRET
      value: "{otp}"
    - name: VAPID_PRIVATE_KEY
      value: |
      {vapid_private}
    - name: VAPID_PUBLIC_KEY
      value: |
      {vapid_public}

"""

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.sample(letters, length))

def main():
    with open(sys.argv[1]) as f:
        pri_key = f.read()
    with open(sys.argv[2]) as f:
        pub_key = f.read()
    base = get_random_string(256)
    otp = get_random_string(256)
    with open(sys.argv[3]+'/secrets.yaml') as f:
        f.write(TEMPLATE.format(key_base=base, otp=otp, vapid_private=pri_key, vapid_public=pub_key))
    print("Done!")
