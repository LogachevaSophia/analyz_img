#1. пользователь вызывает раскадровку видео - это фалй frame.py, параметры - путь к файлу
#2. Вызываем функцию раскадровки, matrix.py, параметры - точки (можно не отсортированные) и путь к файлу, по которому должна построиться матрица, 
# функция возвращает матрицу гомографии 


#тестовые данные для book2.js - p = [(197, 240), (389, 169), (368, 428), (601, 325)]
import os
import matrix;
import frame_modify

def main(p,f):
    global M, M, H
    #строим матрицу гомографии 
    a = matrix.perspective(, f);
    M = a['M']
    H = a['H']
    W = a['W'] 
    directory = 'source/frames/new'
    i = 0;
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            frame_modify.modify(M, f, W,H,'source/frames/modify/frame'+str(i)+'.jpg')
            i+=1;
            print(f[len('source/frames/new')+1:])
    

    
       
    
    
M = []
H = 0;
W = 0;
main([(197, 240), (389, 169), (368, 428), (601, 325)],'forAnastasia/frame.jpg')
