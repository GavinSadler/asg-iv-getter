function RangeLetter=ProperRange(index)
% index = 65 -> RangeLetter=A;
Counter=0;
if index<65
    index=index+64;
end
while index>90
    index=index-26;
    Counter=Counter+1;
end
if Counter>0
    RangeLetter=char(64+Counter);
else
    RangeLetter='';
end
RangeLetter=[RangeLetter,char(index)];