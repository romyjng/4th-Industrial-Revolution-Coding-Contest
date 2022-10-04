#무작위 음식 추천을 위해 random 함수 호출
import random
# 음식목록, 폐기물 목록이 있는 메모장과 연동
# 식단목록의 저장 위치를 입력하면 파일 읽음
a = input("식단파일의 주소를 입력하세요:")
myfile = str(a+'/식단목록.txt')
# 파일 읽기
start=open(myfile,'r')
# 한식, 일식, 중식, 양식, 분식 빈 리스트 생성
korean=list()
korwst=list()

japanese=list()
japwst=list()

chinese=list()
chiwst=list()

western=list()
weswst=list()

street=list()
strwst=list()

# csv파일을 메모장으로 변경한거라 , 기준으로 구분하여 값의 특정위치가 해당 음식 카테고리에 속한다면 값을 리스트에 추가
for i in start:
    value=i.split(',')
    if value==[]:
        break
    if value[3]=='한식':
        korean.append(value[1])
        korwst.append(value[7])
    elif value[3]=='일식':
        japanese.append(value[1])
        japwst.append(value[7])
    elif value[3]=='중식':
        chinese.append(value[1])
        chiwst.append(value[7])
    elif value[3]=='양식':
        western.append(value[1])
        weswst.append(value[7])
    elif value[3]=='분식/야식':
        street.append(value[1])
        strwst.append(value[7])

# tkinter를 통해 프로그램 창 생성
import tkinter as tk
from tkinter import simpledialog
import tkinter.font
# tkinter의 제목, 창크기 설정
application_window = tk.Tk()
application_window.geometry("700x800")
application_window.title('Eco Delivery Food Guide')
# tkinter의 폰트 종류 설정
font1=tkinter.font.Font(family="Verdana", size=20)
font2=tkinter.font.Font(family="Helvetica", size=12)
# 중앙 라벨링 (글씨색: 초록, font1적용)
label = tk.Label(application_window, text = 'Eco Delivery Food Guide',
                 fg="green", font=font1)
# 중앙 라벨 위치 설정
label.grid(row=0, column=1, padx=5, pady=5)
# v 문자열 변수 설정
v = tk.StringVar()
# sel()함수: 
# 1) 문자열변수 값이 특정 음식 카테고리에 속하면 그 음식과 폐기물을 x, y에 할당
def sel():
    if v.get()=='한식':
        x=korean
        y=korwst
    elif v.get()=='일식':
        x=japanese
        y=japwst
    elif v.get()=='중식':
        x=chinese
        y=chiwst
    elif v.get()=='양식':
        x=western
        y=weswst
    elif v.get()=='분식/야식':
        x=street
        y=strwst
# x 즉, 음식들의 갯수만큼 랜덤으로 선출하여 abbox, bbbox (랜덤값이 나오는 창(Entry))에 표현    
    aa= len(x)
    randomn = random.randrange(aa)
    abbox.delete(0,tk.END)
    abbox.insert(0,x[randomn])
    bbbox.delete(0,tk.END)
    bbbox.insert(0,y[randomn])
#2) 각 폐기물별 가이드라인들을 입력   
    plastic = '''내용물을 깨끗이 비우고 헹궈줍니다. 
플라스틱과 다른 재질은 제거합니다. 
만약 제거가 어려운 경우 종량제봉투에 담아줍니다. 
투명과 유색을 분리해 지정된 배출함에 넣습니다.'''
    vinyl = '''내용물을 깨끗이 비우고 헹궈줍니다.
흩날리지 않도록 봉투에 담아 배출합니다.
음식물이 묻은 비닐은 종량제 봉투에 넣습니다.'''
    styrofoam = '''내용물을 깨끗이 비우고 헹궈줍니다.
스티로폼과 다른 재질은 제거합니다.
이물질을 제거하기 어려운 경우 종량제 봉투에 담아줍니다.
유색인 경우 종량제 봉투에 담아 줍니다.'''
    ppack = '''내용물을 비우고 헹궈 말린 후 배출합니다.
종이팩과 다른 재질은 제거합니다.
일반 종이류와 분리하여 종이팩 전용수거함에 배출합니다.
종이팩 전용수거함이 없는 경우엔 종이류와 구분할 수 있도록 끈으로 
묶어 종이류 수거함으로 배출합니다.'''
    paper = '''종이가 코팅되어 있다면 종량제 봉투에 넣어줍니다.'''
    seafood = '''음식물쓰레기가 아닌 종량제 봉투에 넣어줍니다.'''
    bone = '''음식물쓰레기가 아닌 종량제 봉투에 넣어줍니다.'''
    etc ='''나무젓가락, 영수증은 종량제 봉투에 넣어줍니다.'''
# 랜덤값에 특정 폐기물이 포함된다면 가이드라인들을 창에 표현
    if "플라스틱" in y[randomn]:
        T1.insert(tk.END, plastic)
    if "비닐" in y[randomn]:
        T2.insert(tk.END, vinyl)
    if "스티로폼" in y[randomn]:
        T3.insert(tk.END, styrofoam)
    if "종이팩" in y[randomn]:
        T4.insert(tk.END, ppack)
    if "종이류" in y[randomn]:
        T5.insert(tk.END, paper)
    if "어패류" in y[randomn]:
        T6.insert(tk.END, seafood)
    if "뼈" in y[randomn]:
        T7.insert(tk.END, bone)
    T8.insert(tk.END, etc)
        
    return
