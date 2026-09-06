import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

def number_1(array):
    idx_null = np.where(array == 0)[0]

    if idx_null.size == 0:
        print("Нет нулевых элементов.")
    else:
        idx_null = idx_null + 1
        if idx_null.max() > array.shape[0]-1:
            idx_null = np.delete(idx_null,len(idx_null)-1)
        result = array[idx_null]
        return np.max(result)

def number_2(x,value):
    x_deviation = abs(x - value)
    min_idx = np.argmin(x_deviation)
    return x.flat[min_idx]

def fun(x):
    # код этой функции изменять нельзя
    return np.sum(x, axis=1) + np.trace(x @ x.T)

def number_3(data):
    n = data.shape[0]
    m = data.shape[1]
    k = data.shape[2]
    p = n*m
    data_dvumer =  data.reshape(p,k)
    result = fun(data_dvumer)
    result = result.reshape(n,m)
    return result

def number_4(matrix,n,d):
    # matrix_form1 = matrix.reshape(n,1,d)
    # matrix_form2 = matrix.reshape(1,n,d)
    # return np.sqrt(np.sum((np.square(matrix_form1 - matrix_form2)),axis = 2)) но на всякий сделаю через np.newaxis
    diff = matrix[:,np.newaxis,:] - matrix[np.newaxis,:,:]
    return np.sqrt(np.sum(np.square(diff),axis = 2))

def number_5(df):
    male_count = df['Sex'].value_counts()['male']
    print("Кол-во мужчин : ",male_count)
    female_count = df['Sex'].value_counts()['female']
    print("Кол-во женщин : ",female_count,"\n")
    print(df['Pclass'].value_counts().to_string(),"\n") #to_string чтобы вывести без последней строки dtype
    print("Минимальный возраст пассажиров :",df['Age'].min())
    print("Средний возраст пассажиров :",df['Age'].mean())
    print("Максимальный возраст пассажиров :",df['Age'].max(),"\n")
    print("Количество выживших :",df['Survived'].value_counts()[1],"\n")

def number_8(x):
    return np.sin(x) + np.log(x)

