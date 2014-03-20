#coding:utf-8
import time
import datetime
import urllib
import xmltodict
import json
import random

SERVER_KEY = "qqqqqww"
DELTA = 2654435769 

def getkey(s):
        _loc_5=''
        _loc_6=0
        _loc_7=0
        _loc_2=s
        _loc_3=0
        _loc_4=0
        while _loc_4 < len(_loc_2):
                _loc_5 = _loc_2[_loc_4];
                _loc_6 = ord (_loc_5[0])
                _loc_7 = _loc_6 << _loc_4 % 4 * 8;
                _loc_3 = _loc_3 ^ _loc_7;
                _loc_4 = _loc_4 + 1
        return _loc_3


def encrypt(param1, param2):
        
            _loc_5 = 0;
            _loc_6 = 0;
            _loc_7 = 0;
            _loc_13 = 0;
            _loc_14 = 0;
            _loc_15 = 0;
            _loc_16 = 0;
            _loc_17 = 0;
            _loc_18 = 0;
            _loc_19 = 0;
            _loc_20 = 0;
            _loc_21 = 0;
            _loc_22 = 0;
            _loc_23 = 0;
            _loc_24 = 0;
            _loc_25 = 0;
            _loc_26 = 0;
            _loc_27 = 0;
            _loc_28 = 0;
            _loc_29 = 0;
            _loc_30 = 0;
            _loc_31 = 0;
            _loc_32 = 0;
            _loc_33 = 0;
            _loc_34 = 0;
            _loc_35 = 0;
            _loc_36 = 0;
            _loc_37 = 0;
            _loc_38 = 0;
            _loc_39 = 0;
            _loc_40 = 0;
            _loc_41 = 0;
            _loc_3 = 16;
            _loc_4 = getkey(param2);
            _loc_8 = param1;
            _loc_9 = param2;
            _loc_10 = _loc_4;
            _loc_5 = _loc_4 << 8 | _loc_10 >> 24;
            _loc_6 = _loc_10 << 16 | _loc_10 >> 16;
            _loc_7 = _loc_10 << 24 | _loc_10 >> 8;
            _loc_11 = "";
            _loc_12 = 0;
            while _loc_12 + _loc_3 <= len(_loc_8) :
            
                
                _loc_13 = ord(_loc_8[_loc_12]) << 0;
                _loc_14 = ord(_loc_8[(_loc_12 + 1)]) << 8;
                _loc_15 = ord(_loc_8[_loc_12 + 2]) << 16;
                _loc_16 = ord(_loc_8[_loc_12 + 3]) << 24;
                _loc_17 = ord(_loc_8[_loc_12 + 4]) << 0;
                _loc_18 = ord(_loc_8[_loc_12 + 5]) << 8;
                _loc_19 = ord(_loc_8[_loc_12 + 6]) << 16;
                _loc_20 = ord(_loc_8[_loc_12 + 7]) << 24;
                _loc_21 = 0 | _loc_13 | _loc_14 | _loc_15 | _loc_16;
                _loc_22 = 0 | _loc_17 | _loc_18 | _loc_19 | _loc_20;
                _loc_23 = 0;
                _loc_24 = 0;
		
                while (_loc_24 < 32):
                
          
                    _loc_23 =0xffffffff & ( _loc_23 + DELTA);
                    _loc_33 =0xffffffff & (  (_loc_22 << 4) + _loc_4);
                    _loc_34 =0xffffffff & (  _loc_22 + _loc_23);
                    _loc_35 =0xffffffff & (  (_loc_22 >> 5) + _loc_5);
                    _loc_36 =0xffffffff & (  _loc_33 ^ _loc_34 ^ _loc_35);
                    _loc_21 =0xffffffff & (  _loc_21 + _loc_36);
                    _loc_37 =0xffffffff & (  (_loc_21 << 4) + _loc_6);
                    _loc_38 =0xffffffff & (  _loc_21 + _loc_23);
                    _loc_39 =0xffffffff & (  _loc_21 >> 5);
                    _loc_40 =0xffffffff & (  _loc_39 + _loc_7);
                    _loc_41 =0xffffffff & (  _loc_37 ^ _loc_38 ^ _loc_40);
                    _loc_22 =0xffffffff & (  _loc_22 + _loc_41 );
                    _loc_24+=1;

                
                _loc_25 = _loc_21 >> 0 & 255;
                _loc_26 = _loc_21 >> 8 & 255;
                _loc_27 = _loc_21 >> 16 & 255;
                _loc_28 = _loc_21 >> 24 & 255;
                _loc_29 = _loc_22 >> 0 & 255;
                _loc_30 = _loc_22 >> 8 & 255;
                _loc_31 = _loc_22 >> 16 & 255;
                _loc_32 = _loc_22 >> 24 & 255;
	
                _loc_11 = _loc_11 + chr(_loc_21 >> 0 & 255);
                _loc_11 = _loc_11 + chr(_loc_21 >> 8 & 255);
                _loc_11 = _loc_11 + chr(_loc_21 >> 16 & 255);
                _loc_11 = _loc_11 + chr(_loc_21 >> 24 & 255);
                _loc_11 = _loc_11 + chr(_loc_22 >> 0 & 255);
                _loc_11 = _loc_11 + chr(_loc_22 >> 8 & 255);
                _loc_11 = _loc_11 + chr(_loc_22 >> 16 & 255);
                _loc_11 = _loc_11 + chr(_loc_22 >> 24 & 255);
                _loc_12 = _loc_12 + _loc_3;
            
            _loc_11 = _loc_11 + ''.join(param1[8:16]);
            return _loc_11;
 
