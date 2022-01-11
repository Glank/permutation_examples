from PIL import Image, ImageDraw, ImageFont

def get_frame(colors, labels, destinations, img_size, radius, t):
  im = Image.new('RGB', img_size, (255, 255, 255))
  draw = ImageDraw.Draw(im)
  for i, c in enumerate(colors):
    transition = None
    dest = destinations[i]
    if dest > i:
      transition = 'over'
    elif dest < i:
      transition = 'under'
    draw_circle(draw, c, labels[i], radius, len(colors), img_size, i, dest, transition, t, 0.2)
  return im

def lerp(start, end, t):
  assert 0 <= t and t <= 1
  return start*(1-t)+end*t

def draw_circle(draw, color, label, radius, num_circles, img_size, start_index, end_index, transition, t, transition_fraction):
  assert 0 <= t and t <= 1
  """ 
  t = [0, tf) moving out of start position (down or up)
  t = (tf, 1-tf) moving left or right
  t = (1-tf, 1] moving into end position (up or down)
  """
  cy = img_size[1]/2
  if transition == 'under':
    ty = cy+img_size[1]/4
  elif transition == 'over':
    ty = cy-img_size[1]/4
  else:
    ty = cy
  sx = int((start_index+1)*img_size[0]/float(num_circles+1))
  ex = int((end_index+1)*img_size[0]/float(num_circles+1))
  x, y = None, None
  if t < transition_fraction:
    d = t/transition_fraction
    x = sx
    y = lerp(cy, ty, d)
  elif t < 1-transition_fraction:
    d = (t-transition_fraction)/(1-2*transition_fraction)
    x = lerp(sx, ex, d)
    y = ty
  else:
    d = 1-((1-t)/transition_fraction)
    x = ex
    y = lerp(ty, cy, d)
  draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color, outline='black')
  font = ImageFont.truetype('font.ttf', radius-5)
  w, h = draw.textsize(label, font=font)
  draw.text((x-w/2,y-h/2), label, fill="black", font=font)

def get_frames(colors, labels, destinations, img_size, radius, n):
  return [get_frame(colors, labels, destinations, img_size, radius, i/float(n-1)) for i in range(0, n)]

def permute(permutation, array):
  new_array = [None]*len(array)
  for i,d in enumerate(permutation):
    new_array[d] = array[i]
  return new_array

def animate_permutations(permutations, colors, labels, img_size, radius, frames_per_permutation, pause_frames):
  all_frames = []
  for i_p, permutation in enumerate(permutations):
    frames = get_frames(colors, labels, permutation, img_size, radius, frames_per_permutation)
    if i_p == 0:
      all_frames += [frames[0]]*pause_frames
    all_frames += frames
    all_frames += [frames[-1]]*pause_frames
    colors = permute(permutation, colors)
    labels = permute(permutation, labels)
  return all_frames