# 클릭할때마다 업데이트될 수 있도록 기존 입력값을 삭제
def clickme():
    T1.delete("1.0", "end")
    T2.delete("1.0", "end")
    T3.delete("1.0", "end")
    T4.delete("1.0", "end")
    T5.delete("1.0", "end")
    T6.delete("1.0", "end")
    T7.delete("1.0", "end")
    T8.delete("1.0", "end")

# 음식 선택 라벨 설정, font2 적용 
sublabel = tk.Label(application_window, text = "Select the type of food:",
                   font=font2)
# 음식 선택 라벨 위치 설정
sublabel.grid(row=1, column=0, padx=5, pady=5)
# 음식 카테고리 선택 버튼(단일)설정 
tk.Radiobutton(application_window,
               text='한식', variable=v, value='한식').grid(row=2,column=0)
tk.Radiobutton(application_window,
               text='일식', variable=v, value='일식').grid(row=3,column=0)
tk.Radiobutton(application_window,
               text='중식', variable=v, value='중식').grid(row=4,column=0)
tk.Radiobutton(application_window,
               text='양식', variable=v, value='양식').grid(row=5,column=0)
tk.Radiobutton(application_window,
               text='분식/야식', variable=v, value='분식/야식').grid(row=6,column=0)
# select 버튼 설정, 명령어는 clickme -> sel 함수 (삭제 후 기입)
button = tk.Button(application_window, text='select',
                   bg='green', fg='white',command=lambda:[clickme(),sel()])
button.grid(row=6, column=2, sticky=tk.E + tk.W)
# 추천 및 폐기물 라벨 설정 및 가이드 라인 라벨 설정
sublabel_2 = tk.Label(application_window, text='>>> 추천')
sublabel_2.grid(row =2, column =1, padx = 5, pady = 5)
sublabel_3 = tk.Label(application_window, text='>>> 폐기물')
sublabel_3.grid(row =3, column =1, padx = 5, pady = 5)
sublabel_4 = tk.Label(application_window, text='>>> Guide <<<',
                      fg='green', font=font2)
sublabel_4.grid(row =10, column =1, padx =5, pady= 5)
sublabel_5 = tk.Label(application_window, text='플라스틱')
sublabel_5.grid(row =12, column =1, padx =5, pady= 5)
sublabel_6 = tk.Label(application_window, text='비닐')
sublabel_6.grid(row =17, column =1, padx =5, pady= 5)
sublabel_7 = tk.Label(application_window, text='스티로폼')
sublabel_7.grid(row =20, column =1, padx =5, pady= 5)
sublabel_8 = tk.Label(application_window, text='종이팩')
sublabel_8.grid(row =25, column =1, padx =5, pady= 5)
sublabel_9 = tk.Label(application_window, text='종이류')
sublabel_9.grid(row =31, column =1, padx =5, pady= 5)
sublabel_10 = tk.Label(application_window, text='어패류')
sublabel_10.grid(row =33, column =1, padx =5, pady= 5)
sublabel_11 = tk.Label(application_window, text='뼈')
sublabel_11.grid(row =35, column =1, padx =5, pady= 5)
sublabel_12 = tk.Label(application_window, text='기타')
sublabel_12.grid(row =37, column =1, padx =5, pady= 5)
# 가이드라인 텍스트 창 설정(문자열 변수인식)
T1 = tk.StringVar()
T1 = tk.Text(height = 4, width = 50)
T1.grid(row=13, column=1)

T2 = tk.StringVar()
T2 = tk.Text(height = 2, width = 50)
T2.grid(row=18, column=1)

T3 = tk.StringVar()
T3 = tk.Text(height = 4, width = 50)
T3.grid(row=21, column=1)

T4 = tk.StringVar()
T4 = tk.Text(height = 5, width = 50)
T4.grid(row=26, column=1)

T5 = tk.StringVar()
T5 = tk.Text(height = 1, width = 50)
T5.grid(row=32, column=1)

T6 = tk.StringVar()
T6 = tk.Text(height = 1, width = 50)
T6.grid(row=34, column=1)

T7 = tk.StringVar()
T7 = tk.Text(height = 1, width = 50)
T7.grid(row=36, column=1)

T8 = tk.StringVar()
T8 = tk.Text(height = 1, width = 50)
T8.grid(row=38, column=1)
# 랜덤 값이 나오는 창(Entry) 설정
abtext = tk.StringVar()
abtext.set('')
abbox = tk.Entry(application_window, textvariable=abtext)
abbox.grid(row=2, column=2, padx=5, pady=5)

bbtext = tk.StringVar()
bbtext.set('')
bbbox = tk.Entry(application_window, textvariable=bbtext)
bbbox.grid(row =3, column =2, padx =5, pady =5)

# 메인 실행
application_window.mainloop()