def add(param1, param2) : 
        
            _loc_3 = 0;
            param1 = list(  param1 ) 
            while (_loc_3 < param2):
                
                param1 .append( chr(0));
                _loc_3 = _loc_3 + 1;
            
            return param1;
        


def time2String(param1) : 
        
            _loc_8 = 0;
            _loc_2 = list('12345678')
            _loc_3= '';
            _loc_4 = "0123456789abcdef";
            _loc_5 = list("0123456789abcdef")
            _loc_6 = 0;
            while (_loc_6 < 8):
            
                
                _loc_8 = param1 >> 28 - _loc_6 % 8 * 4 & 15;
                _loc_2[_loc_6] = _loc_5[_loc_8];
                _loc_6 = _loc_6 + 1;

            _loc_2 = ''.join(_loc_2)            
   
            return _loc_2

def Str2Hex(param1) : 
        
            _loc_7 = 0;
            _loc_8 = 0;
            _loc_2  = list("0123456789abcdef");
            _loc_3 = _loc_2;
            _loc_4 = param1;
            _loc_5 = list('%*s' % ((2 * len(_loc_4) ),''));
            
            _loc_6 = len(_loc_4);
            _loc_9 = 0;
            while (_loc_9 < _loc_6):
            
                
                if (_loc_9 < 8):
                
                    _loc_7 = ord(_loc_4[_loc_9]) & 15;
                    _loc_8 = ord(_loc_4[_loc_9]) >> 4 & 15;
                    _loc_5[2 * _loc_9] = _loc_3[ord(_loc_4[_loc_9]) & 15];
                    _loc_5[2 * _loc_9 + 1] = _loc_3[ ord(_loc_4[_loc_9]) >> 4 & 15];
                
                else:
                
                    _loc_5[2 * _loc_9] = _loc_3[random.randint(0,15)];
                    _loc_5[2 * _loc_9 + 1] = _loc_3[random.randint(0,15)];
                
                _loc_9+=1;
            
            return ''.join(_loc_5);

def constructKey(param1) :
        
            _loc_2 = time2String(param1);
            _loc_3 = _loc_2;
            if len(_loc_3)< 16:
            
                _loc_2 = add(_loc_2, 16 - len(_loc_3));
            
            _loc_4 = "";
            _loc_5 = SERVER_KEY;
            if len(SERVER_KEY) < 16:
            
                _loc_5 = add(_loc_5, 16 - len(_loc_5));

 
            _loc_4 = encrypt(_loc_2, _loc_5);
            
            _loc_4 = Str2Hex(_loc_4);
            return _loc_4;

def getplaykey(s):

	s = s[4: -4]
	d = datetime.datetime.strptime(s,'%b %d %H:%M:%S %Y')
	d = int( time.mktime(d.timetuple())) - 60 -14400 

	return constructKey (d)


