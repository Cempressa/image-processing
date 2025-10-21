import matplotlib.pyplot as plt


def plot_image(image):
    plt.figure(figsize=(12, 4))
    plt.imshow(image, cmap="gray")
    plt.axis("off")
    plt.show()


def plot_result(*args):
    number_images = len(args)
    fig, axis = plt.subplots(nrows=1, ncols=number_images, figsize=(12, 4))
    names_lst.append("Result")
    # = ["image {}".format(i) for i in range(number_images)]

    # if number_images == 1:
    #    axis = [axis]

    for ax, name, image in zip(axis, names_lst, args):
        ax.imshow(image, cmap="gray")
        ax.set_title(name)
        ax.axis("off")

    # Correção: tight_layout
    fig.tight_layout()
    plt.show()


def plot_histogram(image):
    # Correção: Corrigida a sintaxe do subplots
    fig, axis = plt.subplots(
        nrows=1, ncols=3, figsize=(12, 4), sharex=True, sharey=True
    )

    color_lst = ["red", "green", "blue"]

    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.hist(image[:, :, index].ravel(), bins=256, color=color, alpha=0.8)
        ax.set_title("{} histogram".format(color.title()))

    # Correção: tight_layout
    fig.tight_layout()
    plt.show()
