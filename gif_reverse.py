from PIL import Image, ImageSequence

save_frames = False

def save_frames(iter):
    # separate each frame
    for index, frame in enumerate(iter):
        print("image %d: mode %s, size %s" % (index, frame.mode, frame.size))
        frame.save('./imgs/frame%d.png' % index)


if __name__ == '__main__':
    im = Image.open('origin.gif')
    iter = ImageSequence.Iterator(im)
    if save_frames:
        save_frames(iter)
    imgs = [frame.copy() for frame in ImageSequence.Iterator(im)]
    imgs.reverse()
    imgs[0].save('reversed.gif', save_all=True, append_images=imgs[1:])
