import matplotlib.pyplot as plt
from random_walks import RandomWalk

# keep making random walks while program runs
while True:
    # making a random walk
    rw = RandomWalk()
    rw.fill_walks()

    # plotting graph
    plt.style.use('classic')
    plt.title('Random Walks', fontsize=25)
    plt.xlabel('left/right')
    plt.ylabel('up/down')

    point_numbers = range(rw.walk_points)
    plt.scatter(rw.x_axis, rw.y_axis, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=18)

    # highlighting start and end points
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_axis[-1], rw.y_axis[-1], c='blue', edgecolors='none', s=50)


    keep_running = input('Do you want to make a new walk (y/n)? ')
    if keep_running == 'y':
        plt.show()
    elif keep_running == 'n':
        break
    else:
        print("Please enter either 'y' or 'n'")
        pass
