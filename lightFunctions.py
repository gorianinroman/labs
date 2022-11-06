from tkinter import PhotoImage
import numpy as np
import matplotlib.pyplot as plt
import imageio
from cycler import cycler

def readIntensity(photoName, plotName, lamp, surface):
    photo = imageio.v3.imread(photoName)
    background = photo[350:635, 850:960, 0:3].swapaxes(0, 1)
    
    cut = photo[350:635, 850:960, 0:3].swapaxes(0, 1)
    rgb = abs(np.mean(cut, axis=(0)) - 25)
    luma = (0.2989 * rgb[:, 0] + 0.5866 * rgb[:, 1] + 0.1144 * rgb[:, 2])

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig = plt.figure(figsize=(10, 5), dpi=200)

    plt.title('Интенсивность отражённого излучения\n' + '{} / {}'.format(lamp, surface))
    plt.xlabel('Относительный номер пикселя')
    plt.ylabel('Яркость')

    plt.plot(rgb, label=['r', 'g', 'b'])
    plt.plot(luma, 'y', label='I')
    plt.legend(prop={'size': 8})

    plt.savefig(plotName + 'without background')

    plt.imshow(background, origin='lower')
    
    plt.savefig(plotName)

    plt.close()

    return luma

luma_mercury = readIntensity('mercury_on_white_list.jpg','white-mercury', 'Ртутная лампа', 'Белый лист')
luma_mercury_array = []
for i in range(len(luma_mercury)):
    luma_mercury_array.append(luma_mercury[i])

luma_green_max = 0;
luma_red_max = 0;
pixcel_green_max = 0;
pixcel_red_max = 0;

for pixcel in range(125, 175):
    if (luma_mercury_array[pixcel] > luma_green_max):
        luma_green_max = luma_mercury_array[pixcel];
        pixcel_green_max = pixcel;

for pixcel in range(200, 250):
    if (luma_mercury_array[pixcel] > luma_red_max):
        luma_red_max = luma_mercury_array[pixcel];
        pixcel_red_max = pixcel;

delta_p = pixcel_red_max - pixcel_green_max;
delta_L = 611 - 546
L_p = round(delta_L / delta_p, 2);

with open("calibration.txt", "w") as outfile:
    str_1 = str(L_p) +  ' нМ на пиксель \n'
    str_2 = '546 нМ в пикселе ' + str(pixcel_green_max) + '\n'
    str_3 = 'L(n) = 546 - (' + str(pixcel_green_max) + ' - n) * ' + str(L_p)
    outfile.write(str_1)
    outfile.write(str_2)
    outfile.write(str_3)
    

length_array = []
for pixcel in range(len(luma_mercury_array)):
    length_array.append(546 - (pixcel_green_max - pixcel) * (L_p))

luma_white = (readIntensity('incandescent_on_white_list.jpg','white-incandescent', 'Лампа накаливания', 'Белый лист'))
luma_white_array = []
for i in range(len(luma_white)):
    luma_white_array.append(luma_white[i])

luma_yellow = (readIntensity('incandescent_on_yellow_list.jpg','yellow-incandescent', 'Лампа накаливания', 'Жёлтый лист'))
luma_yellow_array = []
for i in range(len(luma_yellow)):
    luma_yellow_array.append(luma_yellow[i])
     
luma_green = (readIntensity('incandescent_on_green_list.jpg','green-incandescent', 'Лампа накаливания', 'Зелёный лист'))
luma_green_array = []
for i in range(len(luma_green)):
    luma_green_array.append(luma_green[i])

luma_blue = (readIntensity('incandescent_on_blue_list.jpg','blue-incandescent', 'Лампа накаливания', 'Синий лист'))
luma_blue_array = []
for i in range(len(luma_blue)):
    luma_blue_array.append(luma_blue[i])

luma_red = (readIntensity('incandescent_on_red_list.jpg','red-incandescent', 'Лампа накаливания', 'Красный лист'))
luma_red_array = []
for i in range(len(luma_red)):
    luma_red_array.append(luma_red[i])

    plt.close()

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig, ax = plt.subplots()

    plt.title('Отражённая интенсивность излучения лампы накаливания')
    plt.xlabel('Длина волны, [нм]')
    plt.ylabel('Яркость')
    ax.set(facecolor = 'grey')
    plt.plot(length_array, luma_white, color='white', label=['белый лист'])
    plt.plot(length_array, luma_yellow, color='yellow', label=['жёлтый лист'])
    plt.plot(length_array, luma_green, color='green', label=['зелёный лист'])
    plt.plot(length_array, luma_blue, color='blue', label=['синий лист'])
    plt.plot(length_array, luma_red, color='red', label=['красный лист'])
    plt.grid()
    plt.legend(prop={'size': 8})
    plt.savefig('! intensites')

    plt.close()

    albedo_white = []
    albedo_yellow = []
    albedo_green = []
    albedo_blue = []
    albedo_red = []

    for i in range(len(luma_white)):
        albedo_white.append(1)

    for i in range(len(luma_yellow)):
        if luma_white[i] == 0 or luma_yellow[i] < 0.05:
            albedo_yellow.append(0)
        else:
            albedo_yellow.append(luma_yellow[i]/luma_white[i])

    for i in range(len(luma_green)):
        if luma_white[i] == 0 or luma_green[i] < 0.05:
            albedo_green.append(0)
        else:
            albedo_green.append(luma_green[i]/luma_white[i])

    for i in range(len(luma_blue)):
        if luma_white[i] == 0 or luma_blue[i] < 0.05:
            albedo_blue.append(0)
        else:
            albedo_blue.append(luma_blue[i]/luma_white[i])

    for i in range(len(luma_red)):
        if luma_white[i] == 0 or luma_red[i] < 0.05:
            albedo_red.append(0)
        else:
            albedo_red.append(luma_red[i]/luma_white[i])

    plt.rc('axes', prop_cycle=(cycler('color', ['r', 'g', 'b'])))

    fig, ax = plt.subplots()

    plt.title('Альбедо поверхностей')
    plt.xlabel('Длина волны, [нм]')
    plt.ylabel('Альбедо')
    ax.set(facecolor = 'grey')
    plt.plot(length_array, albedo_white, color='white', label=['белый лист'])
    plt.plot(length_array, albedo_yellow, color='yellow', label=['жёлтый лист'])
    plt.plot(length_array, albedo_green, color='green', label=['зелёный лист'])
    plt.plot(length_array, albedo_blue, color='blue', label=['синий лист'])
    plt.plot(length_array, albedo_red, color='red', label=['красный лист'])
    plt.grid()
    plt.legend(loc='upper left', prop={'size': 8})
    plt.savefig('! albedos')

    exit()