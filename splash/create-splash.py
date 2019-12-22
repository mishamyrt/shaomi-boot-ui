import io
from os.path import join

imagePositions = [
    { 'image': 'locked.bmp', 'offset': 0x5000 },
    { 'image': 'fastboot.bmp', 'offset': 0x741000 },
    { 'image': 'unlocked.bmp', 'offset': 0xE7D000 },
    { 'image': 'error.bmp', 'offset': 0x15B9000 }
]

header = [
    0x4C, 0x4F, 0x47, 0x4F, 0x21, 0x21, 0x21, 0x21, 0x05, 0x00, 0x00, 0x00,
    0x3C, 0x07, 0x00, 0x00, 0x41, 0x07, 0x00, 0x00, 0x3C, 0x07, 0x00, 0x00,
    0x7D, 0x0E, 0x00, 0x00, 0x3C, 0x07, 0x00, 0x00, 0xB9, 0x15, 0x00, 0x00,
    0x3C, 0x07
]

output = open('logo.img', 'wb')
# Fill by zeroes
output.write(bytearray([0 for i in range(0x1CF5000)]))
# Write basic header
output.seek(0x4000)
output.write(bytearray(header))
# Write images
for position in imagePositions:
    output.seek(position['offset'])
    img = open(join('splash', position['image']), 'rb')
    output.write(img.read())

