def GeberateDefangIP(str):
 
    defangIP = "";
   
    for c in str:
        if(c == '.'):
            defangIP += "[.]"
        else:
             defangIP += c;
    return defangIP;

str = "255.100.50.0";
print(GeberateDefangIP(str));
 
