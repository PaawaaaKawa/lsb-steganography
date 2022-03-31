# Steganography Python Project  
# Version : 1.00
import base64


red = "\33[91m"
end = "\33[0m"
green = "\33[92m"

# use try/except for if someone haven't moudle install the moudle
try:
    # import moudles
    import numpy as np
    from PIL import Image
except ImportError:
    print(f"{red}moudle didn't install it, type pip install -r requirements.txt{end}")


# create encode function and add src msg and dest
def Encode(src,message,dest,key):
    try:
        # open a image and create variable width and height to get img size
        img = Image.open(src,'r')
        width, height = img.size
        # convert source image to Numpy array of pixels and store the size of the image
        array = np.array(list(img.getdata()))
        # make a mode image if image = RGB make a variable and store 3
        if img.mode == 'RGB':
            n = 3
        #if img equals RGBA make a variable and store 4
        elif img.mode == 'RGBA':
            n = 4
        total_pixels = array.size//n
        
        #make a message because program understand to stop
        message += key
        # change message to binary code
        b_message = ''.join([format(ord(i), "08b")for i in message])
        # and use length to count message binarry
        req_pixels = len(b_message)
        if req_pixels > total_pixels:
            print(f"{red}Your File Size Is Not Large !{end}")
        else:
            index=0
            for p in range(total_pixels):
                for q in range(0,3):
                    if index < req_pixels:
                        # change all image source to binary
                        array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                        index+=1
            # now time to save the hidden message
            array = array.reshape(height,width,n)
            enc_img = Image.fromarray(array.astype('uint8'), img.mode)
            enc_img.save(dest)
            print(f"{green}Image Encode Succses{end}")
    except FileNotFoundError:
        print(f"{red}The File Not Found....{end}")


def Decode(src,key):
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0,3):
            # extract the binary
            hidden_bits += (bin(array[p][q] )[2:][-1])
    hidden_bits = [hidden_bits[i:i+8]for i in range (0,len(hidden_bits),8)]
    message = ""
    key_length = len(key)
    for i in range(len(hidden_bits)):
        if message[-key_length:] == key:
            break
        else:
            # convert ascii code to text
            message += chr(int(hidden_bits[i], 2))
            
    if key in message:
        print(f"{green}Hidden Message:{end}", message[:-key_length])
        msg = message[:-4]
       
    else:
        print(f"{red}No Message Found !{end}")
    





def main():
    import argparse
    import base64
    example_text = f"""{red}
    Usage[+]:
    python3 main.py -i image.png -s paia -m message -o output.png --encryption
    For Decryption:
    python3 main.py -i image.png -s paia
    For Help:
    python3 main.py -h
    {end}
    """
    parser = argparse.ArgumentParser(description="Steganography Tool")
    parser.add_argument("-i","--img", help="to input orginal image")
    parser.add_argument("-s","--secret", help="secret code to stop stegano output")
    parser.add_argument("-m","--message",help="Message To Hide:",type=str)
    parser.add_argument("-o","--output",help="Output Images")
    parser.add_argument("--encryption", help="to encryption data", action="store_true")
    parser.add_argument("--decryption", help="to decrypt data", action="store_true")
    args = parser.parse_args()
    art = f"""{red}
──────────▄██▄▄
─▄▄█████▄─██▀      Welcome To Steganography Tool
▀█████████▄██▄         Fast And Easy For Use !
▒▒▀██████████▀▒
▒▒▒▒▒█▄█▄▄▒▒▒▒▒

    {end}"""
    if (args.encryption):
        base64_text = args.message
        base64_text_bytes = base64_text.encode("ascii")
        base64_bytes = base64.b64encode(base64_text_bytes)
        base64_string = base64_bytes.decode("ascii")
        
        print(art)
        print(f"{green} Please Wait To Processing .......! {end}")
        Encode(args.img,base64_string,args.output,args.secret)
    elif (args.decryption):
        print(art)
        print(f"{green} Please Wait To Processing .......! {end}")
        Decode(args.img,args.secret)
    else:
        print(example_text)
    

if __name__ == "__main__":
    main()
