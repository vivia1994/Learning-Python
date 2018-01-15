# 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
from pylab import *
import numpy as np

def plot_Primary1():
    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)
    plot(X,C, color="blue", linewidth=2.5, linestyle="-")
    plot(X,S, color="red",  linewidth=2.5, linestyle="-")
    show()

def plot_Primary2():
    # 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
    figure(figsize=(8, 6), dpi=80)

    # 创建一个新的 1 * 1 的子图，接下来的图样绘制在其中的第 1 块（也是唯一的一块）
    subplot(1, 1, 1)

    X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    C, S = np.cos(X), np.sin(X)

    # 绘制余弦曲线，使用蓝色的、连续的、宽度为 1 （像素）的线条
    plot(X, C, color="blue", linewidth=2.5, linestyle="-")

    # 绘制正弦曲线，使用绿色的、连续的、宽度为 1 （像素）的线条
    plot(X, S, color="green", linewidth=2.5, linestyle="-")

    # 设置横轴的上下限
    xlim(-4.0, 4.0)

    # 设置横轴记号
    # xticks(np.linspace(-4, 4, 9, endpoint=True))
    # 使用了LaTeX
    xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    # 设置纵轴的上下限
    ylim(-1.0, 1.0)

    # 设置纵轴记号
    # yticks(np.linspace(-1, 1, 5, endpoint=True))
    yticks([-1, 0, +1],
           [r'$-1$', r'$0$', r'$+1$'])

    # 以分辨率 72 来保存图片
    # savefig("exercice_2.png",dpi=72)

    # 移动脊柱
    ax = gca()
    ax.spines['right'].set_color('green')
    ax.spines['top'].set_color('green')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    # 添加图例
    plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cos")
    plot(X, S, color="red", linewidth=2.5, linestyle="-", label="sin")
    legend(loc='upper left')

    # 在 2π/32π/3 的位置给两条函数曲线加上一个注释。首先，我们在对应的函数图像位置上画一个点；
    # 然后，向横轴引一条垂线，以虚线标记；最后，写上标签。
    t = 2 * np.pi / 3
    plot([t,t ], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
    scatter([t, ], [np.cos(t), ], 50, color='blue') #标注了一个点
    annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    print(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$')
    plot([t, t], [0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
    scatter([t, ], [np.sin(t), ], 50, color='red')
    annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    # 在屏幕上显示
    show()

#散点图
def ScatterPlot():
    n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    T = np.arctan2(Y, X)
    # axes([0.025, 0.025, 0.95, 0.95])
    # scatter(X, Y, s=20, c=T, alpha=.5)
    scatter(X, Y, s=20, c=T)
    xlim(-1.5, 1.5), plt.xticks([])
    ylim(-1.5, 1.5), plt.yticks([])
    # savefig('../figures/scatter_ex.png',dpi=48)
    show()


#3D
def ThreeDPlot():
    from mpl_toolkits.mplot3d import Axes3D

    fig = figure()
    ax = Axes3D(fig)
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
    ax.contourf(X, Y, Z, zdir='z', offset=-2)
    ax.set_zlim(-2, 2)
    show()

# plot_Primary1()
# plot_Primary2()
# ScatterPlot()
ThreeDPlot()
