#!/usr/bin/python

import pytesseract
from PIL import Image
import os
import sys

# Delete temporary files

def clean_up():
	os.remove("cp.jpg")
	os.remove("hp.jpg")
	os.remove("sd.jpg")

def main():
	img = Image.open(sys.argv[1])
	w, h = img.size
	img.crop((50, 50, 700, 150)).save("cp.jpg")
	img.crop((200, 600, 500, 650)).save("hp.jpg")
	img.crop((300, 850, 450, 950)).save("sd.jpg")

	hp = pytesseract.image_to_string(Image.open("hp.jpg"))
	cp = pytesseract.image_to_string(Image.open("cp.jpg"))
	star_dust = pytesseract.image_to_string(Image.open("sd.jpg"))

	# Extract HP
	hp = hp[0:3]
	hp = int(hp)

	# Extract CP
	cp_digits = len(cp) - 2
	if cp_digits == 2:
		cp = cp[2:4]
	elif cp_digits == 3:
		cp = cp[2:5]
	else:
		cp = cp[2:6]
	cp = int(cp)

	# Extract Stardust
	sd_digits = len(star_dust) - 3
	if sd_digits == 3:
		star_dust = star_dust[3:7]
	else:
		star_dust = star_dust[3:8]
	star_dust = int(star_dust)

	stats = (cp, hp, star_dust)
	print stats

	# Perform clean up of temp files
	clean_up()

main()
