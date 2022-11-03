import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['a','b','c','d']
    values = [200,203,400,450]

    fig,ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png')
    plt.close()