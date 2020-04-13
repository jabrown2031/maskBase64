#!/user/bin/python

import sys, getopt
import base64, gzip, re;

def usage():
        print("\n=======================================================================================")
        print("Usage:")
        print("maskbase64.py -m string -f string")
        print("-------------")
        print("-m | --message string                   ### message string")
        print("-f | --fill string                      ### filler string. ex. \"super secret key\"")
        print("=======================================================================================\n")

def mask(message, fill):
    s1 = message;
    s2 = fill;

    b1 = base64.b64encode(gzip.compress(s1.encode('ascii'))).decode('ascii').strip('=').strip('AAA');
    b2 = base64.b64encode(gzip.compress(s2.encode('ascii'))).decode('ascii').strip('=').strip('AAA');
    b3="";

    b1=re.sub(r'^.*4C/', '', b1);
    b2=re.sub(r'^.*4C/', '', b2);

#    print(b1);
#    print(b2);

    for i in range(len(b1)):
        b3 = b3 + b1[i] + b2[i];
    
    return b3;

def main(argv):
        message=""; 
        fill="";
        obfText="";

        if len(argv)<1:
                print("Missing Arguments")
                usage()
                sys.exit(2)
        
        # arg parse block, try to get cli arguments
        try:
                opts, args = getopt.getopt(argv, 'hm:f:', ["message=", "fill="])
        except getopt.GetoptError as err:
                print(err)
                usage()
                sys.exit(2)
        
        for opt, arg in opts:
                if opt == '-h':
                        usage()
                        sys.exit()
                elif opt in ('-m', "--message"):
                        message = arg
                elif opt in ('-f', "--fill"):
                        fill = arg
                else:
                        print("what, how did this happen");

        obfText = mask(message, fill);
        print(obfText);


if __name__ == "__main__":
        main(sys.argv[1:])