print("ЗАДАНИЕ №1 : Реализуйте функцию, возвращающую максимальный элемент в массиве X среди элементов, перед которыми стоит нулевой.")
print("ЗАДАНИЕ №2 : Реализуйте функцию, принимающую на вход матрицу X и некоторое число value и возвращающую ближайший к числу элемент матрицы.")
print("ЗАДАНИЕ №3 : Дана функция, обрабатывающая список объектов формы (p, k). А у вас есть матрица (n,m,k) Вычислите функцию относительно этой матрицы. Код функции менять нельзя, нужно преобразовать матрицу. Результат должен быть формы (n,m).")
print("ЗАДАНИЕ №4 : У вас есть массив точек в виде матрицы размерности (n, d), n количество точек, d размерность каждой точки. Вычислите попарные расстояние между всеми точками матрицу (n,n). Используется евклидово расстояние. Попробуйте воспользоваться трюком с расширением размерности матрицы.")
print("ЗАДАНИЕ №5 : Опишите данный набор данных: какое распределение женщин/мужчин в нем? Сколько пассажиров ехало в каждом классе? Какой средний/минимальный/максимальный возраст пассажиров? Сколько было выживших пассажиров?")
print("ЗАДАНИЕ №6 : Сгруппируйте записи по классам пассажиров, в каждой группе посчитайте средний возраст. Верно ли, что во всех классах эта величина примерно одинакова?")
print("ЗАДАНИЕ №7 : Вам даны два набора точек в двумерном пространстве. Найдите центры масс этих наборов, соедините их прямой, постройте срединный перпендикуляр. Постройте проекции точек на срединный перпендикуляр. Подпишите координаты центров наборов точек.\n")
while True:
    try:
        number_task = int(input("Введите номер задания(1 - 8) или 0,чтобы выйти : "))
        if number_task < 0 or number_task > 8:
            print("Попробуйте ещё раз. Вводите цифру от 1 до 8 или 0 для выхода.\n")
            continue
        if number_task == 0:
            break
        elif number_task == 1 :
            my_list = [0,1,0,3,1,0,5,6,0,7,8,9,0]
            array = np.array(my_list, dtype = np.int32)
            print("Массив: ",array,"\n")
            print(number_1(array),"\n\n")
        elif number_task == 2 :
            x = np.array([[-10000,-500,-5],[0,10,100],[1000,10000,67]])
            print("Матрица X:\n", x,"\n")
            while True:
                try:
                    value = int(input("Введите число:"))
                    print(number_2(x,value),"\n\n")
                    break
                except(ValueError):
                    print("Ошибка! Нужно ввести целое число.")
        elif number_task == 3 :
            data = np.random.normal(0, 5, size=(2,2,3))
            print(number_3(data),"\n\n")
        elif number_task == 4 :
            while True:
                try:
                    n = int(input("n = "))
                    d = int(input("d = "))
                    break
                except(ValueError):
                    print("Ошибка! Нужно ввести целое число.")
            matrix = np.random.rand(n,d)
            print(matrix,"\n")
            print(number_4(matrix,n,d),"\n\n")
        elif number_task == 5 :
            df = pd.read_csv("titanic.csv", sep="\t")
            number_5(df)
        elif number_task == 6 :
            df = pd.read_csv("titanic.csv", sep="\t")
            print("Средний возраст в группах :")
            print(df.groupby('Pclass')['Age'].mean(),"\n")
            print("ОТВЕТ : Нет, средний возраст разный во всех группах.","\n\n")
        elif number_task == 7 :
            fig = plt.figure()
            X1 = np.random.multivariate_normal([4,4],[[0.1,-0.4],[-0.4,3]], size = 10)
            plt.scatter(X1[:,0], X1[:,1])
            X2 = np.random.multivariate_normal([8,4],[[0.2,0.4],[0.4,1]], size = 10)
            plt.scatter(X2[:,0], X2[:,1])

            center_1 = np.mean(X1,axis=0)
            center_2 = np.mean(X2,axis=0)
            plt.scatter(center_1[0],center_1[1],marker = 'x',color = 'blue',s = 100,label = 'Центр X1')
            plt.scatter(center_2[0],center_2[1],marker = 'x',color = 'red',s = 100,label = 'Центр X2')

            center_x = (center_1[0] + center_2[0])/2
            center_y = (center_1[1] + center_2[1])/2
            plt.scatter(center_x,center_y,marker = 'x',color = 'pink',s = 100,label = 'Центр X1X2')

            vx=center_2[0] - center_1[0] # направление вектора X1X2 = (Vx,Vy) -> направление перпендикуляра = (-Vx,Vy)
            vy=center_2[1] - center_1[1]
            px=-vy
            py=vx
            scale = 20 #длина линии
            plt.plot([center_x - px*scale,center_x + px*scale],[center_y - py*scale,center_y + py*scale],color = 'green', label = 'Серединный перпендикуляр', linewidth = 3)
            plt.plot([center_1[0],center_2[0]],[center_1[1],center_2[1]],color = 'yellow',linewidth = 3)

            center = np.array([center_x,center_y]) #центр отрезка
            d=np.array([px,py]) #направление зеленого перпендикуляра

            vector_1 = X1 - center
            dot_vector_d = np.dot(vector_1,d)
            dot_d_d = np.dot(d,d) #для нормализации, так как без этого t будет зависеть от длины d
            t = dot_vector_d / dot_d_d
            projections = center + t[:,np.newaxis] * d
            for i in range(len(X1)):
                plt.plot([projections[i,0],X1[i,0]],[projections[i,1],X1[i,1]],color = 'brown')
            vector_2 = X2 - center
            dot_vector_d2=np.dot(vector_2,d)
            t = dot_vector_d2 / dot_d_d
            projections = center + t[:,np.newaxis] * d
            for i in range(len(X2)):
                plt.plot([projections[i,0],X2[i,0]],[projections[i,1],X2[i,1]],color = 'brown')

            #plt.text(center_1[0],center_1[1],'Центр X1') но это перекрывает сами метки точек
            #plt.text(center_2[0],center_2[1],'Центр X2')
            plt.annotate('Центр X1',xy=(center_1[0],center_1[1]),xytext=(-50,8),textcoords='offset points')
            plt.annotate('Центр X2',xy=(center_2[0],center_2[1]),xytext=(8,8),textcoords='offset points')

            plt.legend()
            plt.axis('equal')
            plt.title('ЗАДАНИЕ №7')
            plt.show()
        elif number_task == 8 :
            sizes = np.logspace(1,18,num = 19, base = 2, dtype = int)
            times_1 = []
            times_2 = []
            times_3 = []
            vec = np.vectorize(number_8) # так как время на создание векторизованной ф-ии мы не замеряем + вынес за цикл чтобы не тратить время
            for n in sizes:
                test_massiv = np.ones(n) * 5
                #Обычный цикл
                start = time.perf_counter()
                res1 = [number_8(x) for x in test_massiv]
                time1=time.perf_counter() - start
                times_1.append(time1)
                #np.vectorize
                start = time.perf_counter()
                res2 = vec(test_massiv)
                time2 = time.perf_counter() - start
                times_2.append(time2)
                #numpy
                start = time.perf_counter()
                res3 = number_8(test_massiv)
                time3 = time.perf_counter() - start
                times_3.append(time3)
            plt.figure(figsize=(10, 6))
            plt.plot(sizes, times_1, label='Обычный цикл')
            plt.plot(sizes, times_2, label='np.vectorize')
            plt.plot(sizes, times_3, label='Векторизованный NumPy')
            plt.xscale('log')
            plt.yscale('log')
            plt.xlabel('Размер массива')
            plt.ylabel('Время выполнения')
            plt.title('ЗАДАНИЕ №8 : Сравнение производительности поэлементного применения функции')
            plt.legend()
            plt.show()
    except(ValueError):
        print("Попробуйте ещё раз. Вводите цифру от 1 до 8 или 0 для выхода.\n")
