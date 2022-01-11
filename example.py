from create_permutation_gif import animate_permutations

if __name__=='__main__':
  permutations = [
    [2, 3, 4, 1, 0],
  ]
  imgs = animate_permutations(permutations, ["red", "blue", "yellow", "green", "purple"], ["1", "2", "3", "4", "5"], (500, 250), 30, 50, 20)
  imgs[0].save('examples/example_1.gif', save_all=True, append_images=imgs[1:], loop=0, duration=50)

  permutations = [
    [0, 3, 2, 1, 4],
    [2, 1, 4, 3, 0],
  ]
  imgs = animate_permutations(permutations, ["red", "blue", "yellow", "green", "purple"], ["1", "2", "3", "4", "5"], (500, 250), 30, 50, 20)
  imgs[0].save('examples/example_2.gif', save_all=True, append_images=imgs[1:], loop=0, duration=50)

  permutations = [
    [0, 3, 2, 1, 4],
    [0, 1, 4, 3, 2],
    [2, 1, 0, 3, 4],
  ]
  imgs = animate_permutations(permutations, ["red", "blue", "yellow", "green", "purple"], ["1", "2", "3", "4", "5"], (500, 250), 30, 50, 20)
  imgs[0].save('examples/example_3.gif', save_all=True, append_images=imgs[1:], loop=0, duration=50)
