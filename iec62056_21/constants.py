SOH = "\x01"  # Start of header
STX = "\x02"  # Frame start char
ETX = "\03"  # Frame end char
EOT = "\04"  # End of transmission
ACK = "\x06"
NACK = "\x15"
LINE_END = "\x0d\x0a"
START_CHAR = "/"
END_CHAR = "!"
REQUEST_CHAR = "?"
BREAK = f"{SOH}B0{ETX}"  # still need to calculate BCC
ENCODING = "latin-1"
