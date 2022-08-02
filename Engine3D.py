from gl import Renderer, color, V3, V2

width = 960
height = 540

rend = Renderer(width, height)

rend.glLoadModel("model.obj",
                 translate = V3(width/2, height/2, 0),
                 scale = V3(150, 150, 150))

rend.glFinish("output.bmp")
