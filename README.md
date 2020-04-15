# maskBase64
Data obfuscation with compression and base64

The process takes the message string (STR1) and user string (STR2) and compresses each, CSTR1 and CSTR2.

The compressed strings are then Base64 encoded and stripped of compression headers, footers, and Base64 padding.

The modified strings are then mixed together in the form of CSTR1[1] CSTR2[1] CSTR1[2] CSTR2[2] ....... CSTR1[n] CSTR2[n], where n = length of CSTR1.

STR1 = this is a test

STR2 = a phrase to fill the space

CSTR1 = yvJyCxWAKJEhZLU4hIA6uceDQ4

CSTR2 = 0tUKMgoSixOVSjJV0jLzMlRKMlIVSguSExOBQA1utowGg

Obfuscation text = y0vtJUyKCMxgWoASKiJxEOhVZSLjUJ4Vh0IjAL6zuMcleRDKQM4l 
