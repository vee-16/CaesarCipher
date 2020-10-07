text = str(input("Enter the text to be encrypted: "))
shift = int(input("Shift by: "))
direction = input("Direction to shift: ").lower()

def caesar(text, shift):
    cipher = ""
    for i in text:
        if i.isalpha():
            if direction == 'right':
                pos = ord(i)
                pos += shift
            elif direction == 'left':
                pos = ord(i)
                pos -= shift
            if pos > ord('z'):
                pos -= 26
            if pos < ord('a'):
                pos += 26           
            final = chr(pos)            
            cipher += final
        elif i == " ":
            x = " "
            cipher += x
        
    print("cipher: ", cipher)
    return cipher

caesar(text, shift)
