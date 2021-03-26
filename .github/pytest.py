# uses crt;
# var a,b:string;
#      i:byte;
# begin
# clrscr;
# writeln('Введите строку А:');
# readln(a);
# writeln('Введите строку B:');
# readln(b);
# {если есть пара одинаковых букв, то удалаем их из обеих строк}
# for i:=length(b) downto 1 do
# if pos(b[i],a)>0 then
#  begin
#   delete(a,pos(b[i],a),1);
#   delete(b,i,1);
#  end;
# if b='' then write('Можно'){если из второй удалили все, значит можно}
# else write('Нельзя');
# readln
# end.
def wordgen(mstr,mstr1):
    for i  in mstr[::-1]:
        print(i)
    
if __name__ == '__main__':
    mstr=input()
    mstr1=input()
    wordgen(mstr,mstr1)
    
    