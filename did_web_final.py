#!/usr/bin/env python3
import asyncio
import sys
import didkit
import json
import re


def keys():
    k = json.loads(key_data)
    public_key = k['x']
    private_key = k['d']
    print(f'jwk: {key_data}\nPublic key: {public_key}\nPrivate key: {private_key}\n')


def test_web():
    async def inner():
        did_doc = await didkit.resolve_did(didkey, '{ "accept": "application/did+ld+json", "error": "notFound" }')
        # did resolution metadata (last param of resolve_did: https://www.w3.org/TR/did-core/#did-resolution-metadata
        return did_doc

    return asyncio.run(inner())


if __name__ == "__main__":
    try:
        url = sys.argv[1]
    except IndexError:
        url = 'idhub.pangea.org'

    didweb = 'did:web:' + url

    key_data = didkit.generate_ed25519_key()
    didkey = didkit.key_to_did("key", key_data)
    keys()

    newdid_test = test_web()
    key = didkey.split(':')[2]
    newdid = newdid_test.replace(didkey, didweb).replace('#' + key, '#owner')
    print(f'newdid_doc web:\n{newdid}')