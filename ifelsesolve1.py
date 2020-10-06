import math
import os
import random
import re
import sys

n=int(input("Enter input "))


if(n%2==0 and n in range(6,20)):
    print("Weird")
elif(n%2==0 and n in range(2,5) or n>20):
    print("Not Weird")
