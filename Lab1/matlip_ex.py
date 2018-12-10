from matplotlib import pyplot

#1 Chuẩn bị data
machine_counts = [18 ,4 ,2]


#2 Chuẩn bị labels
machine_name = ["PC", "MAC", "Linux"]

#3 Vẽ hình
pyplot.pie(machine_counts , labels=machine_name,autopct="%.1f%%",explode=[0,0.2,0])
pyplot.title("PC MAC and LINUX")
pyplot.axis("equal")
#4 hiển thị
pyplot.show()