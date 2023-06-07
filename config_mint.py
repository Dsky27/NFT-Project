#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 23:07:24 2021

@author: AlgoKittens
"""

from mint_arc69 import mint_asset
import pandas as pd 

testnet= False

meta_path = r"C:\Users\maxen\OneDrive\Bureau\LOBSTER PYTHON\Metadata\_metadata.json" #location of metadata
meta_type = "HashLips" #metadata type, valid argments = "csv", "JonBecker", "HashLips"
image_path = r"C:\Users\maxen\OneDrive\Bureau\LOBSTER PYTHON\output" #location of images
unit_name = "PLB"
asset_name = "Pixel Lobster #"
api_key = "2a9d4e3db8050433b802" #your pinata key
api_secret = "e983806abeb135a9f28a2520209da34399d05bef2a24dd7d5c54df90936cb9d4" #your pinata secret
mnemonic1 = "toilet involve crash sample thing shock add dash adult idea night opera inject ripple dynamic artist style good comfort analyst catch toast grab ability sell"
external_url = "http://www.pixelobsternft.com/"
description = "A lil Lobster, in love with freedom and equality, who decided to take up arms with its 999 others friends."

if (meta_type=="csv"):
    df = pd.read_csv(meta_path)    

elif (meta_type=="JonBecker"):
    df = pd.read_json(meta_path)    

elif (meta_type=="HashLips"):
    df = pd.read_json(meta_path)    
    
for n in range(333,397):
    mint_asset (n, unit_name, asset_name, mnemonic1, image_path, meta_path, meta_type, api_key, api_secret, external_url, description, testnet=testnet)
