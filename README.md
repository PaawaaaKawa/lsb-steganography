# LSB Steganography   

Steganography is hiding a message inside an image by replacing each pixel’s least significant bit with the bits of the message to be hidden.   

 the usage of a program

```
$ python3 stegano.py
```
And this is usage how to use this   
![image](https://user-images.githubusercontent.com/69034642/161126756-19943e22-1859-4e1a-9971-208228f16e19.png)   

So we need to encrypt a message by this tool

```
$ python3 stegano.py -i test.jpg -s paia -m "Hi Its Paiwand" -o output.png --encryption
```
Image:   
![image](https://user-images.githubusercontent.com/69034642/161128957-35b7f85d-2a5e-4628-abfc-75617125af49.png)   

   
So we need to decrypt a message by this tool   
```
$ python3 stegano.py -i output.png -s paia --decryption
```

Image:   
![image](https://user-images.githubusercontent.com/69034642/161129366-86d2000d-fee0-4124-98c3-fdc5a95fac7c.png)



